from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    phone = TextField("phone")
    address = TextAreaField("address")
    item = TextAreaField("item")
    price = TextAreaField("price")
    description = TextAreaField("description")
    
