# read file input
import sys

with open(sys.argv[1], 'r') as instructions:
  contents = instructions.readlines()

# store plateau coordinate in var
plateau_size = contents.pop(0).strip().split()

cardinal_degrees = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
cardinal_degrees_reverse = {v: k for k, v in cardinal_degrees.items()}

def calculate_position(x, y, h):
  if h == 'N':
    position = (x, y+1)
  elif h == 'S':
    position = (x, y-1)
  elif h == 'E':
    position = (x+1, y)
  elif h == 'W':
    position = (x-1, y)
  return position

# define a function to determine the rover's orientation
# L and R instructions determine what the rover's heading will be
# if the move is M ignore it
# directions for each rover should be separated
def calculate_heading(h, turn):
  cardinal_degree = cardinal_degrees[h]
  if turn == 'L':
    new_degree = cardinal_degree - 90
  elif turn == 'R':
    new_degree = cardinal_degree + 90
  new_degree = new_degree % 360
  return cardinal_degrees_reverse[new_degree]

def rover(start, directions):
  x, y, h = start
  for d in directions:
    if d == 'M':
      x, y = calculate_position(x, y, h)
    else:
      h = calculate_heading(h, d)
  print(x, y, h)

# iterate over instructions, pass start and direction to rover
for i in range(0, len(contents)-1, 2):
  start = contents[i].strip()
  x, y, h = start.split(' ')
  x = int(x)
  y = int(y)
  directions = contents[i+1].strip()
  rover((x, y, h), directions)