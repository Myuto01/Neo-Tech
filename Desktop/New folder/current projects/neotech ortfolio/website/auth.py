from flask import Blueprint, render_template, request, flash,redirect, url_for


auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return '<h1>Login</h1>'