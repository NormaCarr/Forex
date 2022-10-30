from typing import ValuesView
from flask import Flask,flash,request,render_template, redirect, jsonify, flash, session
from forex_python.converter import CurrencyRates
from flask.helpers import url_for
from flask_debugtoolbar import DebugToolbarExtension
from convert import currency
currency_calc = currency()
currencyR = CurrencyRates()

RESPONSES_KEY = "responses"
app = Flask(__name__)
app.config['SECRET_KEY']="super-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)


@app.route("/")
def display_form():
    """Go to the HTML with the form to insert the data"""
    return render_template("dataForm.html")

@app.route("/getarguments")
def form_arguments():
    """Request the arguments from the form"""
    convFrom=request.args.get("convFrom").upper()
    convTo=request.args.get("convTo").upper()
    amount=request.args.get("amount")
    valCurrency=(convFrom,convTo,amount)

    """Pass the dictionary to the method convCurrency in the file convert"""
    verifyvalue=currency_calc.verifyCurrency(valCurrency)
   
    if verifyvalue != "valid_codes":  
  
       """If the codes aren't valid display the error msg in the HTML"""
       return render_template("displayData.html",result=verifyvalue)
    """Calculate the currency and call to display the result"""
    converted=currency_calc.convCurrency(valCurrency)
    
    return render_template("displayData.html",valC=valCurrency,result=converted)

    

