toady = int(input("Enter today(1-365): "))


class Node:
    def __init__(self, name, start_day, end_day):
        self.name = name
        self.end_day = end_day
        self.start_day = start_day
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, name, start_day, end_day):
        temp = Node(name, start_day, end_day)
        if self.first is None:
            self.first = temp
            self.last = temp
        else:
            self.last.next = temp
            self.last = temp
        self.size += 1

    def find(self, name):
        head = self.first
        while head is not None:
            if head.name == name:
                return head
            head = head.next

    def show_user(self):
        head = self.first
        while head is not None:
            print(f"{head.name}: {head.end_day-head.start_day}")
            head = head.next


data = LinkedList()


def add_user():
    name = input("Enter Customer Name: ")
    end_day = int(input("Enter endDay: "))
    data.add(name, toady, end_day)


def update_user():
    name = input("Enter Customer Name: ")
    node = data.find(name)
    if node is not None:
        node.end_day = int(input("Enter new endDay: "))
    else:
        print("User Not Found")


def show_user():
    data.show_user()


menu = {
    "1": add_user,
    "2": update_user,
    "3": show_user,
}
while True:
    print("""    1-Add a User
    2-Update User
    3-Show
    """)
    choice = input("Enter a num from menu:")
    if choice in menu.keys():
        menu[choice]()