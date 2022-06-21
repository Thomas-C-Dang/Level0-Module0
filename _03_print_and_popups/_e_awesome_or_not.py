from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    random.randint(0,3)
    # 2. Print your variable to the console
    print(random)
    # 3. Get the user to enter something that they think is awesome
    name = simpledialog.askstring(title='Greetings!', prompt="Enter what you think is awesome!")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if name=="0":
        messagebox.showinfo(title='AWESOME!', message="You are definitely getting girlfriends")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if name=="1":
        messagebox.showinfo(title='Eh', message="You have a bright future ahead don't worry")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if name=="2":
        messagebox.showinfo(title='Mmmmmm', message="You could have some improvements")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if name=="3":
        messagebox.showinfo(title='LOL', message="YOU JUST GOT TROLLED")
    # Run the window's .mainloop() method
    window.mainloop()
