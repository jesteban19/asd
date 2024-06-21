import falcon.asgi

from web.routes import routes

app = falcon.asgi.App()

routes(app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=9001)
