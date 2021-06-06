# Raspberry Pi Humidity Temperature Sensor

## About The Project

This project uses the SHT-31 from Adafruit connected to a raspberry pi 3 to record the temperature and relative humidty and then sends that information to a Mariadb so that it can be accessed at a later time.

## Getting Started

### Equipment
* SHT-31 https://www.adafruit.com/product/4099
* Raspberry Pi 3 https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/
* Jumper Cables https://www.adafruit.com/product/824

### Prerequisites
You will need to solder jumper cables to the SHT-31 in order to connect it to the GPIO pins on the Raspberry Pi. Plenty of videos can be found on how to solder. Ensure to match the cables colors so its easier to see what is going on. 

On the Raspberry Pi you will need to do the following:

Ensure the Raspberry Pi is up to date by running:
  ```sh
  sudo apt-get update
  sudo apt upgrade
  ```

  You then need to install some python packages:
  ```sh
  sudo pip3 install adafruit_sht31d
  sudo pip3 install mariadb
  ```

### Installation
First we need to connect the SHT-31 to the GPIO pins on the Raspberry Pi. Connect the VIN (red wire) to 3V3 on the Raspberry Pi. Connect the GND to GNG (black wire) on the Raspberry Pi. Connect the SCL to SCL (yellow wire) on the Raspberry Pi. Connect the SDA (blue wire) to SDA on Raspberry Pi.

On the home directory of your Raspberry Pi run:
  ```sh
  git clone https://github.com/charlesshook/raspberrypi-humidity-temperature-sensor.git
  ```

Then you are going to need to edit the config file in the /data folder. To generate a UUID you can go to: https://www.uuidgenerator.net/

## Usage
Inside the project folder on the Raspberry Pi run:
  ```sh
  python3 main.py
  ```