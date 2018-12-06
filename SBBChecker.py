import socket
import ssl


def get_request(ip, socket_family):
    try:
        request_socket = socket.socket(socket_family, socket.SOCK_STREAM)
        ssl_socket = ssl.wrap_socket(request_socket, ssl_version=ssl.PROTOCOL_TLSv1)
        address = (ip, 443)
        ssl_socket.settimeout(5)
        ssl_socket.connect(address)
        request = 'GET / HTTP/1.0\r\n\r\n'
        ssl_socket.sendall(request.encode('utf-8'))
        resp = ssl_socket.recv(1000)
        ssl_socket.close()
    except Exception as exc:
        print(type(exc))
        print(exc.args)
        print(exc)

        resp = "Error"
    return resp


def check_website(url):
    website_ipv4 = socket.getaddrinfo(host=url, port=443, family=socket.AddressFamily.AF_INET)[0][4][0]
    website__ipv6 = socket.getaddrinfo(host=url, port=443, family=socket.AddressFamily.AF_INET6)[0][4][0]
    print("Trying for " + url + ".ipv4 - " + website_ipv4)
    print(get_request(website_ipv4, socket.AF_INET))
    print("\n")
    print("Trying for " + url + ".ipv6 - " + website__ipv6)
    print(get_request(website__ipv6, socket.AF_INET6))
    print("\n")


if __name__ == '__main__':
    check_website("www.google.ch")
    check_website("www.sbb.ch")
