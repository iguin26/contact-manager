📘 Contact Manager – Django Project
📋 Description

Contact Manager is a Django-based web application that allows users to create, view, edit, and delete phone contacts. The system supports user authentication and permission-based access to contact management.
⚙️ Features

    📖 View contact list – Accessible to all users, logged in or not

    ➕ Create new contacts – Anyone can create contacts, even without logging in

    ✏️ Edit contacts – Only available if the user is logged in, and only for contacts they created

    ❌ Delete contacts – Only available if the user is logged in, and only for contacts they created

    🔐 Authentication system – Built-in Django login system

    💾 SQLite database – Simple and effective local data storage

🔐 Permissions Summary
Action Requires Login Owner-Only
View contacts ❌ ❌
Create contacts ❌ ❌
Edit contacts ✅ ✅
Delete contacts ✅ ✅

🚀 Technologies Used

    Python

    Django

    SQLite

    HTML/CSS (Django templates)

🛠️ Setup Instructions

    Clone the repository:

git clone https://github.com/seu-usuario/contact-manager.git

Navigate into the project folder:

cd contact-manager

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # ou venv\Scripts\activate no Windows

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

    python manage.py runserver
