# This file implements a Binary Search Tree (BST), which is a way to organize data
# like a family tree, where smaller values go to the left and larger values go to the right

# First, we define what a single "node" in our tree looks like
class TreeNode:
    # When we create a new node, we:
    def __init__(self, key):
        self.key = key      # Store the value (called 'key') in the node
        self.left = None    # Set left child to nothing (None) initially
        self.right = None   # Set right child to nothing (None) initially

    # This lets us print a node's value as a string
    def __str__(self):
        return str(self.key)

# Now we define the entire tree structure
class BinarySearchTree:
    # When we create a new tree, we:
    def __init__(self):
        self.root = None    # Start with an empty tree (no root node)

    # This is a helper function that adds a new value to the tree
    # It works by comparing values and deciding whether to go left or right
    def _insert(self, node, key):
        # If we've reached an empty spot, create a new node here
        if node is None:
            return TreeNode(key)

        # If the new value is smaller than current node's value
        if key < node.key:
            # Add it to the left side by calling this same function again
            # with the left child as the starting point
            node.left = self._insert(node.left, key)
        # If the new value is larger than current node's value
        elif key > node.key:
            # Add it to the right side by calling this same function again
            # with the right child as the starting point
            node.right = self._insert(node.right, key)
        
        # Return the node after we've made changes
        return node

    # This is the main function to add values to our tree
    def insert(self, key):
        # Start the insertion process from the root of the tree
        self.root = self._insert(self.root, key)
        
    # This is a helper function that looks for a specific value in the tree
    def _search(self, node, key):
        # If we've reached the end or found the value, return the current node
        if node is None or node.key == key:
            return node
        
        # If the value we're looking for is smaller than current node's value
        if key < node.key:
            # Look in the left subtree
            return self._search(node.left, key)
        
        # Otherwise, look in the right subtree
        return self._search(node.right, key)
    
    # This is the main function to search for values in our tree
    def search(self, key):
        # Start the search from the root of the tree
        return self._search(self.root, key)

    # This is a helper function that removes a value from the tree
    def _delete(self, node, key):
        # If we've reached the end without finding the value, return None
        if node is None:
            return node
        
        # If the value we want to delete is smaller than current node's value
        if key < node.key:
            # Look in the left subtree
            node.left = self._delete(node.left, key)
        # If the value we want to delete is larger than current node's value
        elif key > node.key:
            # Look in the right subtree
            node.right = self._delete(node.right, key) 
        # If we found the node to delete
        else:
            # Case 1: Node has no left child
            if node.left is None:
                return node.right
            # Case 2: Node has no right child
            elif node.right is None:
                return node.left   
            
            # Case 3: Node has two children
            # Find the smallest value in the right subtree
            node.key = self._min_value(node.right)
            # Delete that smallest value from the right subtree
            node.right = self._delete(node.right, node.key)   
        
        # Return the node after changes
        return node

    # This is the main function to delete values from our tree
    def delete(self, key):
        # Start the deletion process from the root of the tree
        self.root = self._delete(self.root, key)

    # This function finds the smallest value in a subtree
    def _min_value(self, node):
        # Keep going left until we can't go any further
        while node.left is not None:
            node = node.left
        # Return the smallest value
        return node.key

    # This helper function visits all nodes in order (smallest to largest)
    def _inorder_traversal(self, node, result):
        if node:
            # First, visit all nodes in the left subtree
            self._inorder_traversal(node.left, result)
            # Then, visit the current node
            result.append(node.key)
            # Finally, visit all nodes in the right subtree
            self._inorder_traversal(node.right, result)

    # This is the main function to get all values in order
    def inorder_traversal(self):
        # Create an empty list to store the values
        result = []
        # Start the traversal from the root
        self._inorder_traversal(self.root, result)
        # Return the list of values
        return result

# Here, we create a new Binary Search Tree
bst = BinarySearchTree()

# These are the values we want to add to our tree
nodes = [50, 30, 20, 40, 70, 60, 80]

# Add each value to the tree
for node in nodes:
    bst.insert(node)

# Search for the value 80 and print the result
print('Search for 80:', bst.search(80))

# Get all values in order (smallest to largest) and print them
print("Inorder traversal:", bst.inorder_traversal())

# Remove the value 40 from the tree
bst.delete(40)

# Try to search for 40 again (should return None since we deleted it)
print("Search for 40:", bst.search(40))