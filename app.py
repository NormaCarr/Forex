from dotenv import load_dotenv
import os
from flask import Flask,flash,request,render_template, redirect, jsonify, flash, session
from forex_python.converter import CurrencyRates
from flask.helpers import url_for
from flask_debugtoolbar import DebugToolbarExtension
from convert import currency
currency_calc = currency()
currencyR = CurrencyRates()
load_dotenv()
RESPONSES_KEY = os.getenv("RESPONSES_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY']=SECRET_KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)


@app.route("/")
def display_form():
    """Go to the HTML with the form to insert the data"""
    return render_template("dataForm.html")

@app.route("/getarguments")
def form_arguments():
    """Request the arguments from the form"""
    try:
       convFrom=request.args.get("convFrom").upper()
       convTo=request.args.get("convTo").upper()
       amount=request.args.get("amount")
       valCurrency=(convFrom,convTo,amount)

       """Pass the tupla to the method convCurrency in the file convert"""
       verifyvalue=currency_calc.verifyCurrency(valCurrency)
   
       if verifyvalue != "valid_codes":  
         """If the codes aren't valid display the error msg in the HTML"""
         return render_template("displayData.html",result=verifyvalue)
       """Calculate the currency and call to display the result"""
       converted=currency_calc.convCurrency(valCurrency)
       return render_template("displayData.html",valC=valCurrency,result=converted)
    
    except:
        flash("Operation cannot be processed")
        return redirect("/")   
    

