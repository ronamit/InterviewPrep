import string

def checkValidFoo(s):
      if not isinstance(s, str): 
          return False
      if s is '': 
          return False
      lst = s.split('+')
      if len(lst) < 2:
          return False
      for a in lst:
          if a == '':
              return False
          i = 0
          while a[i] == ' ' and i <= len(a) - 1:
              i += 1
      if i == len(a):
          return False
      j = len(a) - 1
      while j >= 0 and a[j] == ' ':
          j -= 1
      for k in range(i, j + 1):
          c = a[k]
          if c not in string.digits:
              return False
      return True


s = "3+2 "
print(checkValidFoo(s))