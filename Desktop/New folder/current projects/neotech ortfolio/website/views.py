from flask import Blueprint, render_template,flash,request,Flask,session,sessions
from . import models
from datetime import datetime
from . import db


views = Blueprint('views', __name__)

from .models import Meeting



@views.route('/', methods =['GET', 'POST'])
def home():
   

    return render_template('page.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/team')
def team():
    return render_template('team.html')


@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/terms')
def terms():
    return render_template('terms.html')

@views.route('/policy')
def policy():
    return render_template('policy.html')

@views.route('/book_meeting', methods=['POST','GET'])
def booking():
    if request.method == "POST":
        # process the form data
        name = request.form.get('name')
        email =  request.form.get('email')
        meeting_date = datetime.strptime(request.form.get('meeting_date'), '%Y-%m-%dT%H:%M')

        # create a new meeting object and save it to the database
        meeting = Meeting(name=name, email=email, meeting_date=meeting_date)
        db.session.add(meeting)
        db.session.commit()

        # Redirect or render a success message
        return render_template('success.html')

    # Handle the GET request for displaying the form
    return render_template('booking.html')

 

@views.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@views.route('/products')
def products():
    return render_template('products.html')

@views.route('/refund policy')
def refund_policy():
    return render_template('refund.html')