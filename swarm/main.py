import time

from bot import NavSwarmBot

b = NavSwarmBot()

while True:
    inp = input("bot@bot:~/$ ")
    b.xbee.send_message(inp)
    #b.arduino.send_message(inp)
    time.sleep(5)