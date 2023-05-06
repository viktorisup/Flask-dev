from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import Author, Article
from blog.models.database import db
from blog.schemas import AuthorSchema


class AuthorDetailEvent(EventsResource):
    def event_get_count_by_author(self, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvent
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
