## Animal is-an object
class Animal(object):
	pass

## Dog is-an Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-an Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is an object
class Person(object):

	def __init__(self, name):
		## person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-an object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog named 'Rover'
rover = Dog('Rover')

## satan is-a Cat named 'Satan'
satan = Cat('Satan')

## mary is-a Person named 'Mary'
mary = Person('Mary')

## mary has-a pet which is satan
mary.pet = satan

## frank is-an Employee named 'Frank' with a 120,000 salary
frank = Employee('Frank', 120000)

## frank has-a pet which is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()