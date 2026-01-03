FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY mealie_dredger.py .

# Run the script
CMD ["python", "mealie_dredger.py"]
