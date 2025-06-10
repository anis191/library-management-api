# Library Management API - REST API for a Library Management System

![Django](https://img.shields.io/badge/Django-5.1.7-green)
![DRF](https://img.shields.io/badge/DRF-3.15.2-red)
![JWT](https://img.shields.io/badge/JWT_Authentication-5.5.0-yellow)

Library Management API is a secure, scalable RESTful API built with Django and Django REST Framework. It provides comprehensive features to manage books, users, borrowing/returning workflows, and library operations efficiently. The system supports both user and admin roles with JWT-based authentication and rich API documentation.

---

## 🌐 Live Deployment

- 🔗 **Base URL** – [https://library-management-api-coral.vercel.app/api/v1/auth/](https://library-management-api-coral.vercel.app/api/v1/auth/)
- 🔗 **API Root** – [https://library-management-api-coral.vercel.app/api/v1/](https://library-management-api-coral.vercel.app/api/v1/)

---

## 🚀 Key Features

- **JWT Authentication** – Secure token-based authentication with refresh support  
- **User Registration & Management** – Sign up, login, and member profile management  
- **Book Catalog** – Full CRUD operations on books, authors, and categories  
- **Borrowing System** – Borrow and return books with real-time tracking  
- **Admin Capabilities** – Manage users, books, borrowing rules, and reports  
- **Advanced Filtering** – Filter books by category, author, availability, and more  
- **Search & Ordering** – Search books by title, author, ISBN; order by published date or popularity  
- **API Documentation** – Integrated Swagger and ReDoc for intuitive API exploration  

---

## 🛠️ Technologies Used

- **Backend**: Django 5.1.7  
- **REST Framework**: Django REST Framework 3.15.2  
- **Authentication**: JWT (SimpleJWT), Djoser  
- **API Docs**: drf-yasg (Swagger/ReDoc)  
- **Database**: PostgreSQL (production), SQLite (development)  
- **Filtering**: django-filter  
- **Debugging**: django-debug-toolbar  
- **Dependencies**: See [requirements.txt](requirements.txt)  

---

## 📚 API Documentation

- 🔍 **Swagger UI** – [https://library-management-api-coral.vercel.app/swagger/](https://library-management-api-coral.vercel.app/swagger/)  
- 📘 **ReDoc UI** – [https://library-management-api-coral.vercel.app/redoc/](https://library-management-api-coral.vercel.app/redoc/)  

---

## 🔧 Installation & Local Setup

1. **Clone the repository**
   ```bash
    git clone https://github.com/anis191/library-management-api.git
    cd library-management-api
   ```
2. **Create & activate virtual environment**
   ```bash
   python -m venv .example_env
   # For Windows
   source .example_env/Scripts/activate
   # For macOS/Linux
   source .example_env/bin/activate
    ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**
   ```bash
   python manage.py migrate
   ```
5. **Start development server**
   ```bash
   python manage.py runserver
   ```
* API Access:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) *(Localhost only)*

## 🔐 Authentication
This API uses **JWT (JSON Web Tokens)** for secure, stateless user authentication.

### 📌 Authentication Endpoints
**Base URL:** `http://127.0.0.1:8000/api/v1` (Localhost)

| Method | Endpoint            | Description                      |
|--------|---------------------|--------------------------------|
| POST   | `/auth/jwt/create/` | Login – Obtain access & refresh tokens |
| POST   | `/auth/jwt/refresh/`| Refresh access token            |
| POST   | `/auth/users/`      | Register a new user (Sign up)   |

> 💡 **Note:** After registration, use the `/auth/jwt/create/` endpoint to log in and receive your JWT tokens.

## 📂 Project Structure

`library-management-api/`  
&emsp;├── `library_management/` – Core settings & configs  
&emsp;│&emsp;├── `__init__.py`  
&emsp;│&emsp;├── `settings.py`  
&emsp;│&emsp;├── `urls.py`  
&emsp;│&emsp;└── `wsgi.py`  
&emsp;│  
&emsp;├── `api/` – Core API logic and views  
&emsp;│&emsp;├── `views.py`  
&emsp;│&emsp;├── `urls.py`  
&emsp;│&emsp;└── `models.py`  
&emsp;│  
&emsp;├── `borrow/` – Borrowing and returning books logic  
&emsp;│&emsp;└── *(models, views, serializers)*  
&emsp;│  
&emsp;├── `library/` – Book, author, category management  
&emsp;│&emsp;└── *(models, views, serializers)*  
&emsp;│  
&emsp;├── `fixtures/` – Sample data for demo and testing  
&emsp;│&emsp;└── `books_data.json` *(demo data)*  
&emsp;│  
&emsp;├── `users/` – Custom user management and authentication  
&emsp;│&emsp;└── *(models, views, serializers, urls)*  
&emsp;│  
&emsp;├── `.gitignore`  
&emsp;├── `requirements.txt`  
&emsp;├── `manage.py`  
&emsp;└── `README.md`

## 🤝 Contributing

Contributions help make this project better and are always welcome!

### How to Contribute

- ⭐ Star the repo  
- 🍴 Fork the project  
- 📥 Clone your fork  
- 💡 Create a feature branch: `git checkout -b feature/awesome-feature`  
- ✅ Commit your changes: `git commit -m 'Add some feature'`  
- 📤 Push your branch: `git push origin feature/awesome-feature`  
- 🛠️ Open a Pull Request

Ensure your code follows the project standards and passes all tests.

## 💻 Author

[**Anisul Alam**](https://github.com/anis191)  
Backend Developer | Django & REST APIs  
[🔗 LinkedIn](https://www.linkedin.com/in/anisul-alam-a330042a9/)

---