class Employee():
    eid = None
    name = None

    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

    def show_info(self):
        print("사원번호:{0} & 이름:{1}".format(self.eid, self.name))
        