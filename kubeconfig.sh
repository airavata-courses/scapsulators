#!/bin/sh

masterip=$(openstack server list | grep scapsulators-master | awk '{print $9}')
master_private_ip=$(openstack server list | grep scapsulators-master | awk '{print $8}' | cut -b 22- | rev | cut -b 2- | rev)
worker_private_ip=$(openstack server list | grep scapsulators-worker | awk '{print $8}' | cut -b 22- | rev | cut -b 2- | rev)


scp -i ~/.ssh/scapsulators ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip:~/id_rsa
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q 'bash -s' < masterconfig.sh $master_private_ip $worker_private_ip

