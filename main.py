import asyncio
import aiofiles
from datetime import datetime

import settings


async def save_to_file(filename, message):
    async with aiofiles.open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await file.write(f"[{timestamp}] {message}\n")


async def tcp_client():
    reader, writer = await asyncio.open_connection(settings.host, settings.port)
    try:
        while True:
            data = await reader.read(1000)
            message = data.decode()
            print(f"Received: {message!r}")
            await save_to_file(settings.history_file, message)
    except asyncio.CancelledError:
        print("Отмена операции")
    except ConnectionError:
        print("Сетевое подключение потеряно, переподключение...")
    finally:
        writer.close()
        await writer.wait_closed()


def main():
    settings.init_config()
    asyncio.run(tcp_client())


if __name__ == "__main__":
    main()
