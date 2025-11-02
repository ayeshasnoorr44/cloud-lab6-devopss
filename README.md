## DockerHub Deployment

Docker image available at: [https://hub.docker.com/r/ayeshanoorr44/number-converter](https://hub.docker.com/r/ayeshanoorr44/number-converter)

### Pull and Run

```bash
docker pull ayeshanoorr44/number-converter:1.0
docker run -d -p 3000:3000 --name number-converter ayeshanoorr44/number-converter:1.0

## Docker Compose Deployment

### Start All Services
```bash
docker-compose up -d

