class Person(object):
    left_choices_list = []
    right_choices_list = []
    full_name = ""

    def __init__(self, full_name, left_choices_list, right_choices_list):
        self.full_name = full_name
        self.left_choices_list = left_choices_list
        self.right_choices_list = right_choices_list

    def print_data_for_testing(self):
        print "\nNombre completo: %s \nIzquierda: %s \nDerecha: %s\n" % (self.full_name,
                                                                         self.left_choices_list,
                                                                         self.right_choices_list)


def find_pos_by_name(people_list, full_name):
    """ Return position of the element that contains the name """
    found = False
    i = 0
    while not found and i < len(people_list):
        if full_name == people_list[i].full_name:
            return i
        else:
            i += 1
    return None


def run_algorithm(_people_list):
    people_list = _people_list[:]

    matched_list = []

    # busqueda por la izq. mirar si le quiere en la derecha
    for people in people_list:
        pos = find_pos_by_name(people_list, people.left_choices_list[0])
        #print "LA PRIORIDAD DE %r es %r" % (people.full_name, people.left_choices_list[0])

        try:
            #print "LA HEMOS COMPARADO CON LA PERSONA ENCONTRADA CON EL NOMBRE %r" % people_list[pos].right_choices_list[0]
            if people.full_name == people_list[pos].right_choices_list[0]:
                #p2 = people_list.pop(pos)
                #p1 = people_list.pop(find_pos_by_name(people_list, people.full_name))
                p2 = people_list[pos]
                p1 = people_list[find_pos_by_name(people_list, people.full_name)]

                # le anade por la izq
                matched_list.append((p2, p1))
        except TypeError:
            pass

    #print_list(matched_list)

    new_list = []
    for m in matched_list:
        for n in matched_list:
            if m[0] == n[1]:
                pos = find_pos_by_name(people_list, m[0].full_name)
                people_list.pop(pos)

                for p in people_list:
                    try:
                        for choice in range(0, len(p.left_choices_list)-1):
                            if p.left_choices_list[choice] == m[0].full_name:
                                p.left_choices_list.pop(choice)
                        for choice in range(0, len(p.right_choices_list)-1):
                            if p.right_choices_list[choice] == m[0].full_name:
                                p.right_choices_list.pop(choice)
                    except TypeError:
                        pass
                new_list.append((n[0], m[0], m[1]))
    print "CONJUNTO"
    for n in new_list:
        print n[0].full_name, n[1].full_name, n[2].full_name



    # busqueda por la izq. mirar si le quiere en la derecha
    for people in people_list:
        pos = find_pos_by_name(people_list, people.left_choices_list[0])
        print "LA PRIORIDAD DE %r es %r" % (people.full_name, people.left_choices_list[0])

        try:
            print "LA HEMOS COMPARADO CON LA PERSONA ENCONTRADA CON EL NOMBRE %r" % people_list[pos].right_choices_list[0]
            if people.full_name == people_list[pos].right_choices_list[0]:
                #p2 = people_list.pop(pos)
                #p1 = people_list.pop(find_pos_by_name(people_list, people.full_name))
                p2 = people_list[pos]
                p1 = people_list[find_pos_by_name(people_list, people.full_name)]

                # le anade por la izq
                matched_list.append((p2, p1))
        except TypeError:
            pass

def print_list(matched_list):
    print '='*50
    for m in matched_list:
        print '[',
        for p in m:
            print p.full_name, ',',
        print ']'