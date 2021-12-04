#Anna Toledo, CSE20 12/1/21
#Assignment 10.1 "Create Your Own Class"
#Creating a class based on a real world object (Capybara)
#Creds go to Prof and TA


import webbrowser
import time

#Parent Class "Animal"
class Animal:  
    #parent methods (eat, sleep, drink)
    def eat(self):
        print("I can eat!")
        print("I am now full")
    def sleep(self):
        print("I can sleep! I am now well rested")
    def drink(self):
        print("I can drink water! I am now hydrated")

#Child class "Capybara"
class Capybara(Animal):
    color_list = ["black" , "brown" , "red" , "gray"]
    size_list = ["small" , "medium" , "large"]
    age_list = ["baby","adult"]
    speed_list = ["slow" , "medium" , "fast"]
    #class attribute
    species = "rodent"
    #instance attribute
    def __init__(self, color, size, speed, age):
        self.__color = color
        self.__size = size
        self.__speed = speed
        self.__age = age
    def eat(self):
        print("I am vegetarian")
    def swim(self):
        print("I can swim, so I can avoid predators")
    def bark(self):
        print("I can bark! Kind of")

    #getter method age
    def get_age(self):
        return self.__age
    #setter method age
    def set_age(self):
        choice = ("Please input either baby or adult to set Sammy to:\n>>> ")
        if choice == "baby":
            self.__age = "baby"
            print("Sammy is now a baby")
        elif choice == "adult":
            self.__age = "adult"
            print("Sammy is now an adult")
        else:
            print("Invalid input")

    #getter and setter for size
    def get_size(self):
        return self.__size
    def set_size(self):
        print("Capybaras are the largest rodent in the world!")
        choice = input("Input one of the following sizes for Sammy: \nsmall\nmedium\nlarge\n>>> ")
        if choice == "small":
            self.__size = "small"
            print("Sammy is now small")
        elif choice == "medium":
            self.__size = "medium"
            print("Sammy is now Medium")
        elif choice == "large":
            self.__size = "large"
            print("Sammy is now large")
        else:
            print("Invalid input")


    #getter and setter for speed
    def get_speed(self):
        return self.__speed
    def set_speed(self):
        choice = input("Please enter one of the following:\nslow\nmedium\nfast\n>>> ")
        if choice == "slow":
            self.__speed = "slow"
            print("Sammy is now slow")
        elif choice == "medium":
            self.__speed = "medium"
            print("Sammy is now medium speed.")
        elif choice == "fast":
            self.__speed = "fast"
            print("Sammy is now fast")
        else:
            print("Invalid command")
    
    #getter method color
    def get_color(self):
        return self.__color
    #setter method color
    def set_color(self):
        choice = input("A capy's color can be:\nblack \nbrown \nred \ngrey \nPlease pick one of the following to change Sammy's fur\n>>> ")
        if choice == "black":
            self.__color = "black"
            print("Sammy's fur is now black")
        elif choice == "brown":
            self.__color = "brown"
            print("Sammy's fur is now brown")
        elif choice == "red":
            self.__color = "red"
            print("Sammy's fur is now red")
        elif choice == "grey":
            self.__color = "grey"
            print("Sammy's fur is now grey")
        #debug
        else:
            print("Sorry, that was not one of the colors.")

    #Do nothing
    def do_nothing(self):
        print("I am really good at doing nothing. Check it out")
        time.sleep(5)
        print("yup. nothing happening")

    #feed the capy
    def feed_capy(self):
        #set counter to 0
        counter = 0
        print("Capybaras love a range of vegetables, such as:")
        time.sleep(1)
        print("melon\ngrain\nsquash\ngrass")
        time.sleep(1)
        #while loop
        while counter < 3:
            choice = input("Please choose one of the above to feed the capy! Enter exit to exit.\n>>> ")
            if choice == "melon":
                print("Thank you for feeding the capy a melon.")
                counter = counter + 1
            elif choice == "grain":
                print("Thank you for feeding the capy some grain.")
                counter = counter + 1
            elif choice == "squash":
                print("Thank you for feeding the capy some squash.")
                counter = counter + 1
            elif choice == "grass":
                print("Thank you for feeding the capy some grass!")
                counter = counter + 1
            elif choice == "exit":
                break
            #debug
            else:
                print("That was not one of the choices.")
        else:
            print("Sammy is too full to eat more!")
    
    #Capy video will present multiple options, each opening a link for a video
    #new=0 attempts to open the url in the browser window that is currently open
    #Autoraise = True will automatically pull up window if possible to display video
    def capy_video(self):
        choice = input("Would you like to see some cute capy's?\nyes or no\n>>>")
        #yes choice
        if choice == "yes":
            options = input("Please input the one you would like to see. \
                \neating_cabbage\nswim\nmeme\nbaby\nbark\n>>> ")
            if options == "eating_cabbage":
                webbrowser.open("https://www.youtube.com/watch?v=v2SLG0U9ogM",new=0,autoraise=True)
            elif options == "swim":
                webbrowser.open("https://www.youtube.com/watch?v=tE7org6Z16w",new=0,autoraise=True)
            elif options == "meme":
                webbrowser.open("https://www.youtube.com/watch?v=26KooinHoJI",new=0,autoraise=True)
            elif options == "baby":
                webbrowser.open("https://www.youtube.com/watch?v=C7aWIdjYoJQ",new=0,autoraise=True)
            elif options == "bark":
                webbrowser.open("https://www.youtube.com/watch?v=2VjpwYM05eo",new=0,autoraise=True)
            #debug
            else:
                print("Sorry, that was not one of the options.")
        #no choice
        elif choice == "no":
            print("Ok, guess you don't want to see any cuteness")
        #debug
        else:
            print("Incorrect input")






def main():
    #object created, called sammy
    sammy = Capybara("brown" , "medium" , "slow" , "adult")
    #intro the main
    print("Welcome to the custom class capybara!")
    time.sleep(2)
    print("The capy we are working with today is called Sammy. He can do a lot!")
    time.sleep(2)
    print("He can do what other animals can do:")
    print("The #s are just showing what the commands are that are being used.")
    time.sleep(1)
    print("#sammy.eat")
    sammy.eat()
    time.sleep(1)
    print("#sammy.sleep")
    sammy.sleep()
    time.sleep(1)
    print("#sammy.drink")
    sammy.drink()
    time.sleep(1)
    print("#sammy.bark")
    sammy.bark()
    time.sleep(3)
    print("Some avaliable commands are: do_nothing , feed_capy , capy_video , help , explain , and exit")
    time.sleep(2)
    print("There is also the getter and setter commands under the README")
    print("There is also sammy. commands (eat, sleep, drink, bark)")
    #Shell for input
    while True:
        command = input("Please enter a command\n>>> ")
        if command == "do_nothing":
            sammy.do_nothing()
        elif command == "feed_capy":
            sammy.feed_capy()
        elif command == "capy_video":
            sammy.capy_video()
        elif command == "help":
            print ("The avaliable commands are: \
                \ndo_nothing\nfeed_capy\ncapy_video\nhelp\nexit")
        elif command == "explain":
            print("Please pick one of the class/methods you would like explained")
            print("class_Animal\nclass_Capybara\ngetters_setters\ndo_nothing\nfeed_capy\ncapy_video\nhelp")
            #Explain shell
            while True:
                command = input("Please enter a command\n>>> ")
                if command == "class_Animal":
                    print("The parent class for capybara is class Animal. It holds the basic things that animals can all do which are eat, sleep, and drink. The eat method is overriden by the eat method in class Capybara.")
                elif command == "class_Capybara":
                    print("The Capybara class is a child class inherited from class Animal. It is of the species rodent \and contains more advanced methods.")
                elif command == "getters_setters":
                    print("The encapsuled variables are color, size, speed, and age. They are all accessed using the get_ and set_. Each set has avaliable lists to change the capy to. By encapsulating the variables, they are now private.")
                elif command == "do_nothing":
                    print("This is more of a troll command I added that uses the imported time module to show one of a capybara's greatest skills: doing nothing. Seriously, they just lounge around all day.")
                elif command == "feed_capy":
                    print("This command teaches the user what capybaras eat, and offers a list of options for the user to feed the capybara. There is also a counter so if user feeds capy too much, it will be too full to eat.")
                elif command == "capy_video":
                    print("This command offers a list of names, each will open a video in a seperate tab of a cute capybara. I used the module webbrowser to do this.")
                elif command == "help":
                    print("Please pick one of the class/methods you would like explained")
                    print("class_Animal\nclass_Capybara\ngetters_setters\ndo_nothing\nfeed_capy\ncapy_video\nhelp and exit")
                elif command == "exit":
                    break
                else:
                    print("Invalid command")
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")

    print("Goodbye!")



if __name__ == "__main__":
    main()




    

    

    

