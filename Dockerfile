# Use Python 3 as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy all files from the current directory into the container's /app directory
COPY . .

# Define the command to run when the container starts
CMD ["python3", "simple_program.py"]
