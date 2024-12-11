# This program will get the students score and display the grade for the score
 
# 70-100 = A
# 60-69 = B
# 50-59 = C
# 40-49 = D
# 0-39 = F
# invalid score

# Algorithm
# Get the student score
# check if  whats inputed passes the conditions
# display the grade for the score

user_score = input("Please enter student score : ")
score = int(user_score)

if (score >=70 ) and (score <=100) : 
    print("A")
elif (score >= 60) and (score ) :
    print("B")
elif (score >= 50) and (score <= 59) :
    print("C")
elif (score >= 40) and (score <= 49) :
    print("D")
elif (score >= 0) and (score <= 39) :
    print("F")
else:
    print("Invalid score")