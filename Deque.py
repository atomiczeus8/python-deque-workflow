Deque=[]

def insertfront(element):
    if len(Deque)>5:
        print("Deque is full. Cannot Insert more elements. Condition: OVERFLOW")
    else:
        Deque.insert(0,element)
        print(f"{element} has been inserted at the front of the Deque")

def insertrear(element):
    if len(Deque)>5:
        print("Deque is full. Cannot insert more elements. Condition: OVERFLOW")
    else:
        Deque.append(element)
        print(f"{element} has been inserted at the rear of the Deque")

def is_empty():
    return len(Deque)==0

def seekfront():
    if is_empty():
        print("Cannot seek an element. Since the Deque is empty Condition: UNDERFLOW")
    else:
        print(f"The front element of the Deque is {Deque[0]}")

def seekrear():
    if is_empty():
        print("Cannot seek an element. Since the Deque is empty Condition: UNDERFLOW")
    else:
        print(f"The rear element of the Deque is {Deque[-1]}")

def deletefront():
    if is_empty():
        print("Cannot delete an element. Since the Deque is empty Condition: UNDERFLOW")
    else:
        element=Deque.pop(0)
        print(f"{element} has been deleted from the front of the Deque")   

def deleterear():
    if is_empty():
        print("Cannot delete an element. Since the Deque is empty Condition: UNDERFLOW")
    else:
        element=Deque.pop(-1)
        print(f"{element} has been deleted from the rear of the Deque")   