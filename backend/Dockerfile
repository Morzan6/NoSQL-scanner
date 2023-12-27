FROM        python:3.11-alpine
ENV         PYTHONUNBUFFERED=1
ENV         JWT_SECRET=62d714c99175c698d9262e343e71cbb9
WORKDIR     /NoSQL-Scanner
COPY        . .
RUN         pip install -r requirements.txt 
EXPOSE      8000
CMD         ["uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]