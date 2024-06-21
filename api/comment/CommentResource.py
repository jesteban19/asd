import falcon
from falcon import HTTPInternalServerError

from database.orm import get_session_orm
from schemas.models import CommentModel
from services.CommentService import CommentService


class CommentResource:
    service = CommentService()

    async def on_get(self, req, res):
        try:
            parameter = req.get_param('idprospecto', "required")
            session = await get_session_orm()
            last_comment = session.query(CommentModel).filter_by(columna4=parameter).order_by(
                CommentModel.columna7.desc()).first()
            if not last_comment:
                res.status = falcon.HTTP_404
                res.media = {'error': 'Prospecto not found'}
                session.close()
                return

            json = {
                'columna1': last_comment.columna1,
                'columna2': last_comment.columna2,
                'columna3': last_comment.columna3,
                'columna4': last_comment.columna4,
                'columna5': last_comment.columna5,
                'columna6': last_comment.columna6,
                'columna7': last_comment.columna7,
                'columna8': last_comment.columna8,
                'columna9': last_comment.columna9,
            }
            res.media = json
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def on_post(self, req, res):
        try:
            form = await req.get_media()
            async for part in form:
                if part.name == 'file':
                    file_content = await part.stream.read()
                    await self.service.upload(file_content=file_content)

            res.media = {'success': True, 'message': 'comments were uploaded'}
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def on_put(self, req, res):
        try:
            body = await req.get_media()
            session = await get_session_orm()
            comment = session.query(CommentModel).filter_by(columna4=body['idprospecto']).first()
            if not comment:
                res.status = falcon.HTTP_404
                res.media = {'error': 'Comment not found'}
                session.close()
                return

            comment.columna5 = body['comment']
            session.add(comment)
            session.commit()
            session.close()
            res.media = {'success': True, 'message': 'was updated successfully'}
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))
