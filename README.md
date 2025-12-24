# EMS BrainWise - Employee Management System

## 📌 Overview
EMS BrainWise is an Employee Management System with a Django REST Framework backend and planned React.js frontend. The system provides RESTful APIs for managing employees, departments, companies, and user accounts with role-based access control.

---

## 🛠 Tech Stack

**Backend:**
- Python 3.12
- Django 4.2+
- Django REST Framework 3.14+
- PostgreSQL (Production)
- SQLite (Development)
- JWT Authentication

**Frontend (Planned):**
- React.js
- Axios
- React Router

---

## 🗂 Project Structure
```
EMS_BrainWise/
├── Backend/
│   ├── ems_brainwise/         # Django project settings
│   ├── user_accounts/         # User management app
│   ├── company/               # Company CRUD app
│   ├── department/            # Department CRUD app
│   ├── employee/              # Employee CRUD app
│   ├── manage.py
│   └── requirements.txt
└── frontend/                  # React frontend (not implemented yet)
```

---

## ⚙️ Prerequisites

- Python 3.12+
- PostgreSQL
- pip
- Git

---

## 🚀 Setup & Installation

### 1. Clone Repository
```bash
git clone https://github.com/jihad696/EMS_BrainWise.git
cd EMS_BrainWise/Backend
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL
```sql
-- Open PostgreSQL shell
psql -U postgres

-- Create database and user
CREATE DATABASE ems_brainwise_db;
CREATE USER ems_admin WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ems_brainwise_db TO ems_admin;
```

### 5. Environment Variables
Create `.env` file in `Backend/`:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=ems_brainwise_db
DB_USER=ems_admin
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Run Server
```bash
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/`

---

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/api/
```

### Authentication
All endpoints require JWT token:
