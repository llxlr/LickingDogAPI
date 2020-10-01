#!/usr/bin/env bash

#=================================================
#	System Required: Ubuntu
#	Description: Deploying Script
#	Version: 0.0.1
#	Author: James Yang
#	Blog: https://white-album.top/
#=================================================
echo "Hello!"
sudo apt-get install libxss1 libappindicator1 libindicator7
echo "Start install google chrome"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
echo `exec -a "$0" "$HERE/chrome" "$@" --user-data-dir --no-sandbox` > /opt/google/chrome/google-chrome

version=$(google-chrome-stable --version)
echo "google chrome version: ${version}"

# if [!$(google-chrome-stable --version)]; then echo "true"; else echo "fasle"; fi

echo "Start download chromedriver"
wget "https://white-album.top/usr/demo/php/webdriver.php?version=${version: 14: -1}&os=linux"
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

echo "Delete downloaded file"
sudo rm google-chrome*.deb chromedriver_linux64.zip
echo "Delete successfully!"

echo "Thanks for using this script!"