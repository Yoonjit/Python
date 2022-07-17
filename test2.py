# 이중 연결 리스트를 이용한 덱
# 자료구조론 과제로 냈던 거

n = int(input("연산의 횟수를 입력하세요: "))
cnt = 0

class DNode:
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedDeque:
  def __init__(self):	
    self.front = None
    self.rear = None

  def is_empty(self):
    return self.front == None		
      
  def clear(self):
    self.front = self.front = None	

  def size(self):			
    node = self.front			
    count = 0
    while not node == None:
      node = node.next	
      count += 1			
    return count			

  def display(self): 
    print(' ', end=' ')
    node = self.front			
    while not node == None :	 	
      print(node.data, end=' ')	
      node = node.next
    print("<- %d번째 연산(P)에 의한 출력" %cnt)

  def add_front(self, item):
    node = DNode(item, None, self.front)
    if(self.is_empty()):				
      self.front = self.rear = node	
    else :								
      self.front.prev = node			
      self.front = node			

  def add_rear(self, item):
    node = DNode(item, self.rear, None)	
    if(self.is_empty()):
      self.front = self.rear = node	
    else:								
      self.rear.next = node			
      self.rear = node				

  def delete_front(self):
    if self.is_empty():
        print("underflow <- %d번째 연산(DF)에서 underflow 발생, 실행을 종료함" %cnt)
        return exit()
    else:
      data = self.front.data			
      self.front = self.front.next	
      if self.front == None:			
        self.rear = None			
      else:
        self.front.prev = None

  def delete_rear(self):
    if self.is_empty():
        print("underflow <- %d번째 연산(DR)에서 underflow 발생, 실행을 종료함" %cnt)
        return exit()
    else:
      data = self.rear.data
      self.rear = self.rear.prev
      if self.rear == None:
        self.front = None
      else:
        self.rear.next = None

dq = DoublyLinkedDeque()

for i in range(n):
  a, b = input("연산의 종류와 원소의 이름을 입력하세요 (원소 입력이 필요없을 경우 None 입력): ").split()

  if a == "AF":
    cnt += 1
    dq.add_front(b)
  elif a == "AR":
    cnt += 1
    dq.add_rear(b)
  elif a == "DF":
    cnt += 1
    dq.delete_front()
  elif a == "DR":
    cnt += 1
    dq.delete_rear()
  elif a == "P":
    cnt += 1
    dq.display()