
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9736263
#    Student name: Madura Senadeera
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  Publish Your Own Periodical
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design and development to produce a
#  useful application for publishing a customised newspaper or
#  magazine on a topic of your own choice.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression.
from re import findall

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your publication file.
import os
import webbrowser
# An operating system-specific function for 'normalising' a
# path to a file to the path naming conventions used on this
# platform.  Apply this function to the full name of your
# publication file so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date/time function.
from datetime import datetime

#
#--------------------------------------------------------------------#
#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#
# Name of the published newspaper or magazine. To simplify marking,
# your program should publish its results using this file name.
file_name = 'publication.html'
#################################################################
#Variables gathering values for each variables from the RSS Feed#
#################################################################

######Breaking News
NASA_Breaking_News = urlopen('http://www.nasa.gov/rss/dyn/breaking_news.rss')
Breaking_News_code = NASA_Breaking_News.read()
NASA_Breaking_News.close()

Breaking_News_title = findall('<title>(.+)</title>', Breaking_News_code)

Breaking_News_pic = findall('<enclosure url="(.*)" length', Breaking_News_code)

Breaking_News_description = findall('<description>(.+)</description>', Breaking_News_code)

Breaking_News_pubDate=findall('<pubDate>(.+)</pubDate>', Breaking_News_code)

Breaking_News_link=findall('<link>(.+)</link>', Breaking_News_code)

###### Image of the Day
NASA_Image_of_the_Day = urlopen('http://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
Image_code = NASA_Image_of_the_Day.read()
NASA_Image_of_the_Day.close()

Image_title = findall('<title>(.+)</title>', Image_code)

Image_pic = findall('<enclosure url="(.*)" length', Image_code)

Image_description = findall('<description>(.+)</description>', Image_code)

Image_pubDate=findall('<pubDate>(.+)</pubDate>',Image_code)

Image_link=findall('<link>(.+)</link>',Image_code)

###### Education News
NASA_Education_News = urlopen('http://www.nasa.gov/rss/dyn/educationnews.rss')
Education_News_code = NASA_Education_News.read()
NASA_Education_News.close()

Education_News_title = findall('<title>(.+)</title>', Education_News_code)

Education_News_pic = findall('<enclosure url="(.*)" length', Education_News_code)

Education_News_description = findall('<description>(.+)</description>', Education_News_code)

Education_News_pubDate=findall('<pubDate>(.+)</pubDate>',Education_News_code)

Education_News_link=findall('<link>(.+)</link>',Education_News_code)

###### Earth News
NASA_Earth_News = urlopen('http://www.nasa.gov/rss/dyn/earth.rss')
Earth_News_code = NASA_Earth_News.read()
NASA_Earth_News.close()

Earth_News_title = findall('<title>(.+)</title>', Earth_News_code)

Earth_News_pic = findall('<enclosure url="(.*)" length', Earth_News_code)

Earth_News_description = findall('<description>(.+)</description>', Earth_News_code)

Earth_News_pubDate=findall('<pubDate>(.+)</pubDate>',Earth_News_code)

Earth_News_link=findall('<link>(.+)</link>',Earth_News_code)

######### Shuttle News
NASA_Shuttle_News = urlopen('http://www.nasa.gov/rss/dyn/shuttle_station.rss')
Shuttle_News_code = NASA_Shuttle_News.read()
NASA_Shuttle_News.close()

Shuttle_News_title = findall('<title>(.+)</title>', Shuttle_News_code)

Shuttle_News_pic = findall('<enclosure url="(.*)" length', Shuttle_News_code)

Shuttle_News_description = findall('<description>(.+)</description>',Shuttle_News_code)

Shuttle_News_pubDate=findall('<pubDate>(.+)</pubDate>',Shuttle_News_code)

Shuttle_News_link=findall('<link>(.+)</link>',Shuttle_News_code)

######### Solar System News
NASA_Solar_System_News = urlopen('http://www.nasa.gov/rss/dyn/solar_system.rss')
Solar_System_News_code = NASA_Solar_System_News.read()
NASA_Solar_System_News.close()

Solar_System_News_title = findall('<title>(.+)</title>', Solar_System_News_code)

Solar_System_News_pic = findall('<enclosure url="(.*)" length',Solar_System_News_code)

Solar_System_News_description = findall('<description>(.+)</description>',Solar_System_News_code)

Solar_System_News_pubDate=findall('<pubDate>(.+)</pubDate>',Solar_System_News_code)

Solar_System_News_link=findall('<link>(.+)</link>',Solar_System_News_code)

####################################
#Setup HTML Codes for each Section:#
####################################
Breaking_News_section="""
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		BREAKING NEWS
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Breaking_News_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Breaking_News_pic[0]+"""'>
		<style="border:3px solid black">
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Breaking_News_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Breaking_News_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Breaking_News_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">"""

###########
Education_News_section="""
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		EDUCATION NEWS
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Education_News_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Education_News_pic[0]+"""'>
		<style="border:3px solid black"
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Education_News_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Education_News_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Education_News_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">"""
#############
Earth_News_section="""
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		EARTH NEWS
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Earth_News_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Earth_News_pic[0]+"""'>
		<style="border:3px solid black"
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Earth_News_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Earth_News_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Earth_News_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">"""

########
Image_section=  """
                <p align = "center">
		<span style = "font-size:50px; font-family:Times">
		IMAGE OF THE DAY
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Image_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Image_pic[0]+"""' width=500px>
		<style="border:3px solid black"
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Image_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Image_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Image_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">

                """
#############
Shuttle_News_section="""
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		SPACE STATION NEWS
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Shuttle_News_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Shuttle_News_pic[0]+"""'>
		<style="border:3px solid black"
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Shuttle_News_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Shuttle_News_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Shuttle_News_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">"""
#############
Solar_System_News_section="""
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		SOLAR SYSTEM & BEYOND NEWS
		</span>
		</p>
                <hr width = 450px size = 5px>
		<table align = "center">
		 <tr>
                <p align = "center">
		<span style="font-size:22px; font-family:Arial"><b>"""+Solar_System_News_title[1].upper()+"""</b></span></p>
		
		<p align = "center">
		<img src = '"""+Solar_System_News_pic[0]+"""'>
		<style="border:3px solid black"
		</p>
		
		<p align = "left">
		<span style="font-size:22px; font-family:Arial">"""+Solar_System_News_description[1]+"""</span></p>

                <p align = "center">
		<span style="font-size:18px; font-family:Times">Published: """+Solar_System_News_pubDate[0]+"""</span></p>
                <p align = "center">
		<span style="font-size:18px; font-family:Times"><a href="""+Solar_System_News_link[1]+""">Read Full Article </a></span></p>

		<hr width = 450px size = 5px>
		<table align = "center">"""
#######################
#Setting up Gui Window#
#######################

publication_window = Tk()
publication_window.title(file_name)

Window_Title=Label(publication_window, text='NASA',font = ('Times', 40),width=10,height=1, borderwidth = 2, relief = 'groove',fg='white',bg="black").grid(row=0,column=0,columnspan=2)
topics_label=Label(publication_window, text = '1. Choose your preferred topics:   ').grid(row = 1, column = 0, columnspan=2,sticky = W)

#####Establishing boolean variables to check whether the checkboxes are selected
Breaking_checkbox = BooleanVar()
Education_checkbox = BooleanVar()
Earth_checkbox = BooleanVar()
Image_checkbox = BooleanVar()
Shuttle_checkbox = BooleanVar()
System_checkbox = BooleanVar()

# Function to alter the final HTML code developed depending on the checkboxes selected
def update_text():
    # Extract the user's likes from the button variables
    global users_selected
    users_selected = [Breaking_checkbox.get(), Education_checkbox.get(), Earth_checkbox.get(), Image_checkbox.get(),Shuttle_checkbox.get(),System_checkbox.get()]
    # Clear the text box
    Text_Box.delete(0.0, END)
    # Display the user's preferences
    # x variables is the combined HTML code of the news sections to be implemented
    global x
    x="<html>"

    # When the Print button is click, progress is displayed in a text box
    if not True in users_selected:
        Text_Box.insert(0.0, "ERROR: Cannot generate webpage\nNo topics selected! ")
        Read_Button.config(state="disabled")
    else:
        if users_selected[0]:
            x=x+Breaking_News_section
            Text_Box.insert(END, "Printing Breaking News...\n")
        if users_selected[1]:
            x=x+Education_News_section
            Text_Box.insert(END, "Printing Education News...\n")
        if users_selected[2]:
            x=x+Earth_News_section
            Text_Box.insert(END, "Printing Earth News...\n")
        if users_selected[3]:
            x=x+Image_section
            Text_Box.insert(END,"Printing Image of the Day...\n")
        if users_selected[4]:
            x=x+Shuttle_News_section
            Text_Box.insert(END,"Printing Space Station News...\n")
        if users_selected[5]:
            x=x+Solar_System_News_section
            Text_Box.insert(END,"Printing Solar System News..\n")
        Text_Box.insert(END,"Complete!") # prompts complete when all HTML code compiled
        Read_Button.config(state="normal") #This changes the button so be active, originally it is disabled until the print button is clicked

# Function defining the HTML code produced         
def open_page():
    html="""<html> 

	<head>
		<title>
		The NASA Bulletin
		</title>

		<body background="http://www.gunnars.com/wp-content/uploads/2014/08/Space.jpg">
                <style>p {margin:0px 300px 0px 300px}
                </style>
		<style>
		
		hr {border-style: solid; margin-top ; 2em; margin-bottom: 2em;}
		</style>
	</head>

	<body text="white">
		<p align = "center">
		<span style = "font-size:50px; font-family:Times">
		The NASA Bulletin
		</span>
		</p>

		<p align = "center">
		<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/500px-NASA_logo.svg.png">
		<style="border:3px solid black">
		</p>
		
		<p align = "center">
		<span style="font-size:22px; font-family:Arial">
		<em>Developed by</em> Madura Senadeera
		</span>
		</p>

		<hr width = 450px size = 5px>
		<table align = "center"> 
                <body text="white">"""+x+"""</html>""" # x defines the variable mentioned earlier (changes depending on checkboxes selected)
    # code established to allow for a html file to be created in wherever this python file is located
    path = os.path.abspath(file_name)
    url = 'file://' + path

    with open(path, 'w') as html_page:
        html_page.write(html)
    webbrowser.open(url) #html code opened in browser
    global Date_and_Time # global variable to be utilised when presenting the activity log
    Date_and_Time=datetime.now().strftime("%d-%m-%Y %H:%M:%S") # time when the 'Read' button is clicked and newspaper printed in browser
    Activity_Button.config(state="normal")# activity 'Record' button originally disabled, but as the program is used and contains history of pages viewed, it becomes active

# defined activity log function
def activity_log():
#connect to database
    connection = connect(database="internet_activity.db")
    connection.execute("DELETE FROM recent_downloads")
    internet_activity_db=connection.cursor()
# allowed user_likes to be a global list to further alter the activity log depending on the topics previously selected.
    if users_selected[0]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Breaking_News_link[1])+"')")        
    if users_selected[1]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Education_News_link[1])+"')")       
    if users_selected[2]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Earth_News_link[1])+"')")        
    if users_selected[3]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Image_link[1])+"')")        
    if users_selected[4]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Shuttle_News_link[1])+"')")        
    if users_selected[5]:
        connection.execute("INSERT INTO recent_downloads VALUES ('"+str(Date_and_Time)+"','"+str(Solar_System_News_link[1])+"')")       

    connection.commit()
#close connection
    internet_activity_db.close()
    connection.close()

    
####### Tkinter GUI

Breaking_News_Checkbutton=Checkbutton(publication_window, text='Breaking News',variable=Breaking_checkbox).grid(row=2,column=0,sticky = W )

Education_News_Checkbutton=Checkbutton(publication_window, text='Education News',variable=Education_checkbox).grid(row=2,column=1,sticky = W)

Image_Checkbutton=Checkbutton(publication_window, text='Image of the Day',variable=Image_checkbox).grid(row=3,column=0,sticky = W)

Earth_News_Checkbutton=Checkbutton(publication_window, text='Earth News',variable=Earth_checkbox).grid(row=3,column=1,sticky = W)

Solar_System_News_Checkbutton=Checkbutton(publication_window, text='Solar System News',variable=System_checkbox).grid(row=4,column=0,sticky = W)

Space_Station_News_Checkbutton=Checkbutton(publication_window, text='Space Station News',variable=Shuttle_checkbox).grid(row=4,column=1,sticky = W)

Print_Label=Label(publication_window, text = '2. Start printing your newspaper:   ').grid(row = 5, column = 0, columnspan=2,sticky = W)

Print_Button=Button(publication_window, text="Print",command=update_text).grid(row=6,column=0,columnspan=2)

Progress_Label=Label(publication_window, text = '3. Watch its progress:   ').grid(row = 7, column = 0, columnspan=2,sticky = W)

Text_Box=Text(publication_window,width = 40, height = 10,borderwidth = 2, relief = 'groove')
Text_Box.grid(row=8,column=0,columnspan=2)

Read_Label=Label(publication_window, text = '4. Open your newspaper and enjoy:   ').grid(row = 9, column = 0, columnspan=2,sticky = W)

Read_Button=Button(publication_window, text='Read', command=open_page,state=DISABLED)
Read_Button.grid(row=11,column=0,columnspan=2)

Activity_Label=Label(publication_window, text = '5. Save your viewing history:   ').grid(row = 12, column = 0, columnspan=2,sticky = W)

Activity_Button=Button(publication_window, text='Record',command=activity_log,state=DISABLED)
Activity_Button.grid(row=13,column=0,columnspan=2)

publication_window.mainloop()


