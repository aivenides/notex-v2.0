#!bin/python

###############################################################################
###############################################################################

from gevent_fastcgi.server import WSGIServer
from webed.app import app

import os

###############################################################################
###############################################################################

if __name__ == '__main__':

    app.config['GEVENT'] = True
    path = app.config['NIX_FILE']
    if os.path.exists (path): os.remove (path)
    WSGIServer (path, app).serve_forever ()

###############################################################################
###############################################################################
