#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials

# Functions to add credentials


def create_new_credential(site_name,account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(site_name,account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()


def find_credential(site_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(site_name)


def check_existing_credentials(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
    return Credentials.find_by_name(name)


def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()


def delete_credential(credentials):
    '''
    Method to delete credentials
    '''
    return Credentials.delete_credential(credentials)


def main():

    while True:
        print("Welcome to PassWord Locker!")
        print('\n')
        print("Use these short codes to select an option: Create Account use 'ca': Login to your account use 'li' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'ca':
            print("Create UserName")
            created_user_name = input()

            print("Create a Password")
            created_user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!")
                print("Enter a Password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print(" Login to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_user_password:
                    print("Check your username or password,wrong username or password!")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credential")
                    print("3: Delete credential")
                    print("4: Search credential")
                    print("5: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Site Name")
                                site_name = input()
                                print("Enter The Account Name")
                                account_name=input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(10000, 1111111)
                                    print(f"Site: {site_name}")
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Site: {site_name}")
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(
                                     site_name,account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == '1':
                        while True:
                            print("Below is a list of all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"SITE NAME:{credential.site_name}")
                                    print(f"ACCOUNT NAME:{credential.account_name}")
                                    print(f"PASSWORD:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't have any credential saved yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == '5':
                        print("WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == '3':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"SITE NAME: {search_credential.site_name} \n ACCOUNT_NAME:{search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credential(search_credential)
                                    print("Account deleted SUCCESSFULLY")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print("That Site Does not exist on the list")
                                break

                    elif option == '4':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter the site name to find credentials")

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(search_name)
                                    print(f"SITE NAME: {search_credential.site_name} \n ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                else:
                                    print("That Site is not on the list")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'li':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your Password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_user_password != '56789':
                print("Wrong userName or password. Username 'testuser' and password '56789'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'testuser' and default_user_password == '56789':
                print("YOU HAVE SUCCESSFULLY LOGGED IN!")
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1: View Your saved credentials")
                print("2: Add new credential")
                print("3: Delete credential")
                print("4: Search credential")
                print("5: Log Out")
                option = input()

                if option == '2':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter The Site Name")
                            site_name = input()
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter a password")
                            print(
                                "To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                account_password = random.randint(10000, 1111111)
                                print(f"Site: {site_name}")
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                account_password = input()
                                print(f"Site: {site_name}")
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_new_credential(create_new_credential(
                                site_name,account_name, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == '1':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"SITE NAME:{credential.site_name}")
                                print(f"ACCOUNT NAME:{credential.account_name}")
                                print(f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't have any credentials yet")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")
                        
                elif option == '5':
                    print("WARNING! You will lose all your credentials if you log out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("Search by site name, a credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"SITE NAME: {search_credential.site_name} \n ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("Delete this? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("Account deleted Successfully!")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That Site is not on the list")
                            break

                elif option == '4':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter a site name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"SITE NAME: {search_credential.site_name} \n ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            else:
                                print("This Site Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'ex':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()
