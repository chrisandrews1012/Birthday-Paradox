FROM python:3.11-slim-bullseye

WORKDIR /app

COPY pyproject.toml .
COPY src ./src/
COPY app.py .

RUN pip install --no-cache-dir .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
