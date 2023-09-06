# owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise ValueError("Invalid pet type")
        self._owner = None
        if owner is not None:
            self.owner = owner
        Pet.all.append(self)

    def owner(self):
        return self._owner

    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise ValueError("Owner must be an instance of Owner class")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(pets, key=lambda pet: pet.name)

