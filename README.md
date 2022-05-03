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

   change `iam.server.url=https://{host-name}/auth/`



-  Build code
    `mvn clean install -P container`

- Push code images to repo
   `mvn dockerfile:push -P container`

-  deploy artifacts
   `mvn antrun:run -P scp-to-remote`

