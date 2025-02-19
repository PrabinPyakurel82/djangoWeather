
# Django Weather App with Celery

This is a Django-based weather application that fetches weather data for cities and caches the results for efficiency. It uses Celery for periodic background tasks to update the weather cache every 2 minutes.

## Features
- **Weather Data Fetching**: Fetches current weather information for a given city using a third-party weather API.
- **Caching**: Weather data is cached using Django's caching mechanism, reducing the load on the API.
- **Periodic Cache Update**: Celery periodically updates the weather cache every 2 minutes to ensure data remains fresh.
- **Search History**: Keeps track of previously searched cities with timestamps.

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Celery and Redis
This project uses Celery with Redis as the broker. Ensure you have Redis installed and running on your machine.

#### Install Redis
Follow the installation guide based on your OS: [Redis Installation Guide](https://redis.io/docs/getting-started/).

Once Redis is installed, start the Redis server:

```bash
redis-server
```

#### Configure Celery
The Celery configuration is in `core/celery.py`. Ensure the following is set correctly:

```python
app.conf.broker_url = 'redis://localhost:6379/0'  # Broker URL for Redis
```

### 5. Apply Migrations
Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 6. Start the Django Development Server
You can now start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

### 7. Start Celery Workers and Beat Scheduler
To start the Celery worker and the periodic task scheduler, open two terminal windows:

#### In the first terminal:
```bash
celery -A core worker --loglevel=info
```

#### In the second terminal:
```bash
celery -A core beat --loglevel=info
```

This will ensure Celery workers are processing tasks and Celery Beat is scheduling periodic tasks.

## Usage

### Weather Search
To search for weather data:
1. Send a GET request to `/weather/` with the `city` parameter.
   - Example: `/weather/?city=London`

The weather data for the city will be fetched and cached. If you search for the same city again, the cached data will be returned.

### Search History
To view the search history of cities, visit `/search-history/` to see the list of the latest searched cities with their weather data.

## How It Works

1. **WeatherView**: This view receives a city name, checks if the weather data is cached, and returns it. If the data isn't cached, it fetches it from the weather API, stores it in the cache, and returns it.
   
2. **SearchHistoryView**: This view returns the list of the most recent city searches along with their weather data, either from the cache or by fetching from the weather API.

3. **Celery Task**: The periodic task `update_weather_cache` is executed every 2 minutes to update the weather cache for all cities in the cache. This ensures that the cached data stays fresh.

4. **Caching**: Weather data for each city is stored in the cache with the key `weather_<city_name>`, allowing fast retrieval of the latest weather data.

## Project Structure

```
├── core
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── weather
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── make_request.py
│   ├── serializers.py
│   ├── urls.py
│   ├── migrations/
│   └── __init__.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

- `core/celery.py`: Celery configuration and task scheduling.
- `weather/tasks.py`: Celery tasks such as updating the weather cache.
- `weather/views.py`: Django views to handle API requests for weather data and search history.

## Requirements

- Python 3.x
- Django 3.x
- Celery 5.x
- Redis
- Requests (for making API calls)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
