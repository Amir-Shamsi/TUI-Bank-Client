import requests
from subprocess import call
from sys import platform
import json
import turtle
from pip._vendor.colorama import Fore

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Variables:
username, password = "", ""
notFound = {'detail': 'Authentication credentials were not provided.'}


# ----------------------------------------------------------------------------------------------------------------------
# Clear the Shell of Console after the actions done!

def shell_clear():
    print("\n" * 100)


# ----------------------------------------------------------------------------------------------------------------------
# Definitions Done:
def sign_up():
    nw_username = input(Fore.WHITE + "Enter Your UserName:")
    nw_password = input("Enter Your Password:")

    while "" in (nw_username, nw_password):
        print(Fore.RED + "*DON\'T PUT ANY FIELD BLANK!")
        nw_username = input(Fore.WHITE + "Enter Your UserName:")
        nw_password = input("Enter Your Password:")
    token = open("tokan.text").read()
    nw_response = requests.post("http://176.9.164.222:2211/api/accounts/User/SignUp",
                                headers={'Authorization': 'JWT ' + token},
                                data={"username": nw_username, "password": nw_password}).json()

    if nw_username == nw_response['username']:
        shell_clear()
        print(Fore.GREEN + "Congratulation You Signed Up Successfully")
        print(Fore.BLUE + "Username:", nw_username)
        print(Fore.BLUE + "Password:", nw_password)
    elif 'A user with that username already exists.' in nw_response["username"]:
        print(Fore.RED + "A User With That Username Already Exists!")
    else:
        print(Fore.RED + "ERROR! The User Didn't Create!")


def menu_start():
    state = input(Fore.WHITE + "Do You Continue?(enter Y as Yes Otherwise enter any key to exit):> ").upper()
    if state == "Y":
        shell_clear()
    else:
        exit()


# ----------------------------------------------------------------------------------------------------------------------
# Header
print("Hi, Welcome To Bank System")

# Check The Internet Connection
try:
    tkn = open("tokan.txt", "r")
    token = tkn.read()
    tkn.close()
    information = requests.get('http://176.9.164.222:2211/api/accounts/BankAccountListCreate',
                               headers={'Authorization': 'JWT ' + token}).json()
    if 'Error decoding signature.' in list(information.values()):
        tkn = open("tokan.txt", "w")
        tkn.write("")
        tkn.close()
    # Login form and Check if logged in before Done!

except ConnectionError:
    print(Fore.RED + "NO INTERNET CONNECTION, CONNECT THEN TRY AGAIN!" + Fore.WHITE)
    exit()

try:
    info = open("tokan.txt", "r")
    result = info.read()
    info.close()
    if result == "":
        info = None
except:
    info = None

if info is None:
    # Logging In
    print(Fore.BLUE + "You Have To Login!")
    userName = input(Fore.WHITE + "Enter Your UserName:> ")
    passWord = input("Enter Your Password:> ")

    while "" in (userName, passWord):
        print(Fore.RED + "*DON\'T PUT ANY FIELD BLANK!")
        userName = input(Fore.WHITE + "Enter Your UserName:> ")
        passWord = input("Enter Your Password:> ")
    response = requests.post("http://176.9.164.222:2211/api/Login",
                             data={"username": userName, "password": passWord}).json()["token"]

    try:
        savetoken = open("tokan.txt", "w")
        savetoken.write(response)
        savetoken.close()
        shell_clear()
        print(Fore.GREEN + "Congratulation You Logged In Successfully")

    except:
        print(Fore.RED + "User Not Exists Or Password Is Wrong!")
    tkn = open("tokan.txt")
    token = tkn.read()

else:
    # User Found (reading the user info and login)
    print(Fore.BLUE + "Please Wait Until Login")
    token = open("tokan.txt").read()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Variables:
codes = ("GBAL", "GAL", "AATAO", "C", "O", "EXIT", "CCA", "B", "FT", "FTL", "RP", "RA")


# Menu
def menu():
    global statue, response
    print(Fore.WHITE + "Here is A List You Can Do:\nType " + Fore.YELLOW + 'GBAL' + Fore.WHITE +
          " as Getting Bank Account Logs\nType " + Fore.YELLOW + "GAL" + Fore.WHITE +
          " If You Wanna See Accounts List\nType " + Fore.YELLOW + 'AATAO' + Fore.WHITE +
          " If You Wanna Adding Account to AccountOwner\nType " + Fore.YELLOW + 'C' + Fore.WHITE +
          " If You Wanna Close An Account\nType " + Fore.YELLOW + 'O' + Fore.WHITE +
          " If You Wanna Open An account\nType " + Fore.YELLOW + "RP" + Fore.WHITE +
          " If You Wanna Retrieves A Person's All Accounts\nType " + Fore.YELLOW + "RA" + Fore.WHITE +
          " If You Wanna Retrieves An Account\nType " + Fore.YELLOW + "FTL" + Fore.WHITE +
          " If Wanna Get The Accounts Transfer Report\nType " + Fore.YELLOW + 'CCA' + Fore.WHITE +
          " If you Wanna Create A Clerk Account\nType " + Fore.YELLOW + "FT" + Fore.WHITE +
          " If For Fund Transfer\nType " + Fore.YELLOW + "B" + Fore.WHITE +
          " If You Wanna Block An Account\nType " + Fore.YELLOW + "EXIT" + Fore.WHITE +
          " If You Wanna Shut Down The System")

    command = input(Fore.WHITE + "Type Command Here:> ")
    command = command.upper()

    while command not in codes:
        print(Fore.LIGHTRED_EX + "Command is Not Defined")
        command = input(Fore.WHITE + "Type Command Here:> ")
        command = command.upper()
        if command in codes:
            break

    if command == "GAL":
        print(Fore.BLUE + "Please Wait! Data Is Loading . . .")
        information = requests.get('http://176.9.164.222:2211/api/accounts/BankAccountListCreate',
                                   headers={'Authorization': 'JWT ' + token}).json()

        for each_main_account in information:
            each_account = each_main_account['accountOwner']
            print(Fore.BLUE + "First Name:", Fore.WHITE + each_account["firstName"])
            print(Fore.BLUE + "Last Name:", Fore.WHITE + each_account["lastName"])
            print(Fore.BLUE + "Phone Number:", Fore.WHITE + each_account["phoneNumber"])
            print(Fore.BLUE + "I.D. Number:", Fore.WHITE + each_account["nationalCode"])
            print(Fore.BLUE + each_account["lastName"], "Account(s):\n")

            for account in each_account["accounts"]:
                if account["status"] == "O":
                    situation = Fore.GREEN + "Open"
                elif account["status"] == "C":
                    situation = Fore.RED + "Close"
                else:
                    situation = Fore.RED + "Blocked"

                print(Fore.GREEN + "Account #" + str(each_account["accounts"].index(account) + 1), Fore.WHITE +
                      account["accountNumber"] + " -----> " + "  " + "Status:", situation)

            print(Fore.BLUE + "Credit:", Fore.WHITE + str(each_main_account["credit"]))
            print("\n" * 2)

        menu_start()
        shell_clear()
        menu()

    # Getting Bank Account Logs Done
    elif command == "GBAL":
        data = {}
        accountNumber = input(Fore.BLUE + "Please Enter The Account Number:> " + Fore.WHITE)
        logs = requests.post("http://176.9.164.222:2211/api/accounts/GetBankAccountLogs",
                             headers={'Authorization': 'JWT ' + token},
                             data={"accountNumber": accountNumber}).json()

        try:
            for each_action in logs["logs"]:
                print(Fore.CYAN + "Action #" + str(logs["logs"].index(each_action) + 1))
                print(Fore.BLUE + "Amount:", Fore.WHITE + str(each_action["amount"]))
                if each_action["definition"] != "":
                    print(Fore.BLUE + "Definition:", Fore.WHITE + each_action["definition"])

                else:
                    print(Fore.BLUE + "Definition:", Fore.LIGHTBLACK_EX + "No Definition")

                if each_action["logType"] == "+":
                    print(Fore.BLUE + "Action Type:", Fore.GREEN + "Credit")
                    status = "Credit"

                else:
                    print(Fore.BLUE + "Action Type:", Fore.RED + "Debit")
                    status = "Debit"

                date = each_action["date"].split("T")
                print(Fore.BLUE + "Date & Time:", Fore.WHITE + date[0], "At Time", date[1][:8])

                date = status + ": " + date[0] + " At Time " + date[1][:8]
                data[date] = each_action["amount"]
                print("\n")
            print(Fore.LIGHTYELLOW_EX + "THE CURRENT CREDIT:", logs["currentCredit"])

            """START: Using Turtle To Draw Logs Chart"""
            from turtle import Turtle, Screen
            # print(data)
            FONT_SIZE = 8
            FONT = ("Arial", FONT_SIZE, "normal")

            title = accountNumber + "'s Logs Graph"
            print("Please Wait Until Chart Loads...")

            # Create and Setup the Window
            xmax = max(data.values())
            window = Screen()
            window.title(title)
            height = 130 * (len(data) + 1)  # (the space between each bar is 30, the width of each bar is 100)
            window.setup(600, height)  # specify window size (width is 600)

            turtle = Turtle(visible=False)
            turtle.speed('fastest')
            turtle.penup()
            turtle.setpos(-225, -(height / 2) + 50)
            turtle.pendown()

            # draw x-axis and ticks
            xtick = 400 / 7

            for i in range(1, 8):
                turtle.forward(xtick)
                xv = float(xmax / 7 * i)
                turtle.write('%.1f' % xv, move=False, align="center", font=FONT)
                turtle.right(90)
                turtle.forward(10)
                turtle.backward(10)
                turtle.left(90)

            turtle.setpos(-225, -(height / 2) + 50)
            turtle.left(90)

            # draw bar and fill color
            pixel = xmax / 400
            recs = []  # bar height

            for value in data.values():
                recs.append(value / pixel)

            for i, rec in enumerate(recs):
                if "Debit" in list(data.keys())[i]:
                    clr = "#00ff00"
                elif "Credit" in list(data.keys())[i]:
                    clr = "#ff0000"
                turtle.color('black')
                turtle.forward(30)
                turtle.right(90)
                turtle.begin_fill()
                turtle.forward(rec)
                turtle.left(90)
                turtle.forward(50 - FONT_SIZE / 2)
                turtle.write('  ' + str(rec * pixel), move=False, align="left", font=FONT)
                turtle.forward(50 + FONT_SIZE / 2)
                turtle.left(90)
                turtle.forward(rec)
                turtle.color(clr)
                turtle.end_fill()
                turtle.right(90)

            turtle.setpos(-225, -(height / 2) + 50)
            turtle.color('black')

            # draw y-axis and labels
            turtle.pendown()

            for key in data:
                turtle.forward(30)
                turtle.forward(10)
                turtle.write('  ' + key, move=False, align="left", font=FONT)
                turtle.forward(90)

            turtle.forward(30)

            # Wait for the user to close it
            window.mainloop()

            """END: Using Turtle To Draw Logs Chart"""
        except:
            print(Fore.RED + "There Is No Account With This Number!" + Fore.WHITE)

        menu_start()
        shell_clear()
        menu()

    # Adding An Account To The AccountOwner
    elif command == "AATAO":
        id = input(Fore.BLUE + "Please The I.D. Number: ")
        response = requests.post("http://176.9.164.222:2211/api/accounts/AddAccountToAccountOwner",
                                 headers={'Authorization': 'JWT ' + token}, data={"nationalCode": id}).json()

        try:
            print(Fore.GREEN + "Congratulations! Another New Account Added Creat Mr.\Mrs." + response["accountOwner"][
                "lastName"])
            print(Fore.BLUE + "The New Account Number Is:", Fore.WHITE + response["accountNumber"])

        except:
            print(Fore.RED + "NO PERSON FOUND WITH THIS ID CODE!")
        menu_start()
        shell_clear()
        menu()

    # Block an account Done
    elif command == "B":
        account_number = input(Fore.BLUE + "Please Enter Account Number To Block:> ")
        response = requests.post("http://176.9.164.222:2211/api/accounts/BlockAccount",
                                 headers={'Authorization': 'JWT ' + token},
                                 json={"accountNumber": account_number}).json()

        if "ok" in response:
            print(Fore.GREEN + "The Account Successfully, Blocked!")
        else:
            print(Fore.RED + "The Account Number Is Not Defined!")

        menu_start()
        shell_clear()
        menu()

    # Close an account Done
    elif command == "C":
        account_number = input(Fore.BLUE + "Please Enter Account Number To Close:> ")
        response = requests.post("http://176.9.164.222:2211/api/accounts/CloseAccount",
                                 headers={'Authorization': 'JWT ' + token},
                                 json={"accountNumber": account_number}).json()

        if "ok" in response:
            print(Fore.GREEN + "The Account Successfully, Closed!")
        else:
            print(Fore.RED + "The Account Number Is Not Defined!")

        menu_start()
        shell_clear()
        menu()

    # Open an account Done
    elif command == "O":
        print(Fore.WHITE + "Opening An Account:")
        firstName = input(Fore.BLUE + "Enter The First Name: ")
        lastName = input(Fore.BLUE + "Enter The Last Name: ")
        phoneNumber = input(Fore.BLUE + "Enter A Phone Number: ")
        nationalCode = input(Fore.BLUE + "Enter The I.D. Number: ")
        information = requests.post("http://176.9.164.222:2211/api/accounts/BankAccountListCreate",
                                    headers={'Authorization': 'JWT ' + token},
                                    json={"accountOwner": {"firstName": firstName, "lastName": lastName,
                                                           "phoneNumber": phoneNumber,
                                                           "nationalCode": nationalCode}})

        try:
            information = information.json()
            statue = True
            print(Fore.GREEN + "Congratulations! The Account Opened" + Fore.WHITE +
                  "\nThe Information Of Opened Account:")
            print(Fore.BLUE + "Account Number: " + Fore.GREEN + information["accountNumber"])
            print(Fore.BLUE + "First Name: " + Fore.GREEN + information["accountOwner"]["firstName"])
            print(Fore.BLUE + "Last Name: " + Fore.GREEN + information["accountOwner"]["lastName"])
            print(Fore.BLUE + "Phone Number: " + Fore.GREEN + information["accountOwner"]["phoneNumber"])
            print(Fore.BLUE + "National Code: " + Fore.GREEN + information["accountOwner"]["nationalCode"])
            print(Fore.BLUE + "This Person Has ", Fore.GREEN + len(information["accounts"]),
                  Fore.BLUE + "Account Right Now")
            print(Fore.BLUE + "Total Credit in Our Bank: " + Fore.GREEN + information["credit"])

        except:
            if not statue:
                print(Fore.RED + "Account Didn't Opened, Some filed Was Empty! Or Check The Internet Connection.")

        menu_start()
        shell_clear()
        menu()

    # Fund Transferring Done
    elif command == "FT":
        cash = input(Fore.BLUE + "Do You Wanna Do It By Cash? (Yes, No): ").lower()

        # For Invalided Input
        while cash not in ("yes", "no"):
            print(Fore.RED + "You Can Only Enter 'Yes' or 'No'")
            cash = input(Fore.BLUE + "Do You Wanna Do It By Cash? (Yes, No): ").lower()

        # By Cash
        if cash == "yes":
            action = input(Fore.BLUE + "If You Wanna Credit To An Account Enter " + Fore.YELLOW + "'C'" + Fore.BLUE +
                           " Or " + Fore.YELLOW + "'D'" + Fore.BLUE + " For Debit Form Your Account:> ").upper()

            # For Invalided Input
            while action not in ("D", "C"):
                print(Fore.RED + "You Can Only Enter 'D' " + Fore.BLUE + "or" + Fore.YELLOW + " 'C'")
                action = input(Fore.BLUE + "If You Wanna Credit To An Account Enter " + Fore.YELLOW + "'C'" + " Or " +
                               Fore.YELLOW + "'D'" + Fore.BLUE + " For Debit Form Your Account:> ").upper()

            # Don't need toAccount
            if action == "D":
                fromAccount = input(Fore.BLUE + "Enter The Source Account Number: ")
                response = requests.get("http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/" + fromAccount,
                                        headers={'Authorization': 'JWT ' + token}).json()
                if response["status"] not in ("B", "C"):
                    amount = input(Fore.BLUE + "Enter The Amount Of Money: ")
                    definition = input(Fore.BLUE + "Enter Your Definition: ")
                    response = requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",
                                             headers={'Authorization': 'JWT ' + token},
                                             json={"fromAccount": fromAccount, "cash": "true",
                                                   "definition": definition, "amount": int(amount)}).json()

                    try:
                        res = response["id"]
                        print(Fore.GREEN + "Fund Transfer Was Successful!",
                              Fore.YELLOW + amount + "$" + Fore.GREEN + " Debited!")
                    except:
                        if ['not enough credit'] in response.values():
                            print(Fore.RED + "Sorry Source Account Doesn't Has Enough Credit!")
                        else:
                            print(Fore.RED + "ERROR! SERVER COULDN'T TRANSFERS!")
                else:
                    if response["status"] == "B":
                        print(Fore.RED + "You can't do it, your account is blocked")
                    else:
                        print(Fore.RED + "You can't do it, your account is closed")


            # Don't need fromAccount
            else:
                toAccount = input(Fore.BLUE + "Enter The Destination Account Number: ")
                response = requests.get("http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/" + toAccount,
                                        headers={'Authorization': 'JWT ' + token}).json()
                if response["status"] not in ("B", "C"):
                    amount = input(Fore.BLUE + "Enter The Amount Of Money: ")
                    definition = input(Fore.BLUE + "Enter Your Definition: ")
                    response = requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",
                                             headers={'Authorization': 'JWT ' + token},
                                             json={"toAccount": toAccount, "cash": "true",
                                                   "definition": definition, "amount": int(amount)}).json()

                    try:
                        res = response["id"]
                        print(Fore.GREEN + "Fund Transfer Was Successful!",
                              Fore.YELLOW + amount + "$" + Fore.GREEN + " Credited!")
                    except:
                        if ['not enough credit'] in response.values():
                            print(Fore.RED + "Sorry Source Account Doesn't Has Enough Credit!")
                        else:
                            print(Fore.RED + "ERROR! SERVER COULDN'T TRANSFERS!")
                else:
                    if response["status"] == "B":
                        print(Fore.RED + "You can't do it, your account is blocked")
                    else:
                        print(Fore.RED + "You can't do it, your account is closed")

        # Without Cash
        else:
            fromAccount = input(Fore.BLUE + "Enter The Source Account Number: ")
            toAccount = input(Fore.BLUE + "Enter The Destination Account Number: ")
            amount = input(Fore.BLUE + "Enter The Amount Of Money: ")
            definition = input(Fore.BLUE + "Enter Your Definition: ")
            response = requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",
                                     headers={'Authorization': 'JWT ' + token},
                                     json={"fromAccount": fromAccount, "toAccount": toAccount, "cash": "false",
                                           "definition": definition, "amount": int(amount)}).json()

            try:
                res = response["id"]
                print(Fore.GREEN + "Fund Transfer Was Successful!",
                      Fore.YELLOW + amount + "$" + Fore.GREEN + " Transferred!")
            except:
                if ['not enough credit'] in response.values():
                    print(Fore.RED + "Sorry Source Account Doesn't Has Enough Credit!")
                else:
                    print(Fore.RED + "ERROR! SERVER COULDN'T TRANSFERS!")

        menu_start()
        shell_clear()
        menu()

    # Get A List Of Transferred Account Done
    elif command == "FTL":
        response = requests.get("http://176.9.164.222:2211/api/transaction/TransactionListCreate",
                                headers={'Authorization': 'JWT ' + token}).json()
        for each_report in response:
            print(Fore.YELLOW + "REPORT #" + str(each_report["id"]))
            if each_report["fromAccountNumber"] is not None:
                print(Fore.BLUE + "Source Account:", Fore.WHITE + str(each_report["fromAccountNumber"]))

            if each_report["toAccountNumber"] is not None:
                print(Fore.BLUE + "Destination Account:", Fore.WHITE + str(each_report["toAccountNumber"]))

            print(Fore.BLUE + "Amount Of Money, Transferred:", Fore.WHITE + str(each_report["amount"]))

            if each_report["definition"] == "":
                print(Fore.BLUE + "Cause Of Transfer:", Fore.LIGHTBLACK_EX + "No Definition")

            else:
                print(Fore.BLUE + "Cause Of Transfer:", Fore.WHITE + each_report["definition"])

            if str(each_report["cash"]).lower() == "false":
                print(Fore.BLUE + "Is Transfer Did By Cash:", Fore.LIGHTBLACK_EX + "NO")

            else:
                print(Fore.BLUE + "Is Transfer Did By Cash:", Fore.WHITE + "YES")

            print("\n")

        menu_start()
        shell_clear()
        menu()

    # Retrieve Person By ID Done
    elif command == "RP":
        id_code = input(Fore.BLUE + "Enter The Person's National ID Code You Wanna Retrieve:> ")
        while id_code in ("", " "):
            print(Fore.RED + "Sorry The ID Field Can't Be Empty!")
        sitiuation = True
        try:
            response = requests.get("http://176.9.164.222:2211/api/accounts/AccountOwnerRetrieve/" + id_code,
                                headers={'Authorization': 'JWT ' + token}).json()
            sitiuation=False
            try:
                res = response["firstName"]
                print(Fore.GREEN + "Account Found! The Information:")
                print(Fore.BLUE + "Owner First Name:", Fore.WHITE + response["firstName"])
                print(Fore.BLUE + "Owner Last Name:", Fore.WHITE + response["lastName"])
                print(Fore.BLUE + "National ID Code:", Fore.WHITE + response["nationalCode"])
                print(Fore.BLUE + "Phone Number:", Fore.WHITE + response["phoneNumber"])
                print(Fore.YELLOW + "This Person Has", len(response["accounts"]), "Account(s)")
                for each_account in response["accounts"]:
                    if each_account["status"] == "O":
                        status = Fore.GREEN + "Open"
                    elif each_account["status"] == "B":
                        status = Fore.RED + "Blocked"
                    else:
                        status = Fore.RED + "Closed"
                    print(
                        Fore.YELLOW + "Account #" + str(response["accounts"].index(each_account) + 1) + "   " + Fore.WHITE +
                        each_account["accountNumber"] + Fore.YELLOW + "   ----->   " + Fore.WHITE + "Status:", status)
            except:
                print(Fore.RED + "There Is No Person With This ID!")
        except:
            if sitiuation:
                print(Fore.RED + "The Id Code didn't found!")
        menu_start()
        shell_clear()
        menu()

    # Retrieve Account Info.s Done
    elif command == "RA":
        accountNumber = input(Fore.BLUE + "Enter The Account Number You Wanna Retrieve:> ")
        while accountNumber in ("", " "):
            print(Fore.RED + "Sorry Account Number Can't Be Empty!")
        response = requests.get("http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/" + accountNumber,
                                headers={'Authorization': 'JWT ' + token}).json()

        try:
            print("The Retrieved Account Number Was", Fore.YELLOW + response["accountNumber"])
            information = response["accountOwner"]
            print(Fore.BLUE + "Owner First Name:", Fore.WHITE + information["firstName"])
            print(Fore.BLUE + "Owner Last Name:", Fore.WHITE + information["lastName"])
            print(Fore.BLUE + "National ID Code:", Fore.WHITE + information["nationalCode"])
            print(Fore.BLUE + "Phone Number:", Fore.WHITE + information["phoneNumber"])
            print(Fore.YELLOW + "This Person Has", (len(information["accounts"]) - 1), "Other Account(s):")
            print(Fore.BLUE + "Account Credit:", Fore.WHITE + information["credit"])

            if response["status"] == "O":
                status = Fore.GREEN + "Open"
            elif response["status"] == "B":
                status = Fore.RED + "Blocked"
            else:
                status = Fore.RED + "Closed"
            print(Fore.BLUE + "Status:", status)

            for each_account in information["accounts"]:
                if each_account["accountNumber"] == accountNumber:
                    continue
                if each_account["status"] == "O":
                    status = Fore.GREEN + "Open"
                elif each_account["status"] == "B":
                    status = Fore.RED + "Blocked"
                else:
                    status = Fore.RED + "Closed"
                print(
                    Fore.YELLOW + "Account #" + str(response["accounts"].index(each_account) + 1) + "   " + Fore.WHITE +
                    each_account["accountNumber"] + Fore.YELLOW + "   ----->   " + Fore.WHITE + "Status:", status)
        except:
            print(Fore.RED + "There Is No Account With This Number!")
        menu_start()
        shell_clear()
        menu()

    # Exit from Bank Account Done
    elif command == "EXIT":
        exit()

    # Opening A Clerk Account Done
    elif command == "CCA":
        nw_username = input(Fore.WHITE + "Enter Your UserName:")
        nw_password = input("Enter Your Password:")

        while "" in (nw_username, nw_password):
            print(Fore.RED + "*DON\'T PUT ANY FIELD BLANK!")
            nw_username = input(Fore.WHITE + "Enter Your UserName:")
            nw_password = input("Enter Your Password:")
        early_token = requests.post("http://176.9.164.222:2211/api/Login",
                                    data={"username": "test", "password": "test"}).json()
        nw_response = requests.post("http://176.9.164.222:2211/api/accounts/User/SignUp",
                                    headers={'Authorization': 'JWT ' + early_token["token"]},
                                    data={"username": nw_username, "password": nw_password}).json()

        if nw_username == nw_response['username']:
            shell_clear()
            print(Fore.GREEN + "Congratulation You Signed Up Successfully!")
            print(Fore.BLUE + "The New Account Info:")
            print(Fore.BLUE + "UserName:", Fore.YELLOW + nw_username)
            print(Fore.BLUE + "PassWord:", Fore.YELLOW + nw_password)

        elif 'A user with that username already exists.' in nw_response["username"]:
            print(Fore.RED + "A User With That Username Already Exists!")

        else:
            print(Fore.RED + "ERROR! The User Didn't Create!")
        menu_start()
        shell_clear()
        menu()


menu()
