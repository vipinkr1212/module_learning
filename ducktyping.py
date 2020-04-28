class Pycharm:
    def execute(self):
        print("compilling")
        print("running")



class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compilling")
        print("running")


class Laptop:

    def code(self, ide):
        ide.execute()



#ide = Pycharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
