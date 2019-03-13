import enum
import queue
import serial
import threading
import time

# Constant op codes
debugOp = 'd'
gpsOp = 'g'
imuOp = 'i'
reqOp = 'r'


class ArduinoLink():

    def __init__(self, bot, device, baud=115200):
        # The bot to set data points of
        self.bot = bot
        # Serial link with the arduino
        self.ser = serial.Serial(device, baud)
        
        # Queues of strings that are meant for I/O.
        # They should have their own thread to operate "parallel" to one another
        self.send_queue = queue.Queue()
        self.control_queue = queue.Queue()
        self.recv_queue = queue.Queue()

        self.send_thread = threading.Thread(target=self.send_loop)
        self.control_thread = threading.Thread(target=self.control_loop)
        self.recv_thread = threading.Thread(target=self.recv_loop)

        self.send_thread.start()
        self.recv_thread.start()
        self.control_thread.start()

    def send_loop(self):
        while True:
            if not self.send_queue.empty():
                self.ser.write(self.send_queue.get())

    def send_message(self, message):
        self.send_queue.put(str.encode(message + '\n'))

    def control_loop(self):
        while True:
            if self.ser.inWaiting():
                self.recv_queue.put(self.ser.readline())

    def recv_loop(self):
        while True:
            if not self.recv_queue.empty():
                self.recv_message(self.recv_queue.get())
        
    def recv_message(self, m):
        # OpCode is first char
        op = m[0]

        # Data is substring(1)
        data = m[1:]

        # Parse the buffer
        if op == 'd':
            print("    Arduino: {}".format(str(m)))

        if op == 'g':
            self.recv_gps(data)

        elif op == 'i':
            self.recv_imu(data)
            
        # Etc,..
        # If arduino is requesting data
        elif op == 'r':
            # Send the data that it requested
            self.recv_req(data)
        # Add new op codes like this
        # if op == '\0':

    # Send/receive functions
    def send_gps(self, x, y):
        # Pack variables into message
        message = gpsOp + str(x) + "," + str(y)
        self.send_message(message)
        pass

    # Receive functions will set data values into `self.bot`
    def recv_gps(self, data):
        # Unpack into variables
        pass

    # Will need to change what args there are 
    def send_imu(self, args):
        pass

    def recv_imu(self, data):
        pass

    # Will need to change what args there are 
    def send_req(self, args):
        pass

    def recv_req(self, data):
        pass