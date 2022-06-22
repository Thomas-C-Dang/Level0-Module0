from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    answer = simpledialog.askinteger(title='Guess!', prompt="1-100")


    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        print(random_num)
        if answer == random_num:
            exit()
        if answer > random_num:
            answer = simpledialog.askinteger(title='Too high!', prompt="Too high")
        if answer < random_num:
            answer = simpledialog.askinteger(title='Too low!', prompt="Too low")

    messagebox.showinfo(title='Defeat', message="Lmao you lost")
    window.mainloop()
        # 4. Ask the user for a guess using a pop-up window, and save their response


        # 5. If the guess is correct

            # 6. Win. Use 'sys.exit(0)' to end the program

        # 7. if the guess is high
    #if answer > random_num:
       #messagebox.showinfo(title='Too high!', message="Too high")
    #else:
        #messagebox.showinfo(itle='Too low!', message="Too low")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

