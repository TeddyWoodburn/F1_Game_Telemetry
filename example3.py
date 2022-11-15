# This example prints the tyre temperatures

from F1_2021_Telemetry.telemetry import currentState

while True:
    playerCarIndex = currentState.CarTelemetry.m_header.m_playerCarIndex

    if playerCarIndex is not None:
        print(currentState.CarTelemetry.m_carTelemetryData[playerCarIndex].m_tyresInnerTemperature)
