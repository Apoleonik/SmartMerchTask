import asyncio
from argparse import ArgumentParser

import aiohttp

from helpers import load_data_filenames, load_data_file


async def upload_document(session: aiohttp.ClientSession, filename: str, url: str) -> None:
    loaded_file = await load_data_file(filename)
    resp = await session.post(url=url, data=loaded_file)
    print(f'[code: {resp.status}] Upload file {filename} finished!')


async def async_main(threads_count: int, url: str) -> None:
    data_filenames = await load_data_filenames()
    print(f'Files count: {len(data_filenames)}')
    async with aiohttp.ClientSession() as session:
        for number in range(0, len(data_filenames), threads_count):
            print(f'Uploading {number + threads_count}/{len(data_filenames)}')
            batch_to_upload = data_filenames[number:number + threads_count]
            batch_tasks = [upload_document(session=session, filename=filename, url=url) for filename in
                           batch_to_upload]
            await asyncio.gather(*batch_tasks, return_exceptions=True)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-t", "--threads", dest="threads", help="Count of threads", type=int, default=1)
    parser.add_argument("-u", "--url", dest="url", help="url with scheme ex: http://localhost:8888/",
                        default='http://localhost:7654/upload/document/')
    args = parser.parse_args()

    asyncio.run(async_main(threads_count=args.threads, url=args.url))
