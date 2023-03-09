fake_train = ["franklin", "bedford", "nostrand","marcy", "tompkins","throop","marcus garvey","lewis"]

for i in fake_train:
    if i == "franklin":
        print(i)
    else:
        print("not the selected station")


start_break = False #Breaks out of outermost loop and moves onto next chunk of code 
yn_break = False #Breaks out of loop if 'no' was entered so that a correct station name can be re-entered
yn2_break = False #Breaks out of loop as far as the input y/n prompt so that in the case of an invalid (non- yes or no) input, the code will just ask for yes or no again

while not start_break:
    starting_station = input('What station are you at?')
    yn_break = False
    while not yn_break:
        yn2_break = False
        if starting_station in fake_train:
            yes_or_no = input(f"okay, so you are at {starting_station} station? (please enter yes or no): ")
            while not yn2_break:
                if yes_or_no == 'yes':
                    start_break = True #setting the start_break variable to True before breaking out of the [while not yn2_break] loop 
                    yn_break = True
                    yn2_break = True #because start_break is set to true now, we will break out of [while not start_break] loop and resume with the program
                    
                elif yes_or_no == 'no':
                    yn_break = True
                    yn2_break = True
                else:
                    print("yes or no was not entered, please try again.")
                    yn2_break = True #Here we break out of the [while not yn2_break] loop but because in this case start_break boolean was not changed, we stay within the [while not valid_input] loop]
                
        else:
            print("Unrecognized station name. Please enter the station you are at: ")

valid_end = False
while not valid_end:
    ending_station = input('What station are you going to?')
    if ending_station in fake_train:
        print(f"okay, so you are going to {ending_station} station")
        valid_end = True
    else:
        print("Unrecognized station. Please enter the station you are going to.")


# ending_station = input("What station would you like to go to?")
