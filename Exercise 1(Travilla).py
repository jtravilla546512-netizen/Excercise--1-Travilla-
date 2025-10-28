class Dog:
    
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    
    
    def bark(self):
        print("Woof! Woof!")
    
   
    def celebrateBirthday(self):
        self.age = self.age + 1
        print("Happy Birthday! " + self.name + " is now " + str(self.age) + " years old.")
    
    def getInfo(self):
        return "Dog Name: " + self.name + ", Age: " + str(self.age)


max_dog = Dog("Max", 5)


max_dog.bark()              
max_dog.celebrateBirthday() 
print(max_dog.getInfo())    