import socket
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) "https://www.geeksforgeeks.org/broken-pipe-error-in-python/"
"fekk pipe error uten bibloteke øve, (pga blei nåe tull med oversending av data) luringen øve sende det i klyster føkk" \
"så fins annen metode i linken som sende bære, ser om det blir nødvendig i prosjektet okkas"

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect the socket to the port where the server is listening
            server_address = ('10.25.47.143', 9090)#ip adressa te rasberryen
            print("Serving connections on port {}".format(server_address[1]))
            sock.bind(server_address)

            sock.listen()
            conn, addr = sock.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(256).decode("utf-8")[:-1] # remove '\n'
                    conn.send("Hello, {}!\n".format(data).encode("utf-8"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
