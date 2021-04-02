print ("hello, welcome to toronto triva!")
ans = input('are you ready to play (yes/no) : ')
score = 0
total_q=4
if ans.lower () == "yes":
    
    ans=input ("1# how manny runways does toronto have?")
    if ans.lower () == "5":
        score += 1
        print ("Correct")
    else:
        print("incorrect")

    ans=input ("2# what is the initial altitude on departure?")
    if ans.lower () == "5000":
        score += 1
        print ("Correct")
    else:
        print("Incorrect")

    ans=input ("3# do you turn on course after departure? ")
    if ans.lower () == "no" :
        score += 1
        print ("Correct")
    else: 
        print("Incorrect")

    ans=input ("#4 what is the circuit altitude?")
    if ans.lower () == "1500" :
        score += 1
        print ("correct")
    else:
        print("Incorrect")

print (" Thank you for playing, you got ",score,"questions correct." )
mark = (score/total_q) *100
print ("mark: ", str(mark) + "%" )
print("Goodbye")