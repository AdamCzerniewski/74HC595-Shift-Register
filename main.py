#!/usrcoding: utf-8 -*-
"""/bin/env python3
# -*- 
Created on Sat Jan 20 13:27:08 2024

@author: Adam Czerniewski
"""
import sys
import spidev
import time
from ui import Ui_MainWindow
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw 
from PyQt5.QtWidgets import QMessageBox



class Main(qtw.QMainWindow):
    
    def __init__(self):
        
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print ("show GUI")
        
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = 7629
        
        self.ui.btn_shiftRegEnter.clicked.connect(self.shiftRegVal)
        self.ui.btn_enterLEDnum.clicked.connect(self.LEDnum)
        
        self.ui.label_Q0.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q1.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q2.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q3.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q4.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q5.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q6.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q7.setStyleSheet("background-color: darkgrey")

        
    # Sends SPI data (to the 74HC595)
    def spiWrite(self, OutValue):
   
        spiValue = self.spi.xfer([0, OutValue])
        
        return spiValue
    
    # set bit to 1
    def set_bit(self, RegValue, bitNum):
        print ('RegValue=',RegValue, ' bitNum=',bitNum)
        return RegValue | (1<<bitNum)
    
    
    # set bit to 0
    def clear_bit(self, RegValue, bitNum):
        return RegValue & ~(1<<bitNum)
        
    
    # Takes user input and sends to the spiWrite() function, which then turns on the LED(s)
    def shiftRegVal(self):
        registerValue = self.ui.tf_shiftRegVal.text(); registerValue = int(registerValue)
        shiftValue = self.ui.tf_regShiftVal.text()

        
        print("Value =", registerValue)
               # Checks if the user put in a value for the shift (which can't be left blank to represent 0 due to issues)
        try:
            shiftValue = int(shiftValue)
        except ValueError:
            QMessageBox.warning(None, "Value Error", "Please Enter a Number (Ex. 0)", QMessageBox.Ok)
        
        
        # Shifts the bits to the left
        if self.ui.rbtn_regLeftShift.isChecked() == True:
            
            # If the shift value is 0, registerValue will not be shifted
            if shiftValue == 0:
                
                # Divide the data by 2 to shift the bits to the left
                for i in range (0, shiftValue):
                    registerValue /= 2
                
                # Send the data to spiWrite()
                self.spiWrite(int(registerValue))
                print("sent")
        
                # Converts the data to the "LED numbering" format for the user
                self.convertRegVal_LEDnum(int(registerValue))                
                
                # Displays the LEDs that are on
                self.LEDstate(int(registerValue))                           
            
            else:
            
                # Divide the data by 2 to shift the bits to the left
                for i in range (0, shiftValue):
                    registerValue /= 2
                
                # Send the data to spiWrite()
                self.spiWrite(int(registerValue))
                print("sent")
        
                # Converts the data to the "LED numbering" format for the user
                self.convertRegVal_LEDnum(int(registerValue))                
                
                # Displays the LEDs that are on
                self.LEDstate(int(registerValue))       

        
        # Shifts the bits to the right
        elif self.ui.rbtn_regRightShift.isChecked():
            
            # If the shift value is 0, registerValue will not be shifted
            if shiftValue == 0:
                
                # Multiply the data by 2 to shift the bits to the right
                for i in range (0, shiftValue):
                    registerValue *= 2
                 
                # Send the data to spiWrite()
                self.spiWrite(int(registerValue))
                print("sent")
        
                # Converts the data to the "LED numbering" format for the user
                self.convertRegVal_LEDnum(int(registerValue))                    
                 
                # Displays the LEDs that are on
                self.LEDstate(int(registerValue))       
            
            else:            
            
                # Multiply the data by 2 to shift the bits to the right
                for i in range (0, shiftValue):
                    registerValue *= 2

                # Send the data to spiWrite()
                self.spiWrite(int(registerValue))
                print("sent")
        
                # Converts the data to the "LED numbering" format for the user
                self.convertRegVal_LEDnum(int(registerValue))
                
                # Displays the LEDs that are on
                self.LEDstate(int(registerValue))                           
     
    
    
    # Takes user input, converts into readable data, and sends to the spiWrite() function to turn on the LED(s)
    def LEDnum(self):
        self.ui.label_Q0.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q1.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q2.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q3.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q4.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q5.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q6.setStyleSheet("background-color: darkgrey")
        self.ui.label_Q7.setStyleSheet("background-color: darkgrey")   
     
        # Takes the LED number(s) and converts to usable data
        led = self.ui.tf_LEDnum.text()
        led = led.split(",")
        led = [int(digit) for digit in led]
        
        shiftValue = self.ui.tf_LEDshiftVal.text()
        
        # Checks if the user put in a value for the shift (which can't be left blank to represent 0 due to issues)
        try:
            shiftValue = int(shiftValue)
        except ValueError:
            QMessageBox.warning(None, "Value Error", "Please Enter a Number (Ex. 0)", QMessageBox.Ok)
        
        print("LED =", led)
        
        # This array will be the LEDs that are displayed as on in the GUI
        ledShifted = []
        
        regValue = 0
        
        # Shifts the LEDs on display to the left
        if self.ui.rbtn_LEDleftShift.isChecked() == True:
            
            # If the shift value is 0, the ledNum variable will not be decremented
            if shiftValue == 0:
                for i in range (0, len(led)):
                    ledNum = led[i]
                    ledNum = int(ledNum)
                    ledShifted.append(ledNum)
                    print("Led shift", ledShifted)
            else:
            
                # If the shift value is NOT 0, the ledNum variable WILL be decremented    
                for i in range (0, len(led)):
                    ledNum = led[i]
                    ledNum = int(ledNum)
                    ledNum -= 1
                    ledShifted.append(ledNum)
                    print("Led shift", ledShifted)
                    
        # Shifts the LEDs on display to the right
        elif self.ui.rbtn_LEDrightShift.isChecked() == True:
            
            # If the shift value is 0, the ledNum variable will not be incremented          
            if shiftValue == 0:
                for i in range (0, len(led)):                    
                    ledNum = led[i]
                    ledNum = int(ledNum)
                    ledShifted.append(ledNum)
                    print("Led shift", ledShifted)                
            else:   

                # If the shift value is NOT 0, the ledNum variable WILL be incremented    
                for i in range (0, len(led)):
                    ledNum = led[i]
                    ledNum = int(ledNum)
                    ledNum += 1
                    ledShifted.append(ledNum)
                    print("Led shift", ledShifted)  
                
        # Turns on the LEDs in the display
        for i in range(0,len(ledShifted)):
            regValue = self.set_bit(regValue, ledShifted[i])           
            
            print("LED Q[", led[i],"=] 1")
            
            # Goes through each value in the LED array and sets the color to green in the GUI
            ledColor = getattr(self.ui,f"label_Q{ledShifted[i]}")         
            ledColor.setStyleSheet("background-color: lightgreen")
        
            self.ui.tf_shiftRegVal.setText(str(regValue))  # Update the shift register value input field
        

    # Converts the shift register value to the LED numbers 
    def convertRegVal_LEDnum(self, binValue):
        # the binValue variable is converted to binary, adds on 0s till there are 8 digits, and flips the value from end to end (Ex. from 10100000 to 00000101)
        stateOfLED = bin(binValue)[2:].zfill(8)[::-1]
        
        LEDarray = list(stateOfLED)
        LEDarray = [int(digit) for digit in LEDarray]
        print(LEDarray)
        
        self.ui.tf_LEDnum.setText('')
        
        # Goes through each value in LEDarray and updates the LED input field
        for i in range(0,len(LEDarray)):
            
            status = LEDarray[i]
            print("LED Q[", i,"=]",status)
            
            ledStatus = status
            
            # Updates LEDnum if the status of the LED is on and the LED input field is empty
            if ledStatus == 1 and self.ui.tf_LEDnum.text() == '':
                self.ui.tf_LEDnum.setText(str(i))
            
            # Appends data to LEDnum if the status of the LED is on and the LED input field is NOT empty            
            elif ledStatus == 1 and self.ui.tf_LEDnum.text() != '':
                text = self.ui.tf_LEDnum.text()
                text += ',' + str(i)
                self.ui.tf_LEDnum.setText(text)

    # Colors in each box representing the LED number depending on its state
    def LEDstate(self,val):

        stateOfLED = bin(val)[2:].zfill(8)[::-1]
        LEDarray = list(stateOfLED)
        LEDarray = [int(digit) for digit in LEDarray]
        print(LEDarray)       
        
        for i in range(0,len(LEDarray)):
            
            status = LEDarray[i]
            print("LED Q[", i,"=]",status)
            
            Qx = status
            ledColor = getattr(self.ui,f"label_Q{i}")         
            if Qx == 1:
                ledColor.setStyleSheet("background-color: lightgreen")
            else:
                ledColor.setStyleSheet("background-color: darkgrey")
        

if __name__ == "__main__":
    app = qtw.QApplication([])
    
    widget = Main()
    widget.show()
    
    app.exec()
