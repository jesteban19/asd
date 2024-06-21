from falcon import HTTPInternalServerError
from repository.QueryDatabase import update_comment, select_last_comment_by_id
from services.CommentService import CommentService


class CommentResource:
    service = CommentService()

    async def on_get(self, req, res):
        try:
            parameter = req.get_param('idprospecto', "required")
            result = await select_last_comment_by_id(parameter)
            res.media = [dict(row) for row in result]
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
            await update_comment(id=body['idprospecto'], comment=body['comment'])
            res.media = {'success': True, 'message': 'was updated successfully'}
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))
