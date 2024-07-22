#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4

OPEN = 1
CLOSE = 0

LIGADO = 1
DESLIGADO = 0

stateWindow = CLOSE
stateDoor = CLOSE
stateAir = DESLIGADO

@Pyro4.expose
class Window(object):
    name = ""

    def registry(self, name, state):
        window = Window()
        window.name = name
        global stateWindow
        stateWindow = state
        print("Janela registrada")
	
    def setNewState(self, newState):
        print('newState lado ar condicionado(server): ', newState)
        arCondicionado = ArCondicionado()
        global stateWindow
        stateWindow = newState
        print('stateWindow depois de ser mudado: ', stateWindow)
        arCondicionado.checkDoorWindow()
        print("Set new state")


@Pyro4.expose 
class Door(object):
    name = ""

    def registry(self, name, state):
        door = Door()
        door.name = name
        global stateDoor
        stateDoor = state
        print("Porta registrada")
	
    def setNewState(self, newState):
        arCondicionado = ArCondicionado()
        global stateDoor
        stateDoor = newState
        arCondicionado.checkDoorWindow()
        print("Set new state")


class ArCondicionado(object):	
    def setNewState(self, newState):
        arCondicionado = ArCondicionado()
        arCondicionado.state = newState
        print("Ar condicionado está ", newState)
        print("...")

    def checkDoorWindow(self):
        arCondicionado = ArCondicionado()
        print('stateDoor ', stateDoor)
        print('stateWindow ', stateWindow)
        if stateDoor == CLOSE and stateWindow == CLOSE:
            arCondicionado.setNewState(LIGADO)
        else:
            arCondicionado.setNewState(DESLIGADO)

ip_address = '10.25.2.138'
port = 9090
daemon = Pyro4.Daemon(host=ip_address, port=port)

# Registra os objetos com o Daemon
daemon.register(Window, "Window")
daemon.register(Door, "Door")

nameserver = Pyro4.locateNS(host=ip_address, port=port)

# Registra os objetos com o nameserver
uri_window = daemon.registered["Window"]
uri_door = daemon.registered["Door"]
nameserver.register("Window", uri_window)
nameserver.register("Door", uri_door)

# Inicia o servidor
print("Ready. Object URI =", uri_window)
daemon.requestLoop()
