# import pandas as pd
# import json

data_object_1 = dict()
data_object_2 = dict()
data_object_3 = dict()
size_of_the_parking = 0
occupancy_array = list()


class Car:
    def __init__(self, color, reg_num):
        self.color = color
        self.reg_num = reg_num


def find_status():
    global occupancy_array
    print("{0}     {1}     {2} ".format("Slot No.", "Registration No", "Colour"))
    for i in range(len(occupancy_array)):
        if occupancy_array[i]:
            print("{0}    {1}      {2}".format(i, occupancy_array[i].reg_num, occupancy_array[i].color))


# $ status
# Slot No.
# 1
# 2
# 3
# 5
# 6
# Registration No
# KA-01-HH-1234
# KA-01-HH-9999
# KA-01-BB-0001
# KA-01-HH-2701
# KA-01-HH-3141
# Colour
# White
# White
# Black
# Blue
# Black


# $ create_parking_lot 6
# Created a parking lot with 6 slots
def create_parking_lot(n):
    global size_of_the_parking
    size_of_the_parking = n
    global occupancy_array
    occupancy_array = [None for _ in range(n)]
    return "Created a parking lot with {0} slots".format(n)


# $ leave 4
# Slot number 4 is free
def is_vehicle_present(slot_number):
    global occupancy_array
    if occupancy_array[slot_number]:
        return True
    else:
        return False


def leave_the_vehicle(slot_number):
    if is_vehicle_present(slot_number):
        global occupancy_array
        # occupancy_array.pop(slot_number)
        # occupancy_array.insert(slot_number, None)
        occupancy_array[slot_number-1] = None
        return "Slot number {0} is free".format(slot_number)
    else:
        return "Sorry, slot_number:{0} is already empty".format(slot_number)


# $ park KA-01-P-333 White
# Allocated slot number: 4
# $ park DL-12-AA-9999 White
# Sorry, parking lot is full
def is_parking_full():
    global occupancy_array
    for i in range(len(occupancy_array)):
        if occupancy_array[i] is None:
            return False
    else:
        return True


def find_nearest_slot_avl():
    global occupancy_array
    for i in range(len(occupancy_array)):
        if occupancy_array[i] is None:
            slot_num = i+1
            return slot_num


def park(reg_num, color):
    if is_parking_full():
        return "Sorry, parking lot is full"
    else:
        c1 = Car(color, reg_num)
        slot_num = find_nearest_slot_avl()
        data_object_1[color] = data_object_1[color].append(c1.reg_num)
        data_object_2[reg_num] = data_object_2[reg_num].append(slot_num)
        data_object_3[color] = data_object_3[color].append(slot_num)

        slot_number = find_nearest_slot_avl()
        occupancy_array.insert(slot_number-1, c1)
        return "Allocated slot number: {0}".format(slot_num)


#  $ registration_numbers_for_cars_with_colour White
# KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
def find_registration_numbers_for_cars_with_colour(color):
    # data_object_1 = json.dump(data_object_1.json)
    try:
        list_of_reg_num = data_object_1[color]
        return list_of_reg_num
    except KeyError:
        return "Not found"
    except Exception as err_msg:
        return err_msg


# $ slot_numbers_for_cars_with_colour White
# 1, 2, 4
# $ slot_number_for_registration_number KA-01-HH-3141
# 6
# $ slot_number_for_registration_number MH-04-AY-1111
# Not found
def find_slot_numbers_for_cars_with_colour(color):
    global data_object_3
    # data_object_1 = json.dump(data_object_1.json)
    try:
        list_of_reg_num = data_object_3[color]
        return list_of_reg_num
    except KeyError:
        return "Not found"
    except Exception as err_msg:
        return err_msg


if __name__ == '__main__':
    while 1:
        cmd = input()

        if cmd == "exit":
            print("ur input is :{0}".format(cmd))
            break

        else:
            cmd = input().split()
            print("ur input is :{0}".format(cmd))
            if len(cmd) == 1 and cmd[0] == "status":
                print("ur input is :{0}".format(cmd))
                find_status()

            if len(cmd) == 2:
                if cmd[0] == "create_parking_lot":
                    print("ur input is :{0}".format(cmd))
                    create_parking_lot(int(cmd[1]))
                if cmd[0] == "leave":
                    print("ur input is :{0}".format(cmd))
                    leave_the_vehicle(slot_number=int(cmd[1]))
                if cmd[0] == "registration_numbers_for_cars_with_colour":
                    print("ur input is :{0}".format(cmd))
                    find_registration_numbers_for_cars_with_colour(color=cmd[1])
                if cmd[0] == "slot_numbers_for_cars_with_colour":
                    print("ur input is :{0}".format(cmd))
                    find_slot_numbers_for_cars_with_colour(color=cmd[1])

            if len(cmd) == 3:
                print("ur input is :{0}".format(cmd))
                park(vehicle_num=cmd[1], col=cmd[2])
                # park KA-01-P-333 White