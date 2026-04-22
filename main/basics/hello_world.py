class HelloWorld:
    def __init__(self):
        self.name = "Hello World!"
    def say_hi(self):
        print(self.name)

if __name__ == "__main__":
    hello = HelloWorld()
    hello.say_hi()