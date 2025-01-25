abstract classs has one alteast abstract method

abstract class <==> concrete class inherit mehtod from abstract class and  implements methods using overrride.

module abc ----abstract base class


concrete class does not have abstract method

abstract class have method with skeletion but implementation is done in concrete class.




class Aclass(ABC):   #Aclass is abstract base class as it has abstract method, it inherits module ABC 
	@abstractmethod
	def methods(self):
		None

class concrete1(Aclass):
	def methods(self):
		print("Abstract methods")

n1=concrete1()
n1.methods()
