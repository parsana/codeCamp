# codeCamp

## following steps to clone and start tutorial
## $export GIT_SSL_NO_VERIFY=1
## git clone git@github.com/parsana/codeCamp.git

## Part 1
## $idle3 intro/intro.py

## Part 2
## Install the packages you'll need:
## $sudo pip3 install twython
## Test you have everything you need by entering the following commands:
## $python3 -c "import twython"
## https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
## The files you need will be in the twitter directory

---------------------
---------------------
---------------------



# Setup on reboot

## Running Turtle
- On the desktop, click on the terminal icon in the top left corner (it should look like a computer monitor)
- in the terminal, type "cd codeCamp"
- type in "ls" to view all the files in the directory
- type in "cd turtle" to move to the turtle directory
- type in "idle" to open up IDLE, the text editor
- select "File" then "Open" then select a lesson to work on
- you can also do "File" then "New" to start a new project
	- Remember to add the following code to the top of the file
```
import turtle               # allows us to use the turtles library
window = turtle.Screen()    # creates a graphics window
bradley = turtle.Turtle()   # create a turtle named bradley
	
# Exit when you click the turtle graphics window
def exit ():
  window.exitonclick()
```



