FROM kalilinux/kali-rolling 

RUN apt-get -y update && apt-get -y upgrade 
RUN apt-get install python3

WORKDIR C:\Users\Megin\Desktop\Wifi-Scanner

