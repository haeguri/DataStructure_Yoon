class NameCard():
    # make_name_card
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_name_card_info(self):
        print("{0}:{1}".format(self.name, self.phone))

    def name_compare(self, name):
        if self.name == name:
            return 0
        else:
            return 1

    def change_phone_num(self, phone):
        self.phone = phone