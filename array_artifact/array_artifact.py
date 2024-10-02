class ArtifactVault:
    def __init__(self, capacity):
        # Initialize the vault as a fixed-size array with None to represent empty slots
        self.vault = [None] * capacity

    def add_artifact(self, artifact):
        # Add the artifact to the first available slot in the vault
        for index in range(len(self.vault)):
            if self.vault[index] is None:  # Check for an empty slot
                self.vault[index] = artifact
                print(f"Artifact '{artifact['name']}' has been added.")
                return
        print("The vault is full, unable to add more artifacts.")

    def remove_artifact(self, artifact_name):
        # Remove an artifact by its name
        for index in range(len(self.vault)):
            if self.vault[index] is not None and self.vault[index]['name'] == artifact_name:
                print(f"Artifact '{artifact_name}' has been removed.")
                self.vault[index] = None
                return
        print(f"Artifact '{artifact_name}' not found in the vault.")

    def find_artifact_linear(self, artifact_name):
        # Perform a linear search to find an artifact by its name
        for artifact in self.vault:
            if artifact is not None and artifact['name'] == artifact_name:
                return artifact
        return None

    def find_artifact_binary(self, artifact_name):
        # Binary search for an artifact (vault must be sorted by age)
        sorted_vault = [artifact for artifact in self.vault if artifact is not None]
        sorted_vault.sort(key=lambda x: x['age'])  # Sort the vault by artifact age

        left, right = 0, len(sorted_vault) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_vault[mid]['name'] == artifact_name:
                return sorted_vault[mid]
            elif sorted_vault[mid]['name'] < artifact_name:
                left = mid + 1
            else:
                right = mid - 1
        return None


# Example usage:
vault = ArtifactVault(5)
vault.add_artifact({'name': 'Crown of Egypt', 'age': 4000})
vault.add_artifact({'name': 'warrior of ethic', 'age': 2500})
vault.add_artifact({'name': 'king of Troy', 'age': 8000})

vault.remove_artifact('warrior of ethic')

artifact = vault.find_artifact_linear('Crown of Egypt')
if artifact:
    print("Artifact found:", artifact)
else:
    print("Artifact not found.")

artifact = vault.find_artifact_binary('king of Troy')
if artifact:
    print("Artifact found using binary search:", artifact)
else:
    print("Artifact not found in binary search.")
