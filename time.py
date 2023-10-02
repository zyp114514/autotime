import time

a = 0
while a < 100 :
  a = a+1
  time.sleep(200)
  print(a)
  if a == 100 :
    a = 0
