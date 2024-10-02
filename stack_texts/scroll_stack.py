class ScrollNode:
    def __init__(self, title):
        # Each node contains the title of the scroll and a reference to the next node in the stack
        self.title = title
        self.next_scroll = None  # Reference to the following scroll in the stack


class ScrollStack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack

    def push(self, title):
        # Add a new scroll to the top of the stack
        new_scroll = ScrollNode(title)
        new_scroll.next_scroll = self.top  # Link the new scroll to the current top
        self.top = new_scroll  # Update the top to point to the new scroll
        print(f"'{title}' has been added to the stack.")

    def pop(self):
        # Remove the scroll from the top of the stack
        if self.top is None:
            print("The stack is currently empty. Unable to pop.")
            return None

        removed_scroll = self.top.title  # Store the title of the scroll being removed
        self.top = self.top.next_scroll  # Move the top pointer to the next scroll
        print(f"'{removed_scroll}' has been removed from the stack.")
        return removed_scroll

    def peek(self):
        # Retrieve the title of the top scroll without removing it
        if self.top is None:
            print("The stack is empty. No scroll available to peek at.")
            return None

        print(f"The scroll on top is '{self.top.title}'.")
        return self.top.title

    def contains(self, title):
        # Determine if a specific scroll title exists in the stack
        current = self.top
        while current is not None:
            if current.title == title:
                print(f"'{title}' is present in the stack.")
                return True
            current = current.next_scroll

        print(f"'{title}' is not found in the stack.")
        return False

    def display(self):
        # Display all scrolls in the stack from top to bottom
        if self.top is None:
            print("The stack is empty.")
            return

        current = self.top
        stack_contents = []
        while current is not None:
            stack_contents.append(current.title)
            current = current.next_scroll
        print("Current Stack (top to bottom): " + " -> ".join(stack_contents))


# Example usage:
if __name__ == "__main__":
    scroll_stack = ScrollStack()
    scroll_stack.push("Scroll of Knowledge")
    scroll_stack.push("Scroll of Wisdom")
    scroll_stack.push("Scroll of Power")
    scroll_stack.display()

    scroll_stack.peek()

    scroll_stack.pop()
    scroll_stack.display()

    scroll_stack.contains("Scroll of Wisdom")
    scroll_stack.contains("Scroll of Strength")
