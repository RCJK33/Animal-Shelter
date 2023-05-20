from AnimalShelter import AnimalShelter
from Animal import Animal

animalShelter = AnimalShelter()

animalShelter.enqueue_Animal(Animal('Oso',2,'cat','X'))
animalShelter.enqueue_Animal(Animal('Ody',5,'cat','X'))
animalShelter.enqueue_Animal(Animal('Au',7,'cat','X'))
animalShelter.enqueue_Animal(Animal('Zeus',1,'dog','X'))
animalShelter.enqueue_Animal(Animal('kirby',1,'dog','X'))
animalShelter.enqueue_Animal(Animal('Draco',3,'cat','X'))
animalShelter.enqueue_Animal(Animal('Anzu',3,'cat','X'))
animalShelter.enqueue_Animal(Animal('Saike',3,'dog','X'))
animalShelter.enqueue_Animal(Animal('Saike',3,'dog','X'))
animalShelter.enqueue_Animal(Animal('Aasdasu',7,'dog','X'))
animalShelter.enqueue_Animal(Animal('Aasu',8,'dog','X'))

print()

animalShelter.dequeue_any()
animalShelter.displayAnimals()