from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify
)

from werkzeug.utils import secure_filename
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from db import (
    init_db,
    create_user,
    get_user
)

import os
import uuid

# ==================================================
# APP CONFIG
# ==================================================

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "careerpilot_ai_secret_key"
)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# ==================================================
# DATABASE INIT
# ==================================================

init_db()

# ==================================================
# HELPERS
# ==================================================

def allowed_file(filename):

    return (
        "." in filename and
        filename.rsplit(
            ".", 1
        )[1].lower() in ALLOWED_EXTENSIONS
    )


def generate_dashboard_data():

    return {

        "ats_score": 82,

        "job_readiness": 85,

        "skills": [
            "Python",
            "Flask",
            "SQL",
            "HTML",
            "CSS",
            "Bootstrap"
        ],

        "gaps": [
            "Git",
            "GitHub",
            "Docker",
            "AWS"
        ],

        "career": [
            "Python Developer",
            "Full Stack Developer",
            "Data Analyst",
            "Cloud Engineer",
            "AI Engineer"
        ],

        "roadmap": [

            {
                "topic": "Python Fundamentals",
                "youtube":
                "https://www.youtube.com/results?search_query=python+full+course"
            },

            {
                "topic": "Object Oriented Programming",
                "youtube":
                "https://www.youtube.com/results?search_query=python+oop"
            },

            {
                "topic": "Flask Development",
                "youtube":
                "https://www.youtube.com/results?search_query=flask+tutorial"
            },

            {
                "topic": "SQL Database",
                "youtube":
                "https://www.youtube.com/results?search_query=sql+course"
            }
        ],

        "certifications": [

            "Google Data Analytics",

            "AWS Cloud Practitioner",

            "Meta Backend Developer",

            "IBM Python Certificate",

            "Microsoft Azure Fundamentals"
        ],

        "projects": [

            "CareerPilot AI",

            "Job Portal",

            "Hospital Management System",

            "Online Examination System",

            "E-Library Management"
        ],

        "technical_questions": [

            "What is Flask?",

            "What is REST API?",

            "Difference between List and Tuple?",

            "Explain OOP Concepts.",

            "What is SQL JOIN?"
        ],

        "hr_questions": [

            "Tell me about yourself.",

            "Why should we hire you?",

            "What are your strengths?",

            "What are your weaknesses?",

            "Where do you see yourself in 5 years?"
        ]
    }

# ==================================================
# HOME
# ==================================================

@app.route("/")
def home():
    return render_template("home.html")

# ==================================================
# FEATURES
# ==================================================

@app.route("/features")
def features():
    return render_template("features.html")

# ==================================================
# ROADMAP
# ==================================================

@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")

# ==================================================
# CAREERS
# ==================================================

@app.route("/careers")
def careers():
    return render_template("careers.html")

# ==================================================
# CONTACT
# ==================================================

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ==================================================
# REGISTER
# ==================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        email = request.form.get(
            "email"
        )

        password = request.form.get(
            "password"
        )

        hashed_password = (
            generate_password_hash(
                password
            )
        )

        try:

            create_user(
                username,
                email,
                hashed_password
            )

            flash(
                "Registration Successful!",
                "success"
            )

            return redirect(
                url_for("login")
            )

        except Exception:

            flash(
                "Username or Email already exists",
                "danger"
            )

    return render_template(
        "register.html"
    )

# ==================================================
# LOGIN
# ==================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        password = request.form.get(
            "password"
        )

        user = get_user(
            username
        )

        if user and check_password_hash(
            user["password"],
            password
        ):

            session["user"] = username

            flash(
                "Login Successful",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid Username or Password",
            "danger"
        )

    return render_template(
        "login.html"
    )

# ==================================================
# DASHBOARD
# ==================================================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        flash(
            "Please login first",
            "warning"
        )

        return redirect(
            url_for("login")
        )

    result = generate_dashboard_data()

    return render_template(
        "dashboard.html",
        username=session["user"],
        result=result
    )

# ==================================================
# RESUME UPLOAD
# ==================================================

@app.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload():

    if "user" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        file = request.files.get(
            "resume"
        )

        if not file:

            flash(
                "Please select a file",
                "warning"
            )

            return redirect(
                request.url
            )

        if file.filename == "":

            flash(
                "No file selected",
                "warning"
            )

            return redirect(
                request.url
            )

        if not allowed_file(
            file.filename
        ):

            flash(
                "Only PDF files allowed",
                "danger"
            )

            return redirect(
                request.url
            )

        filename = (
            f"{uuid.uuid4()}_"
            f"{secure_filename(file.filename)}"
        )

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        flash(
            "Resume uploaded successfully",
            "success"
        )

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "upload.html"
    )

# ==================================================
# CHATBOT PAGE
# ==================================================

@app.route("/chatbot")
def chatbot():

    if "user" not in session:

        flash(
            "Please login first",
            "warning"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "chatbot.html",
        username=session["user"]
    )


# ==================================================
# CHATBOT AI API
# ==================================================

@app.route(
    "/chatbot/ask",
    methods=["POST"]
)
def chatbot_ask():

    try:

        data = request.get_json()

        message = data.get(
            "message",
            ""
        )

        message_lower = message.lower()

        if "java" in message_lower:

            response = """
# Java Developer Roadmap

1. Learn Core Java
2. Learn OOP Concepts
3. Learn Collections Framework
4. Learn JDBC
5. Learn Spring Boot
6. Build Projects
7. Learn Git & GitHub
8. Prepare for Interviews
"""

        elif "python" in message_lower:

            response = """
# Python Developer Roadmap

1. Learn Python Fundamentals
2. Learn OOP
3. Learn Flask or Django
4. Learn SQL
5. Build Projects
6. Learn APIs
7. Deploy Applications
"""

        else:

            response = f"""
# CareerPilot AI

You asked:

**{message}**

CareerPilot AI is currently running in demo mode.

Integrate Gemini API inside
the chatbot_ask() function
for real AI responses.
"""

        return jsonify({
            "response": response
        })

    except Exception as e:

        return jsonify({
            "response":
            f"Server Error: {str(e)}"
        }), 500

# ==================================================
# LOGOUT
# ==================================================

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully",
        "info"
    )

    return redirect(
        url_for("home")
    )

# ==================================================
# ERROR HANDLERS
# ==================================================

@app.errorhandler(404)
def page_not_found(error):

    return (
        render_template(
            "404.html"
        ),
        404
    )


@app.errorhandler(413)
def file_too_large(error):

    flash(
        "File size exceeds 5 MB",
        "danger"
    )

    return redirect(
        url_for("upload")
    )

# ==================================================
# RUN APP
# ==================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )