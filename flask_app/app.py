
from flask import Flask, render_template
from forms import ContactForm
from flask import request
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contat
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        item = request.form["item"]
        price = request.form["price"]
        description = request.form["description"]

        res = pd.DataFrame({'name':name, 'email':email, 'email':email ,\
        'phone':phone, 'address': address, 'item':item, \
        'price': price, 'description': description}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("The data are saved !")
        return render_template('borrowing.html', form=form)
    else:
        return render_template('borrowing.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
