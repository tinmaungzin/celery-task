import requests
import logging
from celery import Celery
from sqlalchemy.orm import Session
from models import Post, SessionLocal
from celery_config import app

API_URL = "https://jsonplaceholder.typicode.com/posts"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.task(bind=True, max_retries=3)
def fetch_and_store_posts(self):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()   

        data = response.json()

        with SessionLocal() as session:
            for item in data:
                post = Post(
                    id=item['id'],
                    user_id=item['userId'],
                    title=item['title'],
                    body=item['body']
                )
                session.merge(post)
            session.commit()
        
        # Log success
        logger.info("Successfully fetched and stored posts.")

    except requests.RequestException as exc:
        logger.error(f"Network error occurred: {exc}")
        raise self.retry(exc=exc, countdown=60)
    except Exception as exc:
        logger.error(f"An error occurred: {exc}")
        raise self.retry(exc=exc, countdown=60)
