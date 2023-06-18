FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY requirements.txt .
COPY model.py .
COPY price_prediction_model.pkl .


# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]