# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
RUN mkdir -p /app

# Copy file needed and setup work directory
COPY ./src /app
WORKDIR /app

# Install Pipenv
RUN pip install -U pipenv

# Install dependencies using Pipenv
RUN pipenv install --deploy

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "app:app"]
