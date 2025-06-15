FROM texlive/texlive:latest

# Set working directory
WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Copy application code
COPY ./ ./

# Install Python dependencies with override
RUN pip3 install --break-system-packages --upgrade pip && \
    pip3 install --break-system-packages -r requirements.txt

# Expose backend port
EXPOSE 7860

# Launch the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]