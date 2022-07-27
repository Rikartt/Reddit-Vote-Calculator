#credit for the formulas goes to u/Gulliveig. Post link: https://www.reddit.com/r/TheoryOfReddit/comments/k6hi36/ever_wondered_how_many_upvotes_and_downvotes_a/
import os
clear = lambda: os.system('cls')
def calculatevotes(karma, ratio, *whatyouwant):#karma is an integer, ratio is given in the form of a decimal number
    K = karma
    P = ratio
    i = P/(1-P) #intermediate
    d = K/(i-1) #downvotes
    u = d*i #upvotes
    wyw = list(x.lower() for x in whatyouwant) #what outputs you want, list
    if 'along' in wyw:
        a = {'intermediate': i, 'downvotes': d, 'upvotes': u}
    elif 'a' in wyw or len(wyw) == 0:
        a = {'i': i, 'd': d, 'u': u} #returns a dictionary of i (intermediate), d (downvotes), and u (upvotes)
    if 'i' in wyw:
        return i ##return intermediate
    elif 'd' in wyw:
        return d ##Return total downvotes
    elif 'u' in wyw:
        return u ##Return total upvotes
    if 'a' in wyw:
        return a
print("Warning!: If you input that your percentage of upvotes is 50, the program will not work.")
start = True
while start:
    maindict = calculatevotes(int(input("Post Karma: ")), int(input("Percentage of Upvotes: "))/100, 'a')
    print(
        "Your post has:\n",
        round(maindict['u']), "upvotes\n", 
        round(maindict['d']), "downvotes\n")
    input("Press Enter To Clear")
    clear()