from flask import Blueprint, request, redirect, render_template
from flask_jwt_extended import set_access_cookies
from validators.auth_validator import check_pass, check_username, check_pass_len
from services.auth_service import register_service, login_service

auth = Blueprint("auth", __name__)
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        username_error = check_username(username)
        if username_error:
            return username_error
        password_error = check_pass(password)
        if password_error:
            return password_error
        leng_error = check_pass_len(password)
        if leng_error:
            return leng_error
        service_error = register_service(username, password)
        if service_error:
            return service_error
        return redirect("/")
    return render_template("register.html")

@auth.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        username_error = check_username(username)
        password_error = check_pass(password)
        if username_error:
            return username_error
        if password_error:
            return password_error
        token, service_error = login_service(username, password)
        if service_error:
            return service_error
        response = redirect("/upload-post")
        set_access_cookies(response, token)
        return response
    return render_template("login.html")

        
        
