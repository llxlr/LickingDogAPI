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

# sudo apt-get install \
# unzip \
# python3 \
# python3-pip \
# python3-venv \
# libxss1 \
# libappindicator1 \
# libindicator7 \
# fonts-liberation \
# libatk-bridge2.0-0 \
# libatspi2.0-0 \
# libgbm1 \
# libgtk-3-0 \
# libnspr4 \
# libnss3 \
# xdg-utils -y

sudo apt-get install \
unzip \
python3 \
python3-pip \
python3-venv \
fonts-liberation \
libatk-bridge2.0-0 \
libatk1.0-0 \
libatomic1 \
libatspi2.0-0 \
libcairo2 \
libcups2 \
libgbm1 \
libgdk-pixbuf2.0-0 \
libgtk-3-0 \
libnspr4 \
libnss3 \
libpango-1.0-0 \
libxkbcommon0 \
xdg-utils -y

sudo python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# echo "Start install google chrome"
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo dpkg -i google-chrome*.deb
# sudo apt --fix-broken install -y
# sudo dpkg -i google-chrome*.deb
# sed 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --user-data-dir --no-sandbox/g' /opt/google/chrome/google-chrome >> /opt/google/chrome/google-chrome
# version=$(google-chrome-stable --version)
# echo "google chrome version: ${version}"

# echo "Start install microsoft edge dev"
# wget https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-dev/microsoft-edge-dev_89.0.774.4-1_amd64.deb
# sudo dpkg -i microsoft-edge*.deb
# sudo apt --fix-broken install -y
# sudo dpkg -i microsoft-edge*.deb
# sed 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --user-data-dir --no-sandbox/g' /opt/microsoft/msedge-dev/microsoft-edge-dev >> /opt/microsoft/msedge-dev/microsoft-edge-dev
# version=$(microsoft-edge-dev --version)
# echo "microsoft edge dev version: ${version}"

# webdriver="chromedriver"
# webdriver="msedgedriver"
# echo "Start download ${webdriver}"
# wget $(python ./utils/webdriver.py ${version: 14: -1})  # Microsoft Edge 89.0.774.4 dev
# unzip *driver_linux64.zip
# sudo chmod +x ${webdriver}
# sudo mv -f ${webdriver} /usr/local/bin/${webdriver}
# sudo ln -s /usr/local/bin/${webdriver} /usr/bin/${webdriver}
# version=$(${webdriver} --version)
# echo "${webdriver} version: ${version}"

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
sudo rm google-chrome*.deb microsoft-edge*.deb chromedriver_linux64.zip msedgedriver_linux64.zip
echo "Delete successfully!"

# Config Service And Restart Service
sudo systemctl daemon-reload
sudo systemctl enable ldapi
sudo systemctl restart ldapi

echo "Thanks for using this script!"
