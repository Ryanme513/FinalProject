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


