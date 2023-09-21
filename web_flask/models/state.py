#!/usr/bin/python3
class State(BaseModel, Base):
    __tablename__ = "states"
    # ... (other class attributes and methods)

    if storage_type != 'db':
        @property
        def cities(self):
            """Getter method to retrieve the list of City objects linked to the current State."""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

