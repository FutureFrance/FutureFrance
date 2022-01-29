def show_balances():
    with open("testit.txt") as f:
        content = f.read()
        print(content)


def show_balance(name):
    with open("testit.txt") as f:
        content = f.readlines()
        for i in content:
            if i.split(": ")[0] == name:
                print(f'{name} has {i.split(": ")[1]}')


def admin_pass():
    with open("admin_pas.txt") as f_admin:
        return f_admin.read()


run = True

while run:
    character = input("Who are you ADMIN or USER ?\n").upper()

    if character == "ADMIN":
        password_ad = input("Introduce your password\n")
        if password_ad == admin_pass():
            admin_action = input("Hi, admin what do you want to do to ADD a user or to REMOVE a user ?\n")

            if admin_action.upper() == "ADD":
                with open("testit.txt", "a+") as file:
                    tst = f'{input("Introduce the NAME: ")}: {input("Introduce the amount of money: ")}'
                    file.write(tst)
                    print(tst)
            elif admin_action.upper() == "REMOVE":
                target = input("What is the name of the person to delete\n")
                admin_text = ""
                with open("testit.txt", "r+") as file:
                    admin_content = file.readlines()
                    for i in admin_content:
                        if i.split(": ")[0] != target:
                            admin_text += i.replace("\n", "") + "\n"
                    if admin_text != "":
                        file.seek(0)
                        file.truncate(0)
                        file.write(admin_text)
                    else:
                        print("No operation was executed, try one more time if again this message appears then contact support")
            else:
                while True:
                    end_admin = input("You introduced the wrong command, CONTINUE or EXIT ?\n")
                    if end_admin.upper() == "EXIT":
                        run = False
                        break
                    elif end_admin.upper() == "CONTINUE":
                        break
            run = False
        else:
            print("Wrong password, try again")

    elif character == "USER":
        ispositive = True
        found_person = False
        name = input("What is your name ?\n")
        action = input("What you want to do ? (DEPOSIT / SPEND / SEND | amount)\n")

        if "|" in action and (action.split("|")[0].upper() == "DEPOSIT" or "SPEND" or "SEND") and (action.split("|")[1].replace("\n", "").isnumeric()):
            with open("testit.txt", "r+") as f:
                content = f.readlines()
                text_in_file = ""

                if action.split("|")[0].upper() == "SEND":
                    target_name = input("Whom do you want to send the money too ?\n")
                    for i in content:
                        if i.split(": ")[0] == target_name:
                            text_in_file += i.split(": ")[0] + ": " + str((int(action.split("|")[1]) + int(i.split(": ")[1].replace("\n", "")))) + "\n"
                            found_person = True
                        elif i.split(": ")[0] == name:
                            text_in_file += i.split(": ")[0] + ": " + str(int(i.split(": ")[1].replace("\n", "")) - int(action.split("|")[1])) + "\n"
                            if int(i.split(": ")[1].replace("\n", "")) - int(action.split("|")[1]) < 0:
                                ispositive = False
                        else:
                            text_in_file += i
                    if not found_person:
                        text_in_file = ""
                        print("Invalid user name, person not found")

                elif action.split("|")[0].upper() == "DEPOSIT":
                    for i in content:
                        if i.split(": ")[0] == name:
                            text_in_file += i.split(": ")[0] + ": " + str(int(action.split("|")[1]) + int(i.split(": ")[1].replace("\n", "")))
                        else:
                            text_in_file += i

                else:
                    for x in content:
                        if x.split(": ")[0] == name:
                            balance = int(x.split(": ")[1].replace("\n", ""))
                            if action.split("|")[0] == "deposit":
                                balance += int(action.split("|")[1])
                                text_in_file += f'{x.split(": ")[0]}: {balance}\n'
                            else:
                                if balance - int(action.split("|")[1]) >= 0:
                                    balance -= int(action.split("|")[1])
                                    text_in_file += f'{x.split(": ")[0]}: {balance}\n'
                                else:
                                    print(f"{name} does not have sufficient balance")
                                    text_in_file += f'{x.split(": ")[0]}: {balance}\n'
                        else:
                            text_in_file += x.replace("\n", "") + "\n"
                if text_in_file != "" and ispositive:
                    f.seek(0)
                    f.truncate(0)
                    f.write(text_in_file)
                elif not ispositive:
                    print("Insufficient balance")
                else:
                    print("No operation was executed, try one more time if again this message appears then contact support")
                run = False
        else:
            while True:
                end = input("CONTINUE ? to Introduce the data one more time or EXIT ?\n").upper()
                if end == "CONTINUE":
                    break
                elif end == "EXIT":
                    run = False
                    break
    else:
        while True:
            end_character = input("Invalid character,try AGAIN or EXIT \n").upper()
            if end_character == "EXIT":
                run = False
                break
            elif end_character == "AGAIN":
                break
