#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4

name = "Porta"
state = 1

objRemotoDoor = Pyro4.Proxy("PYRONAME:Door")

objRemotoDoor.registry(name, state)
while 1: 
    print 'Qual o estado da porta?'
    print '1 para aberto'
    print '0 para fechado'
    newState = input()
    objRemotoDoor.setNewState(newState)