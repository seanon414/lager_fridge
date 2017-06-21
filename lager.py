import os
import time
from thermometer import read_temp

# os.system('/var/www/rfoutlet/codesend 1054003')
# time.sleep(5)
# os.system('/var/www/rfoutlet/codesend 1054012')
os.system('echo lights on')
time.sleep(1)
os.system('echo fuck it, lights off')

# Store these in sqllite
target_temp = 70
# fridge_on = 'Y'/'N'

def should_turn_off_fridge():
    """Checks if fridge temp is below target temp"""
    temp_data = read_temp()[1]
    # Uncomment following line to test low temp
    # temp_data = 68
    print temp_data
    return temp_data < target_temp

def turn_off_fridge():
    """Turns off fridge"""
    os.system('/var/www/rfoutlet/codesend 1054012')
    time.sleep(10)

def turn_on_fridge():
    """Turns on fridge"""
    os.system('/var/www/rfoutlet/codesend 1054003')
    time.sleep(10)

if __name__ == "__main__":
    if should_turn_off_fridge():
        turn_off_fridge()
    else:
        turn_on_fridge()

