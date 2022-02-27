import random
i = input("Enter Count:")
for x in xrange(i):
  ip = ""
  ip += ".".join(map(str, (random.randint(0, 255)
                          for i in range(4))))
  open('Gen.txt','a').write(str(ip) + '\n')

  print ip
