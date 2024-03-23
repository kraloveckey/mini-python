#!/bin/bash
set -e

# build .deb packages

# check root permissions
if [ "$EUID" -ne 0 ]
	then echo "Please run this script as root!"
	exit
fi

# cd to working dir
cd "$(dirname "$0")"

# create necessary directories
mkdir -p laps-client/usr/bin
mkdir -p laps-client/usr/share/applications
mkdir -p laps-client/usr/share/pixmaps
mkdir -p laps-client-runner/etc/cron.hourly
mkdir -p laps-client-runner/usr/sbin

# copy files in place
cp ../../laps-gui.py laps-client/usr/bin/laps-gui
cp ../../laps-cli.py laps-client/usr/bin/laps-cli
cp ../../assets/laps-client.desktop laps-client/usr/share/applications
cp ../../assets/laps.png laps-client/usr/share/pixmaps
cp ../../assets/laps-runner.cron laps-client-runner/etc/cron.hourly/laps-runner
cp ../../laps-runner.py laps-client-runner/usr/sbin/laps-runner
# test if we have our own laps-runner config
if [ -f ../../laps-runner.json ]; then
    cp ../../laps-runner.json laps-client-runner/etc
else
    echo 'WARNING: You are using the example json config file, make sure this is intended'
    cp ../../laps-runner.example.json laps-client-runner/etc/laps-runner.json
fi

# set file permissions
chown -R root:root laps-client
chown -R root:root laps-client-runner
chmod +x laps-client/usr/bin/laps-gui
chmod +x laps-client/usr/bin/laps-cli
chmod +x laps-client-runner/etc/cron.hourly/laps-runner
chmod +x laps-client-runner/usr/sbin/laps-runner

# build debs
dpkg-deb -Zxz --build laps-client
dpkg-deb -Zxz --build laps-client-runner

echo "Build finished"
