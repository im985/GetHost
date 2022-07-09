import socket

print("     GetHost  \n Twitter: @moodix0 \n Github: @moodix94 \n")


def host():
    global url
    try:
        url = input("Enter URL: ")
        try:
            host = socket.gethostbyname(url)
            hostname = socket.gethostbyaddr(host)
            print("IP: ", host)
            print("AdderInfo: ", hostname)
        except:
            print("Error: ", url, " is not a valid URL")
    except:
        print("Error: ", url, " is not a valid URL")


host()
