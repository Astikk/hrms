# HRMS – Employee & Attendance Management System

A simple **HR Management System (HRMS)** built using **Django REST Framework** for the backend and **React** for the frontend.  
The system allows managing employees and marking daily attendance.

Test Link : https://hrms-production-5644.up.railway.app/api/

---

## 📌 Features

### Employee Management
- Create employees
- List all employees
- Delete employees

### Attendance Management
- Mark attendance (Present / Absent)
- Prevent duplicate attendance for the same employee on the same date
- View all attendance records

---

## 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- PostgreSQL
- Gunicorn

### Frontend
- React
- Axios
- JavaScript (ES6)

### Deployment
- Railway (Backend + PostgreSQL)

---

## 📂 Project Structure

```bash
hrms/
│
├── backend/
│   ├── employees/
│   ├── attendance/
│   ├── hrms_backend/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── Employee.jsx
│   │   ├── Attendance.jsx
│   │   ├── api.js
│   │   └── App.jsx
│
└── README.md



⚙️ Backend Setup (Local)
1. Clone Repository
git clone <repo-url>
cd backend

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Environment Variables (.env)
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

5. Run Migrations
python manage.py migrate

6. Start Backend Server
python manage.py runserver

🌐 API Endpoints
Employees
GET     /employees/          → List employees
POST    /employees/          → Create employee
DELETE  /employees/<id>/     → Delete employee

Attendance
GET     /attendance/         → List attendance records
POST    /attendance/         → Mark attendance

Author
- Astik singh
