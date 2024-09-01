from tasks import fetch_and_store_posts

# Call the Celery task
result = fetch_and_store_posts.delay()

# Optionally, wait for the result and print it
print(f"Task ID: {result.id}")
print(f"Task Result: {result.get(timeout=10)}")  # Waits up to 10 seconds for the result
