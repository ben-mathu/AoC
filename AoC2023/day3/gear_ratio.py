import re

visited_nodes = {}

with open('./AoC2023/day3/input.txt', 'r') as file:
  f = file.readlines()
  part_number_sum = 0
  def getValue(visiting_node, i, j):
    global visited_nodes
    
    result = ''
    value = f[i][0:j+1]
    for k in range(len(value)-1, -1, -1):
      if (re.compile(r'[0-9]').match(value[k]) and '{}{}'.format(i, k) not in visited_nodes[visiting_node]):
        result = value[k] + result
      else:
        break
      
    value = f[i][j+1:len(f[i])-1]
    for k in range(len(value)):
      if (re.compile(r'[0-9]').match(value[k]) and '{}{}'.format(i, j+k) not in visited_nodes[visiting_node]):
        result = result + value[k]
      else:
        break
    return result
  
  p = re.compile(r'[0-9.\n]')
  num_lines = len(f)
  for i in range(num_lines):
    num_chars = len(f[i])
    for j in range(num_chars):
      if (not p.match(f[i][j])):
        # Found a symbol, so store it in a dictionary
        # visited_nodes['{}{}'.format(i,j)] = []
        
        # add the positions to list
        adj_list = []
        visited_nodes['{}{}'.format(i, j)] = adj_list
        p2 = re.compile(r'[0-9]')
        for di in range(-1, 2, 1):
          for dj in range(-1, 2, 1):
            if ((di != 0 or dj != 0) and p2.match(f[i+di][j+dj])):
              value = getValue('{}{}'.format(i, j), i+di, j+dj)
              print(value)
              
              adj_list.append('{}{}'.format(i+di, j+dj))
              visited_nodes['{}{}'.format(i, j)] = adj_list
              part_number_sum += int(value)
        
        # check character at i-1, j-1
        # p2 = re.compile(r'[0-9]')
        # value = 0
        # if (p2.match(f[i-1][j-1])):
        #   value = getValue(i-1, j-1)
        #   part_number_sum += int(value)
        
        # if (p2.match(f[i-1][j]) and value != f[i-1][j]):
        #   value = getValue(i-1, j-1)
        #   part_number_sum += int(value)
        
        # if (p2.match(f[i-1][j+1]) and value != f[i-1][j+1]):
        #   value = getValue(i-1, j+1)
        #   part_number_sum += int(value)
          
        # if (p2.match(f[i][j-1])):
        #   value = getValue(i, j-1)
        #   part_number_sum += int(value)
        
        # if (p2.match(f[i][j+1])):
        #   value = getValue(i, j-1)
        #   part_number_sum += int(value)
          
        # if (p2.match(f[i+1][j-1])):
        #   value = getValue(i+1, j-1)
        #   part_number_sum += int(value)
          
        # if (p2.match(f[i+1][j]) and f[i+1][j] not in str(value)):
        #   value = getValue(i+1, j)
        #   part_number_sum += int(value)
          
        # if (p2.match(f[i+1][j+1]) and value != f[i+1][j+1]):
        #   value = getValue(i+1, j+1)
        #   part_number_sum += int(value)
  
  print(part_number_sum)