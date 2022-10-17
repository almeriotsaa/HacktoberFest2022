import turtle

# Make a turtle project with formulas, variable and function

# Variables for angles
half_serogka = 22.5
serong_kanan = 45.0
go_right = 90.0
sharp_right = go_right + half_serogka


# Welcome
def welcome():
    print("""
        1 for hexagon
        2 for pentagon
        3 for rectangle
    """)
    inp = input("Choose shape : ")
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    if inp == "1":
        draw_hexagon(my_turtle)
    elif inp == "2":
        draw_pentagon(my_turtle)
    elif inp == "3":
        draw_rectangle(my_turtle)
    else:
        print("Bye then!")


# Hexagon (6)
def draw_hexagon(my_turtle):
    my_size = float(input("Input amount of forward : "))
    i = 1
    while i <= 6:
        my_turtle.forward(my_size)
        my_turtle.right(serong_kanan + 15.0)
        my_turtle.forward(my_size)
        i += 1
    isDone = input("Done? (Boolean) : ")
    if isDone == "True" or isDone == "true":
        print("Bye!")
    else:
        turtl = turtle.Turtle()
        draw_hexagon(turtl)


# Pentagon (5)
def draw_pentagon(my_turtle):
    my_size = float(input("Input amount of forward : "))
    in_size = my_size + 20
    i = 1
    my_turtle.right(half_serogka)
    # \
    my_turtle.forward(in_size)
    my_turtle.right(sharp_right)
    # /
    my_turtle.forward(my_size)
    my_turtle.right(serong_kanan)
    # _
    my_turtle.forward(my_size)
    my_turtle.right(serong_kanan)
    # \
    my_turtle.forward(my_size)
    my_turtle.right(sharp_right)
    # /
    my_turtle.forward(in_size)
    isDone = input("Done? (Boolean) : ")
    if isDone == "True" or isDone == "true":
        print("Bye!")
    else:
        turtl = turtle.Turtle()
        draw_pentagon(turtl)


# rectangle (4)
def draw_rectangle(my_turtle):
    my_size = float(input("Input amount of forward : "))
    i = 1
    while i <= 4:
        my_turtle.right(go_right)
        my_turtle.forward(my_size)
        i += 1
    isDone = input("Done? (Boolean) : ")
    if isDone == "True" or isDone == "true":
        print("Bye!")
    else:
        turtl = turtle.Turtle()
        draw_rectangle(turtl)


if __name__ == "__main__":
    welcome()
