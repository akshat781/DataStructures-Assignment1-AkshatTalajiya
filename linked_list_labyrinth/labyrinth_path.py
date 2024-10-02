class LocationNode:
    def __init__(self, location_name):
        # Each node contains a location and a reference to the next node in the path
        self.location_name = location_name
        self.next_location = None  # Reference to the next location (node)


class LabyrinthPath:
    def __init__(self):
        self.start = None  # The head node of the linked list representing the start of the path

    def add_location(self, location_name):
        # Add a new location to the end of the path
        new_location = LocationNode(location_name)
        if self.start is None:  # If path is empty, new location becomes the start
            self.start = new_location
        else:
            current = self.start
            while current.next_location is not None:  # Traverse to the last location
                current = current.next_location
            current.next_location = new_location  # Add the new location at the end
        print(f"Location '{location_name}' added to the path.")

    def remove_last_location(self):
        # Remove the last location from the path
        if self.start is None:
            print("The path is empty. Nothing to remove.")
            return

        if self.start.next_location is None:  # If there's only one location, remove it
            print(f"Location '{self.start.location_name}' removed from the path.")
            self.start = None
        else:
            # Traverse to the second-to-last location
            current = self.start
            while current.next_location.next_location is not None:
                current = current.next_location
            print(f"Location '{current.next_location.location_name}' removed from the path.")
            current.next_location = None  # Remove the last location

    def has_loop(self):
        # Detect if there is a loop (cycle) in the path using Floyd's Cycle Detection Algorithm
        slow_pointer = self.start
        fast_pointer = self.start

        while fast_pointer is not None and fast_pointer.next_location is not None:
            slow_pointer = slow_pointer.next_location  # Move slow pointer by 1 step
            fast_pointer = fast_pointer.next_location.next_location  # Move fast pointer by 2 steps
            if slow_pointer == fast_pointer:  # If they meet, a loop exists
                print("A loop (trap) has been detected in the path.")
                return True

        print("No loop found in the path.")
        return False

    def display_path(self):
        # Display the entire path
        if self.start is None:
            print("The path is empty.")
            return

        current = self.start
        path_locations = []
        while current is not None:
            path_locations.append(current.location_name)
            current = current.next_location
        print("Path: " + " -> ".join(path_locations))


# Example usage:
if __name__ == "__main__":
    labyrinth = LabyrinthPath()
    labyrinth.add_location("Entrance")
    labyrinth.add_location("Hall of Mirrors")
    labyrinth.add_location("Chamber of Secrets")
    labyrinth.display_path()

    labyrinth.remove_last_location()
    labyrinth.display_path()

    # Manually create a loop to test the loop detection
    labyrinth.add_location("Chamber of Secrets")
    loop_node = LocationNode("Trapped Loop")
    labyrinth.start.next_location.next_location.next_location = loop_node  # Point the last node to loop_node
    loop_node.next_location = labyrinth.start.next_location  # Create a loop
    labyrinth.has_loop()
