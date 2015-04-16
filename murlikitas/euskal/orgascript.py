class Member(object):
    leftlist = []
    rightlist = []
    name = ""
    left_locked = ""
    right_locked = ""

    def __init__(self, name, leftlist, rightlist):
        self.leftlist = leftlist
        self.name = name
        self.rightlist = rightlist

    def print_locked(self):
        print "Nombre:", self.name,  "||| Izq: " + self.left_locked,  "||| Der: ", self.right_locked

    def are_already_locked_together(self, name):
        if self.left_locked == name or self.right_locked == name:
            return True
        else:
            return False
    
    def check_left_preference(self, copy, round):
        if(self.left_locked == ""):
            pos = self.find_pos_in_list_by_name(self.leftlist[0], copy)
            if copy[pos].right_locked == "":
                try:
                    if(self.name == copy[pos].rightlist[round].rstrip()):
                        if self.are_already_locked_together(copy[pos].name) == False:
                            self.left_locked = copy[pos].name
                            copy[pos].right_locked = self.name
                            return
                except IndexError:
                    return

    def check_right_preference(self, copy, round):
        if(self.right_locked == ""):
            pos = self.find_pos_in_list_by_name(self.rightlist[0], copy)
            if copy[pos].left_locked == "":
                try:
                    if(self.name == copy[pos].leftlist[round].rstrip()):
                        if self.are_already_locked_together(copy[pos].name) == False:
                            self.right_locked = copy[pos].name
                            copy[pos].left_locked = self.name
                            return
                except IndexError:
                    return

    def find_pos_in_list_by_name(self, name, list):
        ''' Return position of the element that contains the name '''
        found = False
        i = 0
        while found == False and i < len(list):
            if name == list[i].name:
                found = True
            else:
                i += 1

        if found:
            return i
        else:
            return -1