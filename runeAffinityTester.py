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
        print("Input the Material Affinity")
        M = float(input())
        print("Input the Elemental Affinity")
        E = float(input())
        print("Input the Generic Affinity")
        G = float(input())
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
    
#Always run the program
while True != False:
    print("|")
    main()
    print("|")
