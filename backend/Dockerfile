FROM python:3.11-slim-bookworm
WORKDIR /NoSQL-Scanner

RUN apt update && apt install -y nmap git && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/scipag/vulscan.git /usr/share/nmap/scripts/vulscan

COPY ./requirements.txt .
RUN  pip install -r requirements.txt
COPY  . .

EXPOSE  8000
CMD  ["uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]
