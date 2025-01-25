Encaspulation is a concept where you wrapp method and variables using access modifiers.

class Encasp:
	__a=10   #__  is private modifer variable a ,can be accessed only using (self.__a)
	def methods1(self):
		print("welcome")


n1=Encasp()
n1.methods1()
