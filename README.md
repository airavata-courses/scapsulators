Parameters to be added

```
Hostname: js-168-203.jetstream-cloud.org
SSH_user: shubham
SSH_user_password: pass123
SSH_key: your key path
Keycloak_username: admin 
Keycloak_password: keycloak_pass
vault_token: vault_token
MYSQL_user: user
MYSQL_password: pass
docker_repo: scapsulators
```

Changes to be made, 

1. custos-core-services/utility-services/custos-configuration-service/pom.xml --> change skipped to false

2. custos-core-services/utility-services/custos-configuration-service/resource/*-dev.properties 

   change `iam.server.url=https://{host-name}:30079/auth/`



-  Build code
    `mvn clean install -P container`

- Push code images to repo
   `mvn dockerfile:push -P container`

-  deploy artifacts
   `mvn antrun:run -P scp-to-remote`
   
 `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.44.0/deploy/static/provider/baremetal/deploy.yaml`
 
 `helm install cluster-management-core-service /home/shubhpatr/custos/artifacts/cluster-management-core-service-1.1-SNAPSHOT.tgz  -n keycloak`

