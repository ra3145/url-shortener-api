# URL Shortener API

A simple URL Shortener API built using Django and Django REST Framework.

## Features
- Shorten long URLs
- Redirect using short code
- Track access count

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

##  Setup Instructions

1. Clone the repository:
git clone https://github.com/ra3145/url-shortener-api.git

2. Navigate to the project:
cd url-shortener-api

3. Create virtual environment:
python -m venv env

4. Activate environment:
env\Scripts\activate   (Windows)

5. Install dependencies:
pip install -r requirements.txt

6. Run migrations:
python manage.py migrate

7. Start server:
python manage.py runserver

##  API Endpoints

### Create Short URL
POST /shorten/
{
  "url": "https://example.com"
}

### Redirect
GET /<short_code>/

project URL
http://127.0.0.1:8000
GitHub Repository: https://github.com/your-username/url_shortener_api


