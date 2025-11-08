# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose Django default port
EXPOSE 8000

# Run Django server using manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
