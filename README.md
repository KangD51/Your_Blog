# Your_Blog

A full-featured blog web application built with Flask, allowing users to register, log in, create and manage posts, update their profiles, and more. This project demonstrates core concepts of Flask, including blueprints, authentication, database models, forms, and template rendering.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Database Models](#database-models)
- [Forms](#forms)
- [Routes & Functionality](#routes--functionality)
- [Templates](#templates)
- [Static Files](#static-files)
- [Migrations](#migrations)
- [How It Works](#how-it-works)
- [Possible Improvements](#possible-improvements)
- [License](#license)

---

## Features

- User registration and login (with hashed passwords)
- User authentication and session management
- Create, update, and delete blog posts
- View all posts and individual post pages
- Update user profile and profile picture
- Flash messages for user feedback
- Responsive design with custom CSS
- Database migrations with Flask-Migrate

---

## Project Structure

```
Your_Blog/
│
├── flaskblog/
│   ├── __init__.py         # App factory, extension initialization
│   ├── models.py           # SQLAlchemy models (User, Post)
│   ├── forms.py            # WTForms (registration, login, post, account)
│   ├── routes.py           # All route handlers (views)
│   ├── static/
│   │   ├── main.css        # Custom CSS
│   │   ├── yourblog.png    # Logo/image
│   │   ├── yourblogTran.png# Logo/image
│   │   └── profile_pics/   # Uploaded profile pictures
│   └── templates/
│       ├── layout.html     # Base template
│       ├── home.html       # Home page (all posts)
│       ├── about.html      # About page
│       ├── register.html   # Registration form
│       ├── login.html      # Login form
│       ├── account.html    # User account/profile
│       ├── create_post.html# Create/update post
│       └── post.html       # Single post view
│
├── instance/
│   └── site.db             # SQLite database file
│
├── migrations/             # Database migration scripts
│
└── run.py                  # App entry point
```

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Your_Blog
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   *(Create a `requirements.txt` with the following if not present)*
   ```
   Flask
   Flask-SQLAlchemy
   Flask-Migrate
   Flask-Bcrypt
   Flask-Login
   Flask-WTF
   Pillow
   ```
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

---

## Database Models

### **User**
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email
- `image_file`: Profile picture filename (default: `default.jpg`)
- `password`: Hashed password
- `posts`: Relationship to `Post` (one-to-many)

### **Post**
- `id`: Primary key
- `title`: Post title
- `date_posted`: Timestamp (default: now)
- `content`: Post content
- `user_id`: Foreign key to `User`

---

## Forms

All forms use Flask-WTF and WTForms for validation and CSRF protection.

- **RegistrationForm**: Username, email, password, confirm password
- **LoginForm**: Email, password, remember me
- **UpdateAccountForm**: Username, email, profile picture
- **PostForm**: Title, content

---

## Routes & Functionality

- `/` or `/home`: Home page, shows all posts
- `/about`: About page
- `/register`: User registration
- `/login`: User login
- `/logout`: Log out
- `/account`: View/update user profile (login required)
- `/post/new`: Create a new post (login required)
- `/post/<post_id>`: View a single post
- `/post/<post_id>/update`: Update a post (author only)
- `/post/<post_id>/delete`: Delete a post (author only)

**Key Features:**
- **Authentication**: Only logged-in users can create, update, or delete posts.
- **Authorization**: Only the author can edit or delete their posts.
- **Profile Picture Upload**: Users can upload a new profile picture, which is resized and saved securely.
- **Flash Messages**: User actions (register, login, post, update) provide feedback via flash messages.

---

## Templates

- **layout.html**: Base template, includes navigation and flash messages.
- **home.html**: Lists all posts.
- **about.html**: Static about page.
- **register.html**: Registration form.
- **login.html**: Login form.
- **account.html**: User profile and update form.
- **create_post.html**: Form for creating or updating posts.
- **post.html**: Displays a single post.

Templates use Jinja2 for dynamic content and template inheritance.

---

## Static Files

- **main.css**: Custom styles for the app.
- **profile_pics/**: Uploaded user profile images.
- **yourblog.png**, **yourblogTran.png**: App logos/images.

---

## Migrations

Database migrations are managed with Flask-Migrate (Alembic). Migration scripts are in the `migrations/` directory.  
To create or upgrade the database, use:
```bash
flask db migrate -m "Message"
flask db upgrade
```

---

## How It Works

1. **App Initialization**:  
   `flaskblog/__init__.py` sets up the Flask app, configures the database, initializes extensions (SQLAlchemy, Migrate, Bcrypt, LoginManager), and imports routes.

2. **User Authentication**:  
   Users register and log in. Passwords are hashed with Bcrypt. Flask-Login manages sessions and restricts access to certain routes.

3. **CRUD Operations**:  
   Authenticated users can create, update, and delete their own posts. All posts are visible on the home page.

4. **Profile Management**:  
   Users can update their username, email, and profile picture. Uploaded images are resized and stored securely.

5. **Forms & Validation**:  
   All user input is validated using WTForms, with custom validation for unique usernames/emails.

6. **Templates & Static Files**:  
   Jinja2 templates render dynamic content. Static files (CSS, images) are served from the `static/` directory.

---

## Possible Improvements

- Add pagination for posts
- Add comments or tags to posts
- Implement search functionality
- Add email confirmation for registration
- Use environment variables for configuration (e.g., secret key, database URI)
- Add automated tests (unit/integration)
- Deploy to a cloud platform (Heroku, AWS, etc.)

---

## License

This project is for educational purposes.  
Feel free to use, modify, and share!

---
<img width="1440" alt="Screenshot 2025-07-01 at 6 27 13 AM" src="https://github.com/user-attachments/assets/57130250-cde3-46eb-a0bf-6258defd75bc" />
<img width="1440" alt="Screenshot 2025-07-01 at 6 26 31 AM" src="https://github.com/user-attachments/assets/73907bfa-d07b-4223-a27e-007112bac39d" />
<img width="1440" alt="Screenshot 2025-07-01 at 6 26 48 AM" src="https://github.com/user-attachments/assets/c846d39e-fff4-40e4-a0d5-c1be4be832f8" />
<img width="1440" alt="Screenshot 2025-07-01 at 6 27 00 AM" src="https://github.com/user-attachments/assets/048b50c0-c126-431d-ab63-f77d911b3e0c" />
<img width="1440" alt="Screenshot 2025-07-01 at 6 25 52 AM" src="https://github.com/user-attachments/assets/84d1860b-b71e-4fc5-80f1-7bc100c91ab9" />



