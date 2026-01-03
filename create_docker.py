# create_docker.py

dockerfile_content = """FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY mealie_dredger.py .

# Run the script
CMD ["python", "mealie_dredger.py"]
"""

compose_content = """services:
  mealie-dredger:
    build: .
    container_name: mealie-dredger
    volumes:
      # Mount the local script so your config edits apply immediately
      - ./mealie_dredger.py:/app/mealie_dredger.py
    restart: "no"  # Run once and exit
"""

with open("Dockerfile", "w") as f:
    f.write(dockerfile_content)

with open("docker-compose.yml", "w") as f:
    f.write(compose_content)

print("✅ Dockerfile and docker-compose.yml created!")
