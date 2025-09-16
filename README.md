# Online Learning System (OLS)

An online learning platform built with **Django** that supports three user roles (Student, Instructor, Employee), course enrollment, lessons with multimedia content, reviews, dashboards, and role-based access control.

---

## 🚀 Features

- Custom user model with **roles**: `student`, `instructor`, `employee`
- Profiles for each role (OneToOne relationships)
- Course organization:
  - Categories & Tags
  - Course title, description, price, image
  - Published/draft status
- Lessons per course with video links, file uploads, ordering
- Enrollment by students with progress tracking
- Course review & rating by students
- Dashboards:
  - Student: enrolled courses & progress
  - Instructor: own courses and students
  - Employee: site-wide stats, user management
- Admin interface for all models

---

## 🛠️ Setup & Installation

These steps assume you have **Python 3.13+** installed.

```bash
# 1. Clone the repository
git clone https://github.com/AgileEvilBug/online-learning-system.git
cd online-learning-system

# 2. Create and activate a virtual environment
python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS / Linux:
# source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make migrations & migrate
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (Employee role)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
