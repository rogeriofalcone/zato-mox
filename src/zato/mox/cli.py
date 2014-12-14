# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import logging

# Click
import click

# Zato
from .tls import TLSServer
from .zmq_ import ZMQServer

# ################################################################################################################################

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ################################################################################################################################

class PORT:
    TLS_NO_CERTS = 63039
    TLS_CERTS = 49460
    ZMQ_PULL = 33669
    ZMQ_SUB = 59482

# ################################################################################################################################

@click.group()
def main():
    pass

# ################################################################################################################################

@click.command()
@click.pass_context
def tls_no_certs(ctx):
    s = TLSServer(PORT.TLS_NO_CERTS)
    s.run()

@click.command()
@click.pass_context
def tls_certs(ctx):
    s = TLSServer(PORT.TLS_CERTS, True)
    s.run()

# ################################################################################################################################

@click.command()
@click.pass_context
def zmq_pull(ctx):
    s = ZMQServer(PORT.ZMQ_PULL, 'PULL')
    s.run()

@click.command()
@click.pass_context
def zmq_sub(ctx):
    s = ZMQServer(PORT.ZMQ_SUB, 'SUB')
    s.run()

# ################################################################################################################################

main.add_command(tls_no_certs)
main.add_command(tls_certs)
main.add_command(zmq_pull)
main.add_command(zmq_sub)

if __name__ == '__main__':
    main()
