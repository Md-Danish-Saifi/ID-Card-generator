from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import os
import datetime

import pyttsx3#for text to speech

#for text to speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id) #to check voice
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)#for speech increase for speed faster speed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

image = Image.new('RGB', (1000, 900), (255, 255, 255))  # properties of new image to be saved
draw = ImageDraw.Draw(image)  # saving a new blank image to work it on

# Change arial  to any other like Calibri, Its up to you
font = ImageFont.truetype('arial', size=45)
name=input("Enter your name ")
os.system("Title ID CARD")
date = datetime.datetime.now()
speak("Welcome to id card generator by")
speak(f"...{name}!")
formatdate = date.strftime("  %d-%m-%Y\t\t\t\t\tID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print('*************************************************************************************************************************')
print(formatdate)
print(f'**************************************************BY {name.upper()} MCA*********************************************************')
speak('We Require Some Details of you')

# to store information of college
(x, y) = (65, 50)
# college = input('\nEnter Your College Name: ')
college = 'Hi-tech Institute of Engineering and Technology'
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial', size=42)
draw.text((x, y), college, fill=color, font=font)

# to store information of college address
(x, y) = (150, 95)
# college = input('\nEnter Your College Address: ')
college = '24-Milestone, Hapur Road, Ghaziabad(UP)'
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial', size=38)
draw.text((x, y), college, fill=color, font=font)

# adding an unique id number using random finction and concatinating string
(x, y) = (600, 170)
idno = random.randint(1000, 9000)
message = str('ID ' + '19220' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial', size=30)
draw.text((x, y), message, fill=color, font=font)

# to get user enterd information
(x, y) = (50, 250)
speak("enter your full name")
name = input('Enter Your Full Name: ')
name = 'Name - ' + name
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial', size=30)
draw.text((x, y), name, fill=color, font=font)

(x, y) = (50, 350)
speak("enter your gender")
Gender = input('Enter Your Gender: ')
Gender = 'Gender  -  ' + Gender
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), Gender, fill=color, font=font)

(x, y) = (50, 450)
speak("enter your Date Of Birth")
dob = input('Enter Your Date Of Birth: ')
dob = 'DOB  -  ' + dob
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), dob, fill=color, font=font)

(x, y) = (50, 550)
speak("Enter Your Blood Group")
bg = input('Enter Your Blood Group: ')
bg = 'Blood Group  -  ' + bg
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), bg, fill=color, font=font)

(x, y) = (50, 650)
speak("Enter Your Mobile Number")
mob = input('Enter Your Mobile Number: ')
mob = 'Mobile  -  ' + mob
temp = mob
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), mob, fill=color, font=font)

(x, y) = (50, 750)
speak("Enter Your Address")
Address = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), Address, fill=color, font=font)

# save the edited image in current directory.
image.save(str(name) + '.png')

# this info. is added in QR code, also add other things in str function
img = qrcode.make(str(idno) + str(name) + str(mob) + str(formatdate))
img.save(str(idno) + '.bmp')

# open saved named file and save it to final image
til = Image.open(name + '.png')

# open saved qr code to save it on final image
im = Image.open(str(idno) + '.bmp')

# ph=Image.open('ds.jpg')#to open ds named photo


til.paste(im, (475, 200))  # pasted image on named file
til.save(name + '.png')  # saving name image with Qr as final image

speak("Your ID Card Successfully generated")
speak("here you go sir")
os.startfile(name+".png")
input('\nPress any key to Close program...')  # use input yo hold the screen


