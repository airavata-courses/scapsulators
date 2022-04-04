#!/bin/sh

#create security group
openstack security group create --description "ssh, gateway and react ports" scapsulators-security-group

#create rules
openstack security group rule create --protocol tcp --dst-port 22:22 --remote-ip 0.0.0.0/0 scapsulators-security-group

openstack security group rule create --protocol tcp --dst-port 30001:30001 --remote-ip 0.0.0.0/0 scapsulators-security-group

openstack security group rule create --protocol tcp --dst-port 30002:30002 --remote-ip 0.0.0.0/0 scapsulators-security-group

openstack security group rule create --protocol tcp --dst-port 6443:6443 --remote-ip 0.0.0.0/0 scapsulators-security-group

openstack security group rule create --protocol tcp --dst-port 1:65525 --remote-ip 0.0.0.0/0 scapsulators-security-group



openstack security group rule create --protocol icmp scapsulators-security-group

#create network
openstack network create scapsulators-network

#openstack network list ---list-networks

#create subnet
openstack subnet create --network scapsulators-network --subnet-range 10.0.0.0/24 scapsulators-subnet

#add router
openstack router create scapsulators-router

#connect subnet to router
openstack router add subnet scapsulators-router scapsulators-subnet

#set router public
openstack router set --external-gateway public scapsulators-router

# show router 
openstack router show scapsulators-router