from app import socket
from app.console.console_logs import ConsoleLogs, socketDecorator

from threading import Lock

thread = None
thread_lock = Lock()


def background_thread():
    count = 0
    while True:
        socket.sleep(10)
        count += 1
        socket.emit('my_response',
                      {'data': 'Server generated event', 'count': count})


@socket.event(namespace="/order")
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socket.start_background_task(background_thread)


@socket.event(namespace="/order")
def disconnect():
    ...
