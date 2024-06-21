class HealthcheckResource:
    async def on_get(self, req, res):
        res.media = {'status': 'ok'}
