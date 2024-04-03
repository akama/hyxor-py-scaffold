# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file to the working directory
COPY player.py .
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the player name (optional)
# ENV PLAYER=YourPlayerName

# Run the Python script when the container starts
CMD ["python", "player.py"]
