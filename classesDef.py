class stack:
    def __init__(self,size):
        self.storeList = list()
        self.size=size
        self.kind="stack"
        self.index=-1

#check if the stack is empty
#input:the stack
#output: True or False. if it is empty, return True; if it is not empty, return False.
    def isEmpty(self):
        if self.index==-1:
            returnValue=True
        elif self.index!=-1:
            returnValue=False
        return returnValue

#check if the stack is full
#input:the stack
#output:True or False. if it is full, return True; if it it not full yet, return False.
    def isFull(self):
        if self.index<self.size-1:
            return False
        elif self.index==self.size-1:
            return True



#pop:pop out the last element coming into the stack
#input：the stack
#output:if the stack is empty, return False; if the stack is not empty, return the last element coming into the stack, and then take it out of the stack.
#
    def pop(self):
        if self.index==-1:
            #print( "The stack is empty right now")
            return False
        elif self.index!=-1:
            popedEle=self.storeList[self.index]
            del self.storeList[self.index]
            self.index=self.index-1
            #print("First element "+str(popedEle)+" is poped")
            return popedEle
#peek: peek at the last element coming into the stack
#input:the stack
#output:if the stack is empty, return False, if the stack is not empty, return the last element coming into the stack.
    def peek(self):
        if self.index==-1:
            #print ("The stack is empty right now")
            return False
        elif self.index!=-1:
            #print("The first element in stack is:"+str(self.storeList[self.index]))
            return self.storeList[self.index]
#add: same as push(traditional term)
#input: the stack, elementA
#output:when the stack has not reached the size limit, push the new element into the stack and return True. when it's full, return False .
    def add(self,elementA):
        if self.index<self.size-1:
            self.storeList.append(elementA)
            self.index=self.index+1
            #returnString="element "+str(elementA)+ " is added to the current stack"
            #print (returnString)
            return True
        else:
            #returnString="This stack is full. "+str(elementA)+" will be added to the new stack"
            #print (returnString)
            '''inputA=input("Do you still want to add the item? this will result in data loss. answer'YES' or 'NO'")
            if inputA=="YES":
                self.storeList.append(elementA)
                self.index=self.index+1
            else:
                returnString="You decided to not input new item"
                print (returnString)'''
            return False


class queue:

#the storelist is the list built to mimic the queue data structure
#the head is the top of the list. the top of the queue. aka the first element to be taken out of the queue.
#the tail is the end of the list, the tail of the queue, aka the last element to be added to the queue.
    def __init__(self):
        self.storeList = list()
        self.kind="queue"
        self.head=-1
        self.tail=-1


#check the length of the queue
#input：the queue
#the output: the length of the queue
    def lengthQueue(self):
        self.length=self.tail-self.head
        return self.length

#check if this queue is empty.
#input:the queue
#output: True if the queue is empty, False if the queue is not empty.
    def isEmpty(self):
        self.length=self.lengthQueue()
        if self.length==0:
            returnValue=True
        elif self.length!=0:
            returnValue=False
        return returnValue


#add: just like push. add elementA to the end of the queue.
#input: the queue, elementA to be added to the queue
#output: return True. and then add one to the tail of the queue.
 def add(self,elementA):

        self.storeList.append(elementA)
        self.length = self.lengthQueue()
        #returnString="element "+str(elementA)+ " is added to the queue, and there are "+str(self.length)+ " animals at the shelter now"
        #print (returnString)
        self.tail=self.tail+1
        return True
#to pop an element from the top of the queue.
#input:the queue
#output: if the queue is empty, return False.
#        if the queue is not empty, return the top element of the queue,
#               and move the head to the next element in queue.
    def pop(self):
        self.length = self.lengthQueue()
        if self.length==0:
            #print( "The shelter is empty right now")
            return False
        elif self.length!=0:
            popedEle=self.storeList[self.head+1]
            del self.storeList[self.head+1]
            self.head=self.head+1
            #print("First element in the queue "+str(popedEle)+" is poped")
            return popedEle
#peek: to take a look at the top of the queue.
#input:the queue
#output: the top element of the queue. if the queue is empty, return False.
    def peek(self):
        self.length=self.lengthQueue()
        if self.length==0:
            #print ("The shelter is empty right now")
            return False
        elif self.length!=0:
            #print("The first element in queue is:"+str(self.storeList[self.index]))
            return self.storeList[self.head+1]




