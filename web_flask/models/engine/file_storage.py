#!/usr/bin/python3
class FileStorage:
    # ... (other methods)

    def close(self):
        """Close the file and reload the data from the JSON file."""
        self.reload()

