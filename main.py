from turtle import Turtle, Screen
import random


def turtle_race():
    screen = Screen()
    screen.title("Turtle Race!")

    screen_width = 500
    screen_height = 400
    screen.setup(width=screen_width, height=screen_height)

    turtle_names: list = [
        "leonardo",
        "donatello",
        "michelangelo",
        "raphael",
        "striker"
    ]

    user_guess = ""
    while user_guess not in turtle_names:
        user_guess = screen.textinput(title="Guess the winner!",
                                      prompt="Who do you think will win? leonardo, donatello, michelangelo, raphael or striker?")

    turtle_colors: list = [
        "blue",
        "purple",
        "orange",
        "red",
        "grey"
    ]

    turtle_y_offset = -100
    turtle_x_offset = -240
    max_distance = 51
    turtle_info: dict = {}

    for n, turtle in enumerate(turtle_names):
        turtle_info[turtle] = Turtle(shape="turtle", visible=False)
        turtle_info[turtle].color(turtle_colors[n])
        turtle_info[turtle].penup()
        turtle_info[turtle].sety(turtle_y_offset)
        turtle_info[turtle].setx(turtle_x_offset)
        turtle_info[turtle].showturtle()
        turtle_y_offset += 50

    # pick a random turtle from our dictionary and move
    # it by a random distance between 0 and 50
    racing: bool = True

    while racing:
        random_turtle = random.choice(turtle_names)
        random_distance = random.randint(0, max_distance)
        turtle_info[random_turtle].forward(random_distance)
        # subtracting 20 from our screen width as a turtle has a size of 40*40
        racing = turtle_info[random_turtle].xcor() <= (screen_width/2) - 20

    if user_guess == random_turtle:
        print(
            f"Congratulations! You were right, {random_turtle} has won indeed!")
    else:
        print(
            f"Too bad. {user_guess} was your guess, but {random_turtle} has won.")


if __name__ == "__main__":
    turtle_race()
