#!/bin/sh
printf "Install temperature-control-service\n"
sudo cp /home/pi/raspberry-python/temperature-control-service /etc/init.d/temperature-control-service
sudo chmod +x /etc/init.d/temperature-control-service
sudo update-rc.d temperature-control-service defaults
printf "Done\n"
