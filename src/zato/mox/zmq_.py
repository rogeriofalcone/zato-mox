# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import logging

# ZeroMQ
import zmq

class ZMQServer(object):
    def __init__(self, port, socket_type):
        self.port = port
        self.socket_type = socket_type

    def run(self):
        address = 'tcp://0.0.0.0:{}'.format(self.port)

        context = zmq.Context()
        socket = context.socket(getattr(zmq, self.socket_type))

        if self.socket_type == 'SUB':
            socket.setsockopt(zmq.SUBSCRIBE, b'')

        socket.bind(address)

        logging.info('ZMQ %s listening on %s', self.socket_type, address)

        while True:
            msg = socket.recv()
            logging.info(msg)
