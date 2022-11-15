# F1 Game Telemetry
A python package to parse telemetry data from the F1 game into python objects. Currently works for F1 2021.

## Enabling UDP Telemetry in the game
In the F1 game navigate to Telemetry Settings and set the following values:
  - UDP Telemetry: On
  - UDP IP Address: 127.0.0.1
  - UDP Port: 20777
  - UDP Send Rate: Higher is better
  - UDP Format: 2021
  
 ## Installing the package
 Install with pip: `pip install F1-2021-Telemetry`
 
 ## Using the package
 Import the currentState object: `from F1_2021_Telemetry.telemetry import currentState`
 This is continually updated while the game is running.
 
