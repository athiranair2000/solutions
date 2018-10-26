import random
moves=["rock","paper","scissors"]
keep_playing="true"
while keep_playing=="true":
    cmove=random.choice(moves)
    pmove=input("what is your move:rock,paper,scissors?")
    print("the computer chose",cmove)
    if cmove==pmove:
        print("tie")
    elif cmove=="rock":
     if (pmove=="paper"):
            print("you won","player covers computer")
     else:
            print("you loss","computer hits player")
    elif cmove=="paper":
      if(pmove=="rock"):
            print("you loss","computer covers player")
      else:
             print("you won","player smashes computer")
    elif cmove=="scissors":
       if(pmove=="rock"):
             print("you won","player hits computer")
       else:
             print("you loss","computer smashes player")
else:print("invalid usage")
keep_playing="true"
moves=["rock","paper","scissors"]
