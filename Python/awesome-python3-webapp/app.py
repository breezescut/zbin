<<<<<<< HEAD
<<<<<<< HEAD
import logging; logging.basicConfig(Level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_router('GET', '/', index)
=======
import logging; logging.basicConfig(Level=logging.INFO)
=======
import logging; logging.basicConfig(level=logging.INFO)
>>>>>>> update 2017/5/30

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
<<<<<<< HEAD
    app.router.add_router('GET', '/', index)
>>>>>>> 9c601411de8b8a110c0a245fdcd8546b53702ea1
    
=======
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
>>>>>>> update 2017/5/30
