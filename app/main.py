import asyncio

from app.startup import startup
from app.shutdown import shutdown



async def run():

    await startup()


    try:

        while True:

            await asyncio.sleep(1)


    except KeyboardInterrupt:

        await shutdown()


