#!/bin/sh
printf "Install temperature-control-service\n"
sudo cp /home/pi/raspberry-python/temperature-control-service /etc/init.d/temperature-control-service
sudo cp /home/pi/raspberry-python/lcd-service /etc/init.d/lcd-service
sudo chmod +x /etc/init.d/lcd-service
sudo chmod +x /etc/init.d/temperature-control-service
sudo update-rc.d lcd-service defaults
sudo update-rc.d temperature-control-service defaults
printf "Done\n"
