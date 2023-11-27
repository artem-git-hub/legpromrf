# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the application
# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
