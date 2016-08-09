class Point():

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def show_point_pos(self):
        print("[{0}, {1}]".format(self.xpos, self.ypos))

    def point_comp(self, instance):
        if self.xpos == instance.xpos and self.ypos == instance.ypos :
            return 0
        elif self.xpos == instance.xpos:
            return 1
        elif self.ypos == instance.xpos:
            return 2
        else:
            return -1

