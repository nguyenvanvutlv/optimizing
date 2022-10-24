from getData import Input
from outData import Output

source_data = "data.txt"
fx, base, const, saveBonus, aux = Input(source_data)
Output(fx, const, saveBonus, base, aux + base)