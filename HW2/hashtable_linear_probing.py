# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

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
    h = cs5112_hash1(key)%self.array_size
    while self.array.get(h)!= None:
      if self.array.get(h)[0]==key:
        self.array.set(h,(key,value))
        return
      h += 1
      if h == self.array_size-1:
        self._resize_array()
        h = cs5112_hash1(key)%self.array_size
    self.array.set(h, (key,value))
    if self.item_count/self.array_size >= self.load_factor:
      self._resize_array()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # YOUR CODE HERE
    if key == None:
      raise Exception('Key cannot be None!')
    h = cs5112_hash1(key)%self.array_size
    while self.array.get(h)!= None:
      if self.array.get(h)[0] == key:
        return self.array.get(h)[1]
      else:
        h += 1

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # YOUR CODE HERE
    if key == None:
      raise Exception('Key cannot be None!')
    p = cs5112_hash1(key) % self.array_size
    ret = self._get_array().get(p)
    while ret == 'd' or ret and ret[0] != key:
        p += 1
        ret = self._get_array().get(p)
    if not ret:
        return False
    else:
        self._get_array().set(p, 'd')
        return True
        
  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    return self.array_size

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
    # DO NOT EDIT THIS METHOD
    return self.array
