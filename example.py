from serialpy import ComConnection
from threading import Thread
from time import sleep


# Initialize an instance
# I use a China's USB-Serial for testing, is shows the serial number is 7
com = ComConnection(serial_number='7', command='hello world', baudrate=9600)


def read():
    while True:
        data = com.receive_command()
        if data:
            print data
    sleep(1)


def write():

    # If you pass a invalid serial-number, an exception will be thrown
    # inform that no device with provided serial number is found.
    # The exception message also lists the list of COM device's serial numbers
    # currently plugged on your system
    com.connect()

    # If you try to call send_command() before call connect()
    # an exception will be raised inform you are trying to
    # send command in a closed connection
    while True:
        com.send_command()
        sleep(1)

if __name__ == '__main__':
    t = Thread(target=read, args=())
    # Make sure this thread will be killed when main program exits
    t.setDaemon(True)
    t.start()

    write()
