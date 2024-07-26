import time as t

def account_management():
    # Collect user details
    name = input('Enter Name: ')
    phone = input('Enter Mobile Number: ')
    pin = input('Make Pin: ')
    address = input('Enter Address: ')
    adhar = input('Aadhaar Card Number: ')

    content = f"""
    Name: {name}
    Phone: {phone}
    Pin: {pin}
    Address: {address}
    Aadhaar Card Number: {adhar}
    """

    # Append the details to a file
    with open('account_details.txt', 'a') as file:
        file.write(content)
        file.write('\n' + '-'*40 + '\n')

    # Initialize user balance file
    with open('account_balance.txt', 'a') as file:
        file.write(f'Name: {name}, Balance: 0\n')

    t.sleep(1)
    print('Nice! Your account should be started in 1 to 2 hours. For support, contact: +91 99839188')
    print('Thanks for banking with us.')

def login_system():
    print('---LOGIN SYSTEM---')
    username = input('Enter Name: ')
    pin = input('Enter Pin: ')

    with open('account_details.txt', 'r') as file:
        content = file.read()

        if f'Name: {username}' in content and f'Pin: {pin}' in content:
            print('User Found!', '\n')
            t.sleep(2)
            print('Welcome To Our Bank, ', username)

            while True:
                info = f"""
                    Press 1 To Update Bank Balance.
                    Press 2 To Check Balance.
                    Press 3 To Delete Account.
                    Press 4 To Show User Details.
                    Press 5 To Contact Us.
                """
                print(info)
                option = int(input('Enter Your Choice: '))

                # OPTION FUNCTION--------------------------------------------------------------------
                def updateb():
                    balance_dict = {}
                    try:
                        with open('account_balance.txt', 'r') as file:
                            lines = file.readlines()

                        for line in lines:
                            if line.strip():
                                parts = line.split(', Balance: ')
                                if len(parts) == 2:
                                    user = parts[0].replace('Name: ', '').strip()
                                    balance = int(parts[1].strip())
                                    balance_dict[user] = balance

                        if username in balance_dict:
                            default_balance = balance_dict[username]
                        else:
                            default_balance = 0

                    except FileNotFoundError:
                        default_balance = 0

                    amount = int(input('Enter Amount to Add: '))
                    default_balance += amount

                    with open('account_balance.txt', 'w') as file:
                        for user, balance in balance_dict.items():
                            file.write(f'Name: {user}, Balance: {balance}\n')
                        file.write(f'Name: {username}, Balance: {default_balance}\n')

                    t.sleep(2)
                    print('Details Updated!')

                def check_balance():
                    try:
                        with open('account_balance.txt', 'r') as file:
                            lines = file.readlines()

                        for line in lines:
                            if line.strip():
                                parts = line.split(', Balance: ')
                                if len(parts) == 2:
                                    user = parts[0].replace('Name: ', '').strip()
                                    balance = int(parts[1].strip())
                                    if user == username:
                                        print(f'Your current balance is: {balance}')
                                        break
                        else:
                            print('User balance not found.')
                    except FileNotFoundError:
                        print('No balance records found.')

                def delete_account():
                    try:
                        with open('account_details.txt', 'r') as file:
                            lines = file.readlines()

                        with open('account_details.txt', 'w') as file:
                            for line in lines:
                                if not line.startswith(f'Name: {username}'):
                                    file.write(line)

                        with open('account_balance.txt', 'r') as file:
                            lines = file.readlines()

                        with open('account_balance.txt', 'w') as file:
                            for line in lines:
                                if not line.startswith(f'Name: {username}'):
                                    file.write(line)

                        t.sleep(2)
                        print('Account deleted successfully.')

                    except FileNotFoundError:
                        print('No account data found to delete.')

                def show_user_details():
                    try:
                        with open('account_details.txt', 'r') as file:
                            lines = file.readlines()

                        user_found = False
                        for line in lines:
                            if line.startswith(f'Name: {username}'):
                                user_found = True
                                print("User Details:")
                                while not line.strip() == '-'*40:
                                    print(line.strip())
                                    line = next(lines)
                                break

                        if not user_found:
                            print('User details not found.')

                    except FileNotFoundError:
                        print('No user details found.')

                if option == 1:
                    updateb()
                elif option == 2:
                    check_balance()
                elif option == 3:
                    delete_account()
                elif option == 4:
                    show_user_details()
                elif option == 5:
                    print('For support, contact: +91 99839188')

        else:
            print('Error: Invalid username or pin.')

# Uncomment this line to run the account management function
# account_management()
login_system()
