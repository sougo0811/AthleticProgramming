def excepted_value(probability, value):
  return sum([p * v for p, v in zip(probability, value)])

if __name__ == "__main__":
  probability = list(map(float,input().split()))
  value = list(map(float,input().split()))
  print(excepted_value(probability, value))