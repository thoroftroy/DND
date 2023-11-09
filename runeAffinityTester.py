# Define the global variables
numberOfRunes = 0
totalNumberOfRunes = 0
totalAffinity = 0
required_affinity = 0
AR = 0

# Calculates the affinity a user has with a circle using the MEG function
def megFunc():
    global totalAffinity
    global numberOfRunes
    currentAffinity = 0
    calculatedRunes = 0
    while calculatedRunes != numberOfRunes:
        print("Input the affinities for rune",calculatedRunes+1)
        print("Input the Material Affinity")
        M = float(input())
        print("Input the Elemental Affinity")
        E = float(input())
        print("Input the Generic Affinity")
        G = float(input())
        currentAffinity = M+E+G
        calculatedRunes += 1
        totalAffinity += currentAffinity

def megFunc2():
    global totalAffinity
    global numberOfRunes
    currentAffinity = 0
    calculatedRunes = 0
    while calculatedRunes != numberOfRunes:
        M = 0
        E = 0
        G = 10
        currentAffinity = M+E+G
        calculatedRunes += 1
        totalAffinity += currentAffinity

# Calculates the required affinity for the circle
def calculate_required_affinity(numberOfRunes):
    AR = 0.2 * ((2 ** numberOfRunes) / 2)
    return AR
    
# Checks if the affinity meets the minimum requirements
def checkAffinity():
    global required_affinity
    global numberOfRunes
    global totalAffinity
    if required_affinity > totalAffinity:
        print(required_affinity," (the affinity requirement for ", numberOfRunes," runes) is greater than ", totalAffinity," (your current affinity) therefore you CANNOT activate the circle")
    elif required_affinity <= totalAffinity:
        print(required_affinity," (the affinity requirement for ", numberOfRunes," runes) is smaller than or equal to ", totalAffinity," (your current affinity) therefore you CAN activate the circle")
    else:
        print("How did we get here...")

# The main loop of the program
def main():
    global numberOfRunes
    global totalAffinity
    global required_affinity
    global totalNumberOfRunes
    
    totalAffinity = 0
    print('Input the number of non carbon runes in the circle')
    numberOfRunes = int(input())
    totalNumberOfRunes = (numberOfRunes+1)+numberOfRunes
    megFunc()
    print("|")
    print("Your total affinity for this circle is: ",totalAffinity)
    print("|")
    required_affinity = calculate_required_affinity(totalNumberOfRunes)
    checkAffinity()

# Calculate some more stuff
def main2():
    # This is a bit of a lazy hacked together thing trying to make this work better.
    global numberOfRunes
    global totalAffinity
    global required_affinity
    global totalNumberOfRunes
    
    totalAffinity = 0
    print('Input the number of non carbon runes in the circle')
    numberOfRunes = int(input())
    totalNumberOfRunes = (numberOfRunes+1)+numberOfRunes
    megFunc2()
    print("Your total affinity for this circle is: ",totalAffinity)
    required_affinity = calculate_required_affinity(totalNumberOfRunes)
    checkAffinity()

#mmmm numbers
def calculate_sum(x, y):
    result = x
    for i in range(2, y + 1):
        result += x / i
    return result
#This is to eleviate the pain of doing the calculations by hand
def main3():
    # Taking input for x and y
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))

    # Calculating and printing the result
    result = calculate_sum(x, y)
    print("The result of the sum is:", round(result, 2))

#Always run the program
while True != False:
    print("|")
    what = input()
    if what == "main":
        main()
    elif what == "main2":
        main2()
    elif what == "main3":
        main3()
    print("|")
