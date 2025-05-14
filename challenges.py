import random
from linkedList import Linked_list
from player import get_farms
# Farmer Jopliphant can't keep all his farm plots together! He needs a linked list that he can store the plot number and what is planted there! 
# After each year, each plant has to swap with the next plant on a list to ensure right dirt mineral concentration. 
# Find what he will plant in each field after any set amount of years.

# Farmer Jopliphant knows this isn't the best method for this problem. He just has some problems. We will not address this further.

#Order of crop rotation
#tomato -> carrot -> wheat -> potato -> empty -> tomato

def evan_challenge():
    #dictionary relating numbers to crops
    cropDict = {1: "tomato", 2: "carrot", 3: "wheat", 4: "potato", 5: "Empty"}
    #Create a list comprised of random elements, both for numbers and the crops
    numList = []
    cropList = []
    for x in range (10):
        number = random.randint(1,5)
        numList.append(number)
        cropList.append(cropDict[number])
    #Choose a random year to check the crop rotation
    year = random.randint(1,4)
    cropList.append(year)

    #Call the list of farms from a player made function called get_farms, passing in the list of plots and their crops
    linked_crops = get_farms(cropList)

    #Update all of the crop values in the list
    for crop in range (len(numList)):
        numList[crop] = (numList[crop] + year)%5 + 1
        cropList[crop] = cropDict[numList[crop]]

    #verify a random crop
    randCrop = random.randint(0,9)

    if type(linked_crops) != Linked_list():
        print("error, linked list not recieved")
        return (False, None, cropList[randCrop])

    #Verify the results
    current = linked_crops.getNode(randCrop)
    success = False
    if current == cropList[randCrop]:
        success == True

    return (success, current, cropList[randCrop])
