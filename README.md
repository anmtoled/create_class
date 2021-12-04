# create_class
CSE20 Assignment 10.1
Custom Class Capybara by Anna Toledo

The Capybara class is a child class of Animal. Although inherited, it contains a lot more 
advanced commands than the simple Animal class. 

The class Animal has basic methods : eat, sleep, and drink, all that output a simple
print function. The method eat is overriden in the Capybara class, changing it to
"I am a vegetarian!" 

The class Capybara is an inherited class of Animal. It is of the species rodent and 
contains several methods and attributes, described below.

Attributes:
Note: All of the variables have been encapsulated. This means they have __ written before
them and require the proper command set_ and get_ to open. 
Ex: self.__color = color and def get_color

Color: The capybara can be multiple shades. The specifics to colors are put in a list,
titled "color_list" When users input command set_color()They will be presented with said list,
from which they choose from will become the new color of the object Sammy. They may also use
get_color, which simply returns the color of Sammy.

Size: The capybara can be multiple sizes. The specifics to stay proper are put in a list,
titled "size_list" When users input command set_size()They will be presented with said list,
from which they choose from will become the new size of the object Sammy. They may also use
get_size, which simply returns the size of Sammy.

Speed: The specifics to stay proper are put in a list,
titled "speed_list" When users input command set_speed()They will be presented with said list,
from which they choose from will become the new speed of the object Sammy. They may also use
get_speed, which simply returns the speed of Sammy.

Methods:
bark:  print("I can bark! Kind of")
swim: print("I can swim, so I can avoid predators")
do_nothing: does nothing, waits 5 seconds, and repeats
feed_capy: offers multiple items for user to "feed" capybara. counter is also implimented,
	each time food is fed, counter is +1. Once counter is at 3, user no longer able to 
	feed capybara
capy_video: Asks if user would like to see video, if yes, then offered multiple names. Each
	name opens a youtube video in a seperate tab using imported module webbrowser.
	If no, then loop ends.

All of these are implimented in the demo program, which I built to be a shell.
This way user can run through multiple of the commands without the program closing.
There is also a help function, which reiterates all of the commands.
There is also an explain function, which opens an imbedded shell. This shell offers
explanations to each method as well. 

TO USE:
The shell should handle most of it. For clarification, there are
also the sammy.bark, sammy.sleep, sammy.drink, and sammy.eat avaliable 
but are not under another run command. 


