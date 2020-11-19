# essay = "Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"
def lettercount(essay):
    letters = essay.count(" ")
    y = len(essay) - letters
    return ("You have " +  str(y) + " letters in your text.") 
    
print(lettercount("Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"))

def wordcount(essay):
    x = len(essay.split()) 
    return("You have " +  str(x) + " words in your text.") 

print(wordcount("Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"))





import turtle


def U():
    print(turtle.pos()[0])
    x = turtle.pos()[0]
    y = turtle.pos()[1]
    turtle.write(wordcount("Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"), font = style)
    turtle.penup()
    turtle.setpos(x + 23, y)
    turtle.pendown()
