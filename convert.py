from flask.json import jsonify
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask import request
currencyR = CurrencyRates()
currencyC = CurrencyCodes()

"""Initialize a list with the valid codes"""
listCurrecyCodes = ["EUR","Euro", "IDR", "BGN","ILS",
                    "GBP", "DKK", "CAD", "JPY", "HUF",
                    "RON", "MYR", "SEK", "SGD", "HKD",
                    "AUD", "CHF", "KRW", "CNY", "TRY",
                    "HRK", "NZD", "THB", "USD", "NOK",
                    "RUB", "INR", "MXN", "CZK", "BRL",
                    "PLN", "PHP", "ZAR"]


class currency():
         
      def verifyCurrency(this,values):
           """Verify the currency and return a tupla with the codes validation and the codes simbols"""    
           
           cv_f= values[0]
           cv_t=values[1]
    
           if cv_t in listCurrecyCodes and cv_f in listCurrecyCodes:
                return "valid_codes"
           else:
              if cv_t not in listCurrecyCodes and cv_f not in listCurrecyCodes:
                    return "Invalid from",cv_f,"Invalid to",cv_t
              elif cv_f not in listCurrecyCodes:   
                    
                    return "Invalid from",cv_f,"valid to",cv_t
              else:
                        
                    return "valid from",cv_f,"Invalid to",cv_t

    

      def convCurrency(this,valCurrency):
            """Convert the currency"""      
            c = CurrencyCodes()
            currencyC=c.get_symbol(valCurrency[1])
            converted=currencyR.convert(valCurrency[0],valCurrency[1],int(valCurrency[2]))
            converted=round(converted,4)
            return currencyC,converted
               
    
    

