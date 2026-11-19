class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return node
        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if not node:
            return []
        return (self._inorder_recursive(node.left) + 
                [node.val] + 
                self._inorder_recursive(node.right))

    def kth_smallest(self, k):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return inorder(self.root)[k-1]

    def is_valid_bst(self):
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        return validate(self.root)


# Create a BST instance
bst = BST()

# Insert some values
values_to_insert = [5, 3, 7, 2, 4, 6, 8]
for value in values_to_insert:
    bst.insert(value)

print("BST after insertions:")
print("Inorder traversal:", bst.inorder_traversal())

# Search for values
print("\nSearching for values:")
for value in [4, 9]:
    result = bst.search(value)
print(f"Search for {value}: {'Found' if result else 'Not Found'}")

# Find k-th smallest element
k = 3
print(f"\n{k}-th smallest element:", bst.kth_smallest(k))

# Validate BST
print("\nIs valid BST:", bst.is_valid_bst())

# Delete a value
value_to_delete = 3
bst.delete(value_to_delete)
print(f"\nBST after deleting {value_to_delete}:")
print("Inorder traversal:", bst.inorder_traversal())

# Validate BST again
print("\nIs valid BST after deletion:", bst.is_valid_bst())