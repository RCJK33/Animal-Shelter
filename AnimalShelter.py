from Animal import Animal
from Nodo import Nodo


class AnimalShelter:
    """ 
    La clase `AnimalShelter` tiene el proposito de manter el control sobre la lista de nodos con listas ligadas.\n
    Cuenta con los atributos privados:
    - `self.__front` Es el start del primer Animal del que se tiene registro y que aun no se ha sacado.
    - `self.__frontCat` Es el start del primer Animal de tipo Gato del que se tiene registro y que aun no se ha sacado.
    - `self.__frontDog` Es el start del primer Animal de tipo Gato del que se tiene registro y que aun no se ha sacado.\n
    - `self.__back` Es el ultimo Animal del que se tiene registro.
    - `self.__backCat` Es el ultimo Animal de tipo Gato del que se tiene registro.
    - `self.__backDog` Es el ultimo Animal de tipo Perro del que se tiene registro.\n
    Metodos que contiene:
    - `self.enqueue_animal(Animal)`
    - `self.dequeue_cat()`
    - `self.dequeue_dog()`
    - `self.dequeue_any()`
    """
    def __init__(self) -> None:
        self.__front: Nodo = None
        self.__back: Nodo = None
        self.__frontCat: Nodo = None
        self.__frontDog: Nodo = None

    def enqueue_Animal(self, animal: Animal) -> None:
        """ Agrega un nuevo animal que sea de tipo `cat` o `dog` al registro. """
        if animal.typeOA != 'cat' and animal.typeOA != 'dog':
            return False
        
        new_animal = Nodo(animal)
        if self.__front is None:
            self.__front = new_animal
            self.__back = self.__front
        else:
            self.__back.nextAnimal: Nodo = new_animal
            self.__back = self.__back.nextAnimal

        if animal.typeOA == 'cat':
            self.__enqueue_cat(new_animal)

        if animal.typeOA == 'dog':
            self.__enqueue_dog(new_animal)
        return True

    def __enqueue_cat(self, new_animal: Nodo) -> None:
        """ Metodo privado que añade un nuevo animal de tipo `cat` al registro enlazandola con el animal anterior del mismo tipo. """
        if self.__frontCat is None:
            self.__frontCat = new_animal
            return
        NXnodo = self.__NX_Positioner(self.__frontCat)
        NXnodo.next = new_animal

    def __enqueue_dog(self, new_animal: Nodo) -> None:
        """ Metodo privado que añade un nuevo animal de tipo `dog` al registro enlazandola con el animal anterior del mismo tipo. """
        if self.__frontDog is None:
            self.__frontDog = new_animal
            return
        NXnodo = self.__NX_Positioner(self.__frontDog)
        NXnodo.next = new_animal

    def __NX_Positioner(self, nod: Nodo) -> Nodo:
        """ Retorna el nodo en el que esta el ultimo animal registado del mismo tipo. """
        while nod.next:
            nod = nod.next
        return nod
    
    def dequeue_dog(self) -> None:
        """  Elimina el primer animal de tipo `dog` del que se registro, o el mas viejo. Ademas retorna el animal. """
        if self.__frontDog is None:
            return None
        return self.__DEL_Animal(self.__frontDog)

    def dequeue_cat(self) -> None:
        """ Elimina el primer animal de tipo `cat` del que se registro, o el mas viejo. Ademas retorna el animal. """
        if self.__frontCat is None:
            return None
        return self.__DEL_Animal(self.__frontCat)

    def dequeue_any(self) -> None:
        """ Elimina el primer animal del que se registro, o el mas viejo. Ademas retorna el animal. """
        if self.__front is None:
            return None
        
        poped = self.__front
        self.__front = self.__front.nextAnimal
        if poped.animal.name == 'cat':
            self.__DEL_Animal(self.__frontCat, globl=True )
        else:
            self.__DEL_Animal(self.__frontDog, globl=True )
        return poped.animal

    def __DEL_Animal(self, DelNodo: Nodo, globl = False) -> Nodo:
        """ Hace la desconexion del nodo que contiene el animal y retorna dicho nodo. """
        globalNodo = self.__front
        while globalNodo:
            if globalNodo.next is not DelNodo:
                globalNodo = globalNodo.next
            break
        popAn = globalNodo.next
        globalNodo.next = popAn.next
        globalNodo.nextAnimal = popAn.nextAnimal
        popAn.next = None
        popAn.nextAnimal = None
        return popAn.animal
    
    def displayAnimals(self):
        NXnodo = self.__front
        while NXnodo:
            print(NXnodo.animal.name)
            NXnodo = NXnodo.nextAnimal

    def displayAnimalsCats(self):
        NXnodo = self.__frontCat
        while NXnodo:
            print(NXnodo.animal.name)
            NXnodo = NXnodo.next

    def displayAnimalsDogs(self):
        NXnodo = self.__frontDog
        while NXnodo:
            print(NXnodo.animal.name)
            NXnodo = NXnodo.next