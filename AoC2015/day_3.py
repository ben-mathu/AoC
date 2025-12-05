with open('AoC2015/input/3_presents_e.txt', 'r') as f:
  line = f.readline()
  
  dc = {'>': 0, '<': 0, '^': 0, 'v': 0}
  for s in line:
    dc[s] += 1

  hc = 0
  for k in dc:
    if dc[k] != 0:
      hc += dc[k]
  print(hc)