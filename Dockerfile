# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Gunicorn
RUN pip install --no-cache-dir flask gunicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run the application using Gunicorn
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:80", "app:app"]
