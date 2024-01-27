FROM python:3.11-slim-bookworm
WORKDIR /NoSQL-Scanner

RUN apt update && apt install -y nmap git pandoc texlive-xetex && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/scipag/vulscan.git /usr/share/nmap/scripts/vulscan 

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY  . .

RUN mv ./tools/font.ttf /usr/local/share/fonts/font.ttf && \
    fc-cache -vf

EXPOSE  8000
CMD  ["uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]
