# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')
import Queue
class HuffmanTree:
  # Helper object for building the Huffman tree.
  # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.
  class TreeNode:
    def __init__ (self):
      self.left = None
      self.right = None
      self.symbol = None
      self.min_element = None

  # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.
  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)
    # YOUR CODE HERE
    pq = Queue.PriorityQueue()
    for s in symbol_list:
      symbol, weight = s[0],int(s[1])
      node = self.TreeNode()
      node.symbol, node.min_element = symbol,symbol

      # put as tuple ((weight, min_element),node) so in priority queue, is will rank asec, by weight than by the min_element
      pq.put(((weight,node.min_element),node))

    # merger node/tree till one element left (the root)
    while pq.qsize()>1:
      left = pq.get()
      right = pq.get()
      weight = left[0][0]+right[0][0]

      node = self.TreeNode()
      node.left, node.right, node.min_element = left[1],right[1], min(left[1].min_element,right[1].min_element)
      pq.put(((weight,node.min_element),node))

    self.root = pq.get()[1] # (place TreeNode object here)
    #a dict to store huffman code for each symbol
    self.code = {}
    #call generate_huffman_code to fill the dict self.code
    self.generate_huffman_code((self.root), "")

  #recursivly call
  def generate_huffman_code(self, node, code):
    # check if reached leaf node
    if not node.left and not node.right and node.symbol:
      self.code[node.symbol] = code
      return

    self.generate_huffman_code(node.left, code + '0')
    self.generate_huffman_code(node.right, code + '1')


  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)
    # YOUR CODE HERE
    # use list instead of string, save the immutable type cost
    code = []
    for c in s:
      code.append(self.code[c])

    return "".join(code)

  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):
    assert(s is not None)
    # YOUR CODE HERE

    p = self.root
    ans = []
    for c in s:
      if c=="0":
        p = p.left
      if c=="1":
        p = p.right
      # if it reaches leaf, append the huffman code
      if p.symbol:
        ans.append(p.symbol)
        p = self.root

    #if there are extra code left -- so it didn't come back to the root, mean the huffman code is invalid
    if p!=self.root:
      return None
    else:
      return "".join(ans)




