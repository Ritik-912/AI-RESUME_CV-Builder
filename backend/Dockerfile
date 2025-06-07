FROM node:18 AS frontend

FROM python:3.11-slim AS backend

# Install LaTeX
RUN apt-get update && apt-get install -y \
    texlive-fonts-extra \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    lmodern \
    texlive-lang-english \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy Python app
COPY ./ .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]