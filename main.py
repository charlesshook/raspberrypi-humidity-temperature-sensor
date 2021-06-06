# Runs the SHT31 sensor forever and sends data to a remote database

import mariadb
import sys
import json
import sht31
import time
from datetime import datetime

def main():
    sensor = sht31.SHT31()

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

    # Get Cursor
    cur = conn.cursor()

    # Create the table if it doesn't exist in the database
    try:
        query = """CREATE TABLE IF NOT EXISTS sensors (
                uuid CHAR(100) NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                temperature FLOAT NOT NULL,
                relative_humidity FLOAT NOT NULL,
                PRIMARY KEY(uuid, timestamp))"""

        cur.execute(query)
        conn.commit()
    except mariadb.Error as e:
        print(f"Error creating table in Mariadb: {e}")
        sys.exit(1)


    loopcount = 0
    while True:
        loopcount += 1

        # Send data to database every two seconds
        try: 
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cur.execute(
                "INSERT INTO sensors (uuid, timestamp, temperature, relative_humidity) VALUES (?, ?, ?, ?)", 
                (config["UUID"], timestamp, sensor.readTemperature(), sensor.readRelativeHumidity()))

            conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
        
        time.sleep(2)

        # every 10 passes turn on the heater for 1 second
        if loopcount == 10:
            loopcount = 0
            sensor.heater(1)

if __name__ == "__main__":
    main()