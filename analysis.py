import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

df = pd.read_csv('physdata.csv') 
voltage = df.Voltage_v.values 
bulb_current = df.Current_Bulb_A.values 
resistor_current = df.Current_Resistor_A.values 

fit1 = np.polyfit(bulb_current, voltage, 1)     #Bulb
plt.plot(bulb_current, fit1[1] + fit1[0]*bulb_current, color='red')
plt.scatter(bulb_current, voltage, color = 'orange')
plt.xlabel('Current (Amperes)')
plt.ylabel('Voltage')
plt.title('Bulb')
plt.show()

fit2 = np.polyfit(resistor_current, voltage, 1)     #Resistor
plt.plot(resistor_current, fit2[1] + fit2[0]*resistor_current, color='blue')
plt.scatter(resistor_current, voltage, color='green')
plt.xlabel('Current (Amperes)')
plt.ylabel('Voltage')
plt.title('Resistor')
plt.show()

measured_bulb_resistance = 3.5 
measured_resistor_resistance = 99.1 
bulb_error = (measured_bulb_resistance - fit1[0])/measured_bulb_resistance*100
resistor_error = (measured_resistor_resistance - fit2[0])/measured_resistor_resistance*100

print("Bulb percent error: ", bulb_error, '%')
print("Resistor percent error: ", resistor_error, '%') 

