import subprocess

def ping(website):
    print("Ping {}: ".format(website))
    subprocess.call(["ping", "-c 4", website])
    print('------------------------------------------------------------------')


ping("www.microsoft.com")
ping("www.novell.com")
ping("www.yahoo.com")
ping("www.sun.com")
ping("www.microfocus.com")