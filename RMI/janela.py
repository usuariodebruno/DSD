#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4

name = "Janela"
state = 1

objRemotoWindow = Pyro4.Proxy("PYRONAME:Window")

objRemotoWindow.registry(name, state)
while 1: 
    print 'Qual o estado da janela?'
    print '1 para aberto'
    print '0 para fechado'
    newState = input()
    print 'newState lado client: ', newState
    objRemotoWindow.setNewState(newState)