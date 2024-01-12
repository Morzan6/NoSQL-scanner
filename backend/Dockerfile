FROM python:3.11
WORKDIR /NoSQL-Scanner
ENV PYTHONUNBUFFERED=1
ENV JWT_SECRET=62d714c99175c698d9262e343e71cbb9

RUN apt update && apt install -y nmap git && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/scipag/vulscan.git /usr/share/nmap/scripts/vulscan

COPY ./requirements.txt .
RUN  pip install -r requirements.txt
COPY  . .

EXPOSE  8000
CMD  ["uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]
