from falcon.errors import HTTPInternalServerError

from database.orm import get_session_orm
from schemas.models import EventModel
from utils.parser import event_parse_to_json


class EventResource:
    async def on_post(self, req, res):
        try:
            media = await req.get_media()

            session = await get_session_orm()

            new_event = EventModel(
                columna1=media['columna1'],
                columna2=media['columna2'],
                columna3=media['columna3'],
                columna4=media['columna4'],
                columna5=media['columna5'],
                columna6=media['columna6'],
                columna7=media['columna7'],
                columna8=media['columna8'],
                columna9=media['columna9'],
                columna10=media['columna10'],
                columna11=media['columna11'],
                columna12=media['columna12'],
                columna13=media['columna13'],
                columna14=media['columna14'],
                columna15=media['columna15'],
                columna16=media['columna16'],
                columna17=media['columna17'],
                columna18=media['columna18'],
                columna19=media['columna19'],
                columna20=media['columna20'],
                columna21=media['columna21'],
                columna22=media['columna22'],
                columna23=media['columna23'],
                columna24=media['columna24'],
                columna25=media['columna25'],
                columna26=media['columna26'],
                columna27=media['columna27']
            )
            session.add(new_event)
            session.commit()
            session.close()
            res.media = {"ok": True, "message": "successfull", "id": media['columna1']}
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def on_get(self, req, res):
        try:
            id = req.get_param("idprospecto")
            session = await get_session_orm()

            result = session.query(EventModel).filter_by(columna5="7", columna23=id).order_by(
                EventModel.columna1.desc()).limit(5).all()
            res.media = event_parse_to_json(result=result)
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))
