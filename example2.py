# This example check for the startlights event and prints out a representation of them

from F1_2021_Telemetry.telemetry import currentState

# defs contains the possible values of every object which isn't just a number
# in this example we use the defs.EventStringCodes.LIGHTS_OUT value
# check the defs.py file for all the defined values
from F1_2021_Telemetry import defs


previousLightsNum = -1

while True:
    # Wait until there is at least one startlights event 
    if len(currentState.Events.StartLights) == 0:
        continue

    # The number of lights displayed, index -1 is used to get the most recent startlights event
    numLights = currentState.Events.StartLights[-1].m_eventDetails.numLights

    # This generates a list of all the types of simpleEvents 
    # currentState.SimpleEvents is a list of packets.PacketSimpleEvent
    simpleEventsList = [currentState.SimpleEvents[i].m_eventStringCode for i in range(len(currentState.SimpleEvents))]

    # Check if there is a lights out event in our simpleEventList
    if defs.EventStringCodes.LIGHTS_OUT in simpleEventsList:
        print("Lights out!")
        break
    
    # Update the number of lights showing if it has changed
    if numLights != previousLightsNum:
        print("O" * numLights)
        previousLightsNum = numLights

