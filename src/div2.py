#!/usr/bin/env python3 
# vim: nospell:sta:et:sw=2:ts=2:sts=2
"""
Divide numbers.
"""

import math
from   lib   import THE,Pretty,same,first,last,ordered
from   copy  import deepcopy as kopy
from   thing import Num,Sym

class Div2(Pretty):
  """
  Recursively divide a list of numns by finding splits
  that minimizing the expected value of the standard
  deviation (after the splits).
  """
  def __init__(i,lst, x=first, xis=Num, y=last, yis=Num):
    i.x, i.y   = x,y
    i.xis      = lambda lst=[]: xis(lst, key=i.x) # a collector for x things
    i.yis      = lambda lst=[]: yis(lst, key=i.y) # a collector for y things
    i._lst     = ordered(lst,key=x)
    i.xs       = i.xis(i._lst)
    i.ys       = i.yis(i._lst)
    i.gain     = 0                             # where we will be, once done
    i.step     = int(len(i._lst)**THE.div.min) # each split need >= 'step' items
    i.stop     = x(last(i._lst))               # top list value
    i.start    = x(first(i._lst))              # bottom list value
    i.ranges   = []                            # the generted ranges
    i.epsilon  = i.xs.sd() * THE.div.cohen     # bins must be seperated >= epsilon
    i.__divide(1, len(i._lst), i.xs, i.ys, 1)

  def __divide(i, lo, hi, xr, yr, rank):
    """Find a split between lo and hi, then recurse on each split.
     If no split can be found then assign everything a rank of 'rank'.
     'xr' and 'yr' are statistics on the whole x,y space from lo to hi."""
    xb4       = kopy(xr)
    xb4.stats = kopy(yr)
    xl        = i.xis()
    yl        = i.yis()
    best      = yr.variety()
    cut       = None
    for j in range(lo,hi):
      xl + i._lst[j]
      yl + i._lst[j]
      xr - i._lst[j]
      yr - i._lst[j]
      if xl.n >= i.step:
        if xr.n >= i.step:
          now   = i.x( i._lst[j]   ) 
          after = i.x( i._lst[j+1] ) 
          if now == after: continue
          if abs(xr.mu - xl.mu) >= i.epsilon:
            if after - i.start >= i.epsilon:
              if i.stop - now >= i.epsilon: 
                xpect = yl.xpect(yr)
                if xpect*THE.div.trivial < best:
                  best, cut = xpect, j+1
    if cut:
      ls   = i._lst[lo:cut]
      rs   = i._lst[cut:hi] 
      rank = i.__divide(lo, cut, i.xis(ls), i.yis(ls), rank) + 1
      rank = i.__divide(cut, hi, i.xis(rs), i.yis(rs), rank)
    else:
      xb4.rank  = rank
      i.ranges += [ xb4 ]
    return rank
