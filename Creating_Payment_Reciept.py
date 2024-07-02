pip install fpdf
import os
from fpdf import FPDF
import datetime

# Creating class named ReceiptPDF for the details regarding the transaction and storing the transaction details
class ReceiptPDF(FPDF):

    # Declaring the header function
    def head(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 12, "----* XYZ Shop *----", 0, 1, "C")

    # Declaring the footer function of payment receipt
    def foot(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 7)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, "C")

    # Declaring the title function of the payment receipt
    def heading(self, h1):
        self.set_font("Arial", "B", 18)
        self.cell(0, 12, h1, 0, 1, "C")

    # Declaring transaction details function of the payment details 
    def transact_detail(self, transaction_id, cust_name, date):
        self.set_font("Arial", "", 13)
        self.cell(0, 10, f"TRANSACTION ID: {transaction_id}", 0, 1)
        self.cell(0, 10, f"CUSTOMER NAME: {cust_name}", 0, 1)
        self.cell(0, 10, f"DATE: {date}", 0, 1)

    # Declaring the item list function for payment receipt
    def itemslist(self, items):
        self.set_font("Arial", "B", 11)
        self.cell(35, 10, "Sr No.", 1)
        self.cell(35, 10, "Item", 1)
        self.cell(35, 10, "Quantity", 1)
        self.cell(35, 10, "Unit Price", 1)
        self.cell(35, 10, "Total Price", 1)
        self.ln()
        self.set_font("Arial", "", 11)
        for i, (item, qty, unit_p) in enumerate(items, 1):
            self.cell(35, 10, str(i), 1)
            self.cell(35, 10, item, 1)
            self.cell(35, 10, str(qty), 1)
            self.cell(35, 10, f'${unit_p:.2f}', 1)
            self.cell(35, 10, f'${qty * unit_p:.2f}', 1)
            self.ln()

    # Declaring the function to sum up the total amount of payment receipt
    def total(self, t):
        self.set_font("Arial", "B", 11)
        self.cell(140, 10, "Total Amount", 1)
        self.cell(35, 10, f"${t:.2f}", 1)

# Declaring the function for generating the payment receipt 
def gen_receipt(transaction_id, cust_name, items):
    pdf = ReceiptPDF()
    pdf.add_page()
    pdf.heading("Payment Receipt")
    pdf.transact_detail(transaction_id, cust_name, datetime.date.today().strftime("%d-%m-%Y"))
    pdf.ln(10)
    pdf.itemslist(items)
    total = sum(qty * unit_p for _, qty, unit_p in items)
    pdf.total(total)

    # Creating the pdf of receipt
    pdf_file = f'receipt_{transaction_id}.pdf'
    pdf.output(pdf_file)

    # Path of the pdf
    f_path = os.path.abspath(pdf_file)
    print(f"Path of the Saved Receipt: {f_path}")

    # Printing the payment receipt 
    if os.name == 'nt':  # Used for Windows
        os.startfile(f_path, "print")
    elif os.name == 'posix':  # Used for Linux and macOS
        os.system(f'lpr {f_path}')
    else:
        print("Printing receipt not supported on this OS!")

# Taking input for the list of items
x = int(input("Enter the number of items: "))
items = []
for i in range(x):
    item = input("Enter the item: ")
    qty = int(input("Enter the quantity of item: "))
    unit_p = float(input("Enter the amount: "))
    items.append((item, qty, unit_p))

# Generating receipt 
tid = input("Enter the transaction id: ")
name = input("Enter customer name: ")

# Calling function to generate receipt
gen_receipt(tid, name, items)
