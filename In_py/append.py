Options = [1,2,3,4,5,6,100]
Computer_List = []
Computer_List2 = []

print("Please Enter a number 1-6 to see What com part that you want")
print("Enter 100 to exit entering list item")
print("1: PC case")
print("2: Mother Board")
print("3: Power Suppply")
print("4: GPU")
print("5: Coolant")
print("6: Fan")
switcherDict = {
    1: "PC case",
    2: "Mother Booard",
    3: "Power Suppply",
    4: "GPU",
    5: "Coolant",
    6: "Fan",
}

# Using Dict and Match/Case
while True:
    item = int(input("Enter a Number: "))
    if item in Options:
        match item:
            case 1:
                Computer_List.append(switcherDict[1])
            case 2:
                Computer_List.append(switcherDict[2])
            case 3:
                Computer_List.append(switcherDict[3])
            case 4:
                Computer_List.append(switcherDict[4])
            case 5:
                Computer_List.append(switcherDict[5])
            case 6:
                Computer_List.append(switcherDict[6])
            case 100:
                break
    else:
        print("You have entered an unrecognised input")
        print("Please Enter a number 1-6 to see What com part that you want")
        print("Enter 100 to exit entering list item")
        print("1: PC case")
        print("2: Mother Board")
        print("3: Power Suppply")
        print("4: GPU")
        print("5: Coolant")
        print("6: Fan")

print("Your list is",Computer_List)