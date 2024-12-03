NumPlayers = int(input("Enter the number of players playing this round: "))
while NumPlayers < 2 or NumPlayers > 4:
    print("Enter a number between 2 and 4 inclusive.")
    NumPlayers = int(input("Enter the number of players playing this round: "))

CoursePar = int(input("Enter the par for this course: "))
CourseHoles = int(input("Enter the number of holes in this course: "))
while CourseHoles != 9 and CourseHoles != 18:
    print("The number of holes in a course can only be 9 or 18. Please enter a appropriate number")
    CourseHoles = int(input("Enter the number of holes in this course: "))
Name = [None] * NumPlayers
for i in range(0, NumPlayers):
    Name[i] = input("Enter your name: ")

print("The number of players playing in this round are: ", NumPlayers)
print("The par for this course is: ", CoursePar)
print("The number of holes in this course is: ", CourseHoles)
for j in range(0, NumPlayers):
    print("The names of the players playing in this round are: ", Name[j])

print("Is this the information you entered? Enter 1 for yes and 2 for no: ")
Choice = int(input("Enter your choice: "))
while Choice != 1 and Choice != 2:
    print("Enter an appropriate number. 1 for yes and 2 for no: ")
if Choice == 1:
    print("Okay, good. The round will start now. ")
elif Choice == 2:
    print("Enter the information again: ")
    NumPlayers = int(input("Enter the number of players playing this round: "))
    while NumPlayers < 2 or NumPlayers > 4:
        print("Enter a number between 2 and 4 inclusive.")
        NumPlayers = int(input("Enter the number of players playing this round: "))

    CoursePar = int(input("Enter the par for this course: "))
    CourseHoles = int(input(" Enter the number of holes in this course: "))
    while CourseHoles != 9 and CourseHoles != 18:
        print("The number of holes in a course can only be 9 or 18. Please enter a appropriate number")
        CourseHoles = int(input("Enter the number of holes in this course: "))
    Name = [None] * NumPlayers
    for i in range(0, NumPlayers):
        Name[i] = input("Enter your name: ")
    print("The round will start now. ")

ScoreArray = []
Score1 = [0] * CourseHoles
Score2 = [0] * CourseHoles

TotalScore = [0] * NumPlayers

for y in range(0, NumPlayers):
    print("Enter the scores for ", Name[y])
    for x in range(0, CourseHoles):
        Score1[x] = int(input(f"Enter the score for {Name[y]} for hole number: {x + 1} : "))
        Score2[x] = int(input(f"Re-enter the score for {Name[y]} for hole number: {x + 1} : "))

        while Score1 != Score2:
            print("The scores are not the same. Re-enter the score. ")
            Score1[x] = int(input(f"Enter the score for {Name[y]} for hole number: {x + 1} : "))
            Score2[x] = int(input(f"Re-enter the score for {Name[y]} for hole number: {x + 1} : "))

        TotalScore[y] = TotalScore[y] + Score1[x]
        print("Would you like to see your score uptil now?")
        Choice2 = int(input("Enter your choice. 1 for yes and 2 for no: "))
        while Choice2 != 1 and Choice2 != 2:
            print("Enter an appropriate number. 1 for yes and 2 for no: ")
            Choice2 = int(input("Enter your choice. 1 for yes and 2 for no: "))
        if Choice2 == 1:
            print("Your score is: ", TotalScore[y])
        elif Choice2 == 2:
            print("The round will continue now.")
    ScoreArray.append(Score1.copy())
for z in range(0, NumPlayers):
    print("The total score for ", Name[z], " is: ", TotalScore[z])

CourseParDiff = [0] * NumPlayers
print("The round has ended now. These are the results: ")
for w in range(0, NumPlayers):
    CourseParDiff[w] = TotalScore[w] - CoursePar
    if CourseParDiff[w] >= 0:
        print("Player ", Name[w], " achieved the score of ", TotalScore[w], " by being ", CourseParDiff[w],
              " above the par.")
    elif CourseParDiff[w] < 0:
        print("Player ", Name[w], " achieved the score of ", TotalScore[w], " by being ", CourseParDiff[w],
              " below the par.")

    Lowest = 1000
    if TotalScore[w] < Lowest:
        Lowest = TotalScore[w]
        WinnerName = Name[w]
print("The winner of the round is ", WinnerName, "with the score of: ", Lowest)

import mysql.connector as sql
mycon = sql.connect(host="Localhost", user="root", password="Aniket@1234", database="gulf_db")
if mycon.is_connected()== False:
    print("Error connecting to MySQL database")
cursor = mycon.cursor()
for o in range(0, len(ScoreArray)):
    ls = ScoreArray[o]
    for t in range(0, len(ls)):
        st = "insert into scores(Name, hole_number, score) values('{}', {}, {})".format(Name[o], t+1, ls)
    cursor.execute(st)
mycon.commit()
cursor.close()
mycon.close()

x = True
while x == True:
    print(
        "These are the options that you can use: 1: Every player’s score for each hole. 2: The player’s name and hole number of any score of one for a hole (hole-in-one). 3: The average score for the round. 4: The average score for each hole.")
    Choice3 = int(input("Enter your choice. 1, 2, 3 or 4?"))
    if Choice3 == 1:
        for v in range(0, CourseHoles):
            print("These are the scores for hole number: ", v + 1)
            for u in range(0, NumPlayers):
                print("These are the scores for ", Name[u], ": ", ScoreArray[u][v])
    elif Choice3 == 2:
        H1Flag = False
        for g in range(0, NumPlayers):
            for h in range(0, CourseHoles):
                H1 = 0
                if ScoreArray[g][h] == 1:
                    H1 = ScoreArray[g][h]
                    H1Name = Name[g]
                    H1HoleNumber = h + 1
                    print("The player who scored a hole-in-one is: ", H1Name, "at hole number: ", H1HoleNumber)
                    H1Flag = True
        if H1Flag == False:
            print("Nobody scored a hole-in-one.")
    elif Choice3 == 3:
        TotalTotalScore = sum(TotalScore)
        AverageTotalScore = TotalTotalScore / NumPlayers
        print("The average score for the whole round is: ", AverageTotalScore)

    elif Choice3 == 4:
        TotalHoleScore = [0] * CourseHoles
        AverageHoleScore = [0.0] * CourseHoles
        for i in range(0, CourseHoles):
            for j in range(0, NumPlayers):
                TotalHoleScore[i] = TotalHoleScore[i] + ScoreArray[j][i]
            AverageHoleScore[i] = TotalHoleScore[i] / NumPlayers
            print("The average score for hole number: ", i + 1, "is: ", AverageHoleScore[i])
    Choice4 = int(input("Do you want to use more options? Enter 1 for yes and 2 for no: "))
    if Choice4 == 1:
        x = True
    elif Choice4 == 2:
        x = False
        break