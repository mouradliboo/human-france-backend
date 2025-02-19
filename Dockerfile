FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app              
COPY requirements.txt ./  
RUN pip install -r requirements.txt
COPY ./ ./

# add the following
WORKDIR /app/project      
EXPOSE 8000               
CMD python3 ./manage.py runserver 0.0.0.0:8000  # standard command to run