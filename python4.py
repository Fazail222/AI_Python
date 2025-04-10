# class Stack:
#     def __init__(self):  # constructor
#         self.stack=[]
#     def push(self,item):  # add element in stack
#         self.stack.append(item)

#     def pop(self):      # remove last element
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()

#     def peek(self,item):  # return top element
#         if self.is_mpty():
#             return "Stack is empty"
#         return self.stack[-1]
#     def isEmpty(self):    # return true if stack empty
#         return len(self.stack)==0
    
#     def size(self): # return stack size
#         return len(self.stack)
#     def display(self):  # display stack element
#         print("Stack elements:- ")
#         print(self.stack[0::])

# s = Stack()
# s.push("apple")
# s.push("orange")
# s.push("bannana")
# s.push("melon")
# s.push("watermelon")
# s.display()
# s.pop()
# s.pop()
# s.display()
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,item): 
#         self.queue.append(item)
#     def dequeue(self):
#         if self.is_empty():
#             return "Queue is Empty:"
#         return self.queue.pop(0)
#     def is_empty(self):
#         return len(self.queue)==0
#     def display(self):  # display stack element
#         print("Queue elements:- ")
#         print(self.queue[0::])
    
# q=Queue()
# q.enqueue("apple")
# q.enqueue("orange")
# q.enqueue("bannana")
# q.enqueue("melon")
# q.enqueue("watermelon")
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()       

def BS(lis,left,right,target):
    if left > right:
        return False
    mid =left + (right - left )//2
    if target == lis[mid]:
        return True
    if target > lis[mid]:
        return BS(lis,mid+1,right,target)
    elif target < lis[mid]:
        return BS(lis,left,mid-1,target)

lis=[1,2,3,4,5]

print(BS(lis,0,len(lis)-1,0))