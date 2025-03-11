# Pulling the latest Python image (better to specify a version)
FROM python:latest

# Set the working directory inside the container  

WORKDIR  /app
# layer caching 
# Install dependencies in one RUN command to optimize layers  
COPY  requirements.txt .
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
# Copy source code into the container  
COPY . .

  

# Expose port 8000  
EXPOSE 8000  

# Run the Django server when the container starts  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
