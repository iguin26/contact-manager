# 📘 Contact Manager – Django Project


## 📋 Description

Contact Manager is a Django-based web application that allows users to create, view, edit, and delete phone contacts. The system supports user authentication and permission-based access to contact management. 

Additionally, contacts can be populated via a script located at `utils/create_contacts.py`. This script is designed to add **sample contacts** to the database for testing or populating the contact list. These contacts do not have an **owner**, so they **cannot be edited or deleted** by users. They exist as part of the system's initial data and are intended solely for display or testing purposes.




## ⚙️ Features

- 📖 **View contact list** – Accessible to all users, logged in or not.
  
- ➕ **Create new contacts** – Anyone can create contacts, even without logging in.
  
- ✏️ **Edit contacts** – Only available if the user is logged in, and only for contacts they created.
  
- ❌ **Delete contacts** – Only available if the user is logged in, and only for contacts they created.
  
- 🔐 **Authentication system** – Built-in Django login system.
  
- 💾 **SQLite database** – Simple and effective local data storage.

- 📝 **Create contacts via script** – The `utils/create_contacts.py` script populates the contact list with **sample contacts**. These contacts do not have an owner and cannot be edited or deleted by any user.



## 🔐 Permissions Summary

| Action                   | Requires Login | Owner-Only | Created via Script |
| ------------------------ | -------------- | ---------- | ------------------ |
| View contacts            | ❌             | ❌         | ✅                 |
| Create contacts          | ❌             | ❌         | ✅                 |
| Edit contacts            | ✅             | ✅         | ❌                 |
| Delete contacts          | ✅             | ✅         | ❌                 |


## 🚀 Technologies Used

- **Python** – The programming language used for the project.
  
- **Django** – The web framework used to build the backend.
  
- **SQLite** – The database used for local storage.
  
- **HTML/CSS** – Used for structuring and styling the frontend (via Django templates).


## 🛠️ Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/iguin26/contact-manager.git
    ```

2. **Navigate into the project folder**:
    ```bash
    cd contact-manager
    ```

3. **Create and activate a virtual environment**:
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

4. **Install dependencies** from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations** to set up the database:
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

Once the server is running, open your browser and go to [http://localhost:8000](http://localhost:8000) to access the app.

## 🔌 API Endpoints

### **Home**
- **URL**: `/`
- **Description**: The home page of the application that lists all contacts.

### **Search Contacts**
- **URL**: `/search/`
- **Description**: Page to search for contacts.

### **Contact Details**
- **URL**: `/contact/<int:contact_id>/detail/`
- **Description**: Displays details of a specific contact.

### **Edit Contact**
- **URL**: `/contact/<int:contact_id>/update/`
- **Description**: Page to edit a contact's information.

### **Delete Contact**
- **URL**: `/contact/<int:contact_id>/delete/`
- **Description**: Deletes a specific contact.

### **Create Contact**
- **URL**: `/contact/create/`
- **Description**: Page to create a new contact.

---

### **User Endpoints**

#### **User Registration**
- **URL**: `/user/create/`
- **Description**: Page for new users to register.

#### **User Login**
- **URL**: `/user/login/`
- **Description**: Login page for users to access their accounts.

#### **User Logout**
- **URL**: `/user/logout/`
- **Description**: Logs out the currently logged-in user.

#### **User Profile Update**
- **URL**: `/user/update/`
- **Description**: Page for users to update their profile information.

