class Counter:
    counter = 0
    def hello(self):
        self.counter += 1
        print(self.counter)
    
counter=Counter()
counter.hello()
counter.hello()
counter.hello()