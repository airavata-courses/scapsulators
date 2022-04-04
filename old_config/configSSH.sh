#!/bin/sh
masterip=$(openstack server list | grep scapsulators-master | awk '{print $9}')
workerip=$(openstack server list | grep scapsulators-worker | awk '{print $9}')

echo $masterip $workerip

ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q 'bash -s' < serverconfig.sh
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$workerip -q 'bash -s' < serverconfig.sh

ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q 'bash -s' < masterconfig.sh

token=$(ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q "sudo kubeadm token create --print-join-command 2>/dev/null" )
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$workerip sudo $token
