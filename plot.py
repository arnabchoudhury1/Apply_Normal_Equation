# import tensorflow as tf
# import numpy as np
import pandas as pd
print("1")
import matplotlib.pyplot as plt
print("2")
import csv
print("3")

#data = pd.read_csv("data.csv").to_dict(orient="row")
df = pd.read_csv("data.csv")
data = df.values.T.tolist()
#print(data['brain_weight'])
print(data)
plt.plot(data[1], data[2], 'ro')

plt.ylabel('Brain Weight')
plt.xlabel('Body Weight')

plt.show()

