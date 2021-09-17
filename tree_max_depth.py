import collections


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str({"value": self.value})


def maxDepthR(root):
    '''find max depth of the tree using recusion'''
    # Null node has 0 depth.
    if root == None:
        return 0

    # Get the depth of the left and right subtree
    # using recursion.
    # Choose the larger one and add the root to it.
    return max(maxDepthR(root.left), maxDepthR(root.right)) + 1


def maxDepthNR(root):
    '''find max depth of the tree without recusion'''

    q = collections.deque()

    level = 0
    q.append([root])
    while q:
        current = q.popleft()
        print(current)
        level += 1

        nodes = []
        for n in current:
            nodes += [x for x in [n.left, n.right] if x]
        if len(nodes):
            q.append(nodes)

    return level

def test():
  # Driver code
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.right.left = Node(8)
  root.right.left.right = Node(7)
  max_depth = maxDepthNR(root)

  assert(4 == max_depth)

  print("The max depth is:", max_depth)


test()
