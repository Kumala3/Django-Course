# Specify image 
FROM python:3.11-slim

# Set up Work Directory
WORKDIR /home/src/app

RUN pip install poetry

# Copy requirements.txt file to the work directory
COPY pyproject.toml /home/src/app/

# Install dependencies needed for the app
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the app
COPY . /home/src/app/

# Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
