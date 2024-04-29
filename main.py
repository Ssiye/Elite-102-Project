import tkinter as tk
window = tk.Tk()


#account name reterval
label = tk.Label(text="Account Name")
entry = tk.Entry()

label.pack()
entry.pack()

accountname = entry.get()
accountname
#account number id retrval
label = tk.Label(text="Account ID")
entry = tk.Entry()

label.pack()
entry.pack()

accountid = entry.get()
accountid
#account password retrival
label = tk.Label(text="Account Username")
entry = tk.Entry()

label.pack()
entry.pack()

accountuser= entry.get()
accountuser
#entry box for account password
label = tk.Label(text="Account Password")
entry = tk.Entry()

label.pack()
entry.pack()

accountpw = entry.get()
accountpw
#entry box for user email
label = tk.Label(text="Account Email")
entry = tk.Entry()

label.pack()
entry.pack()

accountemail = entry.get()
accountemail
#creates account balance display
label = tk.Label(
    text="Account Balance",
    fg="white",
    bg="black",
    width=10,
    height=10
)

#main code
#welcome statements
Welcome = input("Hello Welcome to the blue berry bank.")

input(" Would you like to \n 1. create an account \n 2. login to an existing account(answer in number form)")

if input = "1":
  account_name = input("Could you please tell me the last name that the account is under:")
  account_id = input("Please enter account ID.")
  account_email = input("Please enter account email .")
  account_user = input ("Could you please ether your account user name")
  

class Bank:
  def init (self):
    self.accounts = {}

  input(" Would you like to \n 1. create an account \n 2. login to an existing account(answer in number form)")

  if input = "1":
    account_name = input("Could you please tell me the last name that the account is under:")
    account_id = input("Please enter account ID.")
    account_email = input("Please enter account email .")
    account_user = input ("Could you please ether your account user name")

  if input = "2" :
  def create_new_account(self, account_name, account_id, account_user, account_pw, account_ email)
  self
  





import sqlite3
conn = sqlite3.connect('bank.db')  # This creates or opens the file 'bank.db' as a database
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE  accounts
            (id integer primary key, accountname text, accountid integer, accountpin integer, accountbalance integer, accountinfoandemail text, accountnumber integer)''')
conn.commit()
conn.close()

nb