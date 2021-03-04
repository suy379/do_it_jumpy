class Calculator:
    def __init__(self, lists): #처음부터 리스트를 입력받음.
        self.list = lists
    def sum(self):
        self.result = 0
        for i in self.list:
            self.result +=i
        return self.result
    def avg(self):
        return self.result/len(self.list)