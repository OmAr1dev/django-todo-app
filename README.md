# 📝 Django To-Do App

A Django-based To-Do List application with **custom user authentication** and a clean **Bootstrap 5 interface**.  
Users can **sign up, log in, create, update, and delete tasks**, all while enjoying a responsive, modern UI.

---

## 🔹 Features

- Custom user authentication (signup, login, logout)
- Add, update, delete tasks (authenticated users only)
- Tasks show status: Completed / Pending
- Bootstrap 5 responsive UI with styled navbar
- Favicon and dynamic navbar links based on login status
- Secure logout via POST request
- Only task owners can edit/delete their tasks

---

## 🔹 Installation (Windows CMD)

1. **Clone the repository**

```cmd
git clone https://github.com/OmAr1dev/django-todo-app.git
cd django-todo-app
```

2. **Create a virtual environment**

```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```cmd
pip install -r requirements.txt
```

4. **Apply migrations**

```cmd
python manage.py migrate
```

5. **Run the development server**

```cmd
python manage.py runserver
```

6. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔹 Usage

1. **Sign up** for a new account or **log in** with an existing account.
2. **Add a task** using the "+ Add Task" button in the navbar.
3. **Edit or delete tasks** (only your own tasks can be modified).
4. **Logout** securely from the navbar.

---

## 🔹 Project Structure

```
django-todo-app/
├─ accounts/       # Custom auth app
├─ todo/           # Task management app
├─ templates/      # HTML templates (base, login, signup, tasks)
├─ static/         # Static files (CSS, images, favicon)
├─ db.sqlite3      # SQLite database
├─ manage.py
├─ requirements.txt
```

---

## 🔹 License

This project is licensed under the **MIT License**.

---

## 🔹 Author

- [OmAr1dev](https://github.com/OmAr1dev)