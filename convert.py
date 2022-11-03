from flask.json import jsonify
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask import request
currencyR = CurrencyRates()
currencyC = CurrencyCodes()

class currency:
         
      def verifyCurrency(self,values):
           """Verify the currency and return a tupla with the codes validation and the codes simbols"""    
           curCodes=CurrencyCodes()
           (convFrom,convTo,amount)=values
        
           cv_f=curCodes.get_currency_name(convFrom)
           cv_t=curCodes.get_currency_name(convTo)
           if cv_t and cv_f :
                return "valid_codes"
           else:
              if not cv_t and not cv_f:
                    return "Invalid from",convFrom,"Invalid to",convTo
              elif not cv_f :   
                    return "Invalid from",convFrom,"valid to",cv_t
              else:
                    return "valid from",cv_f,"Invalid to",convTo

    

      def convCurrency(self,valCurrency):
            """Convert the currency"""   
            (convFrom,convTo,amount)=valCurrency   
            c = CurrencyCodes()
            currencyC=c.get_symbol(convTo)
            converted=currencyR.convert(convFrom,convTo,int(amount))
            converted=round(converted,4)
            return currencyC,converted
               
    
    

