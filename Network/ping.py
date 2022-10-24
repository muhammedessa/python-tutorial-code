from ping3 import ping


def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True


print(myping("www.facebook.com"))
