import numpy as np

"""
AND回路を作成する
---|---|---|
x1 |x2 | y |
---|---|---|
 0 | 0 | 0 |
 1 | 0 | 0 |
 0 | 1 | 0 |
 1 | 1 | 1 |
"""
def AND(x1, x2):
  w1, w2 = 0.5, 0.5 #重み
  theta = 0.7 #闘値(限界値)
  tmp = x1*w1 + x2*w2 #式
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1

# 実行(AND)
print('AND(0, 0) = ' + str(AND(0, 0)))
print('AND(1, 0) = ' + str(AND(1, 0)))
print('AND(0, 1) = ' + str(AND(0, 1)))
print('AND(1, 1) = ' + str(AND(1, 1)))

"""
OR回路を作成する
---|---|---|
x1 |x2 | y |
---|---|---|
 0 | 0 | 0 |
 1 | 0 | 1 |
 0 | 1 | 1 |
 1 | 1 | 1 |
"""
def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5]) #重み
  theta = -0.2
  tmp = np.sum(x*w) + theta
  if tmp <= 0:
    return 0
  else:
    return 1

# 実行(OR)
print('---')
print('OR(0, 0) = ' + str(OR(0, 0)))
print('OR(1, 0) = ' + str(OR(1, 0)))
print('OR(0, 1) = ' + str(OR(0, 1)))
print('OR(1, 1) = ' + str(OR(1, 1)))

"""
NAND回路を作成する
---|---|---|
x1 |x2 | y |
---|---|---|
 0 | 0 | 1 |
 1 | 0 | 1 |
 0 | 1 | 1 |
 1 | 1 | 0 |
"""
def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5]) #重み
  theta = 0.7
  tmp = np.sum(x*w) + theta
  if tmp <= 0:
    return 0
  else:
    return 1

# 実行(NAND)
print('---')
print('NAND(0, 0) = ' + str(NAND(0, 0)))
print('NAND(1, 0) = ' + str(NAND(1, 0)))
print('NAND(0, 1) = ' + str(NAND(0, 1)))
print('NAND(1, 1) = ' + str(NAND(1, 1)))

"""
XOR回路を作成する
---|---|---|
x1 |x2 | y |
---|---|---|
 0 | 0 | 0 |
 1 | 0 | 1 |
 0 | 1 | 1 |
 1 | 1 | 0 |
"""
# XOR回路を関数一つで表すのは無理
# 他の関数を使って表す(層を重ねる)
def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

# 実行(XOR)
print('---')
print('XOR(0, 0) = ' + str(XOR(0, 0)))
print('XOR(1, 0) = ' + str(XOR(1, 0)))
print('XOR(0, 1) = ' + str(XOR(0, 1)))
print('XOR(1, 1) = ' + str(XOR(1, 1)))