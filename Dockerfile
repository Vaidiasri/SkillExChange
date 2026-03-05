# Use the official Python lightweight image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
# Note: The filename 'requirmnet.txt' matches the existing file exactly
COPY requirmnet.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirmnet.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
