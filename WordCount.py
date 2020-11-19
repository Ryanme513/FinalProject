# essay = "Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"
def lettercount(essay):
    space = essay.count(" ")
    period = essay.count(".")
    comma = essay.count(",")
    questionmark = essay.count("?")
    exclamationmark = essay.count("!")
    y = len(essay) - space - period - comma - questionmark - exclamationmark
    return ("You have " +  str(y) + " letters in your text.") 
    
print(lettercount("Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"))

def wordcount(essay):
    x = len(essay.split()) 
    return("You have " +  str(x) + " words in your text.") 

print(wordcount("Enter the equation below and hit submit. If you need to fix your work, go back to the prior screen"))

