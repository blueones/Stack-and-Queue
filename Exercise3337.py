import classesDef
class SetofStacks:
#create stacks that are the sizes of indsize which is an input variable
#init create a new empty stack called stack1
#listNum is the index of the newest created stack.
#the stacks are stored in a list called listofStack
    def __init__(self,indsize):
        self.indsize=indsize
        self.stack1=classesDef.stack(self.indsize)
        self.listofStack=list()
        self.listofStack.append(self.stack1)
        self.listNum=0

#add new elementA to the newest stack
#input:elementA
#output: print out a string

    def add(self,elementA):
        #check if it's full. this is a clearer solution. but what you is have is fine. (resolved)
        if self.listofStack[self.listNum].isFull():
        #if not self.listofStack[self.listNum].add(elementA):
            self.stackNew=classesDef.stack(self.indsize)
            self.stackNew.add(elementA)
            self.listofStack.append(self.stackNew)
            self.listNum=self.listNum+1
        else:
            self.listofStack[self.listNum].add(elementA)



    def peek(self):
        if self.listofStack[self.listNum].isEmpty():
            return "the set of stacks is completely empty right now"
        else:
            returnV=self.listofStack[self.listNum].peek()
            return returnV

    def pop(self):
        if self.listofStack[self.listNum].isEmpty():
            return "there is nothing in the set of stacks"
            #go back to the last stack
        else:
            elementPoped=self.listofStack[self.listNum].pop
            if self.listofStack[self.listNum].isEmpty():
                del self.listofStack[self.listNum]
                self.listNum=self.listNum-1
            return elementPoped

    def popat(self,index):
        if index>self.listNum:
            print ("there is not that many stacks in this set")
            return False
        else:
            if self.listofStack[index].isEmpty():
                print("the stack you ask for is empty")
                return False
            else:
                popedV=self.listofStack[index].pop
                return popedV


class animalShelter:
    def __init__(self):
        self.shelter=classesDef.queue()


    def enqueue(self,animal):
        self.shelter.add(animal)


    def dequeueAny(self):
        anyAnimal=self.shelter.pop()

        return anyAnimal


    def dequeueDog(self):
        catStack=classesDef.stack(100)
        dogflag=0
        while dogflag==0:
            anyAnimal = self.shelter.pop()
            if anyAnimal=="dog":
                dogflag=1
            elif anyAnimal=="cat":
                catStack.add(anyAnimal)
        while catStack.index!=-1:
            cat=catStack.pop()
            self.enqueue(cat)
        print (self.shelter)




    def dequeueCat(self):
        dogStack = classesDef.stack(100)
        catflag = 0
        while catflag == 0:
            anyAnimal = self.shelter.pop()
            if anyAnimal == "cat":
                catflag = 1
            elif anyAnimal == "dog":
                dogStack.add(anyAnimal)
        while dogStack.index != -1:
            dog = dogStack.pop()
            self.enqueue(dog)
        print(self.shelter)

    def listAnimals(self):
        Stack = classesDef.stack(100)
        shelteraniNum=self.shelter.lengthQueue()
        while not self.shelter.isEmpty():
            anyAnimal = self.shelter.pop()
            print (anyAnimal)
            Stack.add(anyAnimal)
        while Stack.index != -1:
            anyAni = Stack.pop()
            self.enqueue(anyAni)



animalshelter=animalShelter()
animalshelter.enqueue("cat")
animalshelter.enqueue("cat")
animalshelter.enqueue("dog")
animalshelter.enqueue("dog")
animalshelter.enqueue("cat")
animalshelter.enqueue("cat")
animalshelter.enqueue("dog")
animalshelter.enqueue("dog")
animalshelter.dequeueDog()
animalshelter.listAnimals()