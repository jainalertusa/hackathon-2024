FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Define environment variables for Flask
ENV FLASK_APP=Endpoints/rest_controller.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Expose the Flask port
EXPOSE 5001

# Run the start.sh script (if needed)
COPY start.sh .
CMD ["./start.sh"]
