import Pyro5.api

uri = input("Enter URI: ")

server = Pyro5.api.Proxy(uri)

name = input("Enter name: ")

print(server.say_hello(name))