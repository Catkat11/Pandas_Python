import turtle  # Importing the Turtle module for creating the game interface
import pandas  # Importing Pandas for reading data from a CSV file

screen = turtle.Screen()  # Creating a screen object
screen.title("U.S. States Game")  # Setting the title for the game
image = "blank_states_img.gif"  # Image file for the U.S. map
screen.addshape(image)  # Adding the image as a shape to the screen

turtle.shape(image)  # Setting the shape of the turtle to the U.S. map image

data = pandas.read_csv("50_states.csv")  # Reading data from a CSV file containing U.S. states info
all_states = data.state.to_list()  # Creating a list of all U.S. states
guessed_states = []  # List to store correctly guessed states

# Main loop for the game
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer = answer_state.title()  # Converting the user input to title case

    if answer == "Exit":  # Checking if the user wants to exit the game
        missing_states = [state for state in all_states if state not in guessed_states]  # Finding states not guessed
        new_data = pandas.DataFrame(missing_states)  # Creating a new DataFrame with missing states
        new_data.to_csv("states_to_learn.csv")  # Saving missing states to a new CSV file
        break  # Exiting the loop if the user chooses to exit

    if answer in all_states:  # Checking if the guessed state is in the list of all states
        guessed_states.append(answer)  # Adding the guessed state to the list of correctly guessed states
        t = turtle.Turtle()  # Creating a turtle object
        t.hideturtle()  # Hiding the turtle icon
        t.penup()  # Lifting the pen to avoid drawing lines
        state_data = data[data.state == answer]  # Getting data for the guessed state
        t.goto(int(state_data.x), int(state_data.y))  # Moving the turtle to the location of the guessed state
        t.write(answer)  # Writing the name of the guessed state on the map
