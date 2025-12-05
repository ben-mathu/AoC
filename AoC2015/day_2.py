with open('AoC2015/input/2_area.txt', 'r') as f:
  lines = f.readlines()
  total_area = 0
  for s in lines:
    dimensions = s.strip().split('x')
    area = 2*int(dimensions[0])*int(dimensions[1]) + 2*int(dimensions[1])*int(dimensions[2]) + 2*int(dimensions[0])*int(dimensions[2])
    s_area = min(int(dimensions[0])*int(dimensions[1]), int(dimensions[1])*int(dimensions[2]), int(dimensions[0])*int(dimensions[2]))
    total_area += s_area + area
  print(total_area)
  
  # Part 2
  total = 0
  for s in lines:
    dimensions = s.strip().split('x')
    min_s = min(int(dimensions[0]), int(dimensions[1]))
    min_s_2 = min(int(dimensions[0]) if min_s == int(dimensions[1]) else int(dimensions[1]), int(dimensions[2]))
    sum_a = min_s + min_s + min_s_2 + min_s_2
    
    total += int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2]) + sum_a
  print(total)