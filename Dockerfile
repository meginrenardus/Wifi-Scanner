FROM kalilinux/kali-rolling
RUN apt-get -y update && apt-get -y upgrade && apt auto-remove && apt auto-clean
RUN apt-get install kali-linux-default
