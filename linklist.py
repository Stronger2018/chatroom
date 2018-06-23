#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        self.head = None

    def __getitem__(self,key):
        if self.is_empty():
            print('linklist is empty')
            return
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return
        else:
            return self.getitem(key)

    def __setitem__(self,key,value):
        if self.is_empty():
            print('link is empty')
            return
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key,value)

# 链表的初始化

    def initlist(self,data):
        self.head = Node(0)

        p = self.head
        
        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

#遍历链表
    def show(self):
        p = self.head.next

        while p != None:
            print(p.val,' ',end = '')
            p = p.next
        print()

# 获取链表长度

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next

        return length

# 判断链表是否为空

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

#清空
    def clear(self):
        self.head = None

#在链表尾部增加节点
    
    def append(self,item):
        p = self.head
        q = Node(item)
        while p.next != None:
            p = p.next
        p.next = q

#获取某个位置节点的值

    def getitem(self,index):
        if self.is_empty():
            print('link is empty')
            return
        j = 0
        p = self.head.next
        while p != None and j < index:
           j += 1
           p = p.next

        if p == None:
            print('target is not exist')
        else:
            return p.val

# 在某个位置插入节点
    
    def insert(self,index,item):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('index is error')
            return

        p = self.head
        j = 0

        while p.next != None and j < index:
            p = p.next
            j += 1

        q = Node(item,p)
        q.next = p.next
        p.next = q

# 删除某个位置的元素
    
    def delete(self,index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty')
            return
        
        p = self.head
        j = 0
        while p.next != None and j < index:
            p = p.next
            j += 1

        if p.next == None:
            print('indes is error')
        else:
            p.next = p.next.next

# 查找操作，返回相应位置
    
    def index(self,value):
        if self.is_empty():
            print('Linklist is empty')
            return
        p = self.head.next
        i = 0
        while p != None and not (p.val == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else : 
            return i

