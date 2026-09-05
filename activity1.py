class myClass:
    __privatevar = 27;
    def __privateMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("private variable value: ",myClass.__privatevar)

foo =  myClass()
foo.hello()
foo.__privMeth 