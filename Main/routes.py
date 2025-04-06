from flask import Flask, render_template, url_for, flash, redirect, request
from Main.form import BookForm
from Main.recomm import recom, bookdisp
from Main.models import User
from flask_sqlalchemy import SQLAlchemy
from Main import app,db,bcrypt
from flask_mail import Message
import secrets
import os
from PIL import Image
import pandas as pd
import numpy as np
from flask_login import login_user, current_user, logout_user, login_required
import csv
from csv import writer
posts = [
    {
    'author' : 'Aswin Kumar Gamango',
    'title' : 'Lovely Professional University'
    }
]

@app.route("/")
@app.route("/home")
def home():
    list1=bookdisp()
    return render_template('home.html',content=list1)

@app.route("/recommender", methods=["GET", "POST"])
def recommender():
    form = BookForm()
    final = []
    no_result = False

    if form.validate_on_submit():
        bookname = form.bookname.data
        try:
            final = recom(bookname)  # This returns the recommended books
            if not final:
                no_result = True
        except Exception as e:
            print("Error:", e)
            no_result = True

    return render_template("recommender.html", form=form, final=final, no_result=no_result)