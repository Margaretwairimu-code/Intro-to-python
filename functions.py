#functions methods
# print("Hello World") #built in

from custom_fuctions import greet

with open("temp.txt" , "w") as file:
    file.write("Hello\n")
    file.write("100\n")
    file.write("54.34\n")

with open("temp.txt" , "r") as file:
    content = file.read()
    print(content)


    # pip install yt-dlp


greet()
