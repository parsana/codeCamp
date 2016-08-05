# codeCamp

##Contact Info:
- Parsana Pillay - Parsana_Pillay@intuit.com
- Garry Bullock - Garry_Bullock@intuit.com
- Jasmine Woo - Jasmine_Woo@intuit.com
- Twitter link - https://twitter.com/PFPillay


---------------------
---------------------
---------------------

# following steps to clone and start tutorial

1. $export GIT_SSL_NO_VERIFY=1
2. git clone git@github.com/parsana/codeCamp.git

---------------------
---------------------
---------------------

## Part 1

1. $idle3 intro/intro.py

## Part 2
1. Install the packages you'll need:
  1.$sudo pip3 install twython
2. Test you have everything you need by entering the following commands:
  1. $python3 -c "import twython"
3. https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
  1. The files you need will be in the twitter directory

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

# Resources

1. [Official Raspberry Pi help guide](https://www.raspberrypi.org/help/)
2. [Official Raspberry Pi tutorials](https://www.raspberrypi.org/resources/)
3. [Turtle Documentation](https://docs.python.org/2/library/turtle.html)
4. [Minecraft Pi getting started](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/)
5. [Minecraft Pi API](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)

