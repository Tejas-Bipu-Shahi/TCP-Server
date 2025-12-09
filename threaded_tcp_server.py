import socket 
import threading

HOST = "0.0.0.0"
PORT = 5000

def handle_client(conn, addr):
    print(f"[+] new connection added {addr}")
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"{addr} {message}")
            
            conn.sendall(f"Server recieved: {message}".encode("utf-8"))

    except Exception as e:
        print(f"error with {addr}: {e}")
    
    finally:
        conn.close()
        print(f" connection closed for {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()


    print(f"server listening on {HOST}: {PORT}")

    while True:
        conn, addr = server.accept()

        client_thread = threading.Thread(target=handle_client, args=(conn,addr))

        client_thread.daemon = True
        client_thread.start()


if __name__ == "__main__":
    start_server()