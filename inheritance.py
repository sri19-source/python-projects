class student:
   def show(self):
       print("hi")
  
class teacher:
    def show(self):
        print("hello")
   
class employee:
   def show(self):
        print("welcome")
   

class order( student,employee, teacher):
    def show3(self):
        print("yes")

obj = order()
obj.show3()
