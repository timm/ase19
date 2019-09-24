#!/usr/bin/env python3 
# vim: nospell:sta:et:sw=2:ts=2:sts=2

from lib   import *
from div2  import Div2
from thing import Sym

def sym(i):
  #return [i, r()]
  if i<0.4: return [i, "a"]
  if i<0.6: return [i, "b"]
  return           [i, "c"]

def num(i):
  #return [i, r()]
  if i<0.4: return [i,     r()*0.1]
  if i<0.6: return [i, 0.4+r()*0.1]
  return           [i, 0.8+r()*0.1]

def x():
  seed(1)
  n = 5
  return  [      r()*0.05 for _ in range(n)] + \
          [0.2 + r()*0.05 for _ in range(n)] +  \
          [0.4 + r()*0.05 for _ in range(n)] +   \
          [0.6 + r()*0.05 for _ in range(n)] +    \
          [0.8 + r()*0.05 for _ in range(n)] 

def xnum():
  return  [num(one) for one in x()] 

def xsym():
  return  [sym(one) for one in x()] * 20

def demo1():
  print("\n----| demo1 |----------------------")
  d = Div2(xnum())
  for x in d.ranges:
     print('%s x.n %4s | x.lo %6.5f x.hi %6.5f | y.lo %6.5f y.hi %6.4f' % (
           x.rank, x.n, x.lo, x.hi, x.stats.lo, x.stats.hi)) 


def demo2():
  print("\n----| demo2 |----------------------")
  #         0      1      2      4      4      5
  d = [[ 1,1],[ 2,1],[ 3,1],[ 4,1],[ 5,1],[ 6,1],
       [ 7,1],[ 8,1],[ 9,1],[10,1],[11,1],[12,1],
       [13,2],[14,2],[15,2],[16,2],[17,2],[18,2]]
  d = Div2(d,x=first, y=last)
  for x in d.ranges:
     print('%s x.n %3s | x.lo %4s x.hi %4s | y.lo %6.4f y.hi %6.4f' % (
           x.rank, x.n, x.lo, x.hi, x.stats.lo, x.stats.hi)) 


def demo3():
  print("\n----| demo3 |----------------------")
  d = Div2(xsym(),yis=Sym)
  for x in d.ranges:
     print('%s x.n %4s | x.lo %6.5f x.hi %6.5f | y.mode %s y.ent %6.4f' % (
           x.rank, x.n, x.lo, x.hi, x.stats.mode, x.stats.ent())) 

def demo4():
  print("\n----| demo4 |----------------------")
  #         0      1      2      4      4      5
  d = [
       [ 1,1],[ 2,1],[ 3,1],[ 4,1],[ 5,1],[ 6,1],
       [ 7,1],[ 8,1],[ 9,1],[10,1],[11,1],[12,1],
       [13,2],[14,2],[15,2],[16,2],[17,2],[18,2],
       [ 20,1],[ 21,1],[ 22,1],[ 23,1],[ 24,1],[ 25,1],
       [ 26,1],[ 27,1],[ 28,1],[29,1],[30,1],[31,1]]*100
  d = Div2(d,x=first, y=last)
  for x in d.ranges:
     print('%s x.n %3s | x.lo %4s x.hi %4s | y.lo %6.4f y.hi %6.4f y.sd %6.4f' % (
           x.rank, x.n, x.lo, x.hi, x.stats.lo, x.stats.hi,x.stats.sd())) 

if __name__ == "__main__":
  demo1()
  demo2()

  demo3()
  demo4()
