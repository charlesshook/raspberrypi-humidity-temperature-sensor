# raspberrypi-humidity-temperature-sensor

## About The Project

This project uses the SHT-31 from Adafruit connected to a raspberry pi 3 to record the temperature and relative humidty and then sends that information to a Mariadb so that it can be accessed at a later time.

## Getting Started

### Equipment
* SHT-31 https://www.adafruit.com/product/4099
* Raspberry Pi 3 https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/

### Prerequisites
Before you get started you need to run these commands on the Raspberry Pi.

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

## Usage