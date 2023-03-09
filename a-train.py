fake_train = ["franklin", "bedford", "nostrand","marcy", "tompkins","throop","marcus garvey","lewis"]

#SECTION: ENTER STARTING LOCATION 
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
            print("Unrecognized station name please try again")
            yn_break = True


#SECTION: ENTER ENDING LOCATION
end_break = False
yn_break = False #Breaks out of loop if 'no' was entered so that a correct station name can be re-entered
yn2_break = False #Breaks out of loop as far as the input y/n prompt so that in the case of an invalid (non- yes or no) input, the code will just ask for yes or no again

while not end_break:
    ending_station = input('What station are you going to?')
    yn_break = False
    while not yn_break:
        yn2_break = False
        if starting_station in fake_train:
            yes_or_no = input(f"okay, so you are going to {ending_station} station? (please enter yes or no): ")
            while not yn2_break:
                if yes_or_no == 'yes':
                    end_break = True #setting the end_break variable to True before breaking out of the [while not yn2_break] loop 
                    yn_break = True
                    yn2_break = True #because end_break is set to true now, we will break out of [while not end_break] loop and resume with the program
                    
                elif yes_or_no == 'no':
                    yn_break = True
                    yn2_break = True
                else:
                    print("yes or no was not entered, please try again.")
                    yn2_break = True #Here we break out of the [while not yn2_break] loop but because in this case end_break boolean was not changed, we stay within the [while not valid_input] loop]
                
        else:
            print("Unrecognized station name please try again")
            yn_break = True

print (f"you will be traveling between {starting_station} and {ending_station}. This ride will have", abs(fake_train.index(ending_station) - fake_train.index(starting_station)), "stops:")

if fake_train.index(starting_station) < fake_train.index(ending_station): #starting at Franklin and heading east
    for station in fake_train:
        if fake_train.index(starting_station) < fake_train.index(station) <= fake_train.index(ending_station):
            print(station)
        # elif fake_train.index(starting_station) > fake_train.index(station) >= fake_train.index(ending_station):
        #     print(station)

if fake_train.index(starting_station) > fake_train.index(ending_station): #starting at Lewis and heading west
    for station in reversed(fake_train):
        if fake_train.index(starting_station) > fake_train.index(station) >= fake_train.index(ending_station):
            print(station)
