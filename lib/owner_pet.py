# owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet if pet.owner == self else None for pet in Pet.all]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):
        pet_list = [pet for pet in Pet.all if pet.owner == self]
        pet_list.sort(key = lambda x: x.name)
        return pet_list




class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    def __init__(self, name, pet_type, owner = None):
        self.name = name 
        self.pet_type = pet_type 
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in self.PET_TYPES:
            raise Exception
        self._pet_type = value



 
