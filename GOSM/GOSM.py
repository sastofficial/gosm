# GOSM by SA ST
import os
html1 = """<h1 style="text-align: center;">Look At This Image</h1>
<h1 style="text-align: center;"><img src=""" # dont forget to add a extra " when making the html document.
html2 = """/></h1>
<meta http-equiv="refresh" content="1; URL='steam://rungameid/""" # dont forget to add another " at the begining of this.
html3 = " />"

input("Welcome to GOSM press enter to continue") # thx to https://stackoverflow.com/questions/19374944/how-to-wait-for-enter-key-press-in-python-2-7
site_name = input("Enter name for the folder: ")
if os.path.exists('GOSM/'+site_name):
    print("Error: Folder Already Exists")
else:
   os.makedirs('GOSM/'+site_name)
   input("Put a image inside the "+site_name+" folder. Then press enter!")
   img = input("What is the file name for the image. Dont forget the file format (.png, .jpg, etc.): ")
   game_id = input("What is the steam game id for the game you want to open: ")
   html = open('GOSM/'+site_name+'/index.html', 'w')
   html.write(html1+'"'+img+'"'+html2+game_id+'"'+html3)
   print("Done! Now upload the folder called "+site_name+" to a web host. Or host it yourself.")
   input(":) ")