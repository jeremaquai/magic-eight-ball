while True:
    import random


    name = ""
    question = ""
    answer = ""
    random_number = random.randint(1, 12)


    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidely so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "reply too confusing, Ask again later"
    elif random_number ==11:
        answer = "Quite spactactully, yes"
    elif random_number == 12:
        answer = "Chances don't look good"
    else:
        answer = "Error"



    
    print("Welcome to the Magic 8-Ball")

    name = input("What is your name? ")
    question = input("what is your question? ")

    if name == "exit":
        exit()
    if name == "":
        print ("Question: " + question)
        print (name + " asks: " + question)

    if question == "":
        print("The Magic 8-Ball is no Fool, " + name + ", you didn't ask a question")
    else:
        print ("Magic 8-ball's answer: " + answer)