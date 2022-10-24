import pandas as pd
from getData import Input
from outData import Output

source_data = "data.txt"
fx, base, const, saveBonus, aux = Input(source_data)
order = [0] * len(base)
for i, element in enumerate(base):
    order[[index+1 for index, value in enumerate(const) if value[0][element-1] == 1][0]-1] = element
Output(fx, const, saveBonus, base, aux + base)
data = pd.read_csv("test.csv")

print(data)