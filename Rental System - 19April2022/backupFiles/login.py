from Utils import confirm_ExitApplication


def login():
    print("(1) ADMIN ")
    print("(2) TENANT")
    print("(3) STAFF")

    error_entry = True

    while error_entry:
        try:
            optionSelected = int(input("Choose Your Option(?): "))
            if optionSelected == 1:
                adminLogin()
            elif optionSelected == 2:
                tenantLogin()
            elif optionSelected == 3:
                staffLogin()
            else:
                print("Wrong option Selected")
        except ValueError:
            continue
        else:
            wishtoContinue = confirm_ExitApplication()
            if wishtoContinue:
                continue
            else:
                error_entry = False
                quit()


def adminLogin():

    print("           Username : ")
    print(" ************** TO DO !!!!!")
    print("Admin Login")


def tenantLogin():
    print(" ************** TO DO !!!!!")
    print("Tenant Login")


def staffLogin():
    print(" ************** TO DO !!!!!")
    print("staffLogin")