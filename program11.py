from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


# ==========================================================
# GLOBAL VARIABLES
# ==========================================================

user_name = "No Data"
user_account_type = "No Data"
loan_type = "No Loan"



#**************************************************************************************

def Dashboard():
    messagebox.showinfo("Dashboard", "Dashboard Opened")

def create_account_window():
    messagebox.showinfo("Account", "Create Account Window")

def view_account_window():
    messagebox.showinfo("Account", "View Account Window")

def update_account_window():
    messagebox.showinfo("Account", "Update Account Window")

def delete_account_window():
    messagebox.showinfo("Account", "Delete Account Window")

def mini_statement_window():
    messagebox.showinfo("Mini Statement", "Mini Statement Window")

def transaction_history_window():
    messagebox.showinfo("Transactions", "Transaction History Window")

def balance_enquiry_window():
    messagebox.showinfo("Balance", "Balance Enquiry Window")

def fund_transfer_window():
    messagebox.showinfo("Transfer", "Fund Transfer Window")

def bank_transfer_window():
    messagebox.showinfo("Transfer", "Bank Transfer Window")

def upi_transfer_window():
    messagebox.showinfo("Transfer", "UPI Transfer Window")

def mobile_transfer_window():
    messagebox.showinfo("Transfer", "Mobile Transfer Window")

def neft_transfer_window():
    messagebox.showinfo("Transfer", "NEFT Transfer Window")

def rtgs_transfer_window():
    messagebox.showinfo("Transfer", "RTGS Transfer Window")

def imps_transfer_window():
    messagebox.showinfo("Transfer", "IMPS Transfer Window")

def show_home_loan():
    messagebox.showinfo("Loan", "Home Loan Details")

def show_car_loan():
    messagebox.showinfo("Loan", "Car Loan Details")

def show_personal_loan():
    messagebox.showinfo("Loan", "Personal Loan Details")

def atm_services_window():
    messagebox.showinfo("Services", "ATM Services")

def cheque_book_request_window():
    messagebox.showinfo("Services", "Cheque Book Request")

def passbook_update_window():
    messagebox.showinfo("Services", "Passbook Update")

def credit_card_services_window():
    messagebox.showinfo("Services", "Credit Card Services")

def debit_card_services_window():
    messagebox.showinfo("Services", "Debit Card Services")

def net_banking_window():
    messagebox.showinfo("Services", "Net Banking")

def mobile_banking_window():
    messagebox.showinfo("Services", "Mobile Banking")

def change_password_window():
    messagebox.showinfo("Security", "Change Password")

def reset_pin_window():
    messagebox.showinfo("Security", "Reset PIN")

def customer_care_window():
    messagebox.showinfo("Support", "Customer Care")

def email_support_window():
    messagebox.showinfo("Support", "Email Support")

def branch_locator():
    messagebox.showinfo("Support", "Branch Locator")

def head_office_window():
    messagebox.showinfo("Support", "Head Office")

def about_bank():
    messagebox.showinfo("About", "About MyBank")


#==================================================================
                                         #First_Page
#==================================================================

def First_page():

    root = tk.Tk()
    root.title("MyBank ")
    root.geometry("1500x800")
    root.resizable(False, False)
    icon=tk.PhotoImage(file="image3.png")
    root.iconphoto(True,icon)
    
    # -------- Background Image --------
    img=tk.PhotoImage(file="image6.png")
    tk.Label(root,image=img).pack()
    img1=tk.PhotoImage(file="D:\\python\\safety (2).png")
    img2=tk.PhotoImage(file="D:\\python\\shield.png")
    img3=tk.PhotoImage(file="D:\\python\\24-hours-support.png")
    img4=tk.PhotoImage(file="D:\\python\\social-media (2).png")
    img5=tk.PhotoImage(file="D:\\python\\transference.png")
    # Background image
    bg = tk.Label(root)
    bg.pack()

# Text on image at custom position
    Label( root, text="🏦MyBank 🏦", font=("Imprint MT Shadow", 50, "bold"), fg="white", bg="#8A1A4A").place(x=10, y=10,width=1480)
    Label( root, image=img4,  compound="right",text="Start Simplifying Your\nFinance Today", font=("Arial",35,"bold"), fg="white", bg="#000245").place(x=0, y=650,width=1500)
    Label( root,image=img5,  compound="left" ,font=("Arial",35,"bold"), fg="white", bg="#000245").place(x=20, y=650,width=100)
    Label( root,image=img4,  compound="left" ,font=("Arial",35,"bold"), fg="white", bg="#000245").place(x=310, y=650,width=130)
    
    Label( root, text="Welcome To MyBank", font=("Imprint MT Shadow", 20, "bold"), fg="white", bg="#367588").place(x=295, y=175,width=350,height=50)
    Label( root, text="Safe -> Secure -> Fast Banking  ", font=("Algerian", 14, "bold"), fg="white", bg="red").place(x=295, y=240,width=350,height=30)
    Label( root,image=img1,  compound="left",text="  Safe & Secure    ", font=("Arial", 15, "bold"), fg="white", bg="Skyblue").place(x=295, y=290,width=300,height=40)
    Label( root,text="Your securty is our\ntop priority.   ", font=("Arial", 12), fg="white", bg="skyblue").place(x=295, y=320,width=300,height=40)
    Label( root, image=img2,compound="left",text="  Fast & Reliable ", font=("Arial", 15, "bold"), fg="white", bg="skyblue").place(x=295, y=380,width=300,height=40)
    Label( root, text="Providing solution\n  that save your time ", font=("Arial", 12), fg="white", bg="skyblue").place(x=295, y=410,width=300,height=40)
    Label( root, image=img3,compound="left",text="  24|7 Support    ", font=("Arial", 15, "bold"), fg="white", bg="skyblue").place(x=295, y=480,width=300,height=40)
    Label( root, text="  We are here for you\n      anytime anywhere        ", font=("Arial", 12), fg="white", bg="skyblue").place(x=295, y=510,width=300,height=40)
   
    # -------- Login Frame --------
    frame = tk.Frame(root, bg="#00124F", bd=2)
    frame.place(x=700, y=120, width=380, height=500)

    # -------- Bank Icon --------
    tk.Label(frame,text="🏦",font=("Arial", 40),bg="#205757",fg="white" ).pack(pady=20)
    
    # -------- Customer ID --------
    tk.Label(frame ,text="Customer ID :--",font=("Arial", 20,"bold"),bg="#00124F",fg="white").place(x=0,y=90)
    customer = tk.Entry(frame, font=("Arial", 14),width=25, bg="#7B68EE",fg="white",bd=0)
    customer.insert(0, "Customer ID")
    customer.pack(pady=30, ipady=8)

    # -------- Password --------
    tk.Label(frame ,text="Password :--",font=("Arial", 20,"bold"),bg="#00124F",fg="white").place(x=0,y=220)
    password = tk.Entry(frame,font=("Arial", 14),width=25,bg="#7B68EE",fg="white",bd=0,show="*")
    password.insert(0, "Password")
    password.pack(pady=60, ipady=8)

   
    # ==================================================
    # LOGIN BUTTON FUNCTION
    # ==================================================

    def login():
  
        customer_id = customer.get()
        user_password = password.get()
    
        # Check login details
        if  customer_id =="Prachi"  and user_password == "1234" :

            messagebox.showinfo("Login", "Login Successful")
      
    
            root.destroy()      # Close first window

            fun()               # Open second window
          
        else:
            messagebox.showerror("Login", "Invalid Customer ID or Password")


    # Login Button
    tk.Button(frame,text="Login",font=("Arial", 14, "bold"),bg="blue",fg="white",width=10,command=login).pack(pady=20)
  

    root.mainloop()




                             #********#

#=========================================================
            #main page#
#===============================================================
def home_loan_form(title_name):

    loan_window = Toplevel()
    loan_window.geometry("750x500")
    loan_window.title(title_name)

    img = PhotoImage(file="image11.png")
    loan_window.img = img

    Label(loan_window, image=img).place( x=0, y=0, relwidth=1, relheight=1  )

    Label(  loan_window,  text=title_name,  font=("Algerian", 30),  fg="green",  bg="lightyellow").place(x=0, y=5, width=750)

    def open_form():

        third = Toplevel()
        third.geometry("1000x700")
        third.title(title_name + " Form")
        third.config(bg="#7092BE")

        Label(  third,  text=title_name + " Form",  font=("Arial", 24, "bold"),  bg="#7092BE",  fg="navy").place(x=20, y=20)

        # ================= NAME =================
        Label(  third,  text="Full Name", bg="#7092BE", font=("Arial", 12) ).place(x=20, y=90)

        name_entry = Entry(third, width=30)
        name_entry.place(x=20, y=120)

        # ================= ACCOUNT NUMBER =================
        Label(third,text="Account Number",bg="#7092BE",font=("Arial", 12) ).place(x=400, y=90)

        acc_entry = Entry(third, width=30)
        acc_entry.place(x=400, y=120)

        # ================= ACCOUNT TYPE =================
        Label(third,text="Account Type",bg="#7092BE",font=("Arial", 12) ).place(x=20, y=180)

        combo = ttk.Combobox( third, values=[ "Saving Account",   "Current Account",   "Fixed Account",    "Salary Account" ], width=27 )

        combo.place(x=20, y=210)

        # ================= MOBILE =================
        Label( third, text="Mobile Number", bg="#7092BE", font=("Arial", 12)).place(x=400, y=180)

        mobile = Entry(third, width=30)
        mobile.place(x=400, y=210)

        # ================= GENDER =================
        gender = StringVar()

        Radiobutton( third, text="Male", variable=gender, value="Male", bg="#7092BE").place(x=20, y=280)

        Radiobutton(  third,  text="Female",  variable=gender,  value="Female",  bg="#7092BE" ).place(x=120, y=280)

        # ================= DOB =================
        Label(   third,   text="DOB",   bg="#7092BE",   font=("Arial", 12) ).place(x=400, y=280)

        day = ttk.Combobox(  third,  values=list(range(1, 32)),  width=5)

        day.place(x=460, y=280)

        month = ttk.Combobox( third, values=[ "January",   "February",   "March",   "April",   "May",
                                              "June",   "July",   "August",   "September",   "October",   "November",   "December"],width=10)

        month.place(x=530, y=280)

        year = ttk.Combobox(third, values=list(range(1980, 2026)), width=8)

        year.place(x=650, y=280)

        # ================= FILE =================
        def open_file():

            file = filedialog.askopenfilename()

            if file:

                messagebox.showinfo(  "Selected File",   file   )
        # ================= SUBMIT =================
        def submit_form():

            global user_name
            global user_account_type
            global loan_type

            user_name = name_entry.get()
            user_account_type = combo.get()
            loan_type = title_name

            messagebox.showinfo(  "Success",  "Form Submitted Successfully")

        # ================= BUTTONS =================
        Button(   third,   text="Submit",   bg="green",   fg="white",   width=12,   command=submit_form ).place(x=20, y=380)

        Button( third, text="Attach File", bg="orange", fg="white", width=12, command=open_file).place(x=200, y=380)

        Button(     third,     text="Close",     bg="red",     fg="white",     width=12,     command=third.destroy ).place(x=380, y=380)

    Button( loan_window, text="Open Form", bg="green", fg="white", font=("Arial", 14, "bold"), command=open_form).pack(pady=220)

# ==========================================================
# LOAN FUNCTIONS
# ==========================================================

def show_home_loan():

    home_loan_form("🏠 Home Loan")

def show_car_loan():

    home_loan_form("🚗 Car Loan")

def show_personal_loan():

    home_loan_form("💰 Personal Loan")

# ==========================================================
# DASHBOARD
# ==========================================================

def Dashboard():

    dashboard = Toplevel()
    dashboard.geometry("500x400")
    dashboard.title("Dashboard")
    dashboard.config(bg="white")

    Label(   dashboard,  text="🏦 MyBank Dashboard",  font=("Arial", 24, "bold"),  fg="darkblue",  bg="white").pack(pady=20)

    Label(   dashboard,  text=f"User Name : {user_name}",  font=("Arial", 16),  bg="white").pack(pady=10)

    Label(  dashboard,  text=f"Account Type : {user_account_type}",  font=("Arial", 16),  bg="white").pack(pady=10)

    Label(dashboard,text=f"Loan Type : {loan_type}", font=("Arial", 16), bg="white").pack(pady=10)

    login_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S"  )

    Label( dashboard,  text=f"Login Time : {login_time}",  font=("Arial", 14),  bg="white").pack(pady=10)

    Button( dashboard, text="Close", bg="red", fg="white", width=12, command=dashboard.destroy).pack(pady=20)

#===============================================================================================================================
                                         
                                                    #Create Account#
#--------------------------------------------------------------------------------------------------------------------------

def create_account_window():

    create_window = Toplevel()
    create_window.title("Create Account")
    create_window.geometry("1100x850")
    create_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(  create_window,  text="Create New Bank Account",   font=("Arial", 24, "bold"),   fg="darkblue",   bg="skyblue"  ).pack(pady=20)

    # ======================================================
    # MAIN FRAME
    # ======================================================

    frame = Frame(create_window, bg="white", bd=3, relief=RIDGE)
    frame.place(x=150, y=90, width=800, height=670)

    # ======================================================
    # FULL NAME
    # ======================================================

    Label(frame, text="Full Name", font=("Arial", 12, "bold"), bg="white").place(x=40, y=30)

    fullname = Entry(frame, width=30, font=("Arial", 11))
    fullname.place(x=40, y=60)

    # ======================================================
    # FATHER NAME
    # ======================================================

    Label(frame, text="Father Name", font=("Arial", 12, "bold"), bg="white").place(x=430, y=30)

    fathername = Entry(frame, width=30, font=("Arial", 11))
    fathername.place(x=430, y=60)

    # ======================================================
    # DATE OF BIRTH
    # ======================================================

    Label(frame, text="Date of Birth", font=("Arial", 12, "bold"), bg="white").place(x=40, y=100)

    dob = Entry(frame, width=30, font=("Arial", 11))
    dob.place(x=40, y=130)

    # ======================================================
    # GENDER
    # ======================================================

    Label(frame, text="Gender", font=("Arial", 12, "bold"), bg="white").place(x=430, y=100)

    gender = ttk.Combobox(  frame,  values=["Male", "Female", "Other"],   width=27,   font=("Arial", 11) )
    gender.place(x=430, y=130)

    # ======================================================
    # MOBILE NUMBER
    # ======================================================

    Label(frame, text="Mobile Number", font=("Arial", 12, "bold"), bg="white").place(x=40, y=170)

    mobile = Entry(frame, width=30, font=("Arial", 11))
    mobile.place(x=40, y=200)

    # ======================================================
    # EMAIL ADDRESS
    # ======================================================

    Label(frame, text="Email Address", font=("Arial", 12, "bold"), bg="white").place(x=430, y=170)

    email = Entry(frame, width=30, font=("Arial", 11))
    email.place(x=430, y=200)

    # ======================================================
    # ADDRESS
    # ======================================================

    Label(frame, text="Address", font=("Arial", 12, "bold"), bg="white").place(x=40, y=240)

    address = Text(frame, width=25, height=3, font=("Arial", 11))
    address.place(x=40, y=270)

    # ======================================================
    # AADHAAR NUMBER
    # ======================================================

    Label(frame, text="Aadhaar Number", font=("Arial", 12, "bold"), bg="white").place(x=430, y=240)

    aadhaar = Entry(frame, width=30, font=("Arial", 11))
    aadhaar.place(x=430, y=270)

    # ======================================================
    # PAN NUMBER
    # ======================================================

    Label(frame, text="PAN Number", font=("Arial", 12, "bold"), bg="white").place(x=40, y=350)

    pan = Entry(frame, width=30, font=("Arial", 11))
    pan.place(x=40, y=380)

    # ======================================================
    # ACCOUNT TYPE
    # ======================================================

    Label(frame, text="Account Type", font=("Arial", 12, "bold"), bg="white").place(x=430, y=350)

    account_type = ttk.Combobox( frame, values=["Savings", "Current", "Fixed Deposit"],   width=27,  font=("Arial", 11) )
    account_type.place(x=430, y=380)

    # ======================================================
    # BRANCH NAME
    # ======================================================

    Label(frame, text="Branch Name", font=("Arial", 12, "bold"), bg="white").place(x=40, y=430)

    branch = Entry(frame, width=30, font=("Arial", 11))
    branch.place(x=40, y=460)

    # ======================================================
    # INITIAL DEPOSIT
    # ======================================================

    Label(frame, text="Initial Deposit", font=("Arial", 12, "bold"), bg="white").place(x=430, y=430)

    deposit = Entry(frame, width=30, font=("Arial", 11))
    deposit.place(x=430, y=460)

    # ======================================================
    # USERNAME
    # ======================================================

    Label(frame, text="Username", font=("Arial", 12, "bold"), bg="white").place(x=40, y=510)

    username = Entry(frame, width=30, font=("Arial", 11))
    username.place(x=40, y=540)

    # ======================================================
    # PASSWORD
    # ======================================================

    Label(frame, text="Password", font=("Arial", 12, "bold"), bg="white").place(x=430, y=510)

    password = Entry(frame, width=30, show="*", font=("Arial", 11))
    password.place(x=430, y=540)

    # ======================================================
    # UPLOAD PHOTO FUNCTION
    # ======================================================

    def upload_photo():

        file = filedialog.askopenfilename(title="Select Photo",  filetypes=[("Image Files", "*.png *.jpg *.jpeg")] )

        if file:
            messagebox.showinfo("Success", "Photo Uploaded Successfully")

    # ======================================================
    # CREATE ACCOUNT FUNCTION
    # ======================================================

    def create_account():

        if fullname.get() == "":
            messagebox.showerror("Error", "Please Enter Full Name")

        elif mobile.get() == "":
            messagebox.showerror("Error", "Please Enter Mobile Number")

        else:
            messagebox.showinfo("Success", "Account Created Successfully")

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(create_window,  text="Upload Photo",  font=("Arial", 12, "bold"),  bg="orange",   fg="black",   padx=15,   command=upload_photo ).place(x=250, y=690)

    Button(create_window, text="Create Account",   font=("Arial", 12, "bold"),   bg="green",   fg="white",   padx=20,   command=create_account ).place(x=470, y=690)

    Button(   create_window,   text="Reset",font=("Arial", 12, "bold"),  bg="red",  fg="white",  padx=20 ).place(x=700, y=690)



#================================================================================================================================
# ==========================================================
# VIEW ACCOUNT WINDOW
# ==========================================================

def view_account_window():

    view_window = Toplevel()
    view_window.title("View Account")
    view_window.geometry("1000x750")
    view_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label( view_window, text="View Account Details",   font=("Arial", 24, "bold"),   fg="darkblue",   bg="skyblue").pack(pady=20)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(view_window, bg="white", bd=3, relief=RIDGE)
    search_frame.place(x=150, y=80, width=700, height=100)

    Label( search_frame, text="Enter Account Number",  font=("Arial", 12, "bold"),  bg="white" ).place(x=20, y=30)

    search_entry = Entry(search_frame, width=30, font=("Arial", 12))
    search_entry.place(x=250, y=30)

    # ======================================================
    # DETAILS FRAME
    # ======================================================

    details_frame = Frame(view_window, bg="white", bd=3, relief=RIDGE)
    details_frame.place(x=150, y=220, width=700, height=420)

    # ======================================================
    # CUSTOMER DETAILS LABELS
    # ======================================================

    Label(details_frame, text="Customer Name :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=30)
    Label(details_frame, text="Father Name :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=70)
    Label(details_frame, text="Date of Birth :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=110)
    Label(details_frame, text="Gender :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=150)
    Label(details_frame, text="Mobile Number :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=190)
    Label(details_frame, text="Email Address :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=230)
    Label(details_frame, text="Address :", font=("Arial", 12, "bold"), bg="white").place(x=30, y=270)

    Label(details_frame, text="Account Type :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=30)
    Label(details_frame, text="Branch Name :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=70)
    Label(details_frame, text="Current Balance :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=110)
    Label(details_frame, text="Aadhaar Number :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=150)
    Label(details_frame, text="PAN Number :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=190)
    Label(details_frame, text="Username :", font=("Arial", 12, "bold"), bg="white").place(x=380, y=230)

    # ======================================================
    # VALUE LABELS
    # ======================================================

    name_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    name_value.place(x=180, y=30)

    father_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    father_value.place(x=180, y=70)

    dob_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    dob_value.place(x=180, y=110)

    gender_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    gender_value.place(x=180, y=150)

    mobile_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    mobile_value.place(x=180, y=190)

    email_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    email_value.place(x=180, y=230)

    address_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    address_value.place(x=180, y=270)

    account_type_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    account_type_value.place(x=550, y=30)

    branch_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    branch_value.place(x=550, y=70)

    balance_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    balance_value.place(x=550, y=110)

    aadhaar_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    aadhaar_value.place(x=550, y=150)

    pan_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    pan_value.place(x=550, y=190)

    username_value = Label(details_frame, text="", font=("Arial", 11), bg="white", fg="blue")
    username_value.place(x=550, y=230)

    # ======================================================
    # SEARCH FUNCTION
    # ======================================================

    def search_account():

        acc_no = search_entry.get()

        if acc_no == "":
            messagebox.showerror("Error", "Please Enter Account Number")

        else:

            # SAMPLE DATA
            name_value.config(text="Prachi Dwivedi")
            father_value.config(text="Rajesh Dwivedi")
            dob_value.config(text="10/05/2005")
            gender_value.config(text="Female")
            mobile_value.config(text="9876543210")
            email_value.config(text="prachi@gmail.com")
            address_value.config(text="Pune, Maharashtra")

            account_type_value.config(text="Savings")
            branch_value.config(text="Pune Branch")
            balance_value.config(text="₹ 50,000")
            aadhaar_value.config(text="1234 5678 9012")
            pan_value.config(text="ABCDE1234F")
            username_value.config(text="prachi123")

            messagebox.showinfo("Success", "Account Found")

    # ======================================================
    # SEARCH BUTTON
    # ======================================================

    Button(search_frame,  text="Search",  font=("Arial", 12, "bold"),  bg="green",  fg="white",  command=search_account).place(x=550, y=25)

    # ======================================================
    # BOTTOM BUTTONS
    # ======================================================

    Button(   view_window,   text="Print",  font=("Arial", 12, "bold"), bg="orange", fg="black").place(x=250, y=680)

    Button(   view_window,   text="Download Statement",   font=("Arial", 12, "bold"),   bg="blue",   fg="white" ).place(x=400, y=680)

    Button( view_window, text="Close", font=("Arial", 12, "bold"), bg="red", fg="white", command=view_window.destroy ).place(x=650, y=680)

#===================================================================================================================================

# ==========================================================
# UPDATE ACCOUNT WINDOW
# ==========================================================

def update_account_window():

    update_window = Toplevel()
    update_window.title("Update Account")
    update_window.geometry("1000x750")
    update_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(  update_window,text="Update Account Details",font=("Arial", 20, "bold"),fg="darkblue", bg="skyblue" ).pack(pady=10)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(update_window, bg="white", bd=2, relief=RIDGE)
    search_frame.place(x=150, y=60, width=700, height=70)

    Label(search_frame, text="Enter Account Number", font=("Arial", 10, "bold"), bg="white").place(x=20, y=20)

    search_entry = Entry(search_frame, width=30, font=("Arial", 10))
    search_entry.place(x=240, y=20)

    # ======================================================
    # MAIN FRAME
    # ======================================================

    frame = Frame(update_window, bg="white", bd=2, relief=RIDGE)
    frame.place(x=70, y=150, width=850, height=500)

    # ======================================================
    # ROW POSITIONS
    # ======================================================

    y1 = 20
    y2 = 80
    y3 = 140
    y4 = 200
    y5 = 260
    y6 = 320
    y7 = 380

    # ======================================================
    # FULL NAME
    # ======================================================

    Label(frame, text="Full Name", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y1)

    fullname = Entry(frame, width=30, font=("Arial", 10))
    fullname.place(x=40, y=y1+25)

    # ======================================================
    # FATHER NAME
    # ======================================================

    Label(frame, text="Father Name", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y1)

    fathername = Entry(frame, width=30, font=("Arial", 10))
    fathername.place(x=450, y=y1+25)

    # ======================================================
    # DATE OF BIRTH
    # ======================================================

    Label(frame, text="Date of Birth", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y2)

    dob = Entry(frame, width=30, font=("Arial", 10))
    dob.place(x=40, y=y2+25)

    # ======================================================
    # GENDER
    # ======================================================

    Label(frame, text="Gender", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y2)

    gender = ttk.Combobox(  frame, values=["Male", "Female", "Other"], width=27,  font=("Arial", 10))
    gender.place(x=450, y=y2+25)

    # ======================================================
    # MOBILE NUMBER
    # ======================================================

    Label(frame, text="Mobile Number", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y3)

    mobile = Entry(frame, width=30, font=("Arial", 10))
    mobile.place(x=40, y=y3+25)

    # ======================================================
    # EMAIL ADDRESS
    # ======================================================

    Label(frame, text="Email Address", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y3)

    email = Entry(frame, width=30, font=("Arial", 10))
    email.place(x=450, y=y3+25)

    # ======================================================
    # ADDRESS
    # ======================================================

    Label(frame, text="Address", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y4)

    address = Text(frame, width=28, height=2, font=("Arial", 10))
    address.place(x=40, y=y4+25)

    # ======================================================
    # AADHAAR NUMBER
    # ======================================================

    Label(frame, text="Aadhaar Number", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y4)

    aadhaar = Entry(frame, width=30, font=("Arial", 10))
    aadhaar.place(x=450, y=y4+25)

    # ======================================================
    # PAN NUMBER
    # ======================================================

    Label(frame, text="PAN Number", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y5)

    pan = Entry(frame, width=30, font=("Arial", 10))
    pan.place(x=40, y=y5+25)

    # ======================================================
    # ACCOUNT TYPE
    # ======================================================

    Label(frame, text="Account Type", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y5)

    account_type = ttk.Combobox(  frame, values=["Savings", "Current", "Fixed Deposit"], width=27, font=("Arial", 10))
    account_type.place(x=450, y=y5+25)

    # ======================================================
    # BRANCH NAME
    # ======================================================

    Label(frame, text="Branch Name", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y6)

    branch = Entry(frame, width=30, font=("Arial", 10))
    branch.place(x=40, y=y6+25)

    # ======================================================
    # CURRENT BALANCE
    # ======================================================

    Label(frame, text="Current Balance", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y6)

    balance = Entry(frame, width=30, font=("Arial", 10))
    balance.place(x=450, y=y6+25)

    # ======================================================
    # USERNAME
    # ======================================================

    Label(frame, text="Username", font=("Arial", 10, "bold"), bg="white").place(x=40, y=y7)

    username = Entry(frame, width=30, font=("Arial", 10))
    username.place(x=40, y=y7+25)

    # ======================================================
    # PASSWORD
    # ======================================================

    Label(frame, text="Password", font=("Arial", 10, "bold"), bg="white").place(x=450, y=y7)

    password = Entry(frame, width=30, show="*", font=("Arial", 10))
    password.place(x=450, y=y7+25)

    # ======================================================
    # NOMINEE NAME
    # ======================================================

    Label(frame, text="Nominee Name", font=("Arial", 10, "bold"), bg="white").place(x=40, y=440)

    nominee = Entry(frame, width=30, font=("Arial", 10))
    nominee.place(x=40, y=465)

    # ======================================================
    # ATM STATUS
    # ======================================================

    Label(frame, text="ATM Card Status", font=("Arial", 10, "bold"), bg="white").place(x=450, y=440)

    atm_var = StringVar()

    Radiobutton( frame,text="Active", variable=atm_var, value="Active", bg="white").place(x=450, y=465)

    Radiobutton(  frame,  text="Blocked",  variable=atm_var,  value="Blocked",  bg="white" ).place(x=540, y=465)

    # ======================================================
    # SEARCH FUNCTION
    # ======================================================

    def search_account():

        if search_entry.get() == "":
            messagebox.showerror("Error", "Enter Account Number")

        else:

            fullname.insert(0, "Prachi Dwivedi")
            fathername.insert(0, "Rajesh Dwivedi")
            dob.insert(0, "10/05/2005")
            gender.set("Female")
            mobile.insert(0, "9876543210")
            email.insert(0, "prachi@gmail.com")
            address.insert(END, "Pune, Maharashtra")
            aadhaar.insert(0, "123456789012")
            pan.insert(0, "ABCDE1234F")
            account_type.set("Savings")
            branch.insert(0, "Pune Branch")
            balance.insert(0, "50000")
            username.insert(0, "prachi123")
            password.insert(0, "12345")
            nominee.insert(0, "Rajesh Dwivedi")

            messagebox.showinfo("Success", "Account Found")

    # ======================================================
    # UPDATE FUNCTION
    # ======================================================

    def update_account():

        if fullname.get() == "":
            messagebox.showerror("Error", "Enter Full Name")

        elif mobile.get() == "":
            messagebox.showerror("Error", "Enter Mobile Number")

        else:
            messagebox.showinfo(
                "Success",
                "Account Updated Successfully"
            )

    # ======================================================
    # RESET FUNCTION
    # ======================================================

    def reset_fields():

        fullname.delete(0, END)
        fathername.delete(0, END)
        dob.delete(0, END)
        mobile.delete(0, END)
        email.delete(0, END)
        address.delete("1.0", END)
        aadhaar.delete(0, END)
        pan.delete(0, END)
        branch.delete(0, END)
        balance.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)
        nominee.delete(0, END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(search_frame,text="Search", font=("Arial", 10, "bold"), bg="green", fg="white", command=search_account).place(x=580, y=15)

    Button(    update_window,    text="Update",    font=("Arial", 11, "bold"),    bg="blue",    fg="white",    padx=20,    command=update_account).place(x=280, y=690)

    Button( update_window,  text="Reset",  font=("Arial", 11, "bold"),  bg="orange",  fg="black",  padx=20,  command=reset_fields ).place(x=470, y=690)

    Button(   update_window,   text="Close",   font=("Arial", 11, "bold"),   bg="red",   fg="white",   padx=20,    command=update_window.destroy ).place(x=660, y=690)

#=================================================================================================================================

# ==========================================================
# DELETE ACCOUNT WINDOW
# ==========================================================

def delete_account_window():

    delete_window = Toplevel()
    delete_window.title("Delete Account")
    delete_window.geometry("900x700")
    delete_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(  delete_window, text="DELETE ACCOUNT", font=("Arial", 22, "bold"), fg="darkred", bg="skyblue"   ).pack(pady=15)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(delete_window, bg="white", bd=2, relief=RIDGE)
    search_frame.place(x=120, y=70, width=650, height=70)

    Label( search_frame,  text="Search Account Number",  font=("Arial", 11, "bold"),  bg="white"  ).place(x=20, y=20)

    search_entry = Entry(search_frame, width=30, font=("Arial", 11))
    search_entry.place(x=250, y=20)

    # ======================================================
    # DETAILS FRAME
    # ======================================================

    details_frame = Frame(delete_window, bg="white", bd=2, relief=RIDGE)
    details_frame.place(x=100, y=170, width=700, height=330)

    # ======================================================
    # LABELS
    # ======================================================

    Label(details_frame, text="Full Name", font=("Arial", 10, "bold"), bg="white").place(x=30, y=20)
    fullname = Entry(details_frame, width=30, font=("Arial", 10))
    fullname.place(x=30, y=45)

    Label(details_frame, text="Father Name", font=("Arial", 10, "bold"), bg="white").place(x=380, y=20)
    fathername = Entry(details_frame, width=30, font=("Arial", 10))
    fathername.place(x=380, y=45)

    Label(details_frame, text="Mobile Number", font=("Arial", 10, "bold"), bg="white").place(x=30, y=80)
    mobile = Entry(details_frame, width=30, font=("Arial", 10))
    mobile.place(x=30, y=105)

    Label(details_frame, text="Email Address", font=("Arial", 10, "bold"), bg="white").place(x=380, y=80)
    email = Entry(details_frame, width=30, font=("Arial", 10))
    email.place(x=380, y=105)

    Label(details_frame, text="Account Number", font=("Arial", 10, "bold"), bg="white").place(x=30, y=140)
    account_no = Entry(details_frame, width=30, font=("Arial", 10))
    account_no.place(x=30, y=165)

    Label(details_frame, text="Account Type", font=("Arial", 10, "bold"), bg="white").place(x=380, y=140)
    account_type = Entry(details_frame, width=30, font=("Arial", 10))
    account_type.place(x=380, y=165)

    Label(details_frame, text="Branch Name", font=("Arial", 10, "bold"), bg="white").place(x=30, y=200)
    branch = Entry(details_frame, width=30, font=("Arial", 10))
    branch.place(x=30, y=225)

    Label(details_frame, text="Current Balance", font=("Arial", 10, "bold"), bg="white").place(x=380, y=200)
    balance = Entry(details_frame, width=30, font=("Arial", 10))
    balance.place(x=380, y=225)

    Label(details_frame, text="Aadhaar Number", font=("Arial", 10, "bold"), bg="white").place(x=30, y=260)
    aadhaar = Entry(details_frame, width=30, font=("Arial", 10))
    aadhaar.place(x=30, y=285)

    Label(details_frame, text="PAN Number", font=("Arial", 10, "bold"), bg="white").place(x=380, y=260)
    pan = Entry(details_frame, width=30, font=("Arial", 10))
    pan.place(x=380, y=285)

    # ======================================================
    # DELETE OPTIONS FRAME
    # ======================================================

    option_frame = Frame(delete_window, bg="white", bd=2, relief=RIDGE)
    option_frame.place(x=100, y=520, width=700, height=80)

    delete_option = StringVar()

    Label(  option_frame, text="Delete Options", font=("Arial", 11, "bold"), bg="white").place(x=20, y=10)

    Radiobutton(option_frame, text="Permanent Delete", variable=delete_option,  value="Permanent",  bg="white").place(x=30, y=40)

    Radiobutton( option_frame,text="Deactivate Account", variable=delete_option, value="Deactivate", bg="white" ).place(x=230, y=40)

    Radiobutton( option_frame, text="Freeze Account", variable=delete_option, value="Freeze", bg="white").place(x=430, y=40)

    # ======================================================
    # ADMIN PASSWORD
    # ======================================================

    Label( delete_window, text="Enter Admin Password", font=("Arial", 10, "bold"), bg="skyblue").place(x=180, y=620)

    admin_password = Entry(  delete_window,  width=25,  show="*",  font=("Arial", 10) )
    admin_password.place(x=360, y=620)

    # ======================================================
    # SEARCH FUNCTION
    # ======================================================

    def search_account():

        if search_entry.get() == "":
            messagebox.showerror("Error", "Enter Account Number")

        else:

            fullname.insert(0, "Prachi Dwivedi")
            fathername.insert(0, "Rajesh Dwivedi")
            mobile.insert(0, "9876543210")
            email.insert(0, "prachi@gmail.com")
            account_no.insert(0, "123456789")
            account_type.insert(0, "Savings")
            branch.insert(0, "Pune Branch")
            balance.insert(0, "0")
            aadhaar.insert(0, "123456789012")
            pan.insert(0, "ABCDE1234F")

            messagebox.showinfo("Success", "Account Found")

    # ======================================================
    # DELETE FUNCTION
    # ======================================================

    def delete_account():

        if search_entry.get() == "":
            messagebox.showerror("Error", "Search Account First")

        elif admin_password.get() == "":
            messagebox.showerror("Error", "Enter Admin Password")

        else:

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this account?"
            )

            if confirm == True:

                messagebox.showinfo(
                    "Success",
                    "Account Deleted Successfully"
                )

    # ======================================================
    # RESET FUNCTION
    # ======================================================

    def reset_fields():

        fullname.delete(0, END)
        fathername.delete(0, END)
        mobile.delete(0, END)
        email.delete(0, END)
        account_no.delete(0, END)
        account_type.delete(0, END)
        branch.delete(0, END)
        balance.delete(0, END)
        aadhaar.delete(0, END)
        pan.delete(0, END)
        admin_password.delete(0, END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button( search_frame,text="Search", font=("Arial", 10, "bold"), bg="green", fg="white", command=search_account).place(x=540, y=15)

    Button(  delete_window,  text="Delete Account",  font=("Arial", 11, "bold"),  bg="red",  fg="white",  padx=15,  command=delete_account).place(x=180, y=660)

    Button(   delete_window,  text="Reset",  font=("Arial", 11, "bold"), bg="orange", fg="black",  padx=20,  command=reset_fields).place(x=400, y=660)
    Button(  delete_window,  text="Close",  font=("Arial", 11, "bold"),  bg="blue",  fg="white",  padx=20,command=delete_window.destroy ).place(x=580, y=660)



#=================================================================================================================================


# ==========================================================
# MINI STATEMENT WINDOW
# ==========================================================

def mini_statement_window():

    mini_window = Toplevel()
    mini_window.title("Mini Statement")
    mini_window.geometry("1100x700")
    mini_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(  mini_window,  text="MINI STATEMENT",  font=("Arial", 22, "bold"),  fg="darkblue",  bg="skyblue"  ).pack(pady=15)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(mini_window, bg="white", bd=2, relief=RIDGE)
    search_frame.place(x=180, y=70, width=700, height=70)

    Label( search_frame,text="Enter Account Number",font=("Arial", 11, "bold"),bg="white" ).place(x=20, y=20)

    search_entry = Entry(search_frame, width=30, font=("Arial", 11))
    search_entry.place(x=250, y=20)

    # ======================================================
    # CUSTOMER DETAILS FRAME
    # ======================================================

    details_frame = Frame(mini_window, bg="white", bd=2, relief=RIDGE)
    details_frame.place(x=120, y=170, width=860, height=100)

    # ======================================================
    # CUSTOMER DETAILS
    # ======================================================

    Label(details_frame, text="Customer Name :", font=("Arial", 11, "bold"), bg="white").place(x=20, y=20)
    Label(details_frame, text="Prachi Dwivedi", font=("Arial", 11), bg="white", fg="blue").place(x=180, y=20)

    Label(details_frame, text="Account Type :", font=("Arial", 11, "bold"), bg="white").place(x=450, y=20)
    Label(details_frame, text="Savings", font=("Arial", 11), bg="white", fg="blue").place(x=580, y=20)

    Label(details_frame, text="Account Number :", font=("Arial", 11, "bold"), bg="white").place(x=20, y=60)
    Label(details_frame, text="123456789", font=("Arial", 11), bg="white", fg="blue").place(x=180, y=60)

    Label(details_frame, text="Current Balance :", font=("Arial", 11, "bold"), bg="white").place(x=450, y=60)
    Label(details_frame, text="₹ 12,000", font=("Arial", 11), bg="white", fg="green").place(x=600, y=60)

    # ======================================================
    # TRANSACTION FRAME
    # ======================================================

    transaction_frame = Frame(mini_window, bg="white", bd=2, relief=RIDGE)
    transaction_frame.place(x=70, y=300, width=960, height=280)

    # ======================================================
    # TREEVIEW TABLE
    # ======================================================

    scroll_x = Scrollbar(transaction_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(transaction_frame, orient=VERTICAL)

    transaction_table = ttk.Treeview(transaction_frame, columns=("date", "type", "amount", "balance", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=transaction_table.xview)
    scroll_y.config(command=transaction_table.yview)

    # ======================================================
    # HEADINGS
    # ======================================================

    transaction_table.heading("date", text="Date")
    transaction_table.heading("type", text="Transaction Type")
    transaction_table.heading("amount", text="Amount")
    transaction_table.heading("balance", text="Balance")
    transaction_table.heading("status", text="Status")

    transaction_table["show"] = "headings"

    # ======================================================
    # COLUMN WIDTH
    # ======================================================

    transaction_table.column("date", width=150)
    transaction_table.column("type", width=220)
    transaction_table.column("amount", width=150)
    transaction_table.column("balance", width=150)
    transaction_table.column("status", width=150)

    transaction_table.pack(fill=BOTH, expand=1)

    # ======================================================
    # SAMPLE DATA
    # ======================================================

    transaction_table.insert(
        "",
        END,
        values=("01/05/2026", "Deposit", "₹ 5000", "₹ 15000", "Success")
    )

    transaction_table.insert(
        "",
        END,
        values=("03/05/2026", "Withdraw", "₹ 2000", "₹ 13000", "Success")
    )

    transaction_table.insert(
        "",
        END,
        values=("05/05/2026", "Transfer", "₹ 1000", "₹ 12000", "Success")
    )

    transaction_table.insert(
        "",
        END,
        values=("06/05/2026", "UPI Payment", "₹ 500", "₹ 11500", "Success")
    )

    transaction_table.insert(
        "",
        END,
        values=("08/05/2026", "ATM Withdraw", "₹ 1000", "₹ 10500", "Success")
    )

    # ======================================================
    # SEARCH FUNCTION
    # ======================================================

    def search_statement():

        if search_entry.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Account Number"
            )

        else:
            messagebox.showinfo(
                "Success",
                "Mini Statement Loaded"
            )

    # ======================================================
    # BUTTON FUNCTIONS
    # ======================================================

    def print_statement():

        messagebox.showinfo(
            "Print",
            "Statement Printed Successfully"
        )

    def download_statement():

        messagebox.showinfo(
            "Download",
            "Statement Downloaded Successfully"
        )

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(search_frame, text="Search", font=("Arial", 10, "bold"), bg="green", fg="white", command=search_statement).place(x=580, y=15)

    Button(  mini_window,  text="Print Statement",  font=("Arial", 11, "bold"),  bg="orange",  fg="black",  padx=15,  command=print_statement ).place(x=180, y=620)

    Button(  mini_window,  text="Download PDF",  font=("Arial", 11, "bold"),  bg="blue",  fg="white",  padx=15,  command=download_statement).place(x=400, y=620)

    Button( mini_window, text="Refresh", font=("Arial", 11, "bold"), bg="purple", fg="white", padx=20  ).place(x=640, y=620)

    Button( mini_window, text="Close", font=("Arial", 11, "bold"), bg="red", fg="white", padx=20, command=mini_window.destroy  ).place(x=840, y=620)


#========================================================================================================================================


# ==========================================================
# TRANSACTION HISTORY WINDOW
# ==========================================================

def transaction_history_window():

    history_window = Toplevel()
    history_window.title("Transaction History")
    history_window.geometry("1200x750")
    history_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(
        history_window,
        text="TRANSACTION HISTORY",
        font=("Arial", 22, "bold"),
        fg="darkblue",
        bg="skyblue"
    ).pack(pady=15)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(history_window, bg="white", bd=2, relief=RIDGE)
    search_frame.place(x=70, y=70, width=1060, height=90)

    # Account Number
    Label(
        search_frame,
        text="Account Number",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=15)

    account_entry = Entry(search_frame, width=22, font=("Arial", 10))
    account_entry.place(x=20, y=45)

    # From Date
    Label(
        search_frame,
        text="From Date",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=280, y=15)

    from_date = Entry(search_frame, width=18, font=("Arial", 10))
    from_date.place(x=280, y=45)

    # To Date
    Label(
        search_frame,
        text="To Date",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=15)

    to_date = Entry(search_frame, width=18, font=("Arial", 10))
    to_date.place(x=500, y=45)

    # Filter
    Label(
        search_frame,
        text="Filter",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=700, y=15)

    filter_box = ttk.Combobox(
        search_frame,
        values=[
            "Today",
            "Last 7 Days",
            "Last 30 Days",
            "Custom"
        ],
        width=18,
        font=("Arial", 10)
    )
    filter_box.place(x=700, y=45)

    # ======================================================
    # CUSTOMER DETAILS FRAME
    # ======================================================

    details_frame = Frame(history_window, bg="white", bd=2, relief=RIDGE)
    details_frame.place(x=70, y=180, width=1060, height=90)

    Label(details_frame, text="Customer Name :", font=("Arial", 10, "bold"), bg="white").place(x=20, y=15)
    Label(details_frame, text="Prachi Dwivedi", font=("Arial", 10), bg="white", fg="blue").place(x=170, y=15)

    Label(details_frame, text="Account Type :", font=("Arial", 10, "bold"), bg="white").place(x=420, y=15)
    Label(details_frame, text="Savings", font=("Arial", 10), bg="white", fg="blue").place(x=550, y=15)

    Label(details_frame, text="Branch Name :", font=("Arial", 10, "bold"), bg="white").place(x=760, y=15)
    Label(details_frame, text="Pune Branch", font=("Arial", 10), bg="white", fg="blue").place(x=890, y=15)

    Label(details_frame, text="Current Balance :", font=("Arial", 10, "bold"), bg="white").place(x=20, y=50)
    Label(details_frame, text="₹ 1,25,000", font=("Arial", 10), bg="white", fg="green").place(x=180, y=50)

    # ======================================================
    # TRANSACTION TABLE FRAME
    # ======================================================

    table_frame = Frame(history_window, bg="white", bd=2, relief=RIDGE)
    table_frame.place(x=40, y=300, width=1120, height=320)

    # ======================================================
    # SCROLLBARS
    # ======================================================

    scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame, orient=VERTICAL)

    # ======================================================
    # TREEVIEW TABLE
    # ======================================================

    transaction_table = ttk.Treeview(
        table_frame,
        columns=(
            "txn_id",
            "date",
            "time",
            "type",
            "amount",
            "mode",
            "balance",
            "status"
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
    )

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=transaction_table.xview)
    scroll_y.config(command=transaction_table.yview)

    # ======================================================
    # HEADINGS
    # ======================================================

    transaction_table.heading("txn_id", text="Transaction ID")
    transaction_table.heading("date", text="Date")
    transaction_table.heading("time", text="Time")
    transaction_table.heading("type", text="Transaction Type")
    transaction_table.heading("amount", text="Amount")
    transaction_table.heading("mode", text="Debit/Credit")
    transaction_table.heading("balance", text="Balance")
    transaction_table.heading("status", text="Status")

    transaction_table["show"] = "headings"

    # ======================================================
    # COLUMN WIDTHS
    # ======================================================

    transaction_table.column("txn_id", width=140)
    transaction_table.column("date", width=100)
    transaction_table.column("time", width=100)
    transaction_table.column("type", width=180)
    transaction_table.column("amount", width=120)
    transaction_table.column("mode", width=120)
    transaction_table.column("balance", width=120)
    transaction_table.column("status", width=120)

    transaction_table.pack(fill=BOTH, expand=1)

    # ======================================================
    # SAMPLE DATA
    # ======================================================

    transactions = [

        ("TXN1001", "01/05/2026", "10:20 AM", "Deposit", "₹ 5000", "Credit", "₹ 50000", "Success"),

        ("TXN1002", "02/05/2026", "11:45 AM", "ATM Withdraw", "₹ 2000", "Debit", "₹ 48000", "Success"),

        ("TXN1003", "03/05/2026", "01:15 PM", "UPI Payment", "₹ 500", "Debit", "₹ 47500", "Success"),

        ("TXN1004", "04/05/2026", "03:30 PM", "Online Transfer", "₹ 1000", "Debit", "₹ 46500", "Success"),

        ("TXN1005", "05/05/2026", "05:10 PM", "Salary Credit", "₹ 25000", "Credit", "₹ 71500", "Success"),

        ("TXN1006", "06/05/2026", "09:00 AM", "Bill Payment", "₹ 3000", "Debit", "₹ 68500", "Success"),

        ("TXN1007", "07/05/2026", "12:40 PM", "Recharge", "₹ 399", "Debit", "₹ 68101", "Success"),

        ("TXN1008", "08/05/2026", "02:15 PM", "Loan EMI", "₹ 7000", "Debit", "₹ 61101", "Success")

    ]

    for row in transactions:
        transaction_table.insert("", END, values=row)

    # ======================================================
    # SUMMARY FRAME
    # ======================================================

    summary_frame = Frame(history_window, bg="white", bd=2, relief=RIDGE)
    summary_frame.place(x=70, y=640, width=700, height=60)

    Label(
        summary_frame,
        text="Total Credit : ₹ 30,000",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="green"
    ).place(x=30, y=18)

    Label(
        summary_frame,
        text="Total Debit : ₹ 13,899",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="red"
    ).place(x=260, y=18)

    Label(
        summary_frame,
        text="Transactions : 8",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="blue"
    ).place(x=500, y=18)

    # ======================================================
    # BUTTON FUNCTIONS
    # ======================================================

    def search_transactions():

        if account_entry.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Account Number"
            )

        else:
            messagebox.showinfo(
                "Success",
                "Transaction History Loaded"
            )

    def export_pdf():

        messagebox.showinfo(
            "Export",
            "Transaction History Exported"
        )

    def print_history():

        messagebox.showinfo(
            "Print",
            "Transaction History Printed"
        )

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(
        search_frame,
        text="Search",
        font=("Arial", 10, "bold"),
        bg="green",
        fg="white",
        padx=15,
        command=search_transactions
    ).place(x=920, y=38)

    Button(
        history_window,
        text="Export PDF",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="white",
        padx=15,
        command=export_pdf
    ).place(x=820, y=650)

    Button(
        history_window,
        text="Print",
        font=("Arial", 11, "bold"),
        bg="orange",
        fg="black",
        padx=20,
        command=print_history
    ).place(x=970, y=650)

    Button(
        history_window,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="red",
        fg="white",
        padx=20,
        command=history_window.destroy
    ).place(x=1060, y=650)

    
#================================================================================================================================

# ==========================================================
# BALANCE ENQUIRY WINDOW
# ==========================================================

def balance_enquiry_window():

    balance_window = Toplevel()
    balance_window.title("Balance Enquiry")
    balance_window.geometry("900x650")
    balance_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(balance_window,text="BALANCE ENQUIRY",font=("Arial", 24, "bold"),fg="darkblue",bg="skyblue" ).pack(pady=15)

    # ======================================================
    # SEARCH FRAME
    # ======================================================

    search_frame = Frame(balance_window, bg="white", bd=2, relief=RIDGE)
    search_frame.place(x=140, y=80, width=620, height=120)

    # Account Number
    Label( search_frame, text="Account Number", font=("Arial", 11, "bold"), bg="white" ).place(x=30, y=20)

    account_entry = Entry(search_frame, width=25, font=("Arial", 11))
    account_entry.place(x=200, y=20)

    # Password
    Label(search_frame,text="Password / PIN",font=("Arial", 11, "bold"),bg="white").place(x=30, y=65)

    password_entry = Entry(search_frame,width=25,show="*",font=("Arial", 11) )
    password_entry.place(x=200, y=65)

    # ======================================================
    # CUSTOMER DETAILS FRAME
    # ======================================================

    details_frame = Frame(balance_window, bg="white", bd=2, relief=RIDGE)
    details_frame.place(x=120, y=230, width=660, height=140)

    Label( details_frame, text="Customer Name :", font=("Arial", 11, "bold"), bg="white" ).place(x=30, y=20)

    customer_name = Label(details_frame,text="Prachi Dwivedi",font=("Arial", 11),bg="white",fg="blue" )
    customer_name.place(x=220, y=20)

    Label(  details_frame,  text="Account Type :",  font=("Arial", 11, "bold"),  bg="white" ).place(x=30, y=60)

    account_type = Label( details_frame, text="Savings", font=("Arial", 11), bg="white", fg="blue")
    account_type.place(x=220, y=60)

    Label(details_frame,text="Branch Name :",font=("Arial", 11, "bold"),bg="white").place(x=30, y=100)

    branch_name = Label(  details_frame,  text="Pune Branch",  font=("Arial", 11),  bg="white",  fg="blue" )
    branch_name.place(x=220, y=100)

    # ======================================================
    # BALANCE FRAME
    # ======================================================

    balance_frame = Frame(balance_window, bg="white", bd=3, relief=RIDGE)
    balance_frame.place(x=220, y=400, width=460, height=140)

    Label(  balance_frame,  text="AVAILABLE BALANCE",  font=("Arial", 18, "bold"),  fg="darkgreen",  bg="white"  ).pack(pady=15)

    balance_label = Label(  balance_frame,  text="₹ 25,000",  font=("Arial", 28, "bold"),  fg="green",  bg="white"  )
    balance_label.pack()

    # ======================================================
    # LAST TRANSACTION FRAME
    # ======================================================

    transaction_frame = Frame(balance_window, bg="white", bd=2, relief=RIDGE)
    transaction_frame.place(x=120, y=560, width=660, height=50)

    Label(transaction_frame,text="Last Transaction : ₹ 2,000 Withdraw on 08/05/2026",font=("Arial", 10, "bold"),bg="white",fg="red" ).place(x=20, y=12)

    # ======================================================
    # FUNCTIONS
    # ======================================================

    def check_balance():

        if account_entry.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Account Number"
            )

        elif password_entry.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Password"
            )

        else:
            messagebox.showinfo(
                "Success",
                "Balance Retrieved Successfully"
            )

    def refresh_balance():

        account_entry.delete(0, END)
        password_entry.delete(0, END)

        messagebox.showinfo(
            "Refresh",
            "Data Refreshed"
        )

    def print_receipt():

        messagebox.showinfo(
            "Print",
            "Receipt Printed Successfully"
        )

    # ======================================================
    # BUTTONS
    # ======================================================

    Button( search_frame, text="Check Balance", font=("Arial", 10, "bold"), bg="green", fg="white", padx=10, command=check_balance ).place(x=470, y=40)

    Button(   balance_window,   text="Refresh",   font=("Arial", 11, "bold"),  bg="orange",  fg="black",  padx=20,  command=refresh_balance  ).place(x=180, y=620)

    Button(   balance_window,   text="Print Receipt",   font=("Arial", 11, "bold"),   bg="blue",   fg="white",   padx=20,   command=print_receipt).place(x=380, y=620)

    Button( balance_window, text="Close", font=("Arial", 11, "bold"), bg="red", fg="white",padx=20,command=balance_window.destroy  ).place(x=620, y=620)


#===============================================================================================================================

# ==========================================================
# FUND TRANSFER WINDOW
# ==========================================================

def fund_transfer_window():

    transfer_window = Toplevel()
    transfer_window.title("Fund Transfer")
    transfer_window.geometry("1000x750")
    transfer_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label( transfer_window, text="FUND TRANSFER", font=("Arial", 24, "bold"), fg="darkblue", bg="skyblue" ).pack(pady=15)

    # ======================================================
    # SENDER DETAILS FRAME
    # ======================================================

    sender_frame = LabelFrame(transfer_window,text="Sender Account Details",font=("Arial", 12, "bold"),bg="white",fg="darkblue", bd=3)

    sender_frame.place(x=60, y=70, width=880, height=140)

    # Sender Account Number
    Label( sender_frame,text="Account Number",font=("Arial", 10, "bold"),bg="white" ).place(x=20, y=20)

    sender_account = Entry(sender_frame, width=25, font=("Arial", 10))
    sender_account.place(x=180, y=20)

    # Customer Name
    Label(  sender_frame, text="Customer Name", font=("Arial", 10, "bold"), bg="white" ).place(x=450, y=20)

    sender_name = Entry(sender_frame, width=25, font=("Arial", 10))
    sender_name.place(x=620, y=20)

    # Balance
    Label(sender_frame,text="Available Balance",font=("Arial", 10, "bold"),bg="white"  ).place(x=20, y=70)

    sender_balance = Entry(sender_frame, width=25, font=("Arial", 10))
    sender_balance.place(x=180, y=70)

    # Branch
    Label( sender_frame, text="Branch Name", font=("Arial", 10, "bold"), bg="white" ).place(x=450, y=70)

    sender_branch = Entry(sender_frame, width=25, font=("Arial", 10))
    sender_branch.place(x=620, y=70)

    # ======================================================
    # RECEIVER DETAILS FRAME
    # ======================================================

    receiver_frame = LabelFrame(  transfer_window,  text="Receiver Details",  font=("Arial", 12, "bold"),  bg="white",  fg="darkblue",  bd=3)

    receiver_frame.place(x=60, y=240, width=880, height=190)

    # Receiver Account
    Label(  receiver_frame,  text="Receiver Account No",  font=("Arial", 10, "bold"),  bg="white").place(x=20, y=20)

    receiver_account = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_account.place(x=220, y=20)

    # Receiver Name
    Label( receiver_frame, text="Receiver Name", font=("Arial", 10, "bold"), bg="white").place(x=450, y=20)

    receiver_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_name.place(x=620, y=20)

    # Bank Name
    Label( receiver_frame, text="Bank Name", font=("Arial", 10, "bold"), bg="white").place(x=20, y=70)

    bank_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    bank_name.place(x=220, y=70)

    # IFSC Code
    Label( receiver_frame, text="IFSC Code", font=("Arial", 10, "bold"), bg="white" ).place(x=450, y=70)

    ifsc = Entry(receiver_frame, width=25, font=("Arial", 10))
    ifsc.place(x=620, y=70)

    # Branch
    Label( receiver_frame, text="Branch Name", font=("Arial", 10, "bold"), bg="white").place(x=20, y=120)

    receiver_branch = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_branch.place(x=220, y=120)

    # ======================================================
    # TRANSFER DETAILS FRAME
    # ======================================================

    transfer_frame = LabelFrame(transfer_window,text="Transfer Details",font=("Arial", 12, "bold"),bg="white",fg="darkblue",bd=3)

    transfer_frame.place(x=60, y=460, width=880, height=180)

    # Transfer Amount
    Label(   transfer_frame,   text="Transfer Amount",   font=("Arial", 10, "bold"),  bg="white").place(x=20, y=20)

    amount = Entry(transfer_frame, width=25, font=("Arial", 10))
    amount.place(x=220, y=20)

    # Transfer Type
    Label(transfer_frame,text="Transfer Type",font=("Arial", 10, "bold"),bg="white").place(x=450, y=20)

    transfer_type = ttk.Combobox(   transfer_frame,   values=["NEFT", "RTGS", "IMPS", "UPI"],   width=22,   font=("Arial", 10))

    transfer_type.place(x=620, y=20)

    # Remark
    Label(transfer_frame,text="Remark",font=("Arial", 10, "bold"),bg="white").place(x=20, y=70)

    remark = Text(transfer_frame, width=30, height=3, font=("Arial", 10))
    remark.place(x=220, y=70)

    # Transaction PIN
    Label(  transfer_frame,  text="Transaction PIN",  font=("Arial", 10, "bold"),  bg="white" ).place(x=450, y=80)

    transaction_pin = Entry( transfer_frame, width=25, show="*", font=("Arial", 10))

    transaction_pin.place(x=620, y=80)

    # ======================================================
    # FUNCTIONS
    # ======================================================

    def verify_account():

        if receiver_account.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Receiver Account Number"
            )

        else:
            messagebox.showinfo(
                "Verified",
                "Receiver Account Verified Successfully"
            )

    def transfer_money():

        if amount.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transfer Amount"
            )

        elif transaction_pin.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transaction PIN"
            )

        else:

            confirm = messagebox.askyesno(
                "Confirm Transfer",
                "Do you want to transfer this amount?"
            )

            if confirm == True:

                messagebox.showinfo(
                    "Success",
                    "Money Transferred Successfully"
                )

    def reset_fields():

        sender_account.delete(0, END)
        sender_name.delete(0, END)
        sender_balance.delete(0, END)
        sender_branch.delete(0, END)

        receiver_account.delete(0, END)
        receiver_name.delete(0, END)
        bank_name.delete(0, END)
        ifsc.delete(0, END)
        receiver_branch.delete(0, END)

        amount.delete(0, END)
        transaction_pin.delete(0, END)

        remark.delete("1.0", END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(transfer_window,text="Verify Account",font=("Arial", 11, "bold"),bg="orange",  fg="black",  padx=15,  command=verify_account ).place(x=180, y=680)

    Button(  transfer_window,  text="Transfer Money",  font=("Arial", 11, "bold"),  bg="green",  fg="white",  padx=15,  command=transfer_money).place(x=400, y=680)

    Button(  transfer_window,  text="Reset",  font=("Arial", 11, "bold"),  bg="blue",  fg="white",  padx=20,  command=reset_fields ).place(x=650, y=680)

    Button(  transfer_window,  text="Close",  font=("Arial", 11, "bold"),  bg="red",  fg="white",  padx=20,  command=transfer_window.destroy).place(x=820, y=680)    


#=================================================================================================================================

# ==========================================================
# BANK TRANSFER WINDOW
# ==========================================================

def bank_transfer_window():

    transfer_window = Toplevel()
    transfer_window.title("Bank Transfer")
    transfer_window.geometry("1000x780")
    transfer_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(
        transfer_window,
        text="BANK TRANSFER",
        font=("Arial", 24, "bold"),
        fg="darkblue",
        bg="skyblue"
    ).pack(pady=10)

    # ======================================================
    # SENDER DETAILS FRAME
    # ======================================================

    sender_frame = LabelFrame(
        transfer_window,
        text="Sender Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    sender_frame.place(x=50, y=60, width=900, height=150)

    # Sender Account Number
    Label(
        sender_frame,
        text="Sender Account Number",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    sender_account = Entry(sender_frame, width=30, font=("Arial", 10))
    sender_account.place(x=240, y=20)

    # Customer Name
    Label(
        sender_frame,
        text="Customer Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=20)

    customer_name = Entry(sender_frame, width=25, font=("Arial", 10))
    customer_name.place(x=660, y=20)

    # Balance
    Label(
        sender_frame,
        text="Available Balance",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=80)

    balance = Entry(sender_frame, width=30, font=("Arial", 10))
    balance.place(x=240, y=80)

    # Branch
    Label(
        sender_frame,
        text="Branch Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=80)

    branch_name = Entry(sender_frame, width=25, font=("Arial", 10))
    branch_name.place(x=660, y=80)

    # ======================================================
    # RECEIVER DETAILS FRAME
    # ======================================================

    receiver_frame = LabelFrame(
        transfer_window,
        text="Receiver Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    receiver_frame.place(x=50, y=230, width=900, height=190)

    # Receiver Account Number
    Label(
        receiver_frame,
        text="Receiver Account Number",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    receiver_account = Entry(receiver_frame, width=30, font=("Arial", 10))
    receiver_account.place(x=240, y=20)

    # Receiver Name
    Label(
        receiver_frame,
        text="Receiver Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=20)

    receiver_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_name.place(x=660, y=20)

    # Bank Name
    Label(
        receiver_frame,
        text="Bank Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=80)

    bank_name = Entry(receiver_frame, width=30, font=("Arial", 10))
    bank_name.place(x=240, y=80)

    # IFSC Code
    Label(
        receiver_frame,
        text="IFSC Code",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=80)

    ifsc = Entry(receiver_frame, width=25, font=("Arial", 10))
    ifsc.place(x=660, y=80)

    # Receiver Branch
    Label(
        receiver_frame,
        text="Branch Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=140)

    receiver_branch = Entry(receiver_frame, width=30, font=("Arial", 10))
    receiver_branch.place(x=240, y=140)

    # ======================================================
    # TRANSFER DETAILS FRAME
    # ======================================================

    transfer_frame = LabelFrame(
        transfer_window,
        text="Transfer Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    transfer_frame.place(x=50, y=440, width=900, height=200)

    # Transfer Amount
    Label(
        transfer_frame,
        text="Transfer Amount",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    amount = Entry(transfer_frame, width=30, font=("Arial", 10))
    amount.place(x=240, y=20)

    # Transfer Type
    Label(
        transfer_frame,
        text="Transfer Type",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=20)

    transfer_type = ttk.Combobox(
        transfer_frame,
        values=["NEFT", "RTGS", "IMPS", "UPI"],
        width=27,
        font=("Arial", 10)
    )

    transfer_type.place(x=660, y=20)

    # Transfer Date
    Label(
        transfer_frame,
        text="Transfer Date",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=70)

    transfer_date = Entry(transfer_frame, width=30, font=("Arial", 10))
    transfer_date.place(x=240, y=70)

    # Remark
    Label(
        transfer_frame,
        text="Remark / Description",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=70)

    remark = Entry(transfer_frame, width=30, font=("Arial", 10))
    remark.place(x=660, y=70)

    # Transaction PIN
    Label(
        transfer_frame,
        text="Transaction PIN",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=130)

    transaction_pin = Entry(
        transfer_frame,
        width=30,
        show="*",
        font=("Arial", 10)
    )

    transaction_pin.place(x=240, y=130)

    # OTP Verification
    Label(
        transfer_frame,
        text="OTP Verification",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=500, y=130)

    otp = Entry(
        transfer_frame,
        width=30,
        font=("Arial", 10)
    )

    otp.place(x=660, y=130)

    # ======================================================
    # SUMMARY FRAME
    # ======================================================

    summary_frame = Frame(
        transfer_window,
        bg="white",
        bd=2,
        relief=RIDGE
    )

    summary_frame.place(x=50, y=660, width=600, height=70)

    Label(
        summary_frame,
        text="Available Balance : ₹50,000",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="green"
    ).place(x=20, y=20)

    Label(
        summary_frame,
        text="Transfer Charges : ₹10",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="red"
    ).place(x=240, y=20)

    Label(
        summary_frame,
        text="Final Deduction : ₹5,010",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="blue"
    ).place(x=420, y=20)

    # ======================================================
    # FUNCTIONS
    # ======================================================

    def verify_account():

        if receiver_account.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Receiver Account Number"
            )

        else:
            messagebox.showinfo(
                "Verified",
                "Receiver Account Verified Successfully"
            )

    def transfer_money():

        if amount.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transfer Amount"
            )

        elif transaction_pin.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transaction PIN"
            )

        else:

            confirm = messagebox.askyesno(
                "Confirm Transfer",
                "Do you want to transfer money?"
            )

            if confirm == True:

                messagebox.showinfo(
                    "Success",
                    "Money Transferred Successfully"
                )

    def reset_fields():

        sender_account.delete(0, END)
        customer_name.delete(0, END)
        balance.delete(0, END)
        branch_name.delete(0, END)

        receiver_account.delete(0, END)
        receiver_name.delete(0, END)
        bank_name.delete(0, END)
        ifsc.delete(0, END)
        receiver_branch.delete(0, END)

        amount.delete(0, END)
        transfer_date.delete(0, END)
        remark.delete(0, END)
        transaction_pin.delete(0, END)
        otp.delete(0, END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(transfer_window,text="Verify Account",font=("Arial", 11, "bold"),bg="orange",fg="black",padx=15,command=verify_account ).place(x=700, y=665)

    Button( transfer_window, text="Transfer", font=("Arial", 11, "bold"), bg="green", fg="white", padx=20, command=transfer_money).place(x=700, y=710)

    Button( transfer_window, text="Reset", font=("Arial", 11, "bold"), bg="blue", fg="white", padx=20, command=reset_fields).place(x=830, y=665)

    Button(transfer_window,text="Close",font=("Arial", 11, "bold"),bg="red",fg="white",padx=20,command=transfer_window.destroy ).place(x=830, y=710)


#================================================================================================================================


# ==========================================================
# UPI TRANSFER WINDOW
# ==========================================================

def upi_transfer_window():

    upi_window = Toplevel()
    upi_window.title("UPI Transfer")
    upi_window.geometry("950x720")
    upi_window.config(bg="skyblue")

    # ======================================================
    # TITLE
    # ======================================================

    Label(
        upi_window,
        text="UPI TRANSFER",
        font=("Arial", 24, "bold"),
        fg="darkblue",
        bg="skyblue"
    ).pack(pady=10)

    # ======================================================
    # USER DETAILS FRAME
    # ======================================================

    user_frame = LabelFrame(
        upi_window,
        text="Your UPI Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    user_frame.place(x=50, y=60, width=850, height=150)

    # UPI ID
    Label(
        user_frame,
        text="Your UPI ID",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    upi_id = Entry(user_frame, width=30, font=("Arial", 10))
    upi_id.place(x=180, y=20)

    # Mobile Number
    Label(
        user_frame,
        text="Mobile Number",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=20)

    mobile = Entry(user_frame, width=25, font=("Arial", 10))
    mobile.place(x=620, y=20)

    # Linked Bank Account
    Label(
        user_frame,
        text="Linked Bank Account",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=80)

    linked_bank = Entry(user_frame, width=30, font=("Arial", 10))
    linked_bank.place(x=180, y=80)

    # Available Balance
    Label(
        user_frame,
        text="Available Balance",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=80)

    balance = Entry(user_frame, width=25, font=("Arial", 10))
    balance.place(x=620, y=80)

    # ======================================================
    # RECEIVER DETAILS FRAME
    # ======================================================

    receiver_frame = LabelFrame(
        upi_window,
        text="Receiver Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    receiver_frame.place(x=50, y=230, width=850, height=180)

    # Receiver UPI ID
    Label(
        receiver_frame,
        text="Receiver UPI ID",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    receiver_upi = Entry(receiver_frame, width=30, font=("Arial", 10))
    receiver_upi.place(x=200, y=20)

    # Receiver Name
    Label(
        receiver_frame,
        text="Receiver Name",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=20)

    receiver_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_name.place(x=620, y=20)

    # QR Code
    Label(
        receiver_frame,
        text="QR Code Scanner",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=80)

    qr_entry = Entry(receiver_frame, width=30, font=("Arial", 10))
    qr_entry.place(x=200, y=80)

    # Saved Contacts
    Label(
        receiver_frame,
        text="Saved Contacts",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=80)

    contacts = ttk.Combobox(
        receiver_frame,
        values=[
            "Rahul Sharma",
            "Aman Verma",
            "Priya Singh",
            "Rohit Kumar"
        ],
        width=22,
        font=("Arial", 10)
    )

    contacts.place(x=620, y=80)

    # ======================================================
    # PAYMENT DETAILS FRAME
    # ======================================================

    payment_frame = LabelFrame(
        upi_window,
        text="Payment Details",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="darkblue",
        bd=3
    )

    payment_frame.place(x=50, y=430, width=850, height=180)

    # Amount
    Label(
        payment_frame,
        text="Amount",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=20)

    amount = Entry(payment_frame, width=30, font=("Arial", 10))
    amount.place(x=200, y=20)

    # Payment Category
    Label(
        payment_frame,
        text="Payment Category",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=20)

    category = ttk.Combobox(
        payment_frame,
        values=[
            "Food",
            "Shopping",
            "Recharge",
            "Electricity Bill",
            "Travel",
            "Rent"
        ],
        width=22,
        font=("Arial", 10)
    )

    category.place(x=620, y=20)

    # Payment Note
    Label(
        payment_frame,
        text="Payment Note",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=20, y=80)

    payment_note = Entry(payment_frame, width=30, font=("Arial", 10))
    payment_note.place(x=200, y=80)

    # UPI PIN
    Label(
        payment_frame,
        text="Enter UPI PIN",
        font=("Arial", 10, "bold"),
        bg="white"
    ).place(x=470, y=80)

    upi_pin = Entry(
        payment_frame,
        width=25,
        show="*",
        font=("Arial", 10)
    )

    upi_pin.place(x=620, y=80)

    # ======================================================
    # TRANSACTION SUMMARY FRAME
    # ======================================================

    summary_frame = Frame(
        upi_window,
        bg="white",
        bd=2,
        relief=RIDGE
    )

    summary_frame.place(x=50, y=630, width=550, height=60)

    Label(
        summary_frame,
        text="Transfer Amount : ₹500",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="green"
    ).place(x=20, y=18)

    Label(
        summary_frame,
        text="Transaction Charges : ₹0",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="blue"
    ).place(x=220, y=18)

    Label(
        summary_frame,
        text="Status : Ready",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="orange"
    ).place(x=420, y=18)

    # ======================================================
    # FUNCTIONS
    # ======================================================

    def verify_upi():

        if receiver_upi.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Receiver UPI ID"
            )

        else:
            messagebox.showinfo(
                "Verified",
                "UPI ID Verified Successfully"
            )

    def pay_now():

        if amount.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Amount"
            )

        elif upi_pin.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter UPI PIN"
            )

        else:

            confirm = messagebox.askyesno(
                "Confirm Payment",
                "Do you want to continue payment?"
            )

            if confirm == True:

                messagebox.showinfo(
                    "Success",
                    "UPI Payment Successful"
                )

    def reset_fields():

        upi_id.delete(0, END)
        mobile.delete(0, END)
        linked_bank.delete(0, END)
        balance.delete(0, END)

        receiver_upi.delete(0, END)
        receiver_name.delete(0, END)
        qr_entry.delete(0, END)

        amount.delete(0, END)
        payment_note.delete(0, END)
        upi_pin.delete(0, END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(
        upi_window,
        text="Verify UPI",
        font=("Arial", 11, "bold"),
        bg="orange",
        fg="black",
        padx=15,
        command=verify_upi
    ).place(x=650, y=635)

    Button(
        upi_window,
        text="Pay Now",
        font=("Arial", 11, "bold"),
        bg="green",
        fg="white",
        padx=20,
        command=pay_now
    ).place(x=650, y=680)

    Button(
        upi_window,
        text="Reset",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="white",
        padx=20,
        command=reset_fields
    ).place(x=790, y=635)

    Button(
        upi_window,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="red",
        fg="white",
        padx=20,
        command=upi_window.destroy
    ).place(x=790, y=680)




#===================================================================================================================================

# ==========================================================
# MOBILE TRANSFER WINDOW
# ==========================================================

def mobile_transfer_window():

    mobile_window = Toplevel()
    mobile_window.title("Mobile Transfer")
    mobile_window.geometry("950x760")
    mobile_window.config(bg="#87CEEB")

    # ======================================================
    # TITLE
    # ======================================================

    Label(
        mobile_window,
        text="MOBILE MONEY TRANSFER",
        font=("Arial", 24, "bold"),
        fg="darkblue",
        bg="#87CEEB"
    ).pack(pady=15)

    # ======================================================
    # USER DETAILS FRAME
    # ======================================================

    user_frame = LabelFrame(
        mobile_window,
        text="User Details",
        font=("Arial", 12, "bold"),
        fg="darkblue",
        bg="white",
        bd=3
    )

    user_frame.place(x=40, y=70, width=860, height=150)

    Label(user_frame, text="Customer Name", font=("Arial", 10, "bold"), bg="white").place(x=20, y=20)
    customer_name = Entry(user_frame, width=30, font=("Arial", 10))
    customer_name.place(x=200, y=20)

    Label(user_frame, text="Mobile Number", font=("Arial", 10, "bold"), bg="white").place(x=470, y=20)
    mobile_number = Entry(user_frame, width=25, font=("Arial", 10))
    mobile_number.place(x=620, y=20)

    Label(user_frame, text="Linked Account", font=("Arial", 10, "bold"), bg="white").place(x=20, y=80)
    linked_account = Entry(user_frame, width=30, font=("Arial", 10))
    linked_account.place(x=200, y=80)

    Label(user_frame, text="Current Balance", font=("Arial", 10, "bold"), bg="white").place(x=470, y=80)
    current_balance = Entry(user_frame, width=25, font=("Arial", 10))
    current_balance.place(x=620, y=80)

    # ======================================================
    # RECEIVER DETAILS FRAME
    # ======================================================

    receiver_frame = LabelFrame(
        mobile_window,
        text="Receiver Details",
        font=("Arial", 12, "bold"),
        fg="darkblue",
        bg="white",
        bd=3
    )

    receiver_frame.place(x=40, y=240, width=860, height=170)

    Label(receiver_frame, text="Receiver Number", font=("Arial", 10, "bold"), bg="white").place(x=20, y=20)
    receiver_number = Entry(receiver_frame, width=30, font=("Arial", 10))
    receiver_number.place(x=200, y=20)

    Label(receiver_frame, text="Receiver Name", font=("Arial", 10, "bold"), bg="white").place(x=470, y=20)
    receiver_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    receiver_name.place(x=620, y=20)

    Label(receiver_frame, text="UPI ID", font=("Arial", 10, "bold"), bg="white").place(x=20, y=80)
    upi_id = Entry(receiver_frame, width=30, font=("Arial", 10))
    upi_id.place(x=200, y=80)

    Label(receiver_frame, text="Bank Name", font=("Arial", 10, "bold"), bg="white").place(x=470, y=80)
    bank_name = Entry(receiver_frame, width=25, font=("Arial", 10))
    bank_name.place(x=620, y=80)

    # ======================================================
    # PAYMENT INFORMATION FRAME
    # ======================================================

    payment_frame = LabelFrame(
        mobile_window,
        text="Payment Information",
        font=("Arial", 12, "bold"),
        fg="darkblue",
        bg="white",
        bd=3
    )

    payment_frame.place(x=40, y=430, width=860, height=170)

    Label(payment_frame, text="Transfer Amount", font=("Arial", 10, "bold"), bg="white").place(x=20, y=20)
    transfer_amount = Entry(payment_frame, width=30, font=("Arial", 10))
    transfer_amount.place(x=200, y=20)

    Label(payment_frame, text="Payment Purpose", font=("Arial", 10, "bold"), bg="white").place(x=470, y=20)
    payment_purpose = Entry(payment_frame, width=25, font=("Arial", 10))
    payment_purpose.place(x=620, y=20)

    Label(payment_frame, text="Payment Mode", font=("Arial", 10, "bold"), bg="white").place(x=20, y=80)

    payment_mode = ttk.Combobox(
        payment_frame,
        values=["UPI", "IMPS", "Wallet Transfer", "Mobile Banking"],
        width=27,
        font=("Arial", 10)
    )

    payment_mode.place(x=200, y=80)

    Label(payment_frame, text="Transfer Date", font=("Arial", 10, "bold"), bg="white").place(x=470, y=80)
    transfer_date = Entry(payment_frame, width=25, font=("Arial", 10))
    transfer_date.place(x=620, y=80)

    # ======================================================
    # SECURITY FRAME
    # ======================================================

    security_frame = LabelFrame(
        mobile_window,
        text="Security Verification",
        font=("Arial", 12, "bold"),
        fg="darkblue",
        bg="white",
        bd=3
    )

    security_frame.place(x=40, y=620, width=550, height=90)

    Label(security_frame, text="Enter OTP", font=("Arial", 10, "bold"), bg="white").place(x=20, y=25)
    otp = Entry(security_frame, width=20, font=("Arial", 10))
    otp.place(x=130, y=25)

    Label(security_frame, text="Transaction PIN", font=("Arial", 10, "bold"), bg="white").place(x=280, y=25)
    pin = Entry(security_frame, width=20, show="*", font=("Arial", 10))
    pin.place(x=420, y=25)

    # ======================================================
    # STATUS FRAME
    # ======================================================

    status_frame = Frame(
        mobile_window,
        bg="white",
        bd=2,
        relief=RIDGE
    )

    status_frame.place(x=620, y=620, width=280, height=90)

    Label(
        status_frame,
        text="Transaction ID : TXN458963",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="blue"
    ).place(x=15, y=15)

    Label(
        status_frame,
        text="Charges : ₹0",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="green"
    ).place(x=15, y=40)

    Label(
        status_frame,
        text="Status : Ready",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="orange"
    ).place(x=150, y=40)

    # ======================================================
    # FUNCTIONS
    # ======================================================

    def verify_number():

        if receiver_number.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Receiver Mobile Number"
            )

        else:
            messagebox.showinfo(
                "Verified",
                "Mobile Number Verified Successfully"
            )

    def send_money():

        if transfer_amount.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transfer Amount"
            )

        elif pin.get() == "":
            messagebox.showerror(
                "Error",
                "Please Enter Transaction PIN"
            )

        else:

            confirm = messagebox.askyesno(
                "Confirm Payment",
                "Do you want to send money?"
            )

            if confirm == True:

                messagebox.showinfo(
                    "Success",
                    "Money Sent Successfully"
                )

    def reset_fields():

        customer_name.delete(0, END)
        mobile_number.delete(0, END)
        linked_account.delete(0, END)
        current_balance.delete(0, END)

        receiver_number.delete(0, END)
        receiver_name.delete(0, END)
        upi_id.delete(0, END)
        bank_name.delete(0, END)

        transfer_amount.delete(0, END)
        payment_purpose.delete(0, END)
        transfer_date.delete(0, END)

        otp.delete(0, END)
        pin.delete(0, END)

    # ======================================================
    # BUTTONS
    # ======================================================

    Button(
        mobile_window,
        text="Verify",
        font=("Arial", 11, "bold"),
        bg="orange",
        fg="black",
        padx=20,
        command=verify_number
    ).place(x=250, y=720)

    Button(
        mobile_window,
        text="Send Money",
        font=("Arial", 11, "bold"),
        bg="green",
        fg="white",
        padx=20,
        command=send_money
    ).place(x=410, y=720)

    Button(
        mobile_window,
        text="Reset",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="white",
        padx=20,
        command=reset_fields
    ).place(x=610, y=720)

    Button(
        mobile_window,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="red",
        fg="white",
        padx=20,
        command=mobile_window.destroy
    ).place(x=770, y=720)



#=================================================================================================================================

# ==========================================================
# NEFT TRANSFER WINDOW
# ==========================================================
def neft_transfer_window():

    root = Toplevel()
    root.title("NEFT Transfer")
    root.geometry("900x700")   
    root.config(bg="#87CEEB")
    root.resizable(False, False)

    # ================= TITLE =================
    Label(
        root,
        text="NEFT TRANSFER",
        font=("Arial", 18, "bold"),
        fg="darkblue",
        bg="#87CEEB"
    ).pack(pady=5)

    # ================= ACCOUNT FRAME =================
    account_frame = LabelFrame(root, text="Account Info",
                               font=("Arial", 10, "bold"),
                               bg="white")
    account_frame.place(x=20, y=50, width=860, height=120)

    holder_name = Entry(account_frame, width=25)
    holder_name.place(x=150, y=10)

    account_number = Entry(account_frame, width=25)
    account_number.place(x=550, y=10)

    branch = Entry(account_frame, width=25)
    branch.place(x=150, y=60)

    balance = Entry(account_frame, width=25)
    balance.place(x=550, y=60)

    Label(account_frame, text="Name", bg="white").place(x=20, y=10)
    Label(account_frame, text="Acc No", bg="white").place(x=450, y=10)
    Label(account_frame, text="Branch", bg="white").place(x=20, y=60)
    Label(account_frame, text="Balance", bg="white").place(x=450, y=60)

    # ================= BENEFICIARY FRAME =================
    beneficiary_frame = LabelFrame(root, text="Beneficiary",
                                   font=("Arial", 10, "bold"),
                                   bg="white")
    beneficiary_frame.place(x=20, y=180, width=860, height=160)

    beneficiary_name = Entry(beneficiary_frame, width=25)
    beneficiary_name.place(x=150, y=10)

    beneficiary_account = Entry(beneficiary_frame, width=25)
    beneficiary_account.place(x=550, y=10)

    ifsc = Entry(beneficiary_frame, width=25)
    ifsc.place(x=150, y=60)

    bank_name = Entry(beneficiary_frame, width=25)
    bank_name.place(x=550, y=60)

    Label(beneficiary_frame, text="Name", bg="white").place(x=20, y=10)
    Label(beneficiary_frame, text="Acc No", bg="white").place(x=450, y=10)
    Label(beneficiary_frame, text="IFSC", bg="white").place(x=20, y=60)
    Label(beneficiary_frame, text="Bank", bg="white").place(x=450, y=60)

    # ================= PAYMENT FRAME =================
    payment_frame = LabelFrame(root, text="Payment",
                               font=("Arial", 10, "bold"),
                               bg="white")
    payment_frame.place(x=20, y=350, width=860, height=120)

    amount = Entry(payment_frame, width=25)
    amount.place(x=150, y=10)

    purpose = Entry(payment_frame, width=25)
    purpose.place(x=550, y=10)

    transaction_date = Entry(payment_frame, width=25)
    transaction_date.place(x=150, y=60)

    timing_slot = ttk.Combobox(payment_frame,
                                values=["9AM","11AM","1PM","3PM","5PM"],
                                width=22)
    timing_slot.place(x=550, y=60)

    Label(payment_frame, text="Amount", bg="white").place(x=20, y=10)
    Label(payment_frame, text="Purpose", bg="white").place(x=450, y=10)
    Label(payment_frame, text="Date", bg="white").place(x=20, y=60)
    Label(payment_frame, text="Slot", bg="white").place(x=450, y=60)

    # ================= SECURITY =================
    security_frame = LabelFrame(root, text="Security",
                               font=("Arial", 10, "bold"),
                               bg="white")
    security_frame.place(x=20, y=480, width=550, height=100)

    transaction_password = Entry(security_frame, show="*", width=20)
    transaction_password.place(x=180, y=10)

    otp = Entry(security_frame, width=20)
    otp.place(x=180, y=50)

    Label(security_frame, text="Password", bg="white").place(x=20, y=10)
    Label(security_frame, text="OTP", bg="white").place(x=20, y=50)

    # ================= SUMMARY =================
    summary_frame = LabelFrame(root, text="Summary",
                              font=("Arial", 10, "bold"),
                              bg="white")
    summary_frame.place(x=580, y=480, width=300, height=100)

    Label(summary_frame, text="Charges ₹10", bg="white").place(x=10, y=10)
    Label(summary_frame, text="Total ₹5010", bg="white").place(x=10, y=40)
    Label(summary_frame, text="Ref NEFT4589", bg="white").place(x=10, y=65)

    # ================= FUNCTIONS =================
    def verify_beneficiary():
        messagebox.showinfo("OK", "Verified")

    def transfer_money():
        messagebox.showinfo("Success", "NEFT Done")

    def reset_fields():
        holder_name.delete(0, END)
        account_number.delete(0, END)
        branch.delete(0, END)
        balance.delete(0, END)

        beneficiary_name.delete(0, END)
        beneficiary_account.delete(0, END)
        ifsc.delete(0, END)
        bank_name.delete(0, END)

        amount.delete(0, END)
        purpose.delete(0, END)
        transaction_date.delete(0, END)

        transaction_password.delete(0, END)
        otp.delete(0, END)

    # ================= BUTTONS (FIXED POSITION) =================
    Button(root, text="Verify", bg="orange",
           command=verify_beneficiary).place(x=180, y=620)

    Button(root, text="Transfer", bg="green",
           fg="white", command=transfer_money).place(x=300, y=620)

    Button(root, text="Reset", bg="blue",
           fg="white", command=reset_fields).place(x=430, y=620)

    Button(root, text="Close", bg="red",
           fg="white", command=root.destroy).place(x=560, y=620)



#=================================================================================================================================

def rtgs_transfer_window():

    # ================= MAIN WINDOW =================
    root = Toplevel()
    root.title("RTGS Transfer")
    root.geometry("900x700")
    root.resizable(False, False)

    
    root.config(bg="#ffe6e6") 

    # ================= TITLE =================
    Label(
        root,
        text="RTGS TRANSFER",
        font=("Arial", 18, "bold"),
        fg="darkred",
        bg="#ffe6e6"
    ).pack(pady=5)

    # ================= ACCOUNT FRAME =================
    account_frame = LabelFrame(root, text="Account Information",
                               font=("Arial", 10, "bold"),
                               bg="white")
    account_frame.place(x=20, y=50, width=860, height=120)

    holder_name = Entry(account_frame, width=25)
    account_number = Entry(account_frame, width=25)
    branch = Entry(account_frame, width=25)
    balance = Entry(account_frame, width=25)

    Label(account_frame, text="Name", bg="white").place(x=20, y=10)
    holder_name.place(x=150, y=10)

    Label(account_frame, text="Acc No", bg="white").place(x=450, y=10)
    account_number.place(x=550, y=10)

    Label(account_frame, text="Branch", bg="white").place(x=20, y=60)
    branch.place(x=150, y=60)

    Label(account_frame, text="Balance", bg="white").place(x=450, y=60)
    balance.place(x=550, y=60)

    # ================= BENEFICIARY FRAME =================
    beneficiary_frame = LabelFrame(root, text="Beneficiary Details",
                                   font=("Arial", 10, "bold"),
                                   bg="white")
    beneficiary_frame.place(x=20, y=180, width=860, height=150)

    beneficiary_name = Entry(beneficiary_frame, width=25)
    beneficiary_account = Entry(beneficiary_frame, width=25)
    ifsc = Entry(beneficiary_frame, width=25)
    bank_name = Entry(beneficiary_frame, width=25)

    Label(beneficiary_frame, text="Name", bg="white").place(x=20, y=10)
    beneficiary_name.place(x=150, y=10)

    Label(beneficiary_frame, text="Acc No", bg="white").place(x=450, y=10)
    beneficiary_account.place(x=550, y=10)

    Label(beneficiary_frame, text="IFSC", bg="white").place(x=20, y=60)
    ifsc.place(x=150, y=60)

    Label(beneficiary_frame, text="Bank", bg="white").place(x=450, y=60)
    bank_name.place(x=550, y=60)

    # ================= PAYMENT FRAME =================
    payment_frame = LabelFrame(root, text="Payment Details",
                               font=("Arial", 10, "bold"),
                               bg="white")
    payment_frame.place(x=20, y=340, width=860, height=120)

    amount = Entry(payment_frame, width=25)
    purpose = Entry(payment_frame, width=25)
    transaction_date = Entry(payment_frame, width=25)

    Label(payment_frame, text="Amount (Min ₹2,00,000)", bg="white").place(x=20, y=10)
    amount.place(x=200, y=10)

    Label(payment_frame, text="Purpose", bg="white").place(x=450, y=10)
    purpose.place(x=550, y=10)

    Label(payment_frame, text="Date", bg="white").place(x=20, y=60)
    transaction_date.place(x=200, y=60)

    # ================= SECURITY FRAME =================
    security_frame = LabelFrame(root, text="Security",
                               font=("Arial", 10, "bold"),
                               bg="white")
    security_frame.place(x=20, y=470, width=550, height=100)

    transaction_password = Entry(security_frame, show="*", width=20)
    otp = Entry(security_frame, width=20)

    Label(security_frame, text="Password", bg="white").place(x=20, y=10)
    transaction_password.place(x=150, y=10)

    Label(security_frame, text="OTP", bg="white").place(x=20, y=50)
    otp.place(x=150, y=50)

    # ================= SUMMARY FRAME =================
    summary_frame = LabelFrame(root, text="Summary",
                              font=("Arial", 10, "bold"),
                              bg="white")
    summary_frame.place(x=580, y=470, width=300, height=100)

    Label(summary_frame, text="RTGS Charges ₹25", fg="red", bg="white").place(x=10, y=10)
    Label(summary_frame, text="Real Time Settlement", fg="green", bg="white").place(x=10, y=40)
    Label(summary_frame, text="Ref: RTGS998877", fg="blue", bg="white").place(x=10, y=65)

    # ================= FUNCTIONS =================
    def verify_beneficiary():
        messagebox.showinfo("Verified", "Beneficiary Verified")

    def transfer_money():
        if amount.get() == "":
            messagebox.showerror("Error", "Enter Amount")
        else:
            messagebox.showinfo("Success", "RTGS Transfer Completed")

    def reset_fields():
        holder_name.delete(0, END)
        account_number.delete(0, END)
        branch.delete(0, END)
        balance.delete(0, END)

        beneficiary_name.delete(0, END)
        beneficiary_account.delete(0, END)
        ifsc.delete(0, END)
        bank_name.delete(0, END)

        amount.delete(0, END)
        purpose.delete(0, END)
        transaction_date.delete(0, END)

        transaction_password.delete(0, END)
        otp.delete(0, END)

    # ================= BUTTONS =================
    Button(root, text="Verify", bg="orange",
           command=verify_beneficiary).place(x=180, y=620)

    Button(root, text="Transfer RTGS", bg="green",
           fg="white", command=transfer_money).place(x=300, y=620)

    Button(root, text="Reset", bg="blue",
           fg="white", command=reset_fields).place(x=460, y=620)

    Button(root, text="Close", bg="red",
           fg="white", command=root.destroy).place(x=580, y=620)


#===============================================================================================================================

# ==========================================================
# IMPS TRANSFER WINDOW
# ==========================================================


def imps_transfer_window():

    root = tk.Toplevel()
    root.title("IMPS Transfer")
    root.geometry("900x600")
    root.config(bg="#0B1D51")   # Unique dark blue background

    # ==================================================
    # TITLE
    # ==================================================
    tk.Label(
        root,
        text="IMPS TRANSFER",
        font=("Arial", 28, "bold"),
        bg="#0B1D51",
        fg="white"
    ).pack(pady=20)

    # ==================================================
    # MAIN FRAME (CARD STYLE)
    # ==================================================
    frame = tk.Frame(
        root,
        bg="#1E3A8A",   # lighter blue card
        bd=0,
        highlightbackground="white",
        highlightthickness=2
    )
    frame.place(x=250, y=120, width=400, height=400)

    # ==================================================
    # RECEIVER ACCOUNT
    # ==================================================
    tk.Label(
        frame,
        text="Receiver Account No",
        bg="#1E3A8A",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    acc_entry = tk.Entry(frame, font=("Arial", 14))
    acc_entry.pack(ipady=5)

    # ==================================================
    # AMOUNT
    # ==================================================
    tk.Label(
        frame,
        text="Amount (₹)",
        bg="#1E3A8A",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    amt_entry = tk.Entry(frame, font=("Arial", 14))
    amt_entry.pack(ipady=5)

    # ==================================================
    # UPI PIN
    # ==================================================
    tk.Label(
        frame,
        text="UPI PIN",
        bg="#1E3A8A",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    pin_entry = tk.Entry(frame, font=("Arial", 14), show="*")
    pin_entry.pack(ipady=5)

    # ==================================================
    # TRANSFER FUNCTION
    # ==================================================
    def transfer():

        acc = acc_entry.get()
        amt = amt_entry.get()
        pin = pin_entry.get()

        if acc and amt and pin:
            messagebox.showinfo("IMPS", "Transfer Successful 🚀")
            root.destroy()
        else:
            messagebox.showerror("IMPS", "Please fill all fields")

    # ==================================================
    # BUTTON
    # ==================================================
    tk.Button(
        frame,
        text="Send Money",
        font=("Arial", 14, "bold"),
        bg="#00C853",
        fg="white",
        command=transfer
    ).pack(pady=30)


#=================================================================================================================================


# ==========================================================
#  transaction history WINDOW
# ==========================================================
def transaction_history_window():

    root = tk.Toplevel()
    root.title("Transaction History")
    root.geometry("900x600")
    root.config(bg="#2D0B4E") 

    # ==================================================
    # TITLE
    # ==================================================
    tk.Label(
        root,
        text="TRANSACTION HISTORY",
        font=("Arial", 26, "bold"),
        bg="#2D0B4E",
        fg="white"
    ).pack(pady=20)

    # ==================================================
    # MAIN FRAME (CARD STYLE)
    # ==================================================
    frame = tk.Frame(
        root,
        bg="#4C1D95",  
        bd=0,
        highlightbackground="white",
        highlightthickness=2
    )
    frame.place(x=150, y=100, width=600, height=420)

    # ==================================================
    # LISTBOX FOR TRANSACTIONS
    # ==================================================
    tk.Label(
        frame,
        text="Recent Transactions",
        font=("Arial", 16, "bold"),
        bg="#4C1D95",
        fg="white"
    ).pack(pady=10)

    listbox = tk.Listbox(
        frame,
        font=("Arial", 12),
        bg="#1E1B4B",
        fg="white",
        width=50,
        height=15,
        bd=0,
        highlightthickness=0
    )
    listbox.pack(pady=10)

    # ==================================================
    # SAMPLE DATA (you can replace with real data)
    # ==================================================
    transactions = [
        "✔ IMPS Transfer - ₹5000 - Success",
        "✔ UPI Payment - ₹1200 - Success",
        "✔ NEFT Transfer - ₹8000 - Pending",
        "✔ ATM Withdrawal - ₹2000 - Success",
        "✔ Online Shopping - ₹1500 - Success"
    ]

    for t in transactions:
        listbox.insert(tk.END, t)

    # ==================================================
    # CLOSE BUTTON
    # ==================================================
    tk.Button(
        frame,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(pady=10)



#================================================================================================================================


 # ==================================================
    # atm  services
 # ==================================================
def atm_services_window():

    root = tk.Toplevel()
    root.title("ATM Services")
    root.geometry("900x600")
    root.config(bg="#061A40")   # Deep navy background

    # ==================================================
    # TITLE
    # ==================================================
    tk.Label(
        root,
        text="ATM SERVICES",
        font=("Arial", 28, "bold"),
        bg="#061A40",
        fg="white"
    ).pack(pady=20)

    # ==================================================
    # MAIN FRAME (CARD STYLE)
    # ==================================================
    frame = tk.Frame(
        root,
        bg="#144272",   # blue card
        highlightbackground="white",
        highlightthickness=2
    )
    frame.place(x=250, y=120, width=400, height=400)

    tk.Label(
        frame,
        text="Select Your Service",
        font=("Arial", 16, "bold"),
        bg="#144272",
        fg="white"
    ).pack(pady=20)

    # ==================================================
    # FUNCTIONS
    # ==================================================
    def withdraw():
        messagebox.showinfo("ATM", "Withdraw Selected")

    def deposit():
        messagebox.showinfo("ATM", "Deposit Selected")

    def balance():
        messagebox.showinfo("ATM", "Balance Inquiry Selected")

    def pin_change():
        messagebox.showinfo("ATM", "PIN Change Selected")

    # ==================================================
    # BUTTONS
    # ==================================================
    tk.Button(
        frame,
        text="Withdraw Cash",
        font=("Arial", 12, "bold"),
        bg="#00C853",
        fg="white",
        width=20,
        command=withdraw
    ).pack(pady=10)

    tk.Button(
        frame,
        text="Deposit Cash",
        font=("Arial", 12, "bold"),
        bg="#2979FF",
        fg="white",
        width=20,
        command=deposit
    ).pack(pady=10)

    tk.Button(
        frame,
        text="Balance Inquiry",
        font=("Arial", 12, "bold"),
        bg="#FFD600",
        fg="black",
        width=20,
        command=balance
    ).pack(pady=10)

    tk.Button(
        frame,
        text="Change PIN",
        font=("Arial", 12, "bold"),
        bg="#FF1744",
        fg="white",
        width=20,
        command=pin_change
    ).pack(pady=10)

    # ==================================================
    # CLOSE BUTTON
    # ==================================================
    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(pady=20)






#=================================================================================================================================



    # ==================================================
    # cheque book request
    # ==================================================
def cheque_book_request_window():

    root = tk.Toplevel()
    root.title("Cheque Book Request")
    root.geometry("900x600")
    root.config(bg="#102A43")   # Deep blue background

    # ==================================================
    # TITLE
    # ==================================================
    tk.Label(
        root,
        text="CHEQUE BOOK REQUEST",
        font=("Arial", 26, "bold"),
        bg="#102A43",
        fg="white"
    ).pack(pady=20)

    # ==================================================
    # MAIN FRAME (CARD STYLE)
    # ==================================================
    frame = tk.Frame(
        root,
        bg="#243B53",   # steel blue card
        highlightbackground="white",
        highlightthickness=2
    )
    frame.place(x=250, y=120, width=400, height=420)

    # ==================================================
    # NAME
    # ==================================================
    tk.Label(
        frame,
        text="Account Holder Name",
        bg="#243B53",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    name_entry = tk.Entry(frame, font=("Arial", 14))
    name_entry.pack(ipady=5)

    # ==================================================
    # ACCOUNT NUMBER
    # ==================================================
    tk.Label(
        frame,
        text="Account Number",
        bg="#243B53",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    acc_entry = tk.Entry(frame, font=("Arial", 14))
    acc_entry.pack(ipady=5)

    # ==================================================
    # NUMBER OF LEAVES
    # ==================================================
    tk.Label(
        frame,
        text="Number of Cheque Leaves",
        bg="#243B53",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    leaves_entry = tk.Entry(frame, font=("Arial", 14))
    leaves_entry.pack(ipady=5)

    def request_cheque():

        name = name_entry.get()
        acc = acc_entry.get()
        leaves = leaves_entry.get()

        if name and acc and leaves:

            messagebox.showinfo(
                "Cheque Book",
                "Cheque Book Request Submitted Successfully"
            )
            root.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Please fill all details"
            )

    # ==================================================
    # BUTTON
    # ==================================================
    tk.Button(
        frame,
        text="Request Cheque Book",
        font=("Arial", 13, "bold"),
        bg="#00C853",
        fg="white",
        command=request_cheque
    ).pack(pady=25)

    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(pady=10)



#=================================================================================================================================


  # ==================================================
    #Passbook Update
    # ==================================================
def passbook_update_window():

    root = tk.Toplevel()
    root.title("Passbook Update")
    root.geometry("950x600")
    root.config(bg="#0D1321")   # dark elegant background

    # ==================================================
    # LEFT SIDEBAR FRAME (MENU STYLE)
    # ==================================================
    left_frame = tk.Frame(
        root,
        bg="#1D2D44",
        width=280,
        height=600
    )
    left_frame.pack(side="left", fill="y")

    tk.Label(
        left_frame,
        text="PASSBOOK\nSERVICE",
        font=("Arial", 20, "bold"),
        bg="#1D2D44",
        fg="white"
    ).pack(padx=60,pady=60)

    tk.Label(
        left_frame,
        text="Update • View • Download",
        font=("Arial", 10),
        bg="#1D2D44",
        fg="#A9BCD0"
    ).pack()

    # ==================================================
    # RIGHT MAIN PANEL (GLASS CARD STYLE)
    # ==================================================
    right_frame = tk.Frame(
        root,
        bg="#F0F4F8",
        bd=0
    )
    right_frame.pack(side="right", fill="both", expand=True)

    tk.Label(
        right_frame,
        text="PASSBOOK UPDATE REQUEST",
        font=("Arial", 22, "bold"),
        bg="#F0F4F8",
        fg="#102A43"
    ).pack(pady=30)

    # ==================================================
    # CENTER CARD (FORM BOX)
    # ==================================================
    card = tk.Frame(
        right_frame,
        bg="white",
        highlightbackground="#3D5A80",
        highlightthickness=2
    )
    card.place(x=120, y=120, width=450, height=350)

    # Account Number
    tk.Label(card, text="Account Number", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
    acc_entry = tk.Entry(card, font=("Arial", 14))
    acc_entry.pack(ipady=5)

    # Last Update Date
    tk.Label(card, text="Last Updated Date", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
    date_entry = tk.Entry(card, font=("Arial", 14))
    date_entry.pack(ipady=5)

    # Branch
    tk.Label(card, text="Branch Name", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
    branch_entry = tk.Entry(card, font=("Arial", 14))
    branch_entry.pack(ipady=5)

    # ==================================================
    # FUNCTION
    # ==================================================
    def update_passbook():

        acc = acc_entry.get()
        date = date_entry.get()
        branch = branch_entry.get()

        if acc and date and branch:
            messagebox.showinfo(
                "Passbook",
                "Passbook Update Request Sent Successfully"
            )
            root.destroy()
        else:
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

    # ==================================================
    # BUTTON
    # ==================================================
    tk.Button(
        card,
        text="Update Passbook",
        font=("Arial", 13, "bold"),
        bg="#00C853",
        fg="white",
        command=update_passbook
    ).pack(pady=25)

    tk.Button(
        right_frame,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(pady=2)



#==================================================================================================================================

 # ==================================================
    # Credit Card Services
    # ==================================================

def credit_card_services_window():

    root = tk.Toplevel()
    root.title("Credit Card Services")
    root.geometry("1200x600")
    root.config(bg="#0A192F")   # deep navy background

    # ==================================================
    # HEADER
    # ==================================================
    tk.Label(
        root,
        text="CREDIT CARD SERVICES",
        font=("Arial", 26, "bold"),
        bg="#0A192F",
        fg="white"
    ).pack(pady=20)

    tk.Label(
        root,
        text="Manage your credit card securely",
        font=("Arial", 12),
        bg="#0A192F",
        fg="#A8B2D1"
    ).pack()

    # ==================================================
    # MAIN WRAPPER FRAME
    # ==================================================
    main_frame = tk.Frame(root, bg="#0A192F")
    main_frame.pack(pady=60)

    # ==================================================
    # CARD STYLE FUNCTION (REUSABLE BLOCK)
    # ==================================================
    def create_card(parent, title, color, command):

        card = tk.Frame(
            parent,
            bg=color,
            width=250,
            height=150,
            highlightbackground="white",
            highlightthickness=1
        )
        card.pack(side="left", padx=15)

        tk.Label(
            card,
            text=title,
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white"
        ).place(x=20, y=20)

        tk.Button(
            card,
            text="Open",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="black",
            command=command
        ).place(x=90, y=90)

    # ==================================================
    # FUNCTIONS
    # ==================================================
    def apply_card():
        messagebox.showinfo("Credit Card", "Apply for Credit Card")

    def limit_check():
        messagebox.showinfo("Credit Card", "Check Credit Limit")

    def bill_payment():
        messagebox.showinfo("Credit Card", "Pay Credit Card Bill")

    def block_card():
        messagebox.showwarning("Credit Card", "Card Blocked Successfully")

    # ==================================================
    # CARD PANELS
    # ==================================================
    create_card(main_frame, "Apply Card", "#1E3A8A", apply_card)
    create_card(main_frame, "Limit Check", "#0F766E", limit_check)
    create_card(main_frame, "Bill Pay", "#7C3AED", bill_payment)
    create_card(main_frame, "Block Card", "#DC2626", block_card)

    # ==================================================
    # EXTRA BIG STATUS FRAME (BOTTOM PANEL STYLE)
    # ==================================================
    status_frame = tk.Frame(
        root,
        bg="#112240",
        highlightbackground="#64FFDA",
        highlightthickness=2
    )
    status_frame.place(x=300, y=350, width=650, height=180)

    tk.Label(
        status_frame,
        text="SECURITY STATUS",
        font=("Arial", 16, "bold"),
        bg="#112240",
        fg="#64FFDA"
    ).pack(pady=10)

    tk.Label(
        status_frame,
        text="✔ Card is Active\n✔ Online Transactions Enabled\n✔ Fraud Protection ON",
        font=("Arial", 12),
        bg="#112240",
        fg="white",
        justify="left"
    ).pack()

    # ==================================================
    # CLOSE BUTTON
    # ==================================================
    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(side=LEFT,padx=560,pady=20)



#==================================================================================================================================


 # ==================================================
    # Debit Card Services
    # ==================================================
def debit_card_services_window():

    root = tk.Toplevel()
    root.title("Debit Card Services")
    root.geometry("950x600")
    root.config(bg="#0B1320")   # deep navy background

    # ==================================================
    # HEADER
    # ==================================================
    tk.Label(
        root,
        text="DEBIT CARD SERVICES",
        font=("Arial", 26, "bold"),
        bg="#0B1320",
        fg="white"
    ).pack(pady=15)

    tk.Label(
        root,
        text="Secure & Fast Debit Card Management",
        font=("Arial", 12),
        bg="#0B1320",
        fg="#A9B4C0"
    ).pack()

    # ==================================================
    # MAIN FRAME
    # ==================================================
    main = tk.Frame(root, bg="#0B1320")
    main.pack(pady=30, fill="both", expand=True)

    # ==================================================
    # LEFT PANEL (INFO CARD STYLE)
    # ==================================================
    left = tk.Frame(
        main,
        bg="#162447",
        width=50,
        height=400,
        highlightbackground="white",
        highlightthickness=2
    )
    left.place(x=30,y=140,width=430)

    tk.Label(
        left,
        text="CARD STATUS",
        font=("Arial", 14, "bold"),
        bg="#162447",
        fg="#00FFAB"
    ).pack(pady=20)

    tk.Label(
        left,
        text="✔ Active Card\n✔ Online Enabled\n✔ ATM Enabled\n✔ Secure Mode ON",
        font=("Arial", 11),
        bg="#162447",
        fg="white",
        justify="left"
    ).pack(pady=10)

    # ==================================================
    # RIGHT PANEL (SERVICE CARDS)
    # ==================================================
    right = tk.Frame(main, bg="#0B1320")
    right.pack(side="right", padx=20)

    # Card function generator
    def create_button(text, color, msg):
        frame = tk.Frame(
            right,
            bg=color,
            width=250,
            height=90,
            highlightbackground="white",
            highlightthickness=1
        )
        frame.pack(pady=10)

        tk.Label(
            frame,
            text=text,
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white"
        ).place(x=20, y=15)

        tk.Button(
            frame,
            text="Open",
            bg="white",
            fg="black",
            font=("Arial", 10, "bold"),
            command=lambda: messagebox.showinfo("Debit Card", msg)
        ).place(x=180, y=30)

    # ==================================================
    # SERVICES
    # ==================================================
    create_button("Block Card", "#E63946", "Card Blocked Successfully")
    create_button("Replace Card", "#457B9D", "Card Replacement Requested")
    create_button("Change PIN", "#2A9D8F", "PIN Change Window Opened")
    create_button("Activate Card", "#F4A261", "Card Activated Successfully")

    # ==================================================
    # CLOSE BUTTON
    # ==================================================
    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        command=root.destroy
    ).place(x=200,y=500,width=60)



#=================================================================================================================================

# ==========================================================
# Net Banking
# ==========================================================

def net_banking_window():

    root = tk.Toplevel()
    root.title("Net Banking")
    root.geometry("1500x800")
    root.config(bg="#081229")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#0F1B3D", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🌐 NET BANKING PORTAL",
        font=("Arial", 30, "bold"),
        bg="#0F1B3D",
        fg="white"
    ).place(x=40, y=20)

    tk.Label(
        header,
        text="Fast • Secure • Smart Banking",
        font=("Arial", 13),
        bg="#0F1B3D",
        fg="#A5C9CA"
    ).place(x=45, y=60)

    # ==========================================================
    # LEFT SIDEBAR
    # ==========================================================

    sidebar = tk.Frame(root, bg="#101C3C")
    sidebar.place(x=0, y=90, width=270, height=710)

    tk.Label(
        sidebar,
        text="DASHBOARD",
        font=("Arial", 20, "bold"),
        bg="#101C3C",
        fg="#00E5FF"
    ).pack(pady=30)

    menu_items = [
        "🏦 Account Summary",
        "💸 Fund Transfer",
        "📜 Transaction History",
        "💳 Card Services",
        "📱 UPI Banking",
        "🧾 Bill Payments",
        "🔐 Security Center"
    ]

    for item in menu_items:

        tk.Button(
            sidebar,
            text=item,
            font=("Arial", 12, "bold"),
            bg="#162447",
            fg="white",
            activebackground="#00ADB5",
            activeforeground="black",
            width=24,
            bd=0,
            pady=12
        ).pack(pady=10)

    # ==========================================================
    # MAIN AREA
    # ==========================================================

    main = tk.Frame(root, bg="#081229")
    main.place(x=270, y=90, width=1230, height=710)

    # ==========================================================
    # WELCOME FRAME
    # ==========================================================

    welcome = tk.Frame(
        main,
        bg="#1B2A49",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    welcome.place(x=30, y=30, width=900, height=130)

    tk.Label(
        welcome,
        text="WELCOME BACK 👋",
        font=("Arial", 26, "bold"),
        bg="#1B2A49",
        fg="white"
    ).place(x=25, y=20)

    tk.Label(
        welcome,
        text="Manage all your banking services from one secure dashboard.",
        font=("Arial", 14),
        bg="#1B2A49",
        fg="#D6E4F0"
    ).place(x=28, y=75)

    # ==========================================================
    # SERVICE CARD FUNCTION
    # ==========================================================

    def service_box(x, y, title, color, msg):

        frame = tk.Frame(
            main,
            bg=color,
            highlightbackground="white",
            highlightthickness=1
        )

        frame.place(x=x, y=y, width=260, height=160)

        tk.Label(
            frame,
            text=title,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white"
        ).place(x=20, y=25)

        tk.Button(
            frame,
            text="Open",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="black",
            command=lambda: messagebox.showinfo("Net Banking", msg)
        ).place(x=95, y=95)

    # ==========================================================
    # SERVICE BOXES
    # ==========================================================

    service_box(
        30, 220,
        "💸 Transfer Money",
        "#006D77",
        "Transfer Window Opened"
    )

    service_box(
        330, 220,
        "📜 Transaction History",
        "#7B2CBF",
        "Transaction History Opened"
    )

    service_box(
        630, 220,
        "💳 Card Services",
        "#E63946",
        "Card Services Opened"
    )

    service_box(
        30, 430,
        "📱 UPI Banking",
        "#FF8800",
        "UPI Services Opened"
    )

    service_box(
        330, 430,
        "🧾 Bill Payments",
        "#2A9D8F",
        "Bill Payment Window Opened"
    )

    service_box(
        630, 430,
        "🔐 Security Center",
        "#3A86FF",
        "Security Center Opened"
    )

    # ==========================================================
    # STATUS PANEL
    # ==========================================================

    status = tk.Frame(
        main,
        bg="#162447",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    status.place(x=940, y=30, width=240, height=560)

    tk.Label(
        status,
        text="ACCOUNT STATUS",
        font=("Arial", 16, "bold"),
        bg="#162447",
        fg="#00FFAB"
    ).pack(pady=25)

    tk.Label(
        status,
        text="✔ Account Active\n\n✔ Internet Banking ON\n\n✔ UPI Linked\n\n✔ Debit Card Active\n\n✔ Last Login:\nToday 10:45 AM",
        font=("Arial", 12),
        justify="left",
        bg="#162447",
        fg="white"
    ).pack(pady=20)

    # ==========================================================
    # LOGOUT BUTTON
    # ==========================================================

    tk.Button(
        main,
        text="Logout",
        font=("Arial", 13, "bold"),
        bg="red",
        fg="white",
        width=15,
        command=root.destroy
    ).place(x=960, y=620)




#=================================================================================================================================

# ==========================================================
    # Mobile Banking
# ==========================================================



def mobile_banking_window():

    root = tk.Toplevel()
    root.title("Mobile Banking")
    root.geometry("1500x800")
    root.config(bg="#0B1026")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#121B3A", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="📱 MOBILE BANKING",
        font=("Arial", 30, "bold"),
        bg="#121B3A",
        fg="white"
    ).place(x=40, y=18)

    tk.Label(
        header,
        text="Secure Banking Anytime • Anywhere",
        font=("Arial", 13),
        bg="#121B3A",
        fg="#B8C1EC"
    ).place(x=45, y=60)

    # ==========================================================
    # LEFT PHONE FRAME
    # ==========================================================

    phone_outer = tk.Frame(
        root,
        bg="#1F2A56",
        highlightbackground="white",
        highlightthickness=2
    )

    phone_outer.place(x=80, y=150, width=320, height=560)

    # Mobile top bar
    tk.Frame(phone_outer, bg="black", height=30).pack(fill="x")

    tk.Label(
        phone_outer,
        text="MyBank App",
        font=("Arial", 18, "bold"),
        bg="#1F2A56",
        fg="white"
    ).pack(pady=20)

    balance_card = tk.Frame(
        phone_outer,
        bg="#00ADB5"
    )

    balance_card.place(x=25, y=90, width=260, height=120)

    tk.Label(
        balance_card,
        text="Available Balance",
        font=("Arial", 12, "bold"),
        bg="#00ADB5",
        fg="white"
    ).place(x=20, y=20)

    tk.Label(
        balance_card,
        text="₹ 2,45,000",
        font=("Arial", 24, "bold"),
        bg="#00ADB5",
        fg="white"
    ).place(x=20, y=55)

    # ==========================================================
    # QUICK ACTION BUTTONS
    # ==========================================================

    def popup(msg):
        messagebox.showinfo("Mobile Banking", msg)

    actions = [
        ("💸 Transfer", "#E63946", "Money Transfer Opened"),
        ("📱 Recharge", "#457B9D", "Recharge Window Opened"),
        ("🧾 Bills", "#2A9D8F", "Bill Payment Opened"),
        ("📜 History", "#9D4EDD", "Transaction History Opened"),
        ("💳 Cards", "#FF8800", "Card Services Opened"),
        ("🏦 Loans", "#3A86FF", "Loan Services Opened")
    ]

    x_positions = [20, 160]
    y = 250
    count = 0

    for text, color, msg in actions:

        tk.Button(
            phone_outer,
            text=text,
            font=("Arial", 11, "bold"),
            bg=color,
            fg="white",
            width=12,
            height=2,
            command=lambda m=msg: popup(m)
        ).place(x=x_positions[count % 2], y=y)

        count += 1

        if count % 2 == 0:
            y += 90

    # ==========================================================
    # RIGHT INFORMATION PANEL
    # ==========================================================

    info = tk.Frame(
        root,
        bg="#162447",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    info.place(x=500, y=150, width=900, height=560)

    tk.Label(
        info,
        text="MOBILE BANKING FEATURES",
        font=("Arial", 26, "bold"),
        bg="#162447",
        fg="#00E5FF"
    ).pack(pady=30)

    features = [
        "✔ Instant Fund Transfer",
        "✔ QR Code Payments",
        "✔ UPI Integration",
        "✔ Credit / Debit Card Management",
        "✔ Recharge & Bill Payments",
        "✔ Real-time Transaction Alerts",
        "✔ Secure Login Authentication",
        "✔ Loan & EMI Services"
    ]

    for feature in features:

        tk.Label(
            info,
            text=feature,
            font=("Arial", 15),
            bg="#162447",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=80, pady=10)

    # ==========================================================
    # STATUS CARD
    # ==========================================================

    status = tk.Frame(
        info,
        bg="#0F3460"
    )

    status.place(x=450, y=420, width=380, height=90)

    tk.Label(
        status,
        text="✔ Mobile Banking Active",
        font=("Arial", 16, "bold"),
        bg="#0F3460",
        fg="#00FFAB"
    ).pack(pady=12)

    tk.Label(
        status,
        text="Last Login : Today 09:40 AM",
        font=("Arial", 11),
        bg="#0F3460",
        fg="white"
    ).pack()

    # ==========================================================
    # CLOSE BUTTON
    # ==========================================================

    tk.Button(
        root,
        text="Close",
        font=("Arial", 13, "bold"),
        bg="red",
        fg="white",
        width=15,
        command=root.destroy
    ).place(x=1080, y=730)





#=================================================================================================================================



# ==========================================================
    # Change Password
# ==========================================================

def change_password_window():

    root = tk.Toplevel()
    root.title("Change Password")
    root.geometry("1000x600")
    root.config(bg="#0B132B")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#1C2541", height=80)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🔐 CHANGE PASSWORD",
        font=("Arial", 28, "bold"),
        bg="#1C2541",
        fg="white"
    ).place(x=30, y=18)

    # ==========================================================
    # LEFT SECURITY PANEL
    # ==========================================================

    left = tk.Frame(
        root,
        bg="#3A506B",
        highlightbackground="white",
        highlightthickness=2
    )

    left.place(x=40, y=120, width=300, height=400)

    tk.Label(
        left,
        text="SECURITY TIPS",
        font=("Arial", 20, "bold"),
        bg="#3A506B",
        fg="#00E5FF"
    ).pack(pady=25)

    tips = [
        "✔ Use strong passwords",
        "✔ Avoid sharing OTP",
        "✔ Change password regularly",
        "✔ Use special characters",
        "✔ Keep account secure"
    ]

    for tip in tips:

        tk.Label(
            left,
            text=tip,
            font=("Arial", 12),
            bg="#3A506B",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=25, pady=10)

    # ==========================================================
    # RIGHT FORM PANEL
    # ==========================================================

    right = tk.Frame(
        root,
        bg="#F4F7FC",
        highlightbackground="#00ADB5",
        highlightthickness=2
    )

    right.place(x=420, y=100, width=500, height=480)

    tk.Label(
        right,
        text="Update Your Password",
        font=("Arial", 22, "bold"),
        bg="#F4F7FC",
        fg="#1C2541"
    ).pack(pady=25)

    # ==========================================================
    # OLD PASSWORD
    # ==========================================================

    tk.Label(
        right,
        text="Old Password",
        font=("Arial", 12, "bold"),
        bg="#F4F7FC"
    ).pack(anchor="w", padx=70)

    old_pass = tk.Entry(
        right,
        font=("Arial", 14),
        width=30,
        show="*"
    )
    old_pass.pack(pady=10, ipady=6)

    # ==========================================================
    # NEW PASSWORD
    # ==========================================================

    tk.Label(
        right,
        text="New Password",
        font=("Arial", 12, "bold"),
        bg="#F4F7FC"
    ).pack(anchor="w", padx=70)

    new_pass = tk.Entry(
        right,
        font=("Arial", 14),
        width=30,
        show="*"
    )
    new_pass.pack(pady=10, ipady=6)

    # ==========================================================
    # CONFIRM PASSWORD
    # ==========================================================

    tk.Label(
        right,
        text="Confirm Password",
        font=("Arial", 12, "bold"),
        bg="#F4F7FC"
    ).pack(anchor="w", padx=70)

    confirm_pass = tk.Entry(
        right,
        font=("Arial", 14),
        width=30,
        show="*"
    )
    confirm_pass.pack(pady=10, ipady=6)

    # ==========================================================
    # CHANGE PASSWORD FUNCTION
    # ==========================================================

    def update_password():

        old = old_pass.get()
        new = new_pass.get()
        confirm = confirm_pass.get()

        if old == "" or new == "" or confirm == "":

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

        elif new != confirm:

            messagebox.showerror(
                "Error",
                "New Password and Confirm Password do not match"
            )

        else:

            messagebox.showinfo(
                "Success",
                "Password Changed Successfully"
            )

            root.destroy()

    # ==========================================================
    # BUTTONS
    # ==========================================================

    tk.Button(
        right,
        text="Update Password",
        font=("Arial", 13, "bold"),
        bg="#00ADB5",
        fg="white",
        width=18,
        command=update_password
    ).pack(pady=25)

    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=12,
        command=root.destroy
    ).place(x=600, y=540)




#=================================================================================================================================


# ==========================================================
    # Reset PIN
# ==========================================================

def reset_pin_window():

    root = tk.Toplevel()
    root.title("Reset PIN")
    root.geometry("1000x600")
    root.config(bg="#09122C")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#14213D", height=80)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🔐 RESET ATM PIN",
        font=("Arial", 28, "bold"),
        bg="#14213D",
        fg="white"
    ).place(x=30, y=18)

    # ==========================================================
    # LEFT INFO PANEL
    # ==========================================================

    left = tk.Frame(
        root,
        bg="#1F4068",
        highlightbackground="white",
        highlightthickness=2
    )

    left.place(x=40, y=120, width=300, height=400)

    tk.Label(
        left,
        text="PIN SECURITY",
        font=("Arial", 20, "bold"),
        bg="#1F4068",
        fg="#00E5FF"
    ).pack(pady=25)

    info = [
        "✔ Keep PIN confidential",
        "✔ Do not share OTP",
        "✔ Use strong PIN numbers",
        "✔ Change PIN regularly",
        "✔ Avoid simple PINs"
    ]

    for item in info:

        tk.Label(
            left,
            text=item,
            font=("Arial", 12),
            bg="#1F4068",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=20, pady=10)

    # ==========================================================
    # RIGHT FORM PANEL
    # ==========================================================

    right = tk.Frame(
        root,
        bg="#F8F9FA",
        highlightbackground="#00ADB5",
        highlightthickness=2
    )

    right.place(x=400, y=120, width=520, height=400)

    tk.Label(
        right,
        text="Create New ATM PIN",
        font=("Arial", 24, "bold"),
        bg="#F8F9FA",
        fg="#14213D"
    ).pack(pady=25)

    # ==========================================================
    # CARD NUMBER
    # ==========================================================

    tk.Label(
        right,
        text="Debit Card Number",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=70)

    card_entry = tk.Entry(
        right,
        font=("Arial", 14),
        width=32
    )
    card_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # NEW PIN
    # ==========================================================

    tk.Label(
        right,
        text="New PIN",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=70)

    pin_entry = tk.Entry(
        right,
        font=("Arial", 14),
        width=32,
        show="*"
    )
    pin_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # CONFIRM PIN
    # ==========================================================

    tk.Label(
        right,
        text="Confirm PIN",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=70)

    confirm_entry = tk.Entry(
        right,
        font=("Arial", 14),
        width=32,
        show="*"
    )
    confirm_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # RESET FUNCTION
    # ==========================================================

    def reset_pin():

        card = card_entry.get()
        pin = pin_entry.get()
        confirm = confirm_entry.get()

        if card == "" or pin == "" or confirm == "":

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

        elif pin != confirm:

            messagebox.showerror(
                "Error",
                "PIN does not match"
            )

        elif len(pin) != 4:

            messagebox.showerror(
                "Error",
                "PIN must be 4 digits"
            )

        else:

            messagebox.showinfo(
                "Success",
                "ATM PIN Reset Successfully"
            )

            root.destroy()

    # ==========================================================
    # BUTTONS
    # ==========================================================

    tk.Button(
        right,
        text="Reset PIN",
        font=("Arial", 13, "bold"),
        bg="#00ADB5",
        fg="white",
        width=18,
        command=reset_pin
    ).pack(pady=30)

    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=12,
        command=root.destroy
    ).place(x=620, y=540)




#================================================================================================================================

 # ==========================================================
    # Customer Care
# ==========================================================

def customer_care_window():

    root = tk.Toplevel()
    root.title("Customer Care")
    root.geometry("1500x800")
    root.config(bg="#071330")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#0B1F4D", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🎧 CUSTOMER CARE CENTER",
        font=("Arial", 30, "bold"),
        bg="#0B1F4D",
        fg="white"
    ).place(x=40, y=20)

    tk.Label(
        header,
        text="24×7 Banking Support & Assistance",
        font=("Arial", 13),
        bg="#0B1F4D",
        fg="#B8C1EC"
    ).place(x=45, y=62)

    # ==========================================================
    # LEFT SUPPORT PANEL
    # ==========================================================

    support = tk.Frame(
        root,
        bg="#112D4E",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    support.place(x=40, y=130, width=350, height=600)

    tk.Label(
        support,
        text="SUPPORT SERVICES",
        font=("Arial", 22, "bold"),
        bg="#112D4E",
        fg="#00E5FF"
    ).pack(pady=25)

    services = [
        "✔ Account Related Issues",
        "✔ ATM / Card Problems",
        "✔ UPI Transaction Support",
        "✔ Loan & EMI Assistance",
        "✔ Internet Banking Help",
        "✔ Fraud Protection Support",
        "✔ Password Reset Services"
    ]

    for item in services:

        tk.Label(
            support,
            text=item,
            font=("Arial", 13),
            bg="#112D4E",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=30, pady=12)

    # ==========================================================
    # CENTER CONTACT CARD
    # ==========================================================

    contact = tk.Frame(
        root,
        bg="#F5F7FA",
        highlightbackground="#3A86FF",
        highlightthickness=3
    )

    contact.place(x=450, y=130, width=500, height=600)

    tk.Label(
        contact,
        text="CONTACT CUSTOMER CARE",
        font=("Arial", 24, "bold"),
        bg="#F5F7FA",
        fg="#0B1F4D"
    ).pack(pady=25)

    # ==========================================================
    # NAME
    # ==========================================================

    tk.Label(
        contact,
        text="Full Name",
        font=("Arial", 12, "bold"),
        bg="#F5F7FA"
    ).pack(anchor="w", padx=70)

    name_entry = tk.Entry(
        contact,
        font=("Arial", 14),
        width=32
    )
    name_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # EMAIL
    # ==========================================================

    tk.Label(
        contact,
        text="Email Address",
        font=("Arial", 12, "bold"),
        bg="#F5F7FA"
    ).pack(anchor="w", padx=70)

    email_entry = tk.Entry(
        contact,
        font=("Arial", 14),
        width=32
    )
    email_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # ISSUE TYPE
    # ==========================================================

    tk.Label(
        contact,
        text="Issue Type",
        font=("Arial", 12, "bold"),
        bg="#F5F7FA"
    ).pack(anchor="w", padx=70)

    issue_box = tk.StringVar()

    options = [
        "ATM Problem",
        "UPI Failed",
        "Loan Query",
        "Card Block",
        "Password Reset"
    ]

    dropdown = tk.OptionMenu(contact, issue_box, *options)
    dropdown.config(font=("Arial", 12), width=25)
    dropdown.pack(pady=10)

    # ==========================================================
    # MESSAGE BOX
    # ==========================================================

    tk.Label(
        contact,
        text="Describe Your Issue",
        font=("Arial", 12, "bold"),
        bg="#F5F7FA"
    ).pack(anchor="w", padx=70)

    message_box = tk.Text(
        contact,
        font=("Arial", 12),
        width=35,
        height=5
    )
    message_box.pack(pady=10)

    # ==========================================================
    # SUBMIT FUNCTION
    # ==========================================================

    def submit_issue():

        name = name_entry.get()
        email = email_entry.get()
        issue = issue_box.get()

        if name == "" or email == "" or issue == "":

            messagebox.showerror(
                "Error",
                "Please fill all details"
            )

        else:

            messagebox.showinfo(
                "Customer Care",
                "Your issue has been submitted successfully"
            )

    # ==========================================================
    # BUTTON
    # ==========================================================

    tk.Button(
        contact,
        text="Submit Request",
        font=("Arial", 13, "bold"),
        bg="#00ADB5",
        fg="white",
        width=18,
        command=submit_issue
    ).pack(pady=20)

    # ==========================================================
    # RIGHT LIVE HELP PANEL
    # ==========================================================

    live = tk.Frame(
        root,
        bg="#162447",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    live.place(x=1030, y=130, width=380, height=600)

    tk.Label(
        live,
        text="LIVE HELP DESK",
        font=("Arial", 22, "bold"),
        bg="#162447",
        fg="#00FFAB"
    ).pack(pady=25)

    tk.Label(
        live,
        text="📞 Toll Free Number",
        font=("Arial", 15, "bold"),
        bg="#162447",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        live,
        text="1800-202-9999",
        font=("Arial", 18, "bold"),
        bg="#162447",
        fg="#FFD60A"
    ).pack()

    tk.Label(
        live,
        text="\n📧 Email Support",
        font=("Arial", 15, "bold"),
        bg="#162447",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        live,
        text="support@mybank.com",
        font=("Arial", 14),
        bg="#162447",
        fg="#90E0EF"
    ).pack()

    tk.Label(
        live,
        text="\n⏰ Working Hours",
        font=("Arial", 15, "bold"),
        bg="#162447",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        live,
        text="24 Hours • 7 Days",
        font=("Arial", 14),
        bg="#162447",
        fg="#F1FAEE"
    ).pack()

    tk.Label(
        live,
        text="\n🟢 Live Agent Available",
        font=("Arial", 16, "bold"),
        bg="#162447",
        fg="#00FFAB"
    ).pack(pady=30)

    # ==========================================================
    # CLOSE BUTTON
    # ==========================================================

    tk.Button(
        root,
        text="Close",
        font=("Arial", 13, "bold"),
        bg="red",
        fg="white",
        width=15,
        command=root.destroy
    ).place(x=1040, y=20,width=80)

    

#=================================================================================================================================

 # ==========================================================
    # Email Support
# ==========================================================


def email_support_window():

    root = tk.Toplevel()
    root.title("Email Support")
    root.geometry("1200x700")
    root.config(bg="#1B263B")   

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#0D1B2A", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="📧 EMAIL SUPPORT CENTER",
        font=("Arial", 30, "bold"),
        bg="#0D1B2A",
        fg="white"
    ).place(x=40, y=20)

    tk.Label(
        header,
        text="Fast & Secure Banking Email Assistance",
        font=("Arial", 13),
        bg="#0D1B2A",
        fg="#B8C1EC"
    ).place(x=45, y=62)

    # ==========================================================
    # LEFT INFO PANEL
    # ==========================================================

    left = tk.Frame(
        root,
        bg="#415A77",
        highlightbackground="white",
        highlightthickness=2
    )

    left.place(x=40, y=130, width=320, height=500)

    tk.Label(
        left,
        text="EMAIL SUPPORT",
        font=("Arial", 22, "bold"),
        bg="#415A77",
        fg="#00E5FF"
    ).pack(pady=25)

    support_items = [
        "✔ Account Assistance",
        "✔ UPI Related Queries",
        "✔ Card Services Support",
        "✔ Internet Banking Help",
        "✔ Loan Information",
        "✔ ATM Related Issues",
        "✔ Password Recovery"
    ]

    for item in support_items:

        tk.Label(
            left,
            text=item,
            font=("Arial", 13),
            bg="#415A77",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=25, pady=12)

    # ==========================================================
    # CENTER EMAIL FORM
    # ==========================================================

    center = tk.Frame(
        root,
        bg="#F8F9FA",
        highlightbackground="#00ADB5",
        highlightthickness=3
    )

    center.place(x=420, y=130, width=450, height=500)

    tk.Label(
        center,
        text="SEND EMAIL REQUEST",
        font=("Arial", 24, "bold"),
        bg="#F8F9FA",
        fg="#0D1B2A"
    ).pack(pady=20)

    # ==========================================================
    # NAME
    # ==========================================================

    tk.Label(
        center,
        text="Full Name",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=60)

    name_entry = tk.Entry(
        center,
        font=("Arial", 14),
        width=30
    )
    name_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # EMAIL
    # ==========================================================

    tk.Label(
        center,
        text="Email Address",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=60)

    email_entry = tk.Entry(
        center,
        font=("Arial", 14),
        width=30
    )
    email_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # SUBJECT
    # ==========================================================

    tk.Label(
        center,
        text="Subject",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=60)

    subject_entry = tk.Entry(
        center,
        font=("Arial", 14),
        width=30
    )
    subject_entry.pack(pady=10, ipady=6)

    # ==========================================================
    # MESSAGE
    # ==========================================================

    tk.Label(
        center,
        text="Message",
        font=("Arial", 12, "bold"),
        bg="#F8F9FA"
    ).pack(anchor="w", padx=60)

    message_box = tk.Text(
        center,
        font=("Arial", 12),
        width=34,
        height=5
    )
    message_box.pack(pady=10)

    # ==========================================================
    # SEND EMAIL FUNCTION
    # ==========================================================

    def send_email():

        name = name_entry.get()
        email = email_entry.get()
        subject = subject_entry.get()

        if name == "" or email == "" or subject == "":

            messagebox.showerror(
                "Error",
                "Please fill all details"
            )

        else:

            messagebox.showinfo(
                "Email Support",
                "Your email request has been sent successfully"
            )

    # ==========================================================
    # SEND BUTTON
    # ==========================================================

    tk.Button(
        center,
        text="Send Email",
        font=("Arial", 13, "bold"),
        bg="#00ADB5",
        fg="white",
        width=18,
        command=send_email
    ).pack(pady=20)

    # ==========================================================
    # RIGHT CONTACT PANEL
    # ==========================================================

    right = tk.Frame(
        root,
        bg="#23395B",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    right.place(x=920, y=130, width=230, height=500)

    tk.Label(
        right,
        text="CONTACT INFO",
        font=("Arial", 20, "bold"),
        bg="#23395B",
        fg="#00FFAB"
    ).pack(pady=25)

    tk.Label(
        right,
        text="📧 Support Email",
        font=("Arial", 14, "bold"),
        bg="#23395B",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        right,
        text="support@mybank.com",
        font=("Arial", 12),
        bg="#23395B",
        fg="#90E0EF"
    ).pack()

    tk.Label(
        right,
        text="\n📞 Toll Free",
        font=("Arial", 14, "bold"),
        bg="#23395B",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        right,
        text="1800-202-9999",
        font=("Arial", 13),
        bg="#23395B",
        fg="#FFD60A"
    ).pack()

    tk.Label(
        right,
        text="\n⏰ Support Time",
        font=("Arial", 14, "bold"),
        bg="#23395B",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        right,
        text="24 × 7 Available",
        font=("Arial", 12),
        bg="#23395B",
        fg="#F1FAEE"
    ).pack()

    # ==========================================================
    # CLOSE BUTTON
    # ==========================================================

    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=12,
        command=root.destroy
    ).place(x=1010, y=20)



#================================================================================================================================

# ==========================================================
    # Branch Locator
# ==========================================================
def branch_locator():

    root = tk.Toplevel()
    root.title("MyBank Branch Locator")
    root.geometry("1500x820")
    root.config(bg="#0B132B")

    # ==========================================================
    # HEADER
    # ==========================================================

    header = tk.Frame(root, bg="#1C2541", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏦 BRANCH LOCATOR",
        font=("Arial", 30, "bold"),
        bg="#1C2541",
        fg="white"
    ).place(x=35, y=18)

    tk.Label(
        header,
        text="Find Nearby Branches, ATM Services & Banking Facilities",
        font=("Arial", 13),
        bg="#1C2541",
        fg="#BFD7EA"
    ).place(x=40, y=60)

    # ==========================================================
    # LEFT SEARCH FRAME
    # ==========================================================

    left = tk.Frame(
        root,
        bg="#243B55",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    left.place(x=20, y=120, width=330, height=650)

    tk.Label(
        left,
        text="SEARCH PANEL",
        font=("Arial", 22, "bold"),
        bg="#243B55",
        fg="#00E5FF"
    ).pack(pady=20)

    # ----------------------------------------------------------

    labels = [
        "Select State",
        "Select City",
        "Enter Area / Pincode",
        "Select Branch Type",
        "Select Service"
    ]

    for text in labels:

        tk.Label(
            left,
            text=text,
            font=("Arial", 12, "bold"),
            bg="#243B55",
            fg="white"
        ).pack(anchor="w", padx=25, pady=5)

        if text == "Enter Area / Pincode":

            entry = tk.Entry(
                left,
                font=("Arial", 12),
                width=28
            )
            entry.pack(pady=8, ipady=5)

        else:

            combo = ttk.Combobox(
                left,
                width=28,
                font=("Arial", 12),
                values=[
                    "Pune",
                    "Mumbai",
                    "Delhi",
                    "Bangalore",
                    "Main Branch",
                    "ATM",
                    "Loan Center",
                    "Cash Deposit",
                    "Locker Facility"
                ]
            )

            combo.pack(pady=8)

    # ==========================================================
    # SEARCH BUTTONS
    # ==========================================================

    tk.Button(
        left,
        text="Search Branch",
        font=("Arial", 13, "bold"),
        bg="#00ADB5",
        fg="white",
        width=18,
        pady=5
    ).pack(pady=25)

    tk.Button(
        left,
        text="Reset",
        font=("Arial", 13, "bold"),
        bg="orange",
        fg="white",
        width=18,
        pady=5
    ).pack()

    # ==========================================================
    # CENTER RESULT FRAME
    # ==========================================================

    center = tk.Frame(
        root,
        bg="#F8FAFC",
        highlightbackground="#3B82F6",
        highlightthickness=3
    )

    center.place(x=370, y=120, width=650, height=650)

    tk.Label(
        center,
        text="AVAILABLE BRANCHES",
        font=("Arial", 24, "bold"),
        bg="#F8FAFC",
        fg="#1E293B"
    ).pack(pady=15)

    # ==========================================================
    # SCROLLBAR + LISTBOX
    # ==========================================================

    scroll = tk.Scrollbar(center)
    scroll.pack(side="right", fill="y")

    branch_list = tk.Listbox(
        center,
        font=("Arial", 12),
        width=75,
        height=28,
        bg="#E2E8F0",
        fg="#0F172A",
        yscrollcommand=scroll.set,
        selectbackground="#00ADB5"
    )

    branch_list.pack(padx=15, pady=10)

    scroll.config(command=branch_list.yview)

    # ==========================================================
    # SAMPLE DATA
    # ==========================================================

    data = [
        "🏦 MyBank Main Branch - Pune",
        "Address : FC Road, Pune",
        "IFSC Code : MYBK000101",
        "Contact : 020-987654321",
        "Working Hours : 10 AM - 5 PM",
        "Status : OPEN",
        "--------------------------------------",

        "🏧 MyBank ATM Center - Shivaji Nagar",
        "24×7 ATM Service Available",
        "Cash Deposit Machine Available",
        "Distance : 1.2 KM",
        "--------------------------------------",

        "🏦 MyBank Loan Center",
        "Home Loan / Car Loan / Personal Loan",
        "Loan Support Available",
        "--------------------------------------",

        "🏦 Locker Facility Available",
        "Internet Banking Help",
        "Passbook Update Machine",
        "Cheque Deposit Service",
        "--------------------------------------",

        "📞 Customer Care : 1800-202-9999",
        "📧 Email : support@mybank.com"
    ]

    for item in data:
        branch_list.insert(tk.END, item)

    # ==========================================================
    # RIGHT TOP FACILITY FRAME
    # ==========================================================

    right_top = tk.Frame(
        root,
        bg="#1D3557",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    right_top.place(x=1050, y=120, width=420, height=300)

    tk.Label(
        right_top,
        text="BRANCH FACILITIES",
        font=("Arial", 22, "bold"),
        bg="#1D3557",
        fg="#00FFAB"
    ).pack(pady=18)

    facilities = [
        "✔ Cash Withdrawal",
        "✔ ATM Facility",
        "✔ Loan Assistance",
        "✔ Locker Facility",
        "✔ Passbook Update",
        "✔ Internet Banking",
        "✔ Credit Card Support",
        "✔ Cheque Deposit"
    ]

    for item in facilities:

        tk.Label(
            right_top,
            text=item,
            font=("Arial", 12),
            bg="#1D3557",
            fg="white",
            anchor="w"
        ).pack(fill="x", padx=25, pady=5)

    # ==========================================================
    # RIGHT CENTER MAP FRAME
    # ==========================================================

    map_frame = tk.Frame(
        root,
        bg="#14213D",
        highlightbackground="white",
        highlightthickness=2
    )

    map_frame.place(x=1050, y=440, width=420, height=160)

    tk.Label(
        map_frame,
        text="🗺 LOCATION DETAILS",
        font=("Arial", 20, "bold"),
        bg="#14213D",
        fg="#FFD60A"
    ).pack(pady=15)

    tk.Label(
        map_frame,
        text="""
Current Location : Pune
Nearest ATM : 1.2 KM
Nearby Branches : 3
Route Direction Available
""",
        font=("Arial", 12),
        bg="#14213D",
        fg="white",
        justify="left"
    ).pack()

    # ==========================================================
    # RIGHT BOTTOM SECURITY FRAME
    # ==========================================================

    security = tk.Frame(
        root,
        bg="#FFE5E5",
        highlightbackground="red",
        highlightthickness=2
    )

    security.place(x=1050, y=620, width=420, height=150)

    tk.Label(
        security,
        text="⚠ SECURITY NOTICE",
        font=("Arial", 18, "bold"),
        bg="#FFE5E5",
        fg="red"
    ).pack(pady=10)

    tk.Label(
        security,
        text="""
Never Share OTP, ATM PIN or Password.

MyBank Never Asks For Confidential Information.

Use Safe & Secure Banking Services.
""",
        font=("Arial", 11, "bold"),
        bg="#FFE5E5",
        fg="#7F0000",
        justify="left"
    ).pack()

    # ==========================================================
    # FOOTER BUTTONS
    # ==========================================================

    '''tk.Button(
        root,
        text="View Details",
        font=("Arial", 12, "bold"),
        bg="#3A86FF",
        fg="white",
        width=15
    ).place(x=430, y=20)'''

    tk.Button(
        root,
        text="Get Direction",
        font=("Arial", 12, "bold"),
        bg="#2A9D8F",
        fg="white",
        width=15
    ).place(x=650, y=20)

    tk.Button(
        root,
        text="Contact Branch",
        font=("Arial", 12, "bold"),
        bg="#8338EC",
        fg="white",
        width=15
    ).place(x=870, y=20)

    tk.Button(
        root,
        text="Close",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=15,
        command=root.destroy
    ).place(x=1090, y=20)





#=================================================================================================================================

 # ==========================================================
    # Head Office
# ==========================================================


def head_office_window():

    root = tk.Toplevel()
    root.title("Head Office")
    root.geometry("1000x650")
    root.config(bg="#0B132B")

    # ======================================================
    # HEADER
    # ======================================================

    header = tk.Frame(root, bg="#1C2541", height=70)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏢 MYBANK HEAD OFFICE",
        font=("Arial", 24, "bold"),
        bg="#1C2541",
        fg="white"
    ).place(x=20, y=15)

    # ======================================================
    # LEFT FRAME
    # ======================================================

    left = tk.Frame(
        root,
        bg="#243B55",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    left.place(x=20, y=90, width=300, height=500)

    tk.Label(
        left,
        text="OFFICE DETAILS",
        font=("Arial", 18, "bold"),
        bg="#243B55",
        fg="#00E5FF"
    ).pack(pady=15)

    details = [

        "🏢 MyBank Corporate Office",
        "",
        "📍 MG Road, Mumbai",
        "Maharashtra - 400001",
        "",
        "📞 +91 1800-202-9999",
        "",
        "📧 support@mybank.com",
        "",
        "🕒 Mon - Fri",
        "10 AM - 6 PM"

    ]

    for item in details:

        tk.Label(
            left,
            text=item,
            font=("Arial", 11),
            bg="#243B55",
            fg="white",
            justify="left"
        ).pack(anchor="w", padx=15, pady=2)

    # ======================================================
    # CENTER FRAME
    # ======================================================

    center = tk.Frame(
        root,
        bg="#F8FAFC",
        highlightbackground="#3B82F6",
        highlightthickness=2
    )

    center.place(x=350, y=90, width=320, height=500)

    tk.Label(
        center,
        text="DEPARTMENTS",
        font=("Arial", 18, "bold"),
        bg="#F8FAFC",
        fg="#1E293B"
    ).pack(pady=15)

    department_list = tk.Listbox(
        center,
        font=("Arial", 11),
        width=35,
        height=18,
        bg="#E2E8F0",
        fg="#0F172A",
        selectbackground="#00ADB5"
    )

    department_list.pack(pady=10)

    departments = [

        "🏦 Banking Operations",
        "💳 Credit Card Services",
        "💰 Loan Department",
        "🔐 Cyber Security",
        "🌐 Digital Banking",
        "📞 Customer Care",
        "📈 Investment Services",
        "🏧 ATM Monitoring"

    ]

    for item in departments:
        department_list.insert(tk.END, item)

    # ======================================================
    # RIGHT FRAME
    # ======================================================

    right = tk.Frame(
        root,
        bg="#1D3557",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    right.place(x=700, y=90, width=270, height=500)

    tk.Label(
        right,
        text="SERVICES",
        font=("Arial", 18, "bold"),
        bg="#1D3557",
        fg="#00FFAB"
    ).pack(pady=15)

    services = [

        "✔ Branch Monitoring",
        "✔ ATM Services",
        "✔ Fraud Protection",
        "✔ Customer Support",
        "✔ Loan Assistance",
        "✔ Secure Banking",
        "✔ Mobile Banking",
        "✔ Internet Banking"

    ]

    for item in services:

        tk.Label(
            right,
            text=item,
            font=("Arial", 11),
            bg="#1D3557",
            fg="white"
        ).pack(anchor="w", padx=15, pady=8)

    # ======================================================
    # FOOTER BUTTONS
    # ======================================================

    tk.Button(
        root,
        text="Contact",
        font=("Arial", 11, "bold"),
        bg="#3A86FF",
        fg="white",
        width=12,
        command=lambda: messagebox.showinfo(
            "Contact",
            "Connecting To Head Office..."
        )
    ).place(x=300, y=610)

    tk.Button(
        root,
        text="Email",
        font=("Arial", 11, "bold"),
        bg="#2A9D8F",
        fg="white",
        width=12
    ).place(x=470, y=610)

    tk.Button(
        root,
        text="Location",
        font=("Arial", 11, "bold"),
        bg="#8338EC",
        fg="white",
        width=12
    ).place(x=640, y=610)

    tk.Button(
        root,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="red",
        fg="white",
        width=12,
        command=root.destroy
    ).place(x=810, y=610)


#==============================================================================================================================

 # ======================================================
    # About MyBank
# ======================================================


def about_bank():

    root = tk.Toplevel()
    root.title("About MyBank")
    root.geometry("950x600")
    root.config(bg="#0B132B")

    # ======================================================
    # HEADER
    # ======================================================

    header = tk.Frame(root, bg="#1C2541", height=80)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏦 ABOUT MYBANK",
        font=("Arial", 26, "bold"),
        bg="#1C2541",
        fg="white"
    ).place(x=25, y=18)

    # ======================================================
    # LEFT FRAME
    # ======================================================

    left = tk.Frame(
        root,
        bg="#243B55",
        highlightbackground="#00E5FF",
        highlightthickness=2
    )

    left.place(x=20, y=100, width=280, height=430)

    tk.Label(
        left,
        text="BANK OVERVIEW",
        font=("Arial", 18, "bold"),
        bg="#243B55",
        fg="#00E5FF"
    ).pack(pady=15)

    overview = [

        "🏦 MyBank",
        "",
        "Established : 1998",
        "",
        "Head Office : Mumbai",
        "",
        "Branches : 500+",
        "",
        "ATM Centers : 1200+",
        "",
        "Customers : 10 Million+",
        "",
        "Trusted Banking Services",
        "Across India"

    ]

    for item in overview:

        tk.Label(
            left,
            text=item,
            font=("Arial", 11),
            bg="#243B55",
            fg="white",
            justify="left"
        ).pack(anchor="w", padx=15, pady=3)

    # ======================================================
    # CENTER FRAME
    # ======================================================

    center = tk.Frame(
        root,
        bg="#F8FAFC",
        highlightbackground="#3B82F6",
        highlightthickness=2
    )

    center.place(x=330, y=100, width=320, height=430)

    tk.Label(
        center,
        text="OUR SERVICES",
        font=("Arial", 18, "bold"),
        bg="#F8FAFC",
        fg="#1E293B"
    ).pack(pady=15)

    services = [

        "✔ Savings Account",
        "",
        "✔ Current Account",
        "",
        "✔ Home Loan",
        "",
        "✔ Car Loan",
        "",
        "✔ Mobile Banking",
        "",
        "✔ Internet Banking",
        "",
        "✔ Credit Card Services",
        "",
        "✔ ATM Services"

    ]

    for item in services:

        tk.Label(
            center,
            text=item,
            font=("Arial", 11),
            bg="#F8FAFC",
            fg="#0F172A"
        ).pack(anchor="w", padx=20, pady=2)

    # ======================================================
    # RIGHT FRAME
    # ======================================================

    right = tk.Frame(
        root,
        bg="#1D3557",
        highlightbackground="#00FFAB",
        highlightthickness=2
    )

    right.place(x=680, y=100, width=250, height=430)

    tk.Label(
        right,
        text="WHY CHOOSE US",
        font=("Arial", 18, "bold"),
        bg="#1D3557",
        fg="#00FFAB"
    ).pack(pady=15)

    reasons = [

        "✔ Secure Banking",
        "",
        "✔ Fast Transactions",
        "",
        "✔ 24×7 Customer Support",
        "",
        "✔ Trusted By Millions",
        "",
        "✔ Safe Online Banking",
        "",
        "✔ Easy Loan Approval",
        "",
        "✔ Smart Banking Features"

    ]

    for item in reasons:

        tk.Label(
            right,
            text=item,
            font=("Arial", 11),
            bg="#1D3557",
            fg="white"
        ).pack(anchor="w", padx=15, pady=2)

    # ======================================================
    # FOOTER
    # ======================================================

    footer = tk.Frame(root, bg="#1C2541", height=50)
    footer.pack(side="bottom", fill="x")

    tk.Label(
        footer,
        text="MyBank - Safe • Secure • Smart Banking",
        font=("Arial", 12, "bold"),
        bg="#1C2541",
        fg="white"
    ).pack(pady=12)

    

#===============================================================================================================================
    

                                                                                                                  # Main Page #

    
#==================================================================================================================================  
           

def fun():
    root =tk.Tk()
    root.geometry("1500x800")
    root.title("MyBank")
    var=IntVar()
    icon=tk.PhotoImage(file="image3.png")
    root.iconphoto(True,icon)
    img = PhotoImage(file="image13.png")
    root.img = img

    Label(root, image=img).place( x=0, y=0, relwidth=1, relheight=1  )

    
    def submit_form():

          messagebox.showinfo("from ","Form Submitted Successfully")
    def open_file():
                 file = filedialog.askopenfilename()
                 print("selected file :",file)

#======================================================================================
    menu = Menu(root)
    root.config(menu=menu,bg="skyblue")

# DashBoard Menu
    dashboard_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Dashboard", menu=dashboard_menu)

    dashboard_menu.add_command( label="Open Dashboard", command=Dashboard)
# Account Menu
    Account_menu = Menu(menu)
    menu.add_cascade(label="Account",menu=Account_menu)
    Account_menu.add_command(label="Create Account",command=create_account_window)
    Account_menu.add_command(label="View Account",command=view_account_window)
    Account_menu.add_command(label="Update Account",command= update_account_window)
    Account_menu.add_command(label="Delete Account",command=delete_account_window)
    Account_menu.add_separator()
    Account_menu.add_command(label="Mini Statement",command= mini_statement_window)
    Account_menu.add_command(label="Transaction History",command=transaction_history_window)
    Account_menu.add_command(label="Balance Enquiry",command=balance_enquiry_window)

#Transfer Menu
    transfer = Menu(menu)                    
    menu.add_cascade(label="Transfer",menu=transfer)
    transfer.add_command(label="Fund Transfer",command=fund_transfer_window)
    transfer.add_command(label="Bank Transfer",command=bank_transfer_window)
    transfer.add_command(label="UPI Transfer",command=upi_transfer_window)
    transfer.add_command(label="Mobile Transfer",command=mobile_transfer_window)
    transfer.add_command(label="NEFT Transfer",command=neft_transfer_window)
    transfer.add_command(label="RTGS Transfer",command= rtgs_transfer_window)
    transfer.add_command(label="IMPS Transfer",command=imps_transfer_window)
    transfer.add_separator()
    transfer.add_command(label="Transaction History",command= transaction_history_window)
    
    
#Loan Menu
    loan = Menu(menu,tearoff=0)
    menu.add_cascade(label="Loan",menu=loan)
    loan.add_command(label="Home Loan ",command=show_home_loan)
    loan.add_command(label="Car Loan ",command=show_car_loan)
    loan.add_command(label="Personal Loan",command=show_personal_loan)
  
    
#Service Menu
    services = Menu(menu)
    menu.add_cascade(label="Services",menu=services)
    services.add_command(label="ATM Services",command=atm_services_window)
    services.add_command(label="Cheque Book Request",command=cheque_book_request_window)
    services.add_command(label="Passbook Update",command=passbook_update_window)
    services.add_command(label="Credit Card Services",command= credit_card_services_window)
    services.add_command(label="Debit Card Services",command=debit_card_services_window)
    services.add_command(label="Net Banking",command=net_banking_window)
    services.add_command(label="Mobile Banking",command= mobile_banking_window)
    services.add_separator()
    services.add_command(label="Change Password",command= change_password_window)
    services.add_command(label="Reset PIN",command=reset_pin_window) 
    

#Contact Menu
    contact = Menu(menu)
    menu.add_cascade(label="Contact Us",menu=contact)
    contact.add_command(label="Customer Care",command=customer_care_window)
    contact.add_command(label="Email Support",command=email_support_window)
    contact.add_command(label="Branch Locator",command=branch_locator)
    contact.add_command(label="Head Office",command= head_office_window)
    contact.add_separator()
    contact.add_command(label="About Bank",command=about_bank)

#Eixt Button
    menu.add_command( label="Exit", command=root.destroy)

#=====================================================================================
 # ==========================================================
    # TOP HEADER
    # ==========================================================

    top_header = Frame( root, bg="#061A40", height=220 )

    top_header.pack(fill=X)

    # ==========================================================
    # LEFT TEXT SECTION
    # ==========================================================

    text_frame = Frame( top_header, bg="#061A40")

    text_frame.place(x=40, y=30)
    J = PhotoImage(file=r"image9.png")
    
    Label(text_frame, image=J,width=400, height=190,bg="#061A40").pack(side=RIGHT,padx=40)
    
    R = PhotoImage(file=r"image3.png")
    Label(text_frame,image=R,width=500,height=200,bg="#061A40").pack(side=RIGHT,padx=30)
    

    Label(  text_frame, text="🏦 Welcome To MyBank", bg="#061A40", fg="white", font=("Arial", 32, "bold") ).pack(anchor="w")

    Label(text_frame,text="Experience Simple, Secure & Smart Banking",bg="#061A40",fg="#dcdde1",font=("Arial", 16) ).pack(anchor="w", pady=8)

    Label( text_frame, text="We are here to help you achieve your dreams.", bg="#061A40", fg="#dcdde1", font=("Arial", 13)).pack(anchor="w")

    Button( text_frame, text="Learn More", bg="#f39c12", fg="white", font=("Arial", 12, "bold"), bd=0, padx=20, pady=8).pack(anchor="w", pady=20)

    # ==========================================================
    # SIDE PANEL
    # ==========================================================

    side_frame = Frame( root, bg="white", bd=3, relief=RIDGE)

    side_frame.place(  x=20,  y=260,  width=250,  height=450)

    Label(  side_frame,  text="📌 Online Banking",  bg="#061A40",  fg="white",  font=("Arial", 18, "bold")).pack(fill=X)

    options = [
        "✔ View Accounts",
        "✔ Fund Transfer",
        "✔ Pay Bills",
        "✔ Transaction History",
        "✔ Customer Support",
        "✔ Mobile Banking",
        "✔ Net Banking"
    ]

    for item in options:

        Label( side_frame, text=item, bg="white", fg="black", font=("Arial", 12), anchor="w", padx=15).pack(fill=X, pady=10)

    # ==========================================================
    # MAIN DASHBOARD
    # ==========================================================

    main_frame = Frame( root, bg="#ecf0f1", bd=3, relief=RIDGE)

    main_frame.place(  x=300,  y=260,  width=1160,  height=450 )

    # ==========================================================
    # DASHBOARD TITLE
    # ==========================================================

    Label(main_frame,text="🏦 MYBANK DIGITAL DASHBOARD",bg="#061539",fg="white",font=("Arial", 20, "bold"),pady=10).pack(fill=X)

    # ==========================================================
    # CARDS SECTION
    # ==========================================================

    cards_frame = Frame( main_frame, bg="#ecf0f1")

    cards_frame.pack(pady=15)

    # CARD FUNCTION

    def create_card(parent, bg, title, value1, value2):

        card = Frame(parent, bg=bg, width=220, height=110, bd=3, relief=RIDGE )

        card.pack(side=LEFT, padx=12)
        card.pack_propagate(False)

        Label(card,text=title,font=("Arial", 14, "bold"),bg=bg,fg="white").pack(pady=8)

        Label(  card,  text=value1,  font=("Arial", 16, "bold"),  bg=bg,  fg="white").pack()

        Label(  card,  text=value2,  font=("Arial", 10),  bg=bg,  fg="white").pack(pady=5)
    # CARDS

    create_card( cards_frame,   "#1faa00",  "💰 Total Balance",  "₹ 2,45,000",  "Available Balance" )

    create_card(  cards_frame, "#f39c12", "💳 Card Services",  "Debit / Credit",   "ATM Services"  )

    create_card( cards_frame, "#8e44ad", "📈 Investments", "FD / Mutual Fund", "Gold Investment")

    create_card(  cards_frame,  "#00a8ff",  "👤 Welcome",  "Prachi",  "Premium Customer")

    # ==========================================================
    # LOWER SECTION
    # ==========================================================

    lower_frame = Frame(  main_frame,  bg="#ecf0f1")

    lower_frame.pack(pady=10)

    # ==========================================================
    # QUICK SERVICES
    # ==========================================================

    quick_frame = Frame(  lower_frame,  bg="white",width=500, height=220, bd=3, relief=RIDGE )

    quick_frame.grid(row=0, column=0, padx=15)
    quick_frame.pack_propagate(False)

    Label(quick_frame,text="⚡ Quick Banking Services",bg="white",font=("Arial", 17, "bold") ).pack(pady=15)

    button_frame = Frame( quick_frame, bg="white" )

    button_frame.pack()

    buttons = [ ("Fund Transfer", "#1faa00"), ("Mini Statement", "#e67e22"),("Mobile Banking", "#00a8ff"), ("Net Banking", "#8e44ad")]

    row = 0
    col = 0

    for text, color in buttons:

        Button( button_frame, text=text, bg=color, fg="white", font=("Arial", 11, "bold"), width=16, height=2, bd=0).grid(row=row, column=col, padx=10, pady=10)

        col += 1

        if col > 1:
            col = 0
            row += 1

    # ==========================================================
    # TRANSACTIONS
    # ==========================================================

    transaction_frame = Frame(  lower_frame, bg="white", width=500, height=220, bd=3, relief=RIDGE )

    transaction_frame.grid(row=0, column=1, padx=15)
    transaction_frame.pack_propagate(False)

    Label( transaction_frame, text="📋 Recent Transactions", bg="white", font=("Arial", 17, "bold")).pack(pady=15)

    transactions = [  ("✔ Electricity Bill Paid", "₹2,500"),  ("✔ ATM Withdrawal", "₹10,000"),  ("✔ Salary Credited", "₹45,000"),  ("✔ UPI Transfer", "₹1,200"),
                      ("✔ Online Shopping", "₹3,450")  ]

    for t, amt in transactions:

        row = Frame(  transaction_frame,   bg="white"   )

        row.pack(fill=X, padx=15, pady=4)

        Label( row, text=t, bg="white", font=("Arial", 10)).pack(side=LEFT)
        Label(   row,   text=amt,   bg="white",   font=("Arial", 10, "bold")  ).pack(side=RIGHT)

    # ==========================================================
    # IMPORTANT NOTICE
    # ==========================================================

    notice = Frame( root, bg="#d4efdf", bd=3, relief=RIDGE)

    notice.place(  x=20,  y=730,  width=1440,  height=50)

    Label(notice, text="⚠ Never share your OTP, PIN or Password with anyone. Your security is our priority.", bg="#d4efdf", fg="darkgreen",
               font=("Arial", 12, "bold")).pack(pady=10)

    # ==========================================================
    # FOOTER
    # ==========================================================

    footer = Frame( root, bg="#061539",  height=35 )

    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="🔒 Secure Banking  |  ☎ 24x7 Customer Support  |  🌍 Branch Locator Available", bg="#061539", fg="white", font=("Arial", 10, "bold") ).pack(pady=7)

    # ==========================================================
    # WELCOME MESSAGE
    # ==========================================================

    messagebox.showinfo( "Welcome To MyBank", "Welcome To MyBank Website")

    root.mainloop()

# ==========================================================
# CALL FUNCTION
# ==========================================================

First_page()
















