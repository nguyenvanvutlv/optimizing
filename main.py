from getData import Input
from outData import Output
from calculator import sol


source_data = "data.txt"
fx, base, const, saveBonus, aux = Input(source_data)
order = [0] * len(base)
for i, element in enumerate(base):
    order[[index+1 for index, value in enumerate(const) if value[0][element-1] == 1][0]-1] = element
# Output(fx, const, saveBonus, base, aux + base)

answer_start = [0] * len(const[0][0])
for i,j in enumerate(order):
    answer_start[j-1] = const[i][1][1]
print("Phương án xuất phát: ")
print(answer_start)


sol(fx[:-1] + [0] * (len(const[0][0]) - len(fx[:-1])), order, const, answer_start, saveBonus, fx[-1])