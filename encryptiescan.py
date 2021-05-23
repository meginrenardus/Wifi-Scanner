import subprocess
from subprocess import check_output
import os
import time

def encryption():
    currentssid = check_output(["iwlist", "wlan0", "scan"])

    ssid = ""

    for line in currentssid.split():
        line = line.decode("utf-8")
        if line[:5] == "ESSID":
            ssid = line.split('"')[1]
    print(ssid)

    # Gebruik van airmon-ng om te controleren op storende processen.
    os.system("sudo airmon-ng check")

    # Het stoppen van de storende processen
    os.system("sudo airmon-ng check kill")

    # De WLAN interface in monitoring modus zetten
    os.system("sudo airmon-ng start wlan0")

    # Scannen naar draadloze netwerken in de buurt d.m.v. een subprocess. Hierdoor kan deze na een bepaalde tijd gestopt worden.
    process = subprocess.Popen(
        ['sudo', 'airodump-ng', 'wlan0mon'], stdout=subprocess.PIPE)
    start = time.time()
    #start een while loop die gedurende 5 secodent loopt. Hierbij wordt de output van de console gelezen en in de variabele 'output' geplaatst.
    while time.time() - start <= 5:
	#readline wordt gebruikt om alleen incrementele waardes van afzonderlijke regels per keer in te lezen en ze als strings te retourneren.
        output = process.stdout.readline()
        scanline = str(output).split()
        if scanline[-2] == ssid:
            print(scanline[8])
            return scanline[8]

    # Zet de wifi adapter terug in managed mode
    os.system("sudo airmon-ng stop wlan0mon")

    # De network manager service herstarten
    os.system("sudo service NetworkManager restart")


def main():
    encryptionscan = encryption()

if __name__ == '__main__':
    main()
