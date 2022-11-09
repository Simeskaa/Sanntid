import socket
import jsonlib as json
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) "https://www.geeksforgeeks.org/broken-pipe-error-in-python/"
"fekk pipe error uten bibloteke øve, (pga blei nåe tull med oversending av data) luringen øve sende det i klyster føkk" \
"så fins annen metode i linken som sende bære, ser om det blir nødvendig i prosjektet okkas"

client_test = json.write({'hast_h' : "vrooooooooom",
                          'hast_v' : "brabom"},sort_keys=True, indent=' ').decode ('utf8')

def main():

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 9090)
        print("Connecting to {} port {}".format(server_address[0], server_address[1]))
        sock.connect(server_address)

        for i in range(0, 10):
            #sock.send("{}\n".format(i).encode("utf-8"))
            sock.send(client_test.encode("utf-8"))
            data = sock.recv(256).decode("utf-8")#[:-1]
            read = json.read(data)
            #print("Got: {}".format(data))
            #print(read)
            print(read["sensor 3"])


if __name__ == "__main__":
    main()