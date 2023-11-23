## Deployment

1. Install Gunicorn (pipenv install Gunicorn)
2. Make sure all source code all under src (including Pipfile Pipfile.lock and .env)
3. Create Dockerfile
4. Run docker build and docker run

docker build -t your-flask-app .
docker run -p 4000:8000 your-flask-app


5. Register to Google Cloud, setup billing
6. Install gcloud cli



# Create Instance in GCP
1. f1-micro region sg (cheapest)
2. spot provisioning
3. allow http and https
4. network interface use external static ip (0.004 usd per hour)
5. setup container 