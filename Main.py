def solve():
  x = (x1+x2)/2
  y = (y1+y2)/2
  return x, y

print("Find midpoint:")
x1 = float(input('Enter a value of x1:\n'))
x2 = float(input('Enter a value of x2:\n'))
y1 = float(input('Enter a value of y1:\n'))
y2 = float(input('Enter a value of y2:\n'))
print("Co-ordinates of midpoint are)", solve(),")")