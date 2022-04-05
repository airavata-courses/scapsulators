#!/bin/sh

master=scapsulators-k8s-n1
worker=scapsulators-k8s-n2

./createmasterServer.sh master
./createworkerServer.sh worker
./kubeconfig.sh master worker