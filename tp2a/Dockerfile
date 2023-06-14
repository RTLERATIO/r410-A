FROM debian:11
RUN # ... update+upgrade
CMD sudo apt-get install −y python3−pip
CMD pip3 install flask uvicorn
WORKDIR /srv # il faut bien sur que ce dossier existe...
COPY app1.py .
CMD uvicorn app1 : app −−host 0.0.0.0