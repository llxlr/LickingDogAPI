#!/usr/bin/env bash
set -eu

echo "
#=================================================#
#             System Required: Linux              #
#	  Description: Deploying Script           #
#	          Version: 0.0.1                  #
#	        Author: James Yang                #
#	   Blog: https://white-album.top/         #
#=================================================#
"

sudo apt-get install \
python3 \
python3-pip \
python3-venv \
libxss1 \
libappindicator1 \
libindicator7 \
fonts-liberation \
libatk-bridge2.0-0 \
libatspi2.0-0 \
libgbm1 \
libgtk-3-0 \
libnspr4 \
libnss3 \
xdg-utils -y

sudo python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Start install google chrome"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
sudo apt --fix-broken install -y
sudo dpkg -i google-chrome*.deb
sed 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --user-data-dir --no-sandbox/g' /opt/google/chrome/google-chrome >> /opt/google/chrome/google-chrome
version=$(google-chrome-stable --version)
echo "google chrome version: ${version}"

echo "Start download chromedriver"
wget $(python ./utils/webdriver.py ${version: 14: -1})
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

if [[ -d /etc/api/ ]]
then
  if [[ -f /etc/api/.env ]]
  then
    echo "The .env exist, everything is ok."
  else
    sudo cp .env.example /etc/api/.env
  fi
else
  sudo mkdir /etc/api/
  sudo cp .env.example /etc/api/.env
fi

if [[ -f /etc/systemd/system/ldapi.service ]]
then
  echo "The ldapi.service exist, everything is ok."
else
  sudo cp ./conf/ldapi.service /etc/systemd/system/ldapi.service
  path=$(pwd)
  sed 's/${path//\//\\\/}/\/www\/html\/LickingDogAPI/g' /etc/systemd/system/ldapi.service >> /etc/systemd/system/ldapi.service
fi

echo "Delete downloaded file"
sudo rm google-chrome*.deb chromedriver_linux64.zip
echo "Delete successfully!"

# Config Service And Restart Service
sudo systemctl daemon-reload
sudo systemctl enable ldapi
sudo systemctl restart ldapi

echo "Thanks for using this script!"
