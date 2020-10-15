#!/usr/bin/env bash

#=================================================
#	System Required: Ubuntu
#	Description: Deploying Script
#	Version: 0.0.1
#	Author: James Yang
#	Blog: https://white-album.top/
#=================================================
echo "Hello!"
sudo apt-get install python3 python3-pip python3-venv -y
sudo python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
sudo cp .env.example .env
sudo cp ./conf/ldapi.service /etc/systemd/system/ldapi.service
path=$(pwd)
sed 's/${path//\//\\\/}/\/www\/html\/LickingDogAPI/g' /etc/systemd/system/ldapi.service >> /etc/systemd/system/ldapi.service
sudo systemctl daemon-reload
sudo systemctl enable ldapi

echo "Start install google chrome"
sudo apt-get install libxss1 libappindicator1 libindicator7 fonts-liberation libatk-bridge2.0-0 -y
sudo apt-get install libatspi2.0-0 libgbm1 libgtk-3-0 libnspr4 libnss3 xdg-utils -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
sudo apt --fix-broken install -y
sudo dpkg -i google-chrome*.deb
sed 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --user-data-dir --no-sandbox/g' /opt/google/chrome/google-chrome >> /opt/google/chrome/google-chrome

version=$(google-chrome-stable --version)
echo "google chrome version: ${version}"

# if [!$(google-chrome-stable --version)]; then echo "true"; else echo "fasle"; fi

echo "Start download chromedriver"
wget $(python ./utils/webdriver.py ${version: 14: -1})
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# Restart Service
sudo systemctl restart ldapi

echo "Delete downloaded file"
sudo rm google-chrome*.deb chromedriver_linux64.zip
echo "Delete successfully!"

echo "Thanks for using this script!"