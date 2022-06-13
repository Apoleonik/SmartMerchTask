import os

from aiohttp import web
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from services import create_document_from_uploaded_json

load_dotenv()

CONNECTION_URL = os.getenv('CONNECTION_URL')
API_PORT = int(os.getenv('API_PORT'))

engine = create_async_engine(CONNECTION_URL, pool_size=1, max_overflow=0)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def handle_upload(request):
    async with async_session() as session:
        async with session.begin():
            uploaded_document = await request.json()
            try:
                await create_document_from_uploaded_json(session=session, uploaded_document=uploaded_document)
            except IntegrityError:
                return web.Response(status=500)
    return web.Response()


if __name__ == '__main__':
    app = web.Application()

    app.router.add_route(method='post', path='/upload/document/', handler=handle_upload)

    web.run_app(app, port=API_PORT)
