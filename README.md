# Azure Minecraft Server Controller v2
A discord bot to allow friends to start and stop Azure resources hosting a Minecraft server on command.

## setup

### local development

python: [link](https://www.python.org/downloads/])

```
git clone <this_repo_url>
cd amsc-v2

python -m venv venv
. ./venv/Scripts/activate

python -m pip install -r requirements.txt


# Make sure to set your AMSC_BOT_TOKEN environment variable
python main.py
```

### deployment

docker desktop: [link](https://www.docker.com/products/docker-desktop/)

```
docker build -t amsc-v2 .

# Test locally
docker run --env-file .env amsc-v2

# Login
az act login --name azuremcservercontroller

# Tag
docker tag amsc-v2 azuremcservercontroller-d5cgbxhtceahd0f8.azurecr.io/amsc-v2:v1

# Push to ACR
docker push azuremcservercontroller-d5cgbxhtceahd0f8.azurecr.io/amsc-v2:v1

# Deploy to Azure Container Instance
TODO
```



