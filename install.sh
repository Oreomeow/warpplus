#!/usr/bin/env bash

pip3 install -r requirements.txt
systemctl stop warpplus
rm -rf /var/log/journal/*
chmod 755 warpplus.service
cp -f warpplus.service /etc/systemd/system/warpplus.service
systemctl daemon-reload
systemctl start warpplus
systemctl enable warpplus
