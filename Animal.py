import datetime

class Animal:
    """ 
    La clase animal contiene los atributos o caracteristicas del animal en cuestion:
    - `self.name` El nombre del animal.
    - `self.age` La edad del animal.
    - `self.typeOA` El tipo de animal `cat` o `dog`.
    - `self.breed` El tipo o la raza del perro.
    - `self.date` la fecha en la que se registro el nuevo animal.
    """
    def __init__(self,name: str, age: int, typeOA: str, breed: str) -> None:
        self.name: str = name
        self.age: int = age
        self.typeOA = typeOA
        self.breed: str = breed
        # self.date: datetime = datetime.datetime.now()