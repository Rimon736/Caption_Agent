FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements_clean.txt .
RUN pip install --no-cache-dir -r requirements_clean.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false"]
