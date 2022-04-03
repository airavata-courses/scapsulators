#!/bin/sh
openstack server create scapsulators-master \
--flavor m3.quad \
--image Featured-Ubuntu20 \
--key-name scapsulators \
--security-group scapsulators-security-group \
--nic net-id=scapsulators-network \
--wait

#create public ip address
openstack floating ip create public



#openstack server add floating ip master-server 149.165.155.41

openstack server add floating ip scapsulators-master $(openstack floating ip create public -f value | sed -n '6 p')
#ssh -i scapsulators ubuntu@$(openstack server list | grep scapsulators-master | awk '{print $9}') -q


public_ip=$(openstack server list | grep scapsulators-master | awk '{print $9}')
private_ip=$(openstack server list | grep scapsulators-master | awk '{print $8}' | cut -b 22- | rev | cut -b 2- | rev)

echo Public Ip = $public_ip  Private Ip = $private_ip