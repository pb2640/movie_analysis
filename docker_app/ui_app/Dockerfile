# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variables if needed (optional)
ENV PORT=8080

# Command to run the Streamlit app
CMD ["streamlit", "run", "uiapp.py"]