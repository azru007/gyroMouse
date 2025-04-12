
import serial
import pyautogui

# Replace with your PC's Bluetooth COM port
PORT = 'COM6'
BAUD = 9600

ser = serial.Serial(PORT, BAUD)
print("Connected to Bluetooth device")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if ',' in line:
            x, y = map(float, line.split(','))
            pyautogui.moveRel(x * 10, -y * 10)  # Adjust multiplier as needed
    except Exception as e:
        print("Error:", e)
