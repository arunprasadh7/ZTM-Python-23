# Our first GUI - printing a tree pattern using loops

picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
  for item in row:
    if item == 0:
      print(' ', end='')
    elif item == 1:
      print('*', end  ='')
  print()