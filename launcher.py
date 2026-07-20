import asyncio
import traceback

from app.main import run


if __name__ == "__main__":

    try:

        asyncio.run(
            run()
        )

    except Exception:

        traceback.print_exc()

        input(
            "\nPresiona ENTER para cerrar..."
        )