class ITcast(object):
    def __init__(self, subjec1):
        self.subject1 = subject1
        self.subject2 = subject2
    def __getattribute__(self,obj):
        print("===1>%s"%obj)