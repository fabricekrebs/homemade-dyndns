# Gandi DNS Updater

This project is a Python-based tool that updates the DNS records for a domain using the Gandi LiveDNS API. The script checks your public IP address and updates the specified DNS record if the IP has changed. It is packaged in a Docker container for ease of deployment and is designed to run every hour.

---

## Features

- Automatically fetches the public IP address using the [ipify API](https://www.ipify.org/).
- Updates the DNS record via the [Gandi LiveDNS API](https://api.gandi.net/docs/livedns/).
- Runs on an hourly schedule using a simple loop inside the Docker container.
- Easy configuration via environment variables.

---

## Prerequisites

1. **Gandi API Key**: Obtain your API key from the Gandi account dashboard.
2. **Docker**: Ensure Docker is installed on your system.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gandi-dns-updater.git
cd gandi-dns-updater
```

### 2. Configure Environment Variables
Create a `config.env` file with the following variables:

- `GANDIAPIKEY`: Your API key from Gandi.
- `DOMAIN`: The domain name you wish to update, e.g., `example.com`.
- `RECORDNAME`: The specific DNS record to update, e.g., `www` for `www.example.com`.

Replace `GANDIAPIKEY`, `DOMAIN`, and `RECORDNAME` with your actual values.

### 3. Build the Docker Image
To build the Docker image, use the following command:

```bash
docker-compose build
```

To start the container. This will run the container as a background process, executing the DNS updater script every hour.
```bash
docker-compose up -d
```

To access the logs in real-time.
```bash
docker-compose logs -f
```

To stop the container and remove it, but it will retain the built images and network settings.
```bash
docker-compose down
```
