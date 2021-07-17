
pi = round((22/7), 2)

def firstOption():  #Calculates Diameter,Circumference and Area given the radius
    d = round((2*r), 2)
    c = round((2*pi*r), 2)
    a = round((pi*(r*r)), 2)
    return d, c, a

def secondOption():   #Calculates Diameter,Radius and Area given the circumference
    d = round((c/pi), 2)
    a = round(((c*c)/(4*pi)), 2)
    r = round((c/(2*pi)), 2)
    return d, a, r

def thirdOption(): #Calculates Diameter,Radius and Circumference given the area
    r = round(((a/pi)**(1/2)), 2)
    c = round((2*pi*r), 2)   #As we calculate r above we can use 2*pi*r instead of using 2*pi*(a/pi)**(1/2)
    d = round((2*r), 2)      #As we calculate r above we can use 2r instead of using 2(a/pi)**(1/2)
    return r, c, d



print("********Welcome to Circle Calculator Program********")
print("\n1 --> Calculate {0} (d), {1} (c) and {2} (a), given the {3} (r) of a circle.".format("diameter", "circumference", "area", "radius") +
        "\n2 --> Calculate {0} (d), {1} (a) and {2} (r), given {3} (c) of a circle".format("diameter", "area", "radius", "circumference") +
        "\n3 --> Calculate {0} (d), {1} (r) and {2} (c), given {3} (a) of a circle".format("diameter", "radius", "circumference", "area") +
        "\nq --> Quit\n")

while True:
    # Taking input choice from User
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            try:
                r = float(input("Enter the {0}: ".format("Radius")))
                # Checking if user has entered a negative value
                # User will be prompted again to provide a positive input
                if r < 0:
                    print("Error! Radius cannot be negative.Please enter again.")
                    print()
                # Calling function and printing out required output if input is valid
                else:
                    Diameter, Circumference, Area = firstOption()
                    print("Diameter of circle: {0} cm".format(Diameter))
                    print("Circumference of circle: {0} cm".format(Circumference))
                    print("Area of circle: {0} sq cm\n".format(Area))
                    break
            # ValueError exception will be called if any other character instead of int or float input is provided.
            except ValueError:
                # User will be prompted again to provide a valid input.
                print("Error! You have entered an incorrect input. Please enter again.\n")

    elif choice == "2":
        while True:
            try:
                c = float(input("Enter the {0}: ".format("Circumference")))
                # User will be prompted again to provide a positive input
                if c < 0:
                    print("Error! Radius cannot be negative.Please enter again.")
                    print()
                # Calling function and printing out required output if input is valid
                else:
                    Diameter, Area, Radius = secondOption()
                    print("Diameter of circle: {0} cm".format(Diameter))
                    print("Area of circle: {0} sq cm ".format(Area))
                    print("Radius of circle: {0} cm\n".format(Radius))
                    break
            # ValueError exception will be called if any other character instead of int or float input is provided.
            except ValueError:
                # User will be prompted again to provide a valid input.
                print("Error! You have entered an incorrect input. Please enter again.\n")

    elif choice == "3":
        while True:
            try:
                a = float(input("Enter the {0}: ".format("Area")))
                # User will be prompted again to provide a positive input
                if a < 0:
                    print("Error! Radius cannot be negative.Please enter again.")
                    print()
                # Calling function and printing out required output if input is valid
                else:
                    Radius, Circumference, Diameter = thirdOption()
                    print("Radius of circle: {0} cm ".format(Radius))
                    print("Circumference of circle: {0} cm ".format(Circumference))
                    print("Diameter of circle: {0} cm\n".format(Diameter))
                    break
            # ValueError exception will be called if any other character instead of int or float input is provided.
            except ValueError:
                # User will be prompted again to provide a valid input.
                print("Error! You have entered an incorrect input. Please enter again.\n")

    # Exiting the loop because User has selected Quit option.
    elif choice == "q":
        print("*********Thank You!*********")
        break

    # Choice made by User is not valid.
    # User will be prompted again to input a valid choice.
    else:
        print("Please enter a valid choice\n")


