What the project does:
- Takes user input in two ways (a base 10 representation of a binary value, or the LED's number(s))
- Raspberry Pi communicates to the Shift Register via SPI communication
- Turns on desired LEDs for the user
- Displays the status of the LEDs on the GUI

What it uses:
- Requires a 74HC595 Shift Register IC
- 8 LEDs to simulate the bits 
- 1 LED to indicate if the circuit is powered (optional)
- 4 pins connecting the Shift Register to the Raspberry Pi for SPI communication

Connections:
- Raspberry Pi SPI Connections
<img src="https://github.com/AdamCzerniewski/74HC595-Shift-Register/blob/main/PinoutRPI.png" width="400">
- Shift Register SPI Connections
<img src="https://github.com/AdamCzerniewski/74HC595-Shift-Register/blob/main/ShiftRegCircuitPinout1.png" width="400">
- Shift Register VCC and GND
<img src="https://github.com/AdamCzerniewski/74HC595-Shift-Register/blob/main/ShiftRegCircuitPinout2.png" width="400">

HOW to use this:
There are 4 inputs in the 'Shift Register Input' groupbox
- In the "Value" input, the minimum is 0, and the max is 255
- 0 turns off all LEDs, and 255 turns on all LEDs
- Anything in between that range will turn on different LEDs 

- The direction shift choice is for the shift direction you'd like
- The "Shift #:" input is for how much you would like to shift the binary value
- Lastly, press the Enter button, and the results should appear

There are 5 inputs the 'LED Number Input' groupbox; The "LED #:", shift direction, shift value, "Turn Off All", and "Enter" 
- The LEDs are numbered 0 to 7 from left to right
- You can put one, or multiple LED numbers into the "LED #:" input (ex. "0", "2", "3", or "0,2", "0,3", "2,3") without including the quotation marks
- The direction shift choice is for the shift direction you'd like
- The "Shift #:" input is for how much you would like to shift the binary value
- The "Turn Off All" button is to set the status to off for ALL LEDs
- Lastly, press the Enter button, and the results should appear
