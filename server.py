#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random
import time

localIP = "127.0.0.1"
localPort = 8081
bufferSize = 512
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Начало работы термометра")


def temp():
    return str(random.randint(-6, 0))


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode("utf-8")
    address = bytesAddressPair[1]
    print("Статус подключения клиента:{}".format(message))
    print("IP клиента:{}".format(address))
    while True:
        time.sleep(14)
        current_temp = temp()
        print("Температура воздуха - " + current_temp)
        UDPServerSocket.sendto(current_temp.encode("utf-8"), address)