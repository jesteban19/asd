import falcon.asgi

from web.routes import routes

app = falcon.asgi.App()

routes(app)

if __name__ == '__main__':
    import uvicorn
    port = 9001
    print(f'Running server listening port {port}')
    uvicorn.run(app, host='127.0.0.1', port=9001)
