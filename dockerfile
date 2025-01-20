# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN sudo apt install -y build-essential python3-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to tell Flask to listen on all IP addresses
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask when the container launches
CMD ["flask", "run"]
