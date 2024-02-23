class HelloWorld:
    def say_hello(self, name):
        print("Hello", name)

    def hello_world(self):
        print("Hello, world!")

if __name__ == "__main__":
    hello_instance = HelloWorld()

    hello_instance.hello_world()

    hello_instance.say_hello("Majkel")