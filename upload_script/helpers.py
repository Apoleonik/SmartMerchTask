import os

import aiofiles

PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(PATH, 'data')


async def load_data_filenames() -> list[str]:
    return os.listdir(DATA_PATH)


async def load_data_file(filename) -> bytes:
    async with aiofiles.open(os.path.join(DATA_PATH, filename), 'rb') as file:
        return await file.read()
