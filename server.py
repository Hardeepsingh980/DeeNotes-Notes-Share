import socket
import _thread

clients = []

s = socket.socket()
s.bind(('',5000))
s.listen(5)



def recv_msg(conn):
    while True:
        msg = conn.recv(10000000).decode('utf-8')
        if 'post!@!' in msg:
            msg = msg.split('!@!')[1]
            send_to_all(msg)


def send_to_all(msg):
    for client in clients:
        client.send(msg.encode('utf-8'))


while True:
    conn, addr = s.accept()
    clients.append(conn)
    print('Connection Establised With ', str(addr))
    _thread.start_new_thread(recv_msg,(conn,))
