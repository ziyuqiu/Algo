# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    # YOUR CODE HERE
    if key == None:
      raise Exception('Key cannot be None!')
    if value == None:
      raise Exception('Value cannot be None!')
    k = cs5112_hash1(key)%self.array_size
    pointer = self.array.get(k)
    node = SLLNode((key,value))
    if pointer==None:
      self.array.set(k, node)
    else:
      while pointer.get_next()!= None:
        if pointer.get_value()[0]== key:
          pointer.set_value((key,value))
          return
        pointer = pointer.get_next()
      pointer.set_next(node)
    self.item_count += 1
    # if self.item_count/self.array_size >= self.load_factor:
    #   self._resize_array()
    
    
  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # YOUR CODE HERE
    if key == None:
      raise Exception('Key cannot be None!')
    k = cs5112_hash1(key)%self.array_size
    start = self.array.get(k)
    while start != None and start.get_value()!= None:
      if start.get_value()[0] == key:
        return start.get_value()[1]
      start = start.get_next()
    return None
        
  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # YOUR CODE HERE
    # REWRITE!!!
    if key == None:
      raise Exception('Key cannot be None!')
    k = cs5112_hash1(key)%self.array_size
    prev = curr = self.array.get(k)
    if curr != None:
      while curr.get_next()!= None:
        if curr.get_value()[0]== key:
          if curr.get_next()==None:
            prev.set_next(None)
          else:
            prev.set_next(curr.get_next())
          self.item_count-=1
          return curr.get_value()
        else:
          prev = curr
          curr = curr.get_next()
    else:
      return None

  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    # raise NotImplementedError()
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    # YOUR CODE HERE
    orgsize = self.array_size
    orgarray = self.array

    self.array_size *= 2
    self.array = FixedSizeArray(self.array_size)
    self.item_count = 0

    for i in range(orgsize):
      orgelem = orgarray.get(i)
      if orgelem != None:
        self.insert(orgelem[0],orgelem[1])


  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
