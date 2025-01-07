# Use Python image as base
FROM python:3.9-slim

# Install dependencies
WORKDIR /app

# Copy requirements file for the whole pipeline if you have one or install dependencies for each component
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Alternatively, if you want to install each script's dependencies separately:
# COPY Data_Generator/requirements.txt /app/Data_Generator/ && pip install -r /app/Data_Generator/requirements.txt
# COPY Data_Ingestion/requirements.txt /app/Data_Ingestion/ && pip install -r /app/Data_Ingestion/requirements.txt
# COPY Process_Stream_Data/requirements.txt /app/Process_Stream_Data/ && pip install -r /app/Process_Stream_Data/requirements.txt

# Copy all project files into the container
COPY . /app

# Set the working directory to where the entry scripts are located (adjust if needed)
WORKDIR /app

# Install additional dependencies (if required) like Kafka
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Run all parts of the pipeline (producer -> consumer -> processing jobs)
CMD ["bash", "-c", "python /app/Data_Ingestion/kafka_producer.py & python /app/Data_Ingestion/kafka_consumer.py & python /app/Process_Stream_Data/process_job.py"]
