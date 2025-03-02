# Pulling the latest Python image (better to specify a version)
FROM python:latest

# Set the working directory inside the container  

WORKDIR  /app
# Copy source code into the container  
COPY . .

# Install dependencies in one RUN command to optimize layers  
RUN pip install --no-cache-dir -r requirements.txt  

# Expose port 8000  
EXPOSE 8000  

# Run the Django server when the container starts  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
