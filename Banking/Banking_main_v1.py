'''I just wanted to learn python Oop's, I only saw videos on youtube and understood the concept, 
 Now iam trying to make a banking application using the oops concept
Here in this appliaction we are trying to give some banking features like creating an account(database can be mysql and a csv file)
and user can register and if done he can login and He can do Diposite, Withdrawl, MoneyTransfer, check balance when ever he wants'''

'''Iam writing this code by taking referance of the youtube video : https://www.youtube.com/watch?v=gQlbH3qr1l4&t=1s&ab_channel=IshaanSharma'''

''' Workflow '''
import csv
import pandas as pd

class Bank():
    acc_num = 63010
    no_of_acc = 0
    def __init__(self): #Name, MobileNUmber, initial_dipo, pin
        # self.name = Name
        # self.mobile = MobileNUmber
        # self.balance = initial_dipo
        # self.password = pin
        # self.acc_num = Bank.acc_num
        
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
        
    def create_account(self):
        self.name = input("Enter the user name :")
        self.mobile = int(input("Enter the mobile number :"))
        self.password = input("Create a password:")
        self.balance = int(input("Enter the initial deposite amount:"))
        # self.name ="Eswar"
        # self.mobile ="6301189779"
        # self.password ="1234"
        # self.balance = 1000
        database_dict = self.read_database()
        for row in database_dict:
            self.acc_num= row["Account_number"]
        self.acc_num=int(self.acc_num)+1
        account_details = [self.name, self.mobile, self.acc_num, self.password, self.balance]
        # with open(self.database,"a")as file:
        #     self.writer = csv.writer(file)
        #     self.writer.writerow(account_details)
        self.append_to_database(account_details)
        print(f"Your account number is : {self.acc_num}")
    
    def login(self):
        self.verify_acc = input("Account number: ")
        self.verify_pass= input("Password: ")
             
    def verify_user_cridentials(self):
            # with open(self.database,"r") as file:
            #     database_dict1 = csv.DictReader(file)
            #     print(database_dict1) 
                self.verify_acc = input("Account number: ")
                self.verify_pass= input("Password: ")
                database_dict = self.read_database()
                self.index_count = 0
                for row in database_dict:
                    # print(row)
                    # print(str(row["Account_number"]),self.verify_acc)
                    if str(row["Account_number"]) == self.verify_acc:
                        if str(row["Password"]) == self.verify_pass:
                            print(f"Hello, {row['Name']}")
                            self.current_user_name = row['Name']
                            self.current_account_num = row['Account_number']
                            self.current_account_balance = row['Balance']
                            self.current_index = self.index_count
                            break
                        else:
                            print("Invalid Credentials! Please try again..")
                        self.index_count+=1
        
    def account_details(self):
        print(f"Account holder name :{self.current_user_name}\t Account Number: {self.current_account_num}")
    
    def diposite(self):
        amount = int(input("Enter the amount: "))
        if amount>0:
            self.current_account_balance = self.current_account_balance+amount
            self.update_balance(self.current_index,"Balance",self.current_account_balance)
            print(f"Transaction Completed!\nAvailable Balance:{self.current_account_balance}")
        else:
            print("Invalid amount, Transaction aborted..!")
            
    def withdrawl(self):
        amount = int(input("Enter the amount: "))
        if amount <= self.current_account_balance:
            self.current_account_balance = self.current_account_balance-amount
            self.update_balance(self.current_index,"Balance",self.current_account_balance)
            print(f"Transaction Completed!\nAvailable Balance:{self.current_account_balance}")
        else:
            print("Invalid amount, Transaction aborted..!")
            
    def transfer(self):
        receiver = input("Enter Receiver's Account Number: ")
        database_dict = self.read_database()
        receiver_index = 0
        for row in database_dict:
            if str(row["Account_number"])==str(receiver):
                self.receiver_name = row['Name']
                self.receiver_balance = row['Balance']
                amount = int(input("Enter the amount : "))     
                if amount <= self.current_account_balance and amount>0:
                    receiver_balance = self.receiver_balance+amount
                    self.current_account_balance = self.current_account_balance-amount
                    self.update_balance(self.current_index,"Balance",self.current_account_balance)
                    self.update_balance(receiver_index,"Balance",receiver_balance)
                    print("Transaction Completed!")
                else:
                    print(f"Invalid amount transaction aborted..!, Current Balance : {self.current_account_balance}")
            receiver_index+=1
            
    def check_balance(self):
        print(f"Account Balance : {self.current_account_balance}")
        return self.current_account_balance
    
if __name__ == "__main__":
    test = Bank()
    test.create_account()
    test.login()
    test.verify_user_cridentials()
    test.account_details()
    test.diposite()
    test.withdrawl()
    test.transfer()
    test.check_balance()