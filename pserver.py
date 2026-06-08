import Pyro5.api

@Pyro5.api.expose
class HelloServer:
    def say_hello(self, name):
        return "Hello " + name

daemon = Pyro5.api.Daemon()

uri = daemon.register(HelloServer())

print("Server is running...")
print("URI:", uri)

daemon.requestLoop()