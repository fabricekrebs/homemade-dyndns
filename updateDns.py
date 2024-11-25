from dotenv import load_dotenv
import os
import requests

# Definition of the global variables
load_dotenv('config.env')

# Gandi API Key
gandiApiKey = os.getenv('GANDIAPIKEY')
# Domain and record details
domain = os.getenv('DOMAIN')
recordName = os.getenv('RECORDNAME')

# Gandi API Base URL
gandiApiBase = "https://api.gandi.net/v5/livedns/domains"

def getPublicIp():
    """Fetch the current public IP address."""
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def getDnsRecord(domain, recordName):
    """Retrieve the existing DNS record for the specified domain and name."""
    url = f"{gandiApiBase}/{domain}/records/{recordName}"
    headers = {"Authorization": f"Bearer {gandiApiKey}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching DNS record: {e}")
        return None

def updateDnsRecord(domain, recordName, ip):
    """Update the DNS record with the new IP."""
    url = f"{gandiApiBase}/{domain}/records/{recordName}"
    headers = {
        "Authorization": f"Bearer {gandiApiKey}",
        "Content-Type": "application/json"
    }
    payload = {
        "items": [
            {
                "rrset_type": "A",
                "rrset_values": [ip]
            }
        ]
    }
    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"DNS record updated successfully: {response.json()}")
    except requests.RequestException as e:
        print(f"Error updating DNS record: {e}")

def main():
    ip = getPublicIp()
    if not ip:
        print("Could not determine public IP. Exiting.")
        return

    print(f"Current public IP: {ip}")

    # Check current DNS record
    record = getDnsRecord(domain, recordName)
    if record:
        currentIps = [item["rrset_values"] for item in record if item["rrset_name"] == recordName and item["rrset_type"] == "A"]
        if currentIps and ip in currentIps[0]:
            print("DNS record is already up to date. No action needed.")
            return

    # Update the DNS record
    print("Updating DNS record...")
    updateDnsRecord(domain, recordName, ip)

if __name__ == "__main__":
    main()
