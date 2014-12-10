# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import os, ssl

# Distribute
import pkg_resources

# gevent
from gevent import pywsgi

def app(env, start_response):
    start_response(b'200 OK', [(b'Content-Type', b'application/json')])
    return [b'{"response":"OK"}\n']

class TLSServer(object):
    def __init__(self, port, require_certs=False):
        self.port = port
        self.require_certs = ssl.CERT_REQUIRED if require_certs else ssl.CERT_OPTIONAL

    def run(self):
        pem_dir = os.path.join(pkg_resources.get_distribution('zato-mox').location, '..', 'pem')

        tls_args = {
            'keyfile': os.path.join(pem_dir, 'server.key.pem'),
            'certfile': os.path.join(pem_dir, 'server.cert.pem'),
            'ca_certs': os.path.join(pem_dir, 'ca.cert.pem'),
            'cert_reqs': self.require_certs,
            'server_side': True,
        }

        server = pywsgi.WSGIServer(('0.0.0.0', self.port), app, **tls_args)
        server.serve_forever()
