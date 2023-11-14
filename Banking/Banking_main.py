'''I just wanted to learn python Oop's, I only saw videos on youtube and understood the concept, 
 Now iam trying to make a banking application using the oops concept
Here in this appliaction we are trying to give some banking features like creating an account(database can be mysql and a csv file)
and user can register and if done he can login and He can do Diposite, Withdrawl, MoneyTransfer, check balance when ever he wants'''

'''Iam writing this code by taking referance of the youtube video : https://www.youtube.com/watch?v=gQlbH3qr1l4&t=1s&ab_channel=IshaanSharma'''

''' Workflow '''
import csv
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from bank_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget

class Bank(QMainWindow,Ui_MainWindow):
    acc_num = 63010
    no_of_acc = 0
    def blur_effect(self,thewidget,strength):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(strength)  
        thewidget.setGraphicsEffect(blur_effect)
    def __init__(self): #Name, MobileNUmber, initial_dipo, pin
        super(Bank,self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.Login_widget.setVisible(True)
        self.Create_account_widget.setVisible(False)
        self.Banking.setVisible(False)
        self.deposit_widget.setVisible(False)
        self.withdrawl_widget.setVisible(False)
        self.transfer_widget.setVisible(False)
        self.check_balance_widget.setVisible(False)
        self.transaction_completed_widget.setVisible(False)
        self.transaction_aborted_widget.setVisible(False)
        self.authentication_failed_widget.setVisible(False)
        self.account_details_widget.setVisible(False)
        
        ####Buttons.clicked.connect()####
        self.Login.clicked.connect(self.verify_user_cridentials)
        self.authentication_failed_ok.clicked.connect(self.authentication_failed_close)
        self.Create_account.clicked.connect(self.create_account1)
        self.Create_account_button.clicked.connect(self.create_account)
        self.create_acc_x_button.clicked.connect(self.close_create_acc)
        self.account_details_thanks_ok.clicked.connect(self.close_acc_details)
        self.log_out_button.clicked.connect(self.log_out)
        self.bank_deposit_button.clicked.connect(self.deposite_view)
        self.deposit_ok.clicked.connect(self.deposite)
        self.transaction_completed_ok.clicked.connect(self.close_transaction_completed_widget)
        self.bank_withdrawl_button.clicked.connect(self.withdrawl_view)
        self.withdrawl_ok.clicked.connect(self.withdrawl)
        self.bank_transfer_button.clicked.connect(self.transfer_view)
        self.transfer_ok.clicked.connect(self.transfer)
        self.bank_check_balance.clicked.connect(self.check_balance_view)
        self.balance_ok.clicked.connect(self.check_balance)
        self.deposite_x_button.clicked.connect(self.close_deposite)
        self.withdrawl_x_button.clicked.connect(self.close_withdrawl)
        self.transfer_x_button.clicked.connect(self.close_transfer)
        self.transaction_aborted_ok.clicked.connect(self.transaction_aborted_close)
        
        self.database = "database.csv"
        try:
            with open(self.database,"r") as file:
                    database_dict = csv.DictReader(file)
        except: 
            header = ["Name", "Mobile_number", "Account_number", "Password", "Balance"]
            with open(self.database,"w")as file:
                self.writer =csv.writer(file)
                self.writer.writerow(header)
            
        # Bank.acc_num = Bank.acc_num+1
        # Bank.no_of_acc = Bank.no_of_acc+1
  
    def read_database(self):
        self.database_file = pd.read_csv(self.database)
        database_dict = self.database_file.to_dict(orient='records') ##orient='records' will makes each row a distonary, so that we can get data by specifying the column name of a specific row
        return database_dict
    
    def append_to_database(self,details):
        with open(self.database,"a")as file:
            self.writer = csv.writer(file)
            self.writer.writerow(details)
    
    def update_balance(self,index,column_name,data):
        self.database_file = pd.read_csv(self.database)
        self.database_file.at[index,column_name] = data
        self.database_file.to_csv(self.database,index=False)
    
    def create_account1(self):
        self.Login_widget.setVisible(False)
        self.Create_account_widget.setVisible(True)
        
    def create_account(self):
        self.name = self.create_name_line.text()##
        self.mobile = self.create_phone_line1.text()
        self.password = self.create_pswd_line1.text()
        self.balance = self.create_deposite_amount1.text()
        # print("Details : ",self.name,self.mobile,self.password,self.balance)
        # # self.name ="Eswar"
        # # self.mobile ="6301189779"
        # # self.password ="1234"
        # # self.balance = 1000
        database_dict = self.read_database()
        for row in database_dict:
            self.acc_num= row["Account_number"]
        self.acc_num=int(self.acc_num)+1
        account_details = [self.name, self.mobile, self.acc_num, self.password, self.balance]
        # with open(self.database,"a")as file:
        #     self.writer = csv.writer(file)
        #     self.writer.writerow(account_details)
        self.append_to_database(account_details)
        # print(f"Your account number is : {self.acc_num}")
        self.Login_widget.setVisible(False)
        self.Create_account_widget.setVisible(True)
        self.account_user_name_lable.setText(str(self.name))
        self.account_number_lable.setText(str(self.acc_num))
        self.blur_effect(self.Create_account_widget,5)
        self.account_details_widget.setVisible(True)
    
    def close_acc_details(self):
        self.login_acc_line.clear()
        self.login_pswd_line.clear()
        self.create_name_line.clear()
        self.create_phone_line1.clear()
        self.create_pswd_line1.clear()
        self.create_deposite_amount1.clear()
        self.blur_effect(self.Create_account_widget,0)
        self.Create_account_widget.setVisible(False)
        self.account_details_widget.setVisible(False)
        self.Login_widget.setVisible(True)
        
    def close_create_acc(self):
        self.login_acc_line.clear()
        self.login_pswd_line.clear()
        self.create_name_line.clear()
        self.create_phone_line1.clear()
        self.create_pswd_line1.clear()
        self.create_deposite_amount1.clear()
        self.Login_widget.setVisible(True)
        self.Create_account_widget.setVisible(False)
        
    def login(self):
        self.verify_acc = input("Account number: ")
        self.verify_pass= input("Password: ")
             
    def verify_user_cridentials(self):
            # with open(self.database,"r") as file:
            #     database_dict1 = csv.DictReader(file)
            #     print(database_dict1) 
                self.verify_acc = str(self.login_acc_line.text())
                self.verify_pass= str(self.login_pswd_line.text())
                database_dict = self.read_database()
                self.index_count = 0
                for row in database_dict:
                    # print(row)
                    # print(str(row["Account_number"]),self.verify_acc)
                    # try:

                        if str(row["Account_number"]) == self.verify_acc and str(row["Password"]) == self.verify_pass:
                            # if str(row["Password"]) == self.verify_pass:
                                print(f"Hello, {row['Name']}")
                                self.current_user_name = row['Name']
                                self.current_account_num = row['Account_number']
                                self.current_account_balance = row['Balance']
                                self.current_index = self.index_count
                                self.Login_widget.setVisible(False)
                                self.Banking.setVisible(True)
                                self.user_name.setText(str(self.current_user_name))
                                self.display_acc_number.setText(str(self.current_account_num))
                                # print("Index:",self.index_count)
                                break
                        else:
                            print("wrong first else",row["Account_number"],self.verify_acc,row["Password"],self.verify_pass)
                            self.blur_effect(self.Login_widget,5)
                            self.Login_widget.setEnabled(False)
                            self.authentication_failed_widget.setVisible(True)
                            break
                            
                        # elif str(row["Account_number"]) != self.verify_acc:
                        #     print("Elif")
                        #     self.blur_effect(self.Login_widget,5)
                        #     self.Login_widget.setEnabled(False)
                        #     self.authentication_failed_widget.setVisible(True)
                                       
                    # except:
                    #     print("wrong second except")
                    #     self.blur_effect(self.Login_widget,5)
                    #     self.Login_widget.setEnabled(False)
                    #     self.authentication_failed_widget.setVisible(True)
                        
                self.index_count+=1
                    
    def authentication_failed_close(self):
        self.blur_effect(self.Login_widget,0)
        self.login_acc_line.clear()
        self.login_pswd_line.clear()
        self.Login_widget.setEnabled(True)
        self.authentication_failed_widget.setVisible(False)
        
    def account_details(self):
        print(f"Account holder name :{self.current_user_name}\t Account Number: {self.current_account_num}")
    
    def deposite_view(self):
        self.blur_effect(self.Banking,5)
        self.deposit_amount.clear()
        self.Banking.setEnabled(False)
        self.deposit_widget.setVisible(True)
    
    def deposite(self):
        try:
            amount = int(self.deposit_amount.text())
            if amount>0:
                self.current_account_balance = self.current_account_balance+amount
                self.update_balance(self.current_index,"Balance",self.current_account_balance)
                # print(f"Transaction Completed!\nAvailable Balance:{self.current_account_balance}")
                 ##After deposit ok
                self.blur_effect(self.Banking,0)
                self.Banking.setEnabled(True)
                self.deposit_widget.setVisible(False)
                self.transaction_completed_widget.setVisible(True)
                self.blur_effect(self.Banking,5)
            else:
                # print("Invalid amount, Transaction aborted..!")
                self.transaction_aborted_widget.setVisible(True)
                self.deposit_widget.setVisible(False)
                self.blur_effect(self.Banking,3)
        except:
            self.transaction_aborted_widget.setVisible(True)
            self.deposit_widget.setVisible(False)
            self.blur_effect(self.Banking,3)
            
       
        
    def transaction_aborted_close(self):
        self.transaction_aborted_widget.setVisible(False)
        self.blur_effect(self.Banking,0)
        self.Banking.setEnabled(True)
        self.deposit_widget.setVisible(False)
           
    def close_deposite(self):
        self.blur_effect(self.Banking,0)
        self.deposit_amount.clear()
        self.Banking.setEnabled(True)
        self.deposit_widget.setVisible(False)
        
    def withdrawl_view(self):
        self.blur_effect(self.Banking,5)
        self.withdrawl_amount.clear()
        self.Banking.setEnabled(False)
        self.withdrawl_widget.setVisible(True)
    
    def withdrawl(self):
        try:
            amount = int(self.withdrawl_amount.text())
            if amount <= self.current_account_balance:
                self.current_account_balance = self.current_account_balance-amount
                self.update_balance(self.current_index,"Balance",self.current_account_balance)
                # print(f"Transaction Completed!\nAvailable Balance:{self.current_account_balance}")
                ##After withdrawl ok
                self.blur_effect(self.Banking,0)
                self.Banking.setEnabled(True)
                self.withdrawl_widget.setVisible(False)
                self.transaction_completed_widget.setVisible(True)
                self.blur_effect(self.Banking,5)
            else:
                # print("Invalid amount, Transaction aborted..!")
                self.transaction_aborted_widget.setVisible(True)
                self.withdrawl_widget.setVisible(False)
                self.blur_effect(self.Banking,3)
        except:
            self.transaction_aborted_widget.setVisible(True)
            self.withdrawl_widget.setVisible(False)
            self.blur_effect(self.Banking,3)
        
        
    def close_withdrawl(self):
        self.blur_effect(self.Banking,0)
        self.withdrawl_amount.clear()
        self.Banking.setEnabled(True)
        self.withdrawl_widget.setVisible(False)
    
    def transfer_view(self):
        self.blur_effect(self.Banking,5)
        self.transfer_amount.clear()
        self.transfer_account.clear()
        self.Banking.setEnabled(False)
        self.transfer_widget.setVisible(True)
        
    def transfer(self):
        receiver = self.transfer_account.text()
        database_dict = self.read_database()
        receiver_index = 0
        for row in database_dict:
            try:
                if str(row["Account_number"])==str(receiver):
                    self.receiver_name = row['Name']
                    self.receiver_balance = row['Balance']
                    amount = int(self.transfer_amount.text())  
                    if amount <= self.current_account_balance and amount>0:
                        self.receiver_balance = self.receiver_balance+amount
                        self.current_account_balance = self.current_account_balance-amount
                        self.update_balance(receiver_index,"Balance",self.receiver_balance)
                        self.update_balance(self.current_index,"Balance",self.current_account_balance)
                        # print("Transaction Completed!",self.current_account_balance)
                        
                        ##After transfer ok
                        self.blur_effect(self.Banking,0)
                        self.Banking.setEnabled(True)
                        self.transfer_widget.setVisible(False)
                        self.transaction_completed_widget.setVisible(True)
                        self.blur_effect(self.Banking,5)
                        break
                    else:
                        print("aborted else1")
                        self.transfer_widget.setVisible(False)
                        self.transaction_aborted_widget.setVisible(True)
                        self.blur_effect(self.Banking,3)
                        break
                else:
                    print("aborted else2")
                    self.transfer_widget.setVisible(False)
                    self.transaction_aborted_widget.setVisible(True)
                    self.blur_effect(self.Banking,3)
                    break
            except:
                print("aborted except")
                self.transfer_widget.setVisible(False)
                self.transaction_aborted_widget.setVisible(True)
                self.blur_effect(self.Banking,3)
            receiver_index+=1
        
    def close_transfer(self):
        self.blur_effect(self.Banking,0)
        self.transfer_amount.clear()
        self.Banking.setEnabled(True)
        self.transfer_widget.setVisible(False)
     
    def close_transaction_completed_widget(self):
        self.transaction_completed_widget.setVisible(False)
        self.Banking.setEnabled(True)
        self.blur_effect(self.Banking,0)
    
    def check_balance_view(self):
        self.blur_effect(self.Banking,5)
        self.Banking.setEnabled(False)
        self.check_balance_widget.setVisible(True)
        self.balance_amount.setText(str(self.current_account_balance))
        
    def check_balance(self):
        # print(f"Account Balance : {self.current_account_balance}")
        #After check balance OK
        self.blur_effect(self.Banking,0)
        self.Banking.setEnabled(True)
        self.check_balance_widget.setVisible(False)
        self.transaction_completed_widget.setVisible(False)
        self.blur_effect(self.Banking,0)
        
    def log_out(self):
        self.Login_widget.setVisible(True)
        self.login_acc_line.clear()
        self.login_pswd_line.clear()
        self.Banking.setVisible(False)
        
if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Bank_window = Bank()
    Bank_window.show()
    sys.exit(app.exec_())
    