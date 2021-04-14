import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset_deep.mnist import load_mnist
from PIL import Image
from common.functions import sigmoid, softmax

# mainで動く関数
def main():
  x, t = get_data()
  network = init_network()

  accuracy_cnt = 0
  for i in range(len(x)):
    y = predict(network, x[i])
    # 複数の確率からmax値を取得します
    p = np.argmax(y)
    # maxの確率がテストラベルと同じかを判定
    if p == t[i]:
      accuracy_cnt += 1
  print("Accuracy: " + str(float(accuracy_cnt) / len(x)))

# ソフトマックス関数
def softmax(a):
  c = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a

  return y

# 訓練画像とテスト画像の2枚を取得します
def get_data():
  # (訓練画像, 訓練ラベル), (テスト画像, テストラベル)
  (x_train, t_train), (x_test, t_test) = (
    load_mnist(normalize=True, flatten=True, one_hot_label=False)
  )
  return x_test, t_test

# ネットワークを構築する(重みパラメータとバイアスを取得)
def init_network():
  with open("sample_weight.pkl", 'rb') as f:
    network = pickle.load(f)

  return network

# 
def predict(network, x):
  # 重みパラメータとバイアスをそれぞれ取得する
  w1, w2, w3 = network['W1'], network['W2'], network['W3']
  b1, b2, b3 = network['b1'], network['b2'], network['b3']

  # シグモンド関数でバイアスを三回計算にかける
  a1 = np.dot(x, w1) + b1
  z1 = sigmoid(a1)

  a2 = np.dot(z1, w2) + b2
  z2 = sigmoid(a2)

  a3 = np.dot(z2, w3) + b3
  y = softmax(a3)

  return y

if __name__ == '__main__':
  main()