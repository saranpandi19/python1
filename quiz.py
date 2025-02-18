player = input('do you want to play?')

if player.lower() != 'yes':
    quit()
print ('okk lets play')
score=0  

question = input('1.How many days do we have in a week?')

if question.lower() == "seven":
    print("correct")
    score += 1  #score = score + 1

else:
    print("incorrect")

question = input('2.Which animal is known as the "King of the Jungle"?')

if question.lower() == "lion":
    print("correct")
    score += 1
else:
    print("incorrect")

question = input('3.What is the capital of India??')

if question.lower() == "delhi":
    print("correct")
    score += 1
else:
    print("incorrect")

print("your score"+ str(score))