# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script, environment configuration, and requirements file into the container
COPY updateDns.py config.env requirements.txt ./

# Install required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the script every hour in an infinite loop
CMD ["sh", "-c", "while true; do python /app/updateDns.py; sleep 3600; done"]
