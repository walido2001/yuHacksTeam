from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    phone = TextField("Phone Number")
    address = TextAreaField("Address")
    item = TextAreaField("Item")
    price = TextAreaField("Price")
    description = TextAreaField("Description")
    submit = SubmitField("Send")
