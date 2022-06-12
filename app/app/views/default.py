from paginate_sqlalchemy import SqlalchemyOrmPage
from pyramid.view import view_config
from sqlalchemy import and_

from .. import models

DEFAULT_PAGE_SIZE = 15


def _parse_page_param(request):
    page = request.params.get('page')
    if page and page.isdigit():
        return int(page)


@view_config(route_name='home', renderer='app:templates/documents.jinja2')
def index_view(request):
    page = _parse_page_param(request) or 1
    query = request.dbsession.query(models.Document, models.User, models.Place, models.Scene, models.Visit) \
        .select_from(models.Document) \
        .join(models.User) \
        .join(models.Place) \
        .join(models.Visit, and_(models.Document.visit_id == models.Visit.id)) \
        .join(models.Scene)

    paginated_queryset = SqlalchemyOrmPage(query, page=page, items_per_page=DEFAULT_PAGE_SIZE)

    return {'paginated_documents': paginated_queryset}
