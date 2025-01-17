# Use an Ubuntu base image
FROM ubuntu:22.04

# Set the working directory inside the container
WORKDIR /app

# Update the system and install Python 3.10 and pip
RUN apt-get update && apt-get install -y \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-distutils && \
    apt-get install -y curl && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install X11 and other dependencies

RUN apt-get update && apt-get install -y \
    x11-apps libx11-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install Xvfb and dependencies
RUN apt-get update && apt-get install -y \
    xvfb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set the working directory
WORKDIR /app


# Copy requirements.txt and main.py to the container
COPY requirements.txt .
COPY main.py .

# Install Python dependencies
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt




# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf


# # Copy the requirements file and install dependencies
# # Install dependencies
# COPY requirements.txt .
# COPY main.py .


# RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
