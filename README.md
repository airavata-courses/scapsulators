Parameters to be added

```
UserProfile: staging
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

   custos-core-services/utility-services/custos-configuration-service/resource/*-staging.properties 

   change `iam.server.url=https://{host-name}:30079/auth/`

3. Open custos-integration-services/tenant-management-service-parent/tenant-management-service/src/main/java/tasks/TenantActivationTask.java

   comment lines 225-249
   
 4. Create folder custos in home directory of master and give 777 permission

- Login Docker
   `docker login`

-  Build code
    `mvn clean install -P container`

- Push code images to repo
   `mvn dockerfile:push -P container`

-  deploy artifacts
   `mvn antrun:run -P scp-to-remote`
   
- if pods are not ready, follow these steps highlighted here. 
   https://airavata.slack.com/archives/C030JRE25ED/p1651617616011969
   
 `kubectl delete all --all -n ingress-nginx`  
   
 `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.44.0/deploy/static/provider/baremetal/deploy.yaml`
 
 `helm install cluster-management-core-service /home/shubhpatr/ssh_user/artifacts/cluster-management-core-service-1.1-SNAPSHOT.tgz  -n keycloak`
 
 Login to vault  https://{host_name}:30079 service, 
 
 Enable new engines named "secret" and "resourcesecret". 
 
Post Request to register tenant
https://{hostname}:30079/tenant-management/v1.0.0/oauth2/tenant

```
{
    "client_name":"scapsulators",
    "requester_email":"shmoha@iu.edu",
    "admin_username":"user",
    "admin_first_name":"Shubham",
    "admin_last_name":"Mohapatra",
    "admin_email":"email@iu.edu",
    "contacts":["email1@iu.edu","email2@gmail.com"],
    "redirect_uris":["http://localhost:8080/callback*",
    "https://{host_name}/callback*"],
    "scope":"openid profile email org.cilogon.userinfo",
    "domain":"host_name",
    "admin_password":"shubham123",
    "client_uri":"host_name",
    "logo_uri":"host_name",
    "application_type":"web",
    "comment":"Custos super tenant for production"
}
```

Open secret in vault, edit 100001 and change supertenant to "true".

Set supertenant to active. 

POST https://{host_name}:30079/tenant-management/v1.0.0/status

```
{
"client_id":"custos-asdfdff-10000001",
"status":"ACTIVE",
"super_tenant":true,
"updatedBy":"user"
}

```







