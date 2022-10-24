def Output(const, saveBonus, Base, aux):
    print("Các ràng buộc")
    for index, value in enumerate(const):
        print("{}x1".format(value[0][0]), end = " ")
        for sub_index, sub_value in enumerate(value[0][1:]):
            sign = "-" if sub_value < 0 else "+"
            print("{} {}x{}".format(sign, abs(sub_value), sub_index+2),end = " ")
        print("{} {}".format(value[1][0], value[1][1]))

    print("Trong đó:")
    print("X: " + ",".join([str(i) for i in saveBonus]) + " là biến giả") if len(saveBonus) else ""
    print("X: " + ",".join([str(i) for i in aux if i not in saveBonus]) + " là biến phụ") if len([i for i in aux if i not in saveBonus]) else ""

    print("X: 1 -> {} >= 0".format(max( max(saveBonus+[0]) , max( max(Base+[0]), max(aux+[0]) ) )))

    print("Cơ sở: ", Base)