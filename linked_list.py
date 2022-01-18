
class Composition:
    def __init__(self, path, name):
        self.name = name
        self.path = path


class LinkedListItem:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    @property
    def next_item(self):
        return self.next
    
    @next_item.setter
    def next_item(self, next):
        self.next = next
    
    @property
    def prev_item(self):
        return self.prev
    
    @prev_item.setter
    def prev_item(self, prev):
        self.prev = prev
    
    # returns True if the  node points to another node
    def hasNext(self):
        return self.next != None
    
    def hasPrev(self):
        return self.prev != None
    
    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data)
    


class LinkedList:
    def __init__(self, item=None):
        if isinstance(item, LinkedListItem):
            self.head = item
        else:
            self.head = LinkedListItem(item)
        
        self.head.prev_item = self.head.next_item = self.head
        self.length = 0
        self.count = 0
        self.now = self.head
    @property
    def last(self):
        return self.head.prev_item

    @last.setter
    def last(self, item):
        self.head.prev_item = item

    def append_left(self, item):
        if isinstance(item, LinkedListItem):
            newNode = item
        else:
            newNode = LinkedListItem(item)
        # if head is None, then the newNode will next and prev
        #  will point to itself
        if self.head is None:
            self.head.next_item = self.head.prev_item = self.head = newNode
            
        else:
            current_item = self.head
            self.head = newNode
            self.head.prev_item = current_item.prev_item
            self.head.next_item = current_item
            current_item.prev_item = self.head
            self.last.next_item = self.head
        self.length += 1
        self.now = self.head
    

    def append_right(self, item):
        if isinstance(item, LinkedListItem):
            newNode = item
        else:
            newNode = LinkedListItem(item)
        
        if self.head is None:
            self.head.next_item = self.head.prev_item = self.head =  newNode
        else:
            self.last.next_item = newNode
            newNode.next_item = self.head
            newNode.prev_item = self.last
            self.head.prev_item = newNode
        self.length += 1

        
    def display(self):
        current = self.head
        while current.next_item != self.head:
            current = current.next_item
            print(current.prev_item, current, current.next_item)


    def remove(self, item):
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(item)
        current = self.head
        if self.head is None:
            raise ValueError()
        count = 0
        if self.head.data == item.data:
            self.head = current.next_item
            self.head.prev_item = current.prev_item
            self.last.next_item = current.next_item
            print('removed first element')
            return
        while current.next_item != item:
            current = current.next_item
            count += 1
            if count > self.length:
                break
            if current.data == item.data:
                # removes if the song is in the middle
                before = current.prev_item
                after = current.next_item
                before.next_item = current.next_item
                after.prev_item = current.prev_item
                self.length -= 1
                return
        raise ValueError('not found')


    def insert(self, previous, item):
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(item)
        if not isinstance(previous, LinkedListItem):
            previous = LinkedListItem(previous)

        # inserting element after the last element
        if self.last.data == previous.data:
            self.append_right(item)
            return
        # inserting element just after the first one
        if self.head.data == previous.data:
            next = self.head.next_item
            self.head.next_item = item
            item.prev_item = self.head
            item.next_item = next
            next.prev_item = item
            print('inserted successfully...')
            return
        
        current = self.head
        # inserting element anywhere in middle
        while current.next_item != self.head:
            if current.data == previous.data:
                next = current.next_item
                current.next_item = item
                item.prev_item = current
                item.next_item = next
                next.prev_item = item
                return
            else:
                ValueError('notfound')
            current = current.next_item

        
    def __len__(self):
        return self.length


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.count < self.length:
            current = self.now
            self.now = self.now.next_item
            self.count += 1
            return current
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        if self.length == 0 or index >= self.length or index < 0:
            raise IndexError
        now = self.head
        for i in range(self.length):
            if i == index:
                return type(now), now.data
            now = now.next_item
            

    def __contains__(self, item: object) -> bool:
        current = self.head
        for _ in range(self.length):
            if current.data == item:
                return True
            current = current.next_item
        return False

    # Traverse the linked list in reverse order
    # cpython/Lib/collections/__init__.py
    def __reversed__(self):
        root = self.head
        curr = self.head.prev_item
        while curr is not root:
            yield curr.data
            curr = curr.prev_item
        


        

# obj = LinkedList('0')
# print("------------------------------")

# # appending on the left
# obj.append_left('7')
# obj.append_left('6')
# obj.append_left('5')
# obj.append_left('4')
# obj.append_left('3')
# obj.append_left('2')
# obj.append_left('1')
# obj.display()
# print("------------------------------")

# #appending on the right
# obj.append_right('8')
# obj.append_right('9')
# obj.append_right('10')
# obj.append_right('11')
# obj.append_right('12')
# obj.append_right('13')
# obj.append_right('14')
# obj.append_right('15')
# obj.display()
# print("------------------------------")
# # removing elements
# # obj.remove('1')
# # obj.remove('2')
# # obj.remove('3')
# # obj.remove('4')
# # obj.remove('5')
# # obj.remove('6')
# # obj.remove('7')
# # obj.remove('14')
# # obj.display()
# print("------------------------------")
# # inserting element after the specified element
# # obj.insert('14', '65')
# # print("------------------------------")
# # iterating using iter and next method
# # i = iter(obj)
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# print("------------------------------")
# obj.display()
# print(obj[0])
# print(obj[1])
# print(obj[2])
# print(obj[3])
# print(obj[4])
# print(obj[5])
# print(obj[6])
# # print("------------------------------")
# obj2 = reversed(obj)
# for i in obj2:
#     print(i)
    

        

        

    