
import os
import asyncio
from aiohttp import web
from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir


WOOSH_DIR = os.getenv('WHOOSH_DIR')


def get_indexer(name):
    index_dir = os.path.join(WOOSH_DIR, name)
    if not os.path.isdir(index_dir):
        raise '404'
    return open_dir(index_dir)


@asyncio.coroutine
def handle_create(request):
    name = request.match_info.get('name')
    index_dir = os.path.join(WOOSH_DIR, name)
    if not os.path.isdir(index_dir):
        os.mkdir(index_dir)

    # TODO: create schema from request body
    schema = Schema(title=TEXT, content=TEXT)
    create_in(index_dir, schema)
    return web.Response(body=b'ok')


@asyncio.coroutine
def handle_search(request):
    name = request.match_info.get('name', "Anonymous")
    ix = get_indexer(name)
    with ix.searcher() as searcher:
        # TODO: build query from request.body
        query = None
        # TODO: format result
        searcher.search(query)
    return web.Response(body=b'TODO')


@asyncio.coroutine
def handle_index(request):
    name = request.match_info.get('name', "Anonymous")
    ix = get_indexer(name)

    writer = ix.writer()
    # TODO: write request.body
    writer.add_document()
    writer.commit()
    return web.Response(body=b'TODO')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('POST', '/{name}/_create', handle_create)
    app.router.add_route('POST', '/{name}/_search', handle_search)
    app.router.add_route('POST', '/{name}', handle_index)

    srv = yield from loop.create_server(
        app.make_handler(), '127.0.0.1', 8080
    )
    print("Server started at http://127.0.0.1:8080")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
