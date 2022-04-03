openstack server create master-server \
--flavor m3.quad \
--image Featured-Ubuntu20 \
--key-name scapsulators \
--security-group scapsulators-security-group \
--nic net-id=scapsulators-network \
--wait

#create public ip address
openstack floating ip create public



openstack server add floating ip master-server 149.165.155.41

ssh -i scapsulators ubuntu@149.165.155.41 -q