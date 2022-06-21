from tkinter import messagebox, simpledialog, Tk

   # Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
     # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero.
    score = 0

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring(title='Question 1', prompt="Whats 1 + 1")
    #      // 3.  Use an if statement to check if their answer is correct

    if answer=="2":
        score+=1

    else:
        score-=1

#      // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer1 = simpledialog.askstring(title='Question 2', prompt="Whats the capital of the US")
    if answer1=="Washington D.C.":
        score+=1

    else:
        score-=1

    answer2 = simpledialog.askstring(title='Question 3', prompt="What's the best fast food place in the world?")
    if answer2=="McDonalds":
        score+=1

    else:
        score-=1

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print(score)
# Run the window's .mainloop() method
window.mainloop()
