from Animal import Animal

class Nodo:
    """ Contiene los atributos:
    - `self.animal`: Contiene el registro del anamal en custion.
    - `self.next`: Contiene el siguiente nodo con un animal del mismo tipo añadido.
    - `self.nextAnimal`: Contiene el siguiente nodo con un animal añadido.
    """
    def __init__(self, animal: Animal) -> None:
        self.animal: Animal = animal
        self.next: Nodo = None
        self.nextAnimal: Nodo = None
