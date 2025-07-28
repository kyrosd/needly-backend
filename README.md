## Backend Setup (Django API)

### Prerequisites

- Python 3.10+ installed ([download here](https://www.python.org/downloads/))
- PostgreSQL installed and running (or another supported database)
- (Optional) Python virtual environment tool (venv)

### Steps

1. Clone the backend repo and navigate to it:

   ```bash
   git clone https://github.com/YOUR_USERNAME/needly-backend.git
   cd needly-backend
   python3 -m venv venv
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
