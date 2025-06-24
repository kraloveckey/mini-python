#!/bin/bash
set -e

# build .rpm packages

# cd to working dir
cd "$(dirname "$0")"

# ensure that the rpm build tools are installed
yum install -y rpmdevtools rpmlint
rpmdev-setuptree

# get the version from the python script
VERSION=$(awk '/PRODUCT_VERSION\s+=/ { print $3 }' ../../laps-runner.py | tr -d \' )

# generate and fill the source folders
mkdir -p laps-client-$VERSION/usr/bin
mkdir -p laps-client-$VERSION/usr/share/applications
mkdir -p laps-client-$VERSION/usr/share/pixmaps
mkdir -p laps-client-runner-$VERSION/usr/sbin
mkdir -p laps-client-runner-$VERSION/etc/cron.hourly
cp ../../laps-gui.py laps-client-$VERSION/usr/bin/laps-gui
cp ../../laps-cli.py laps-client-$VERSION/usr/bin/laps-cli
cp ../../assets/laps-client.desktop laps-client-$VERSION/usr/share/applications
cp ../../assets/laps.png laps-client-$VERSION/usr/share/pixmaps
cp ../../assets/laps-runner.cron laps-client-runner-$VERSION/etc/cron.hourly/laps-runner
cp ../../laps-runner.py laps-client-runner-$VERSION/usr/sbin/laps-runner
chmod +x laps-client-$VERSION/usr/bin/laps-gui
chmod +x laps-client-$VERSION/usr/bin/laps-cli
chmod +x laps-client-runner-$VERSION/usr/sbin/laps-runner
chmod +x laps-client-runner-$VERSION/etc/cron.hourly/laps-runner

# test if we have our own laps-runner config
if [ -f ../../laps-runner.json ]; then
    cp ../../laps-runner.json laps-client-runner-$VERSION/etc
else
    echo 'WARNING: You are using the example json config file, make sure this is intended'
    cp ../../laps-runner.example.json laps-client-runner-$VERSION/etc/laps-runner.json
fi

# create .tar.gz source package
tar --create --file laps-client-$VERSION.tar.gz laps-client-$VERSION
tar --create --file laps-client-runner-$VERSION.tar.gz laps-client-runner-$VERSION
if [ ! -f laps-client-runner-$VERSION.tar.gz ] || [ ! -f laps-client-$VERSION.tar.gz ]; then
    echo 'Tar file was not detected, exiting'
    exit 1
fi

# remove out build directory, now that we have our tarball
rm -fr laps-client-$VERSION
rm -fr laps-client-runner-$VERSION
mkdir -p rpmbuild/SOURCES
mv laps-client-$VERSION.tar.gz rpmbuild/SOURCES/
mv laps-client-runner-$VERSION.tar.gz rpmbuild/SOURCES/

# build the rpm package
cd rpmbuild
rpmbuild --define "_topdir $(pwd)" -bb SPECS/laps-client.spec
rpmbuild --define "_topdir $(pwd)" -bb SPECS/laps-client-runner.spec

