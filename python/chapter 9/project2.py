class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass


acc1=account(14234,12345)
print(acc1.acc_no)
print(acc1.__acc_pass)