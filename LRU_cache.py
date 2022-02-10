# Video link: https://youtu.be/3ocyjP7gnHY
# Method 1: using doubly linked list + dictionary

class Node:
  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.dic = {} # {key : node}
    self.head = self.tail = Node() #dummy nodes
    self.head.next = self.tail
    self.tail.prev = self.head
  def get(self, key):
    if key not in self.dic:
      return -1
    else:
      node = self.dic[key]
      self.evict(node)
      self.insertToEnd(node)
      return node.value
  def put(self, key, value):
    if key in self.dic:
      self.dic[key].value = value
      node = self.dic[key]
      self.evict(node)
      self.insertToEnd(node)
    else:
      if len(self.dic)==self.capacity:
        # delete lru least recently used node in dictionary and in list. order does not matter because we've save that node in a variable (lru_node is referencing to that node, so it won't lost in this block, if will lost once we are out of the block)
        # if we do not save self.head.next to a new reference, we need to delete it in dic first then in list, otherwise, the when we say del self.dic[self.head.next], the key is the second node's key
        lru_node = self.head.next
        del self.dic[lru_node.key]
        self.evict(lru_node)

      newNode = Node(key, value)
      self.insertToEnd(newNode)
      self.dic[key] = newNode

  def evict(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

  def insertToEnd(self, node):
    last_node = self.tail.prev # tail is dummy node, last_node is the most recently used node
    node.prev = last_node
    node.next = self.tail
    self.tail.prev = node
    last_node.next = node

# Method 2: using OrderedDict

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            self.dic.move_to_end(key)
            return self.dic[key]
            

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.dic.move_to_end(key)
        else:
            if self.capacity == len(self.dic):
                self.dic.popitem(last = False) # throw away the first in queue
            self.dic[key] = value

