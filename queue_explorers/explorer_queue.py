class ExplorerQueue:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum capacity of the queue
        self.queue = [None] * max_size  # Initialize the queue with None values
        self.front_index = -1  # Index for the front of the queue
        self.rear_index = -1  # Index for the rear of the queue

    def is_empty(self):
        # Return True if the queue is empty
        return self.front_index == -1

    def is_full(self):
        # Return True if the queue is full
        return (self.rear_index + 1) % self.max_size == self.front_index

    def enqueue(self, explorer_name):
        # Add a new explorer to the rear of the queue
        if self.is_full():
            print("The queue is full. Cannot add the explorer.")
            return

        if self.is_empty():
            self.front_index = 0  # Set front index to 0 if the queue is empty

        self.rear_index = (self.rear_index + 1) % self.max_size  # Move rear index forward
        self.queue[self.rear_index] = explorer_name  # Place explorer in the queue
        print(f"Explorer '{explorer_name}' has been added to the queue.")

    def dequeue(self):
        # Remove an explorer from the front of the queue
        if self.is_empty():
            print("The queue is empty. Cannot remove an explorer.")
            return None

        removed_explorer = self.queue[self.front_index]  # Store the front explorer's name
        if self.front_index == self.rear_index:
            # Reset the queue if it has only one element
            self.front_index = -1
            self.rear_index = -1
        else:
            # Move the front index to the next explorer
            self.front_index = (self.front_index + 1) % self.max_size

        print(f"Explorer '{removed_explorer}' has entered the temple.")
        return removed_explorer

    def peek(self):
        # Show the next explorer in line
        if self.is_empty():
            print("The queue is empty. No explorer to view.")
            return None

        next_explorer = self.queue[self.front_index]
        print(f"The next explorer in line is '{next_explorer}'.")
        return next_explorer

    def display(self):
        # Display all explorers in the queue from front to rear
        if self.is_empty():
            print("The queue is empty.")
            return

        print("Current Queue (from front to rear):", end=" ")
        index = self.front_index
        while True:
            print(self.queue[index], end=" -> ")
            if index == self.rear_index:
                break
            index = (index + 1) % self.max_size
        print("None")  # Mark the end of the queue


# Example usage:
if __name__ == "__main__":
    explorer_queue = ExplorerQueue(5)  # Initialize a queue with a maximum size of 5
    explorer_queue.enqueue("Explorer A")
    explorer_queue.enqueue("Explorer B")
    explorer_queue.enqueue("Explorer C")
    explorer_queue.display()

    explorer_queue.peek()

    explorer_queue.dequeue()
    explorer_queue.display()

    explorer_queue.enqueue("Explorer D")
    explorer_queue.enqueue("Explorer E")
    explorer_queue.enqueue("Explorer F")  # Attempting to add to a full queue
    explorer_queue.display()
