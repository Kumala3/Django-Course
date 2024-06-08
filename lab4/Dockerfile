# Specify image 
FROM python:3.11-slim

# Set up Work Directory
WORKDIR /home/src/app

# Copy requirements.txt file to the work directory
COPY requirements.txt /home/src/app/

# Install dependencies needed for the app
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . /home/src/app/

# Run the app
CMD ["python", "manage.py", "runserver"]
