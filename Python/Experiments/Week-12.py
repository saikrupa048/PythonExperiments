import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [10, 20, 30, 40]

arr = np.array(data)
df = pd.DataFrame(arr, columns=["Values"])

print(df)

plt.plot(arr)
plt.show()