import datetime
now = datetime.datetime.now()
print("Welcome to Baily Square Officers Quarter")
print("Here are 16 buildings.")
print("Building number 2,4,6,8,10,12,14,16 have 12 homes.")
print("Building number 1,3,5,7,9,11,13 have 24 homes.")
print("Building number 15 building have 36 homes. ")
print("If you want to enter here please provide your information at first.")
print("---------------------------------------------")
username = input("Please enter your name: ")
building = int(input("Please enter the building number: "))
home = int(input("Please enter the home number: "))
print("00. Entry Date and Time: "+str(now))
print("01. User Name: "+username)
if building < 1 or building >= 17:
    print("02. Wrong building number.")
elif building % 2 == 0 and home > 12 or home < 1:
    print("03. Wrong Home number.")
elif building % 2 == 1 and home > 24 and building != 15 or home < 1:
    print("03. Wrong Home number.")
elif building == 15 and home > 36 or home < 1:
    print("03. Wrong Home number.")
else:
    if building >= 1 or building <= 16:
        print("02. Building number is: " + str(building))
        print("03. Home number is: " + str(home))
        if building % 2 == 0 and building <= 8:
            print("04. Use south gate. Go to the left side.")
        elif building % 2 == 1 and building < 8:
            print("04. Use south gate. Go to the right side.")
        elif building % 2 == 0 and building > 8:
            print("04. Use north gate. Go to the right side.")
        else:
            print("04. Use north gate. Go to the left side.")
        if building == 1 or building == 2 or building == 15 or building == 16:
            print("05. Located at last row.")
        if building == 3 or building == 4 or building == 13 or building == 14:
            print("05. Located at second last row.")
        if building == 5 or building == 6 or building == 11 or building == 12:
            print("05. Located at second row.")
        if building == 7 or building == 8 or building == 9 or building == 10:
            print("05. Located at first row.")

        if building % 2 == 1 and building != 15 and home <= 24:
            if home == 1 or home == 2 or home == 3 or home == 4 or home == 5 or home == 6 or home == 7 or home == 8 or home == 9 or home == 10 or home == 11 or home == 12:
                print("06. Use left stair.")
            if home == 13 or home == 14 or home == 15 or home == 16 or home == 17 or home == 18 or home == 19 or home == 20 or home == 21 or home == 22 or home == 23 or home == 24:
                print("06. Use right stair.")

            if home == 1 or home == 2 or home == 13 or home == 14:
                print("07. Go to the first floor")
            elif home == 3 or home == 4 or home == 15 or home == 16:
                print("07. Go to the second floor")
            elif home == 5 or home == 6 or home == 17 or home == 18:
                print("07. Go to the third floor")
            elif home == 7 or home == 8 or home == 19 or home == 20:
                print("07. Go to the fourth floor")
            elif home == 9 or home == 10 or home == 21 or home == 22:
                print("07. Go to the fifth floor")
            elif home == 11 or home == 12 or home == 23 or home == 24:
                print("07. Go to the sixth floor")

            if home == 1 or home == 3 or home == 5 or home == 7 or home == 9 or home == 11:
                print("08. Please knock to the left side door.")
            elif home == 2 or home == 4 or home == 6 or home == 8 or home == 10 or home == 12:
                print("08. Please knock to the right side door.")

            elif home == 13 or home == 15 or home == 17 or home == 19 or home == 21 or home == 23:
                print("08. Please knock to the left side door.")
            elif home == 14 or home == 16 or home == 18 or home == 20 or home == 22 or home == 24:
                print("08. Please knock to the right side door.")

        if building == 15:
            if home == 1 or home == 2 or home == 3 or home == 4 or home == 5 or home == 6 or home == 7 or home == 8 or home == 9 or home == 10 or home == 11 or home == 12:
                print("06. Use right stair.")
            if home == 13 or home == 14 or home == 15 or home == 16 or home == 17 or home == 18 or home == 19 or home == 20 or home == 21 or home == 22 or home == 23 or home == 24:
                print("06. Use middle stair.")
            if home == 25 or home == 26 or home == 27 or home == 28 or home == 29 or home == 30 or home == 31 or home == 32 or home == 33 or home == 34 or home == 35 or home == 36:
                print("06. Use left stair.")

            if home == 1 or home == 2 or home == 13 or home == 14 or home == 25 or home == 26:
                print("07. Go to the first floor")
            elif home == 3 or home == 4 or home == 15 or home == 16 or home == 27 or home == 28:
                print("07. Go to the second floor")
            elif home == 5 or home == 6 or home == 17 or home == 18 or home == 29 or home == 30:
                print("07. Go to the third floor")
            elif home == 7 or home == 8 or home == 19 or home == 20 or home == 31 or home == 32:
                print("07. Go to the fourth floor")
            elif home == 9 or home == 10 or home == 21 or home == 22 or home == 33 or home == 34:
                print("07. Go to the fifth floor")
            elif home == 11 or home == 12 or home == 23 or home == 24 or home == 35 or home == 36:
                print("07. Go to the sixth floor")

            if home == 1 or home == 3 or home == 5 or home == 7 or home == 9 or home == 11:
                print("08. Please knock to the left side door.")
            elif home == 2 or home == 4 or home == 6 or home == 8 or home == 10 or home == 12:
                print("08. Please knock to the right side door.")

            elif home == 13 or home == 15 or home == 17 or home == 19 or home == 21 or home == 23:
                print("08. Please knock to the left side door.")
            elif home == 14 or home == 16 or home == 18 or home == 20 or home == 22 or home == 24:
                print("08. Please knock to the right side door.")
            elif home == 25 or home == 27 or home == 29 or home == 31 or home == 33 or home == 35:
                print("08. Please knock to the left side door.")
            elif home == 26 or home == 28 or home == 30 or home == 32 or home == 34 or home == 36:
                print("08. Please knock to the right side door.")

        if building % 2 == 0 and home <= 12:
            print("06. Use the middle stair.")
            if home == 1 or home == 2:
                print("07. Go to the first floor")
            elif home == 3 or home == 4:
                print("07. Go to the second floor")
            elif home == 5 or home == 6:
                print("07. Go to the third floor")
            elif home == 7 or home == 8:
                print("07. Go to the fourth floor")
            elif home == 9 or home == 10:
                print("07. Go to the fifth floor")
            elif home == 11 or home == 12:
                print("07. Go to the sixth floor")

            if home == 1 or home == 3 or home == 5 or home == 7 or home == 9 or home == 11:
                print("08. Please knock to the left side door.")
            elif home == 2 or home == 4 or home == 6 or home == 8 or home == 10 or home == 12:
                print("08. Please knock to the right side door.")
