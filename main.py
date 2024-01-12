import asyncio
import aiofiles
from datetime import datetime

FILENAME = "history.txt"


async def save_to_file(filename, message):
    async with aiofiles.open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await file.write(f"[{timestamp}] {message}\n")


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection("minechat.dvmn.org", 5000)

    try:
        while True:
            data = await reader.read(1000)
            print(data)
            message = data.decode()
            print(f"Received: {message!r}")
            await save_to_file("filename.txt", message)
    except asyncio.CancelledError:
        print("Отмена операции")
    except ConnectionError:
        print("Сетевое подключение потеряно, переподключение...")
    finally:
        writer.close()
        await writer.wait_closed()


asyncio.run(tcp_echo_client())
