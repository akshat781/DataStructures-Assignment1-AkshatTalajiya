class Node:
    def __init__(self, clue):
        # Each node holds a clue and pointers to its left and right children
        self.clue = clue
        self.left_child = None  # Reference to the left child node
        self.right_child = None  # Reference to the right child node


class ClueBinaryTree:
    def __init__(self):
        self.root_node = None  # The root of the binary tree

    def insert_clue(self, clue):
        # Insert a new clue into the binary tree
        if self.root_node is None:
            self.root_node = Node(clue)  # Create the root node if tree is empty
        else:
            self._insert_recursively(self.root_node, clue)  # Recursively insert the clue

    def _insert_recursively(self, current_node, clue):
        # Helper method for recursive insertion
        if clue < current_node.clue:
            if current_node.left_child is None:
                current_node.left_child = Node(clue)  # Insert as left child if empty
            else:
                self._insert_recursively(current_node.left_child, clue)  # Recur left
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(clue)  # Insert as right child if empty
            else:
                self._insert_recursively(current_node.right_child, clue)  # Recur right

    def in_order(self, node):
        # In-order traversal: left -> root -> right
        if node:
            self.in_order(node.left_child)  # Visit left subtree
            print(node.clue, end=" -> ")  # Visit node
            self.in_order(node.right_child)  # Visit right subtree

    def pre_order(self, node):
        # Pre-order traversal: root -> left -> right
        if node:
            print(node.clue, end=" -> ")  # Visit node
            self.pre_order(node.left_child)  # Visit left subtree
            self.pre_order(node.right_child)  # Visit right subtree

    def post_order(self, node):
        # Post-order traversal: left -> right -> root
        if node:
            self.post_order(node.left_child)  # Visit left subtree
            self.post_order(node.right_child)  # Visit right subtree
            print(node.clue, end=" -> ")  # Visit node

    def find_clue(self, clue):
        # Search for a specific clue in the tree
        return self._search_clue_recursively(self.root_node, clue)

    def _search_clue_recursively(self, current_node, clue):
        # Helper method for recursive search
        if current_node is None:
            return False  # Clue not found

        if clue == current_node.clue:
            return True  # Clue found
        elif clue < current_node.clue:
            return self._search_clue_recursively(current_node.left_child, clue)  # Search left
        else:
            return self._search_clue_recursively(current_node.right_child, clue)  # Search right

    def count_clues(self):
        # Count the total number of clues in the tree
        return self._count_clues_recursively(self.root_node)

    def _count_clues_recursively(self, current_node):
        # Helper method for counting clues recursively
        if current_node is None:
            return 0
        return 1 + self._count_clues_recursively(current_node.left_child) + self._count_clues_recursively(
            current_node.right_child)


# Example usage
if __name__ == "__main__":
    clue_tree = ClueBinaryTree()

    # Inserting clues
    clue_tree.insert_clue("Map of the Temple")
    clue_tree.insert_clue("Golden Idol")
    clue_tree.insert_clue("Secret Passage")
    clue_tree.insert_clue("Ancient Scroll")

    print("In-Order Traversal:")
    clue_tree.in_order(clue_tree.root_node)  # Output should be sorted
    print("\nPre-Order Traversal:")
    clue_tree.pre_order(clue_tree.root_node)
    print("\nPost-Order Traversal:")
    clue_tree.post_order(clue_tree.root_node)

    # Finding clues
    clue_to_find = "Golden Idol"
    if clue_tree.find_clue(clue_to_find):
        print(f"\nClue '{clue_to_find}' found in the tree.")
    else:
        print(f"\nClue '{clue_to_find}' not found in the tree.")

    # Counting total clues
    total_clues = clue_tree.count_clues()
    print(f"\nTotal number of clues in the tree: {total_clues}")
