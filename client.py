from rudp.rudp_socket import RudpSocket

CLI_ADDR = ('127.0.0.1', 4444)
SV_ADDR = ('127.0.0.1', 9999)

def main():
    print('init client')

    rudp = RudpSocket(CLI_ADDR)
    rudp.sendto(b'start', SV_ADDR)
    rudp.close()

    print('end client')

main()