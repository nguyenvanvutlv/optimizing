from getData import Input
from outData import Output

source_data = "data.txt"
base, const, saveBonus, aux = Input(source_data)
Output(const, saveBonus, base, aux + base)