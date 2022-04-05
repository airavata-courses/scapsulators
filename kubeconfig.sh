#!/bin/sh

masterip=$(openstack server list | grep $1 | awk '{print $9}')
workerip=$(openstack server list | grep $2 | awk '{print $9}')
master_private_ip=$(openstack server list | grep $1 | awk '{print $8}' | cut -b 22- | rev | cut -b 2- | rev)
worker_private_ip=$(openstack server list | grep $2 | awk '{print $8}' | cut -b 22- | rev | cut -b 2- | rev)


scp -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ~/.ssh/scapsulators  ubuntu@$masterip:~/.ssh/id_rsa
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q 'bash -s' < masterconfig.sh $master_private_ip $worker_private_ip

echo Trying again..
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q <<'EOL'
	echo Running Playbook..
    cd kubespray
    ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
EOL


ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q 'bash -s' < config.sh master
ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$workerip -q 'bash -s' < config.sh worker

echo Deploying to Master..

ssh -i ~/.ssh/scapsulators -oStrictHostKeyChecking=no ubuntu@$masterip -q <<'EOL'
	echo Running Playbook..
    cd kubespray
    ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml


    echo Running App now.

    cd ~

    git clone https://github.com/airavata-courses/scapsulators
    cd scapsulators
    git checkout project2-release
    cd kubernetes
    sudo kubectl apply -f react.yaml
EOL


