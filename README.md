# Music Hub API

A fully featured music streaming REST API built with Django REST Framework.

## Tech Stack
- Python
- Django & Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger UI Documentation

##  Features
- User registration and login with JWT authentication
- Full CRUD for Artists, Albums, Songs and Playlists
- File uploads for audio files and cover images
- Search and filter functionality
- Pagination
- API documentation with Swagger UI

##API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/register/` | POST | Register a new user |
| `/api/token/` | POST | Login and get JWT token |
| `/api/token/refresh/` | POST | Refresh JWT token |
| `/api/artists/` | GET, POST | List and create artists |
| `/api/artists/{id}/` | GET, PUT, DELETE | Manage a single artist |
| `/api/albums/` | GET, POST | List and create albums |
| `/api/albums/{id}/` | GET, PUT, DELETE | Manage a single album |
| `/api/songs/` | GET, POST | List and create songs |
| `/api/songs/{id}/` | GET, PUT, DELETE | Manage a single song |
| `/api/playlists/` | GET, POST | List and create playlists |
| `/api/playlists/{id}/` | GET, PUT, DELETE | Manage a single playlist |

## How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/Mea-xoxo/Music-Hub-API.git
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your settings
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=musichub
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the server
```bash
python manage.py runserver
```

7. Visit API documentation
```
http://127.0.0.1:8000/api/docs/
```
