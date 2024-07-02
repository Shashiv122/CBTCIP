import os
pip install fpdf
from fpdf import FPDF
import datetime

#creating class named recieptpdf for the details regarding the transaction and storing the transaction details
#initialization of the class  recieptpdf
class reciept_pdf(FPDF):

        #declaring the function that helps to crate the payment reciept
        #declaring the header function
        def head(s):
                s.set_foont("Eras Demi ITC", "B",12)
                s.cell(0,12,"----* XYZ Shop *----",0,1,"c")


        #declaring the footer function of payment reciept
        def foot(s):
                s.set_y(-15)
                s.set_font("Cambria","I",7)
                s.cell(0,12,f'page {s.page_no()}',0,0,"c")


        #declaring the title function of the payment reciept
        def heading(s,h1):
                s.set_font("Arial", "B",18)
                s.cell(0,12,h1,0,1,"c")


        #declaring transaction details function of the paayment details 
        def transact_detail(s,transaction_id, cust_name, date):
                s.set_font("Arial","",13)
                s.cell(0,10,f"TRANSACTION ID:  {transaction_id}",0,1)
                s.cell(0,10,f"CUSTOMER NAME: {cust_name}",0,1)
                s.cell(0,10,f"DATE: {date}",0,1)


        #declaring the item list function for payment reciept
        def itemslist(s,item):
                s.set_font("Calibri (Body)","B",11)
                s.cell(35,5,"Sr No.",1)
                s.cell(35,5,"Item",1)
                s.cell(35,5,"Quantity",1)
                s.cell(35,5,"Unit Price",1)
                s.cell(35,5,"Total Price",1)
                s.ln()
                s.set_font("Arial","",11)
                for i, (Itm, Qty, Unit_P) in enumerate(items,1):
                        s.cell(35,5,str(i),1)
                        s.cell(35,5,Itm,1)
                        s.cell(35,5,str(Qty),1)
                        s.cell(35,5,f'${Unit_P:.2f}',1)
                        s.cell(35,5,f'${Qty*Unit_P:.2f}',1) 
                        s.ln()


        #Declaring the funcion to sum up the total amount of payment Reciept
        def total(s, t):
                s.set_font("Calibri (Body)","B",11)
                s.cell(175,5,"Total Amount",1)
                s.cell(35,5,f"${t:.2f}",1)

 #Declaring the function for generating the payment reciept 
def gen_receipt(transaction_id,cust_name, items):
        pdf=reciept_pdf()
        pdf.add_page()
        pdf.heading("Payment Receipt")
        pdf.transact_detail(transaction_id, cust_name, datetime.date.today().strftime("%d-%m-%Y"))
        pdf.ln(10)
        pdf.itemslist(items)
        tot=sum(Qty*Unit_P for _,Qty,Unit_P in items)
        pdf.total(tot)

        #creating the pdf of receipt
        p_file=f'receipt_{transaction_id}.pdf'
        pdf.output(p_file)


        #path of the pdf
        f_path=os.path.abspath(p_file)
        print(f"Path of the Saved Receipt: {f_path}")

        #printing the payment receipt 
        if os.name=='nt': #used for windows
                os.startfile(f_path,"print")
        elif os.name=='posix': #used for linux and macOS
                os.system(f'lpr{f_path}')
        else:
                print("Printing receipt not supported on this OS!")


#taking input the list of items
x=int(input("Enter the number of items"))
items=[]
for i in range(x):
        item= (input("Enter the item: ")
        qty = int(input("Enter the quantity of item: "))
        unit_P = float(input("inter the amount: "))
        items.append((items,qty,unit_P))


#generrating receipt 
tid=input("Enter the transaction id: ")
name=input("Enter customer name: ")

#Calling function to generate receipt
gen_receipt(tid,name,items)
