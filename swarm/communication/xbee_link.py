import enum
import queue
import serial
import threading
import time

from digi.xbee.devices import XBeeDevice


# Constant op codes
debugOp = 'd'
bestOp = 'b'


class XBeeLink():

    def __init__(self, bot, device, baud=9600):
        # The bot to set data points of
        self.bot = bot
        # Serial link with the arduino
        self.xbee = XBeeDevice(device, baud)
        self.xbee.open()

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
                self.xbee.send_data_broadcast(self.send_queue.get())

    def send_message(self, message):
        self.send_queue.put(str.encode(message + '\n'))

    def control_loop(self):
        while True:
            d = self.xbee.read_data()
            if d is not None:
                self.recv_queue.put(d.data)

    def recv_loop(self):
        while True:
            if not self.recv_queue.empty():
                self.recv_message(self.recv_queue.get().decode("utf-8"))
        
    def recv_message(self, m):
        # OpCode is first char
        op = m[0]

        # Data is substring(1)
        data = m[1:]

        # Parse the buffer
        if op == bestOp:
            self.bot.local_best = data

        elif op == debugOp:
            print('From bot: {}'.format(data))
