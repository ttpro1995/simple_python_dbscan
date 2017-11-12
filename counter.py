class MeowCounter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter+=1
        print(self.counter)