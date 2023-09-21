#!/usr/bin/python3
class DBStorage:
    # ... (other methods)

    def close(self):
        """Close the database session."""
        self.__session.close()

