# ALGORITHM
# define score variable to zero
# Ask user series of questions and get their inputed replies
# if answer is correct, add + 10 to the score 
# else skip to the next.
# after all questions have been answered display the score


score = 0

user_name = input("Please enter your player name: ")

question1 = print("What is the capital of Nigeria? ")
user_answer = input("")
if user_answer == "Abuja":
    print("Correct")
    score += 10
else:
    print("wrong, the answe is Abuja.")
    score -= 5

question2 = print("who is the richest man in the world currently?  ")
user_answer = input("")
if user_answer == "Elon Musk":
    print("correct")
    score += 10
else : 
    print("Wrong answer, Elon Musk")
    score -= 5


question3 = print("Is web3 de-centralized?")
user_answer = input("")
if user_answer == "yes" :
    print("correct")
    score += 10
else :
    print("Wrong answer, yes")
    score -= 5

question4 = print("which company made react js ?")
user_answer = input("")
if user_answer == "Facebook" :
    print("correct")
    score += 10
else : 
    print("Wrong answer, it is facebook")
    score -= 5

question5 = print("Who made this game? ")
user_answer = input("")
if user_answer == "Sam" : 
    print("Correct answer")
    score += 10
else: 
    print("wrong, answer.., Sam")
    score -= 5

print("you passed 55% of players! ", user_name)
print("Your total score is ", score)