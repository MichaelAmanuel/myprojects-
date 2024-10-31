# -*- coding: utf-8 -*-
"""replaceValueInTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19590nUeYrPa7so5J0zjWB7OKAA9eMkyU
"""

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        if not root:
            return root

        # Queue for level-order traversal (BFS)
        queue = deque([(root, None)])  # Store node and its parent

        while queue:
            level_size = len(queue)
            level_sum = 0
            level_nodes = []

            # Compute the total sum of the current level
            for _ in range(level_size):
                node, parent = queue.popleft()
                level_sum += node.val
                level_nodes.append((node, parent))

                # Add children to queue for the next level
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # Update the value of each node based on cousin sums
            for node, parent in level_nodes:
                sibling_sum = 0
                if parent:
                    if parent.left:
                        sibling_sum += parent.left.val
                    if parent.right:
                        sibling_sum += parent.right.val

                node.val = level_sum - sibling_sum

        return root