import socket

print("     GetHost  \n Twitter: @im_985 \n Github: @im985 \n")


def host():
    URL = input("Enter URL: ")
    byname = socket.gethostbyname(URL)
    byaddr = socket.gethostbyaddr(URL)
    print(f" Ip: {byname},\n Host: {byaddr}")


print(host())
