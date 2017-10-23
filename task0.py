import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
sock.bind(('127.0.0.1', 8080))
sock.listen(10)

numReq = 0
while True:
    try:
        conn, addr = sock.accept()
    except:
        print ("Error")

    tmp = conn.recv(1024)
    print (tmp)
    if not tmp:
        break
    numReq += 1
    conn.send(bytes((str(numReq)+'\n').encode('utf-8')))
    conn.close()
