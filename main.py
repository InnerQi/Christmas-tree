#Christmas tree

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for element in picture:
  for pixel in element:
    if (pixel == 1):
      print('*',end='')
    else:
      print(' ',end='')
  print('')