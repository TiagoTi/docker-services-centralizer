FROM ubuntu

RUN apt update -y && \
  apt install -y git vim curl wget telnet && \
  wget -O /bin/teresa https://github.com/luizalabs/teresa/releases/download/v0.28.0/teresa-linux-amd64 && \
  chmod +x /bin/teresa && \
  teresa version
