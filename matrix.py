def hello():
  print("Hello World")

lst = [10, 30, 40]  

tuple = (10, 20, 40)

def sum(L=None):
  if len(L) == 1:
    return L[0]
  else:
    return L[0] + sum(L[1:])

def logs():
  print('*'*100)
  
