cd audit
call mvnw clean package
cd ..\authentication\authentication
call mvnw clean package
cd ..\database-connect
call mvnw clean package
cd ..

docker-compose rm -svf
docker-compose up