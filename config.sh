#!/bin/sh

echo Configuring $1 Server..



sudo systemctl daemon-reload
sudo systemctl unmask containerd
sudo systemctl start containerd
sudo systemctl status containerd --no-pager






