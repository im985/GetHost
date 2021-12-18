import socket

print("     GetHost  \n Twitter: @imohafa \n Github: @imohafa \n")


def host():
    URL = input("Enter URL: ")
    byname = socket.gethostbyname(URL)
    byaddr = socket.gethostbyaddr(URL)
    print(f" Ip: {byname},\n Host: {byaddr}")


print(host())
