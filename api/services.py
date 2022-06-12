from datetime import datetime

from sqlalchemy.ext.asyncio import async_session
from sqlalchemy.future import select

from app.models import User, Place, Visit, Scene, Document


async def _get_document_date(document_urls: dict) -> datetime:
    min_timestamp = int(min([url['time'] for url in document_urls]))
    return datetime.fromtimestamp(min_timestamp)


async def _get_or_create(session: async_session, model, **kwargs):
    result = await session.execute(select(model).filter_by(**kwargs))
    instance = result.scalars().first()

    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        await session.flush()
        return instance


async def create_document_from_uploaded_json(session: async_session, uploaded_document: dict):
    user = await _get_or_create(session, User, ext_id=uploaded_document['userId'])

    place = await _get_or_create(session, Place, address=uploaded_document['extension_data']['place']['address'],
                                 ext_id=uploaded_document['placeId'])
    visit = await _get_or_create(session, Visit, user_id=user.id, ext_id=uploaded_document['visitId'])
    scene = await _get_or_create(session, Scene, ext_id=uploaded_document['settings']['options']['type'])

    document_date = await _get_document_date(uploaded_document['urls'])
    await _get_or_create(session, Document, date=document_date, guid=uploaded_document['guid'],
                         data=uploaded_document, user_id=user.id, place_id=place.id, visit_id=visit.id,
                         scene_id=scene.id)
