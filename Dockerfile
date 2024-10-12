# Use the official Python image from the Docker Hub
FROM python:3.10

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]