"""
Submitted By: SAHIB BIR SINGH BHATIA
Student ID: 201547831
COMP 517 - Assignment 4 - 2020-21 - JAN21 - CA Assignment 4 - CACHE MANAGEMENT
"""

cache = []      # Initialising an empty list for Cache
requests = []   # Initialising an empty list for Requests


def fifo(req):    # Function fifo() takes one argument as a list and works on the principle of First In First Out
    cursor = 0    # Initialising cursor value to be the starting index
    for i in req:  # For every value in list
        if i not in cache and len(cache) < 8:  # Checking if the value exists in cache list and cache is not full
            cache.append(i)  # Adding the value in the cache if it doesn't exist
            print(i, "Miss")
        elif i in cache and len(cache) < 8:  # Checking if the value exists in cache list and cache is not full
            print(i, "Hit")
        elif (i not in cache) and (len(cache) == 8):  # Checking if the value exists in cache list and cache is full
            cache.pop(cursor)       # Removing oldest value
            cache.insert(0, i)      # Adding new value
            cursor = cursor + 1     # Updating cursor value
            print(i, "Miss")
        else:  # Checking if the value exists in cache list and cache is full
            print(i, "Hit")
    return "Cache: {}\n ".format(cache)   # Function fifo() returns the final state of cache


def lfu(req):  # Function lfu() takes one argument as a list and works on the principle of Least Frequently Used
    temp = []  # Initialising a temporary list
    count = {}  # Initialising a dictionary to keep track of count of hits
    minimumValue = []  # Initialising a list to keep track of smallest values
    for i in req:  # For every value in list
        if i not in cache and len(cache) < 8:  # Checking if the value exists in cache list and cache is not full
            count[i] = "1 Hit"  # Updating frequency of occurrence of the value
            cache.append(i)  # Adding the value in the cache
            print(i, "Miss")
        elif i in cache and len(cache) < 8:  # Checking if the value exists in cache list and cache is not full
            k = count[i][0]
            k = int(k) + 1
            count[i] = str(k) + " Hits"  # Updating frequency of occurrence of the value
            print(i, "Hit")
        elif i not in cache and len(cache) == 8:  # Checking if the value exists in cache list and cache is full
            for key in count:     # Finding value with least hits
                if count[key] == min(count.values()):
                    minimumValue.append(key)
            m = min(minimumValue)   # Finding smallest value with least hits
            minimumValue = []     # Reinitialising list to be empty
            cache.remove(m)  # Removing smallest value with least hits
            count.pop(m)  # Removing smallest value with least hits
            count[i] = "1 Hit"  # Updating frequency of occurrence of the new value
            cache.append(i)   # Adding the value in the cache
            print(i, "Miss")
        else:
            k = count[i][0]
            k = int(k) + 1
            count[i] = str(k) + " Hits"   # Updating frequency of occurrence of the value
            print(i, "Hit")
    for items in count:
        temp.append((items, count[items]))
        temp = sorted(temp)
    return "Cache: {}\n ".format(temp)   # Function lfu() returns the final state of cache


def handleRequests():   # Function handleRequests
    flag = True  # Initialising a flag for while loop
    global cache  # Referencing to globally initialised cache list
    global requests  # Referencing to globally initialised cache list
    while flag:      # Loop runs while flag is True
        try:
            userInput = int(input("Please enter a number: "))  # Fetching input from user
            if userInput == 0 and len(requests) != 0:  # Check if user input is 0 and there is at least 1 value present
                while True:
                    userChoice = input("Press 1 for FIFO \nPress 2 for LFU \nPress Q to Quit \n")  # Choice from user
                    if userChoice == "1":  # Checking user choice if it is 1 which references to fifo method to be used
                        cacheState = fifo(requests)   # Calling fifo() function with argument as requests list
                        print(cacheState)  # Printing out the final state of cache
                        cache = []
                    elif userChoice == "2":  # Checking user choice if it is 2 which references to lfu method to be used
                        cacheState = lfu(requests)  # Calling lfu() function with argument as requests list
                        print(cacheState)  # Printing out the final state of cache
                        cache = []
                    elif userChoice == "Q" or userChoice == "q":  # Checking user choice if user wants to quit program
                        flag = False  # updating flag to exit the program
                        break
                    else:  # Checking if user choice is a valid choice
                        print("Selection not valid. Please select again.\n")
                        continue
            elif len(requests) == 0 and userInput == 0:  # Check if the first input by user is 0
                print("Please enter again. First number cannot be zero.\n")
                continue
            elif userInput < 0:  # Check if user input is a negative number
                print("Please enter a positive integer.Value cannot be negative.\n")
                continue
            else:
                requests.append(userInput)  # Adding user input to the requests list
                continue
        except ValueError:  # Invalid input entered
            print("That was not a valid number.Please try again.\n")


def main():   # Function main()
    handleRequests()  # Function handleRequests() is called


if __name__ == "__main__":
    main()
