from api.healthcheck.HealthcheckResource import HealthcheckResource
from api.migrations.CommentMigrationResource import CommentMigrationResource
from api.migrations.EventMigrationResource import EventMigrationResource
from api.migrations.AccionMigrationResource import AccionMigrationResource

from api.migrations.ProspectoMigrationResource import ProspectMigrationResource
from api.comment.CommentResource import CommentResource
from api.event.EventResource import EventResource


def routes(app):
    app.add_route('/api/migration/action', AccionMigrationResource())
    app.add_route('/api/migration/prospect', ProspectMigrationResource())
    app.add_route('/api/migration/event', EventMigrationResource())
    app.add_route('/api/migration/comment', CommentMigrationResource())

    app.add_route('/api/event', EventResource())
    app.add_route('/api/comment', CommentResource())

    app.add_route('/', HealthcheckResource())
