import os
pip install fpdf
import fpdf from FPDF
import datetime

#creating class named recieptpdf for the details regarding the transaction and storing the transaction details
#initialization of the class  recieptpdf
class reciept_pdf(FPDF):

        #declaring the function that helps to crate the payment reciept
        #declaring the header function
        def head(s):
                s.set_foont("Eras Demi ITC", "B",12)
                s.cell(0,12,"----* XYZ Shop *----",1,1,"c")


        #declaring the footer function of payment reciept
        def foot(s):
                s.set_y(-15)
                s.set_font("Cambria","I",7)
                s.cell(0,12,f'page ',s.page_no(),0,0,"c")


        #declaring the title function of the payment reciept
        def heading(s,h1):
                s.set_font("Arial", "B",18)
                s.cell(0,12,h1,0,1,"c")


        #declaring transaction details function of the paayment details 

        
