import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Leonardo = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Leonardo.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Leonardo.speed(5)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Leonardo.color('green')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
   # Leonardo.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    #Leonardo.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    #for i in range(3):
    #    Leonardo.forward(100)
    #    Leonardo.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
   # Leonardo.goto(6,90)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    #Leonardo.begin_fill()
    #Leonardo.circle(radius=30, steps=30)
    #Leonardo.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below


    # Draw 3 more shapes with different fill colors!

    Leonardo.begin_fill()
    Leonardo.circle(radius=30, steps=30)
    Leonardo.end_fill()

    Leonardo.color('blue')
    Leonardo.begin_fill()
    for i in range(3):
        Leonardo.forward(100)
        Leonardo.left(90)
    Leonardo.end_fill()

    Leonardo.color('red')
    Leonardo.begin_fill()
    for i in range(3):
        Leonardo.left(60)
        Leonardo.forward(100)
    Leonardo.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
