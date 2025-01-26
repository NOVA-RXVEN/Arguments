import os

shutdown = input("Do you wish to shudown your Computer? (Yes or No)")

if shutdown == 'no' or shutdown == 'No':
    exit()
else:
    os.system("shutdown /s /t 1")
