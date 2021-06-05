# Runs the SHT31 sensor forever and sends data to a remote database

import mariadb
import sys
import json
import sht31
import time

def main():
    with open("./data/config.json") as jf:
        config = json.load(jf)
    
    try:
        conn = mariadb.connect(
            user=config["mariadb"]["user"],
            password=config["mariadb"]["password"],
            host=config["mariadb"]["host"],
            port=config["mariadb"]["port"],
            database=config["mariadb"]["database"]
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    sensor = sht31.SHT31()
    loopcount = 0
    while True:
        loopcount += 1
        # every 10 passes turn on the heater for 1 second
        if loopcount == 10:
            loopcount = 0
            sensor.heater(1)

if __name__ == "__main__":
    main()