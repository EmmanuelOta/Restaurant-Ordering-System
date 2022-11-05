import re
import json


class MainApp():
    def __init__(self):
        print("Please Enter 1 for Sign Up")
        print("Please Enter 2 for Sign In")
        print("Please enter 3 for Quit")
        self.input = input(":") 


class SignUP():
    def __init__(self):
        self.user_data = {}
        self.name = input("Please enter your full name:")
        self.user_data["name"] = self.name
        self.number = input("Please enter your contact number:")
        self.user_data["number"] = self.number
        while True:
            if len(self.number) == 10 and self.number.startswith("0"):
                break
            else:
                print("You have entered an incorrect number!!\n")
                self.number = input("Please enter your contact number:")
                self.user_data["number"] = self.number

        self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
        self.confirm_pass = input("Password confirmation:")
        self.patterns = "[A-Z][a-z][a-z][@|&][0-9]*$"
        while True:
            if  self.password == self.confirm_pass and re.match(self.patterns, self.password):
                self.user_data["password"] = self.confirm_pass
                break
            else:
                print("Your password doesn't follow the required pattern please enter a valid password!!")
                self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                self.confirm_pass = input("Password confirmation:")
                self.user_data["password"] = self.password    


        self.date_of_birth = input("Please enter your date of birth in the format DD/MM/YYYY (NO SPACE):")
        match = "(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/]\d{4}"
        while True:
            if re.match(match, self.date_of_birth):
                self.split_D0B = self.date_of_birth.split("/")
                self.birth_year = self.split_D0B[2]
                age = 2021 - int(self.birth_year)
                if age >= 21:
                    print("You have successfully Signed up!!")
                    break
                else:
                    print("You are too young to Sign up!")
                    break

            else:
                print("You have the entered the Date of Birth in invalid format.\nPlease start again\n:")
                self.date_of_birth = input("Please enter your date of birth in the format DD/MM/YYYY (No Space):")

        with open(f"{self.number}.json", "w") as file:
                    json.dump(self.user_data, file)

class SignIn():
    def __init__(self):
        self.username = input("Please enter your username (Mobile Number):")
        try:
            with open(f"{self.username}.json", "r") as file:
                self.loaded_data = json.load(file)
                self.password = input("Please enter your password:")
                self.count = 0
                while self.count < 3:
                    if self.loaded_data["password"] != self.password:
                        print(f"You have entered the wrong Password\nPlease try again!")
                        self.password = input("Please enter your password:")
                        self.count += 1
                        if self.count == 3:
                            print("You have used the maximum attempts of login:")
                            print("Please reset the password by entering the below details:")
                            try:
                                self.username_confirmation = input("Please enter your Username (Mobile Number) to confirm:")
                                with open(f"{self.username_confirmation}.json", "r") as file:
                                    self.userConfirmData = json.load(file)
                            except:
                                print("You have not signed in with this username!!\n")
                                app = MainApp()
                            self.dob_confirmation = input("Please enter your Date of Birth in DD/MM/YYYY format, to confirm:")
                            self.match = "[A-Z][a-z][a-z][@|&][0-9]*$"
                            self.new_password = input("Please enter your new password in format Sam@20 or Sam&20:")
                            self.new_password_confirm = input("Please re-enter your new password:")
                            while True:
                                if re.match(self.match, self.password) and self.password == self.new_password_confirm:
                                    self.userConfirmData["password"] = self.new_password_confirm
                                    with open(f"{self.username_confirmation}.json", "w") as file:
                                        json.dump(self.userConfirmData, file)
                                    print("Your password has been reset successfully!!")
                                    break

                                if self.userConfirmData["password"] == self.new_password_confirm:
                                    print("You cannot use the password used earlier.")
                                    self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                                    self.new_password_confirm = input("Please re-enter your new password:")

                                else:
                                    print("Your password doesn't follow the required pattern or they don't match, Please enter a valid password!!")
                                    self.password = input("Please enter your password (Password must be of format Sam@20 or Sam&20):")
                                    self.new_password_confirm = input("Please re-enter your new password:")

                    else:
                        print("You have successfully signed in.")
                        break
                
                print(f"Welcome {self.loaded_data['name']}")
            print("Please enter 1 for Resetting the Password")
            print("Please enter 2 for Signout")
            self.input = input(":")
            if self.input == "1":
                self.username = input("Please enter your username (Mobile Number):")
                self.Oldpassword = input("Please enter your old password:")
                self.Newpassword = input("Please enter your new password:")
                self.loaded_data["password"] = self.Newpassword
                print("Your password has been reset successfully!!")
                with open(f"{self.username}.json", "w") as file:
                    json.dump(self.loaded_data, file)
            elif self.input == "2":
                pass
        except:
            print("You have not Signed up with this Contact Number, Please Sign up first.")        


while True:
    app = MainApp()
    if app.input == "3":
        print("Thank You for using the application.")
        break
    if app.input == "1":
        sign_up = SignUP()
    if app.input == "2":
        login = SignIn()
    