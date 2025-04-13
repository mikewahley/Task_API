#  FastAPI Task Manager API

A simple yet powerful task management REST API built with FastAPI, PostgreSQL, and JWT authentication. Users can register, log in, and manage their personal to-do tasks securely.

---

##  Features

- User Registration & JWT-based Login
- Create / Read / Update / Delete tasks
- Assign tasks to authenticated users only
- Password hashing (with `bcrypt`)
- PostgreSQL for persistent storage
- Swagger UI for interactive API testing
- Modular structure for easy scalability

---

##  Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Auth:** JWT (JSON Web Tokens)
- **Database:** PostgreSQL
- **Environment Management:** python-dotenv
- **ORM:** SQLAlchemy

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/mikewahley/task-api.git
cd task-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```
SECRET_KEY=your_super_secret_key
DATABASE_URL=postgresql://username:password@localhost:5432/yourdb
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

---

##  API Authentication

Authentication is done via JWT tokens.

1. **Register:** `/register`
2. **Login:** `/token`  
   - Body: `username` and `password`
3. Use the returned JWT token in the `Authorization` header:
   ```
   Authorization: Bearer <your_token_here>
   ```

---

##  API Endpoints

### 👤 User

| Method | Endpoint   | Description       |
|--------|------------|-------------------|
| POST   | /register  | Create new user   |
| POST   | /token     | Login & get token |

###  Tasks (Require Auth)

| Method | Endpoint          | Description          |
|--------|-------------------|----------------------|
| POST   | /tasks/           | Create task          |
| GET    | /tasks/           | List user tasks      |
| GET    | /tasks/{task_id}  | Get a specific task  |
| PUT    | /tasks/{task_id}  | Update a task        |
| DELETE | /tasks/{task_id}  | Delete a task        |

---

## 📁 Folder Structure

```
.
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
├── .env
├── requirements.txt
├── README.md
```
