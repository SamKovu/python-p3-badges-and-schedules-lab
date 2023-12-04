def badge_maker(name):
    message = "Hello, my name is " + name + "."
    return message

"""
def batch_badge_creator(names):
    myList=list()
    for name in names:
        myList.append(badge_maker(name))
    return myList
"""

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    myList=list()
    i=1
    for name in names:
        myList.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i+=1
    return myList




def printer(names):
    for x in batch_badge_creator(names):
        print(x)
    for x in assign_rooms(names):
        print(x)

    return None
