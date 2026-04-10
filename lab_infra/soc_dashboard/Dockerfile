FROM python:3.10-slim
WORKDIR /app
RUN pip install Flask==2.2.5
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]
