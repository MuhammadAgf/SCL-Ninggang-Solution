class park:
  stayl = -1
  stayr = -1
  cross = -1

  def __init__(self, points):
    maxl = 0
    suml = 0
    for p in points:
      suml += p
      maxl = max(maxl, suml)

    maxr = 0
    sumr = 0
    for p in points[::-1]:
      sumr += p
      maxr = max(maxr, sumr)

    self.cross = suml
    self.stayl = maxl
    self.stayr = maxr
  
  def print(self):
    print('sl:', self.stayl)
    print('sr:', self.stayr)
    print('xx:', self.cross)

def dp2(days):
  n = len(days)
  state = [{True: None, False: None} for _ in range(n)]

  state[n-1][True] = max(days[n-1].stayr, days[n-1].cross)
  state[n-1][False] = max(days[n-1].stayl, days[n-1].cross)
  for d in range(n-1)[::-1]:
    r_stay  = days[d].stayr + state[d+1][True]
    r_cross = days[d].cross + state[d+1][False]
    state[d][True] = max(r_stay, r_cross)

    l_stay  = days[d].stayl + state[d+1][False]
    l_cross = days[d].cross + state[d+1][True]
    state[d][False] = max(l_stay, l_cross)

  return state[0][False]

def solve(n, m, farms):
  days = []
  for f in farms:
    days.append(park(f))

  res = dp2(days)
  print(res)

def main():
  tc = int(input())

  for _ in range(tc):
    n,m = input().split()
    n,m = int(n), int(m)

    farms = []
    for _ in range(n):
      pts = input().split()
      pts = [int(d) for d in pts]
      farms.append(pts)
    
    solve(n, m, farms)

if __name__ == '__main__':
  main()
