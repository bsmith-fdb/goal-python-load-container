# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD /src /app

# Install any needed packages specified
RUN pip install --no-cache-dir requests

# Make port 80 available to the world outside this container
#EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]