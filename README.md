## Python serial wrapper class
### Change log

- Fix typo
- Add test example

## Install requirement

This class uses `pyserial` package

Make sure to install `pyserial` first

```python
pip install pyserial

```

## Usage

```python
# Initialize an instance
# The baudrate default is 9600
#  baudrate can be one of the standard values: 50, 75, 110, 134, 150, 200,
# 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200
com = ComConnection(serial_number='7', command='hello world', baudrate=9600)
# If you pass a invalid serial-number, an exception will be thrown
# inform that no device with provided serial number is found
com.connect()

# If you try to call send_command() before call connect()
# an exception will be raised inform you are trying to
# send command in a closed connection
com.send_command()
```

## Example

### Arduino
Code for Arduino
```C++
void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
}

void loop() {
  char inByte = ' ';
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line
  }
}
```

Run example:
```python
python example.py
```

### Self read/write

In this test, we will connect the Rx an the Tx pint of the USB-Serial together. This makes the USB-Serial echo what it sent

```python
python example.py
```

## API

### Constructor
ComConnection(serial_number, command=None, baudrate=9600)

### Methods

- connect() - Connect to serial port

- send_command() - Send command

- receive_command() - Receive -command

- close() - Close connection
- get_device_name(serial_number) - Get full device name/path from serial number

