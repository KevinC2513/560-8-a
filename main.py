import sys
import csv

def csv_stripper(file_path):
    athlete_data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            stripped_row = [cell.strip() for cell in row]  # Strip spaces from each cell
            athlete_data.append(stripped_row)
    return athlete_data


def what_file():
    file_select = input('''
    What file would you like to search for? 
    a ) Athlete File
    b ) 60s Music File
    x ) Quit
    ''').lower()
    return file_select
    

def file_do(file_select):
    #initializing some variables before assigning values
    state = "start"
    selected_file = "none"
    search_term = "none"

    while state == "start":
        if file_select == "a":
#           with open("atheletes.csv") as selected_file:
                #loop breaker
            selected_file = "athletes.csv"
            state = "done"
            
                
        elif file_select == "b":
#            with open("60s_music.csv") as selected_file:
                selected_file = "60s_music.csv"
                state = "done"
                
        elif file_select == "x":
                print("You have selected to quit.")
                state = "break" 
                
        else:
            print(f"You put {file_select}, Invalid input")
            
    return selected_file


def file_manipulator(selected_file, file_data):
    inputted_search_term  = input(f"Enter the search term for {selected_file} file: ")
    print(inputted_search_term)
    
    found = False
    if selected_file == "athletes.csv":
        for row in file_data:   
            if any(inputted_search_term.lower() in term.lower() for term in row):
                print(f"Your search term {inputted_search_term} exists in the {selected_file} file")
                found = True
                break
            
        if found == False:
            print(f"Not in found in the file")
        
        see_entry = input("Would you like to see the entries? y or n ").lower()
        if see_entry == "y":
                print(f"Here are all of the entries with the term {inputted_search_term}:")
                for row in file_data:
                    if any(inputted_search_term.lower() in term.lower() for term in row):
                        row_string = ', '.join(row)
                        print(row_string)
#instead of printing something like this
# -> ['Brady', ' Tom', '  American Football']
#it becomes Brady, Tom, American Football

        elif see_entry == "n":
            print("You did not want to see the results.")
            sys.exit()
        else:
            print("Invalid Input")
    else:
        for row in file_data:  
            #any() is used here to accept "any" time the input matches anything \
            #found without the string. the term.lower() turns all the values in the file to 
            #lower case and compares them all one by one. for each term in the row. 
            if any(inputted_search_term.lower() in term.lower() for term in row):
                print(f"Your search term {inputted_search_term} exists in the {selected_file} file")
                found = True
                break
        if found == False:
            print(f"Not in found in the file")
                
        see_entry = input("Would you like to see the entries? y or n ").lower()
        if see_entry == "y":
            print(f"Here are all of the entries with the term {inputted_search_term}:")
            for row in file_data:
                if any(inputted_search_term.lower() in term.lower() for term in row):
                    row_string = ', '.join(row)
                    print(row_string)
        elif see_entry == "n":
            print("You did not want to see the results.")
            print("The application will now end, Goodbye")
            sys.exit()
        else:
            print("Invalid Input")
             
                

def main():
    file_path = 'athletes.csv'  
    athlete_data = csv_stripper(file_path)
# For testing to see what is returned, gets rid of space before words
#    print(athlete_data)
    
    file_path = "60s_music.csv"
    music_data = csv_stripper(file_path)
#    print(music_data)

    
    #asks for input, pick a, b, x
    #calls what_file(), then stores the returned output as a variable
    file_select = what_file()
    #testing return, 
    print(f"You picked {file_select}")
    #calling file_do func, while passing in file_select, setting output as 
    #search term for the next step.
    selected_file = file_do(file_select)
    
    if selected_file == "athletes.csv":
        file_data = athlete_data
    else:
        file_data = music_data 
    
    file_manipulator(selected_file, file_data)
    

main()