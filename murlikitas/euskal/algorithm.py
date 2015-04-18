class Person(object):
    left_choices_list = []
    right_choices_list = []
    full_name = ""

    def __init__(self, full_name, left_choices_list, right_choices_list):
        self.full_name = full_name
        self.left_choices_list = left_choices_list
        self.right_choices_list = right_choices_list

    def print_data_for_testing(self):
        print "\nNombre completo: %s \nIzquierda: %s \nDerecha: %s\n" % (self.full_name, self.left_choices_list, self.right_choices_list)


def find_pos_by_name(people_list, full_name):
    """ Return position of the element that contains the name """
    found = False
    i = 0
    while not found and i < len(people_list):
        if full_name == people_list[i].full_name:
            return i
        else:
            i += 1
    return -1


def run_algorithm(people_list):
    print find_pos_by_name(people_list, people_list[0].full_name)


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

