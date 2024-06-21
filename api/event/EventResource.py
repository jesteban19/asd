from falcon.errors import HTTPInternalServerError

from repository.QueryDatabase import insert_event, get_recent_actions


class EventResource:
    async def on_post(self, req, res):
        try:
            media = await req.get_media()
            columns = [media[f"columna{i}"] for i in range(1, 28)]
            await insert_event(columns)
            res.media = {"ok": True, "message": "successfull"}
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def on_get(self, req, res):
        try:
            id = req.get_param("idprospecto")
            result = await get_recent_actions(id)
            res.media = [dict(row) for row in result]
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))
