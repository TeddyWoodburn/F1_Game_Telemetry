# This example prints a list of the buttons currently being held down

from F1_2021_Telemetry.telemetry import currentState

# First, wait until a button event is received
while len(currentState.Events.Buttons) == 0:
    pass


while True:
    # Set currentButtons to a list of the buttons currently being held down
    # Note: the type of each item in this list is defs.Buttons
    # The index -1 is used because the most recent events are at the end of the list
    currentButtons = currentState.Events.Buttons[-1].m_eventDetails.m_selectedButtons

    # Convert each item from type defs.Buttons to a friendly string using str()
    currentButtonStrings = [str(button) for button in currentButtons]

    print(currentButtonStrings)
