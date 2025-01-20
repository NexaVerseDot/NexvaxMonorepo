

**Useful commands** 

In order for the settings to be applied, it is enough to restart the containers, for this you need to run the commands: 

**Update backend code \+ full restart** 

cd /app/opencex/backend/   
sudo git pull   
sudo docker build \-t opencex \-f Dockerfile .   
cd /app/opencex/   
docker compose stop   
docker compose up \-d   
docker exec \-it opencex python manage.py migrate 

**Update backend settings** 

**cd /app/opencex/backend**   
**docker compose restart** 

**Update frontend** 

**cd /app/opencex/frontend/ ;**  
**git pull ;**  
**docker build \-t frontend \-f deploy/Dockerfile . ;**  
**cd /app/opencex/ ;**   
**docker compose up \-d \--force-recreate** 

**Update static** 

**cd /app/opencex/nuxt/ ;**  
**git pull ;**  
**docker build \-t nuxt \-f deploy/Dockerfile . ;**  
**cd /app/opencex ;**  
**docker compose up \-d \--force-recreate** 

