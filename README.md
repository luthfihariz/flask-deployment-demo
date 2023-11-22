## Deployment

1. Install Gunicorn (pipenv install Gunicorn)
2. Make sure all source code all under src (including Pipfile Pipfile.lock and .env)
3. Create Dockerfile
4. Run docker build and docker run

docker build -t your-flask-app .
docker run -p 4000:8000 your-flask-app


5. Register to Google Cloud, setup billing
6. Install gcloud cli


# Without Docker

sudo apt-get update
sudo apt-get install -y build-essential python3.9 python3.9-dev libpq-dev curl git
