class Car():
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print("{0} 폐차 되고 있다.".format(self.data))

class Trash():
    def delete_obj(self, instance):
        print("{0}를 폐차 합니다.".format(instance.data))
        del instance

trash = Trash()

a = Car('소나타')
b = a

trash.delete_obj(a)
print("삭제 되지 않았어. ", a.data)

print("맨 마지막 코드이다.")