import logging
import os
import time
from thermometer import read_temp

logging.basicConfig(filename='/home/pi/Documents/lager/lager_fridge/lager_history.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# os.system('/var/www/rfoutlet/codesend 1054003')
# time.sleep(5)
# os.system('/var/www/rfoutlet/codesend 1054012')
# os.system('echo lights on')
# time.sleep(1)
# os.system('echo fuck it, lights off')

# Store these in sqllite
target_temp = 72
# fridge_on = 'Y'/'N'

def should_turn_off_fridge():
    """Checks if fridge temp is below target temp"""
    temp_data = read_temp()[1]
    # Uncomment following line to test low temp
    # temp_data = 68
    print temp_data
    logging.info('Current temp is: {}, target temp is: {}'.format(temp_data, target_temp))
    return temp_data < target_temp

def turn_off_fridge():
    """Turns off fridge"""
    logging.info('Sending code to turn off fridge')
    # os.system('/var/www/rfoutlet/codesend 1054012')

def turn_on_fridge():
    """Turns on fridge"""
    logging.info('Sending code to turn on fridge')
    # os.system('/var/www/rfoutlet/codesend 1054003')

if __name__ == "__main__":
    if should_turn_off_fridge():
        turn_off_fridge()
    else:
        turn_on_fridge()

