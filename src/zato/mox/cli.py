# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# Click
import click

# Zato
from .tls import TLSServer

@click.group()
def main():
    pass

@click.command()
@click.pass_context
def tls_no_certs(ctx):
    s = TLSServer(63039)
    s.run()

@click.command()
@click.pass_context
def tls_certs(ctx):
    s = TLSServer(49460, True)
    s.run()

main.add_command(tls_no_certs)
main.add_command(tls_certs)

if __name__ == '__main__':
    main()
