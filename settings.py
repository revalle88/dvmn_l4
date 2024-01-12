import argparse
import os

CHAT_SERVER_HOST = "minechat.dvmn.org"
CHAT_SERVER_PORT = 5000
HISTORY_FILE = "chat-history.txt"


args = None
host = CHAT_SERVER_HOST
port = CHAT_SERVER_PORT
history_file = HISTORY_FILE


def init_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", dest="chat_host", type=str, help="chat server host")
    parser.add_argument("--port", dest="chat_port", type=int, help="chat server port")
    parser.add_argument(
        "--history-file",
        dest="history_file",
        type=str,
        help="Path to file with chat history",
    )
    args = parser.parse_args()
    global host
    host = (
        args.chat_host
        if args.chat_host is not None
        else os.getenv("CHAT_SERVER_HOST", CHAT_SERVER_HOST)
    )
    global port
    port = (
        args.chat_port
        if args.chat_port is not None
        else int(os.getenv("CHAT_SERVER_PORT", CHAT_SERVER_PORT))
    )
    global history_file
    history_file = (
        args.history_file
        if args.history_file is not None
        else os.getenv("HISTORY_FILE", HISTORY_FILE)
    )
