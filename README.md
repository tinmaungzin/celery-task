# Celery Task Processing with SQLAlchemy

This project demonstrates a simple setup for processing tasks using Celery with Redis as the broker and backend, and SQLAlchemy for database interactions. The task fetches posts from an external API and stores them in a SQLite database.

## Project Structure

- `celery_config.py`: Contains Celery configuration and application setup.
- `models.py`: Defines SQLAlchemy models and database setup.
- `tasks.py`: Contains Celery tasks for fetching and storing posts.
- `app.py`: Example script to run the Celery task (optional).

## Prerequisites

- Python 3.x
- Redis server
- SQLite database

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tinmaungzin/celery-task.git
    cd celery-task
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Redis:**

    Follow the [Redis installation guide](https://redis.io/download) for your operating system.

## Configuration

1. **Celery Configuration:**

    The `celery_config.py` file is configured to use Redis as both the broker and backend. Ensure that Redis is running on `localhost:6379`.

2. **Database Configuration:**

    The SQLite database is defined in `models.py` and is created automatically.

## Running the Application

1. **Start Redis Server:**

    Make sure the Redis server is running. You can start it with:

    ```bash
    redis-server
    ```

2. **Start the Celery Worker:**

    ```bash
    celery -A tasks worker --loglevel=info
    ```

3. **Run the Task (Optional):**

    You can run the task using the `app.py` script:

    ```bash
    python app.py
    ```

4. **Check Task Results:**

    Monitor the Celery worker logs to see task progress and results.

## Task Details

- **Task Name:** `fetch_and_store_posts`
- **Description:** Fetches posts from `https://jsonplaceholder.typicode.com/posts` and stores them in the SQLite database.

## Logging

Logs are handled by Python's `logging` module. Successful task completion and errors are logged to the console where the Celery worker is running.

