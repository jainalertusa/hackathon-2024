# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./
COPY notebooks/Hackathon.ipynb /usr/src/app/notebooks/Hackathon.ipynb

# Upgrade pip 
RUN pip install --upgrade pip

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter
RUN pip install jupyter

# Copy the rest of the application code
COPY . .

# Expose the port Jupyter runs on
EXPOSE 8888

# Command to run Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
