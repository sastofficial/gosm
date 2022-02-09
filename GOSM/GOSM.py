# GOSM by SA ST 1.3
import os
html1 = """<h1 style="text-align: center;">Look At This Image</h1>
<h1 style="text-align: center;"><img src=""" # dont forget to add a extra " when making the html document.
html2 = """/></h1>
<meta http-equiv="refresh" content=""" # add an extra " to this
html22 = "; URL='steam://rungameid/""" # dont forget to add another " at the begining of this.
html3 = " />"

vscode_mode = input("Welcome to GOSM press enter to continue\n") # thx to https://stackoverflow.com/questions/19374944/how-to-wait-for-enter-key-press-in-python-2-7
if vscode_mode == "vscode":
    site_name = "GOSM/"+input("Enter name for the folder\n")
else:
    site_name = input("Enter name for the folder\n")
if os.path.exists(site_name):
    print("Error: Folder Already Exists\n")
else:
   os.makedirs(site_name)
   input("Put a image inside the "+site_name+" folder. Then press enter!\n")
   img = input("What is the file name for the image. Dont forget the file format (.png, .jpg, etc.)\n")
   game_id = input("What is the steam game id for the game you want to open\n")
   custom_redirect_time = input("Do you want to customize the time it takes to open steam? (Default is 0)(Y/N)\n")
   y = "Y","y"
   if custom_redirect_time == y:
       redirect_time = input("How many seconds to open steam do you want?\n")
   html = open(site_name+'/index.html', 'w')
   if custom_redirect_time == y:
       html.write(html1+'"'+img+'"'+html2+redirect_time+html22+game_id+'"'+html3)
   else:
        html.write(html1+'"'+img+'"'+html2+"0"+html22+game_id+'"'+html3)
input("Done! Now upload the folder called "+site_name+" to a web host. Or host it yourself.\n:)\n")