1. build and tag the image

``docker build -t gcr.io/your-project-id/api-flask .

2. push to container registry

```docker push gcr.io/your-project-id/api-flask

3. deploy cloud run

```gcloud run deploy api-flask \
    --image gcr.io/your-project-id/api-flask \
    --platform managed \
    --allow-unauthenticated
