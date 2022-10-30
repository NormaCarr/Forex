import unittest

from werkzeug.wrappers.response import Response 
from app import app
from flask import session
from convert import currency

class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True 
    
    def test_verifyValidC(self):
        values=('USD','MXN','45')     
        response=currency.verifyCurrency(self,values)
        self.assertEqual(response,"valid_codes")

    def test_verifyNotValidC(self):
        values=('UPO','SSS','45')           
        response=currency.verifyCurrency(self,values)
        self.assertTupleEqual(response,("Invalid from","UPO","Invalid to","SSS"))
        
    
    def test_verifyValidCvt(self):
        values= ('UPO','MXN','45')         
        response=currency.verifyCurrency(self,values)
        self.assertTupleEqual(response,("Invalid from","UPO","valid to","MXN"))
        

    def test_verifyValidCvf(self):    
        values=('USD','ADA','45')          
        response=currency.verifyCurrency(self,values)
        self.assertTupleEqual(response, ("valid from","USD","Invalid to","ADA"))
        
    def test_convCurrency(self):
        values=('USD','MXN','45')
        response=currency.convCurrency(self,values)
        self.assertTupleEqual(response, ("$",response[1]))
    
    def test_convCurrency(self):
        values=('CAD','USD','6')
        response=currency.convCurrency(self,values)
        self.assertTupleEqual(response, ("$",response[1]))
        


if __name__ == '__main__':
    unittest.main()