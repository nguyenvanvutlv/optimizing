def Output(fx, const, saveBonus, Base, aux):
    print("Bài toán ở dạng chuẩn\nF(X): " + str(fx[0])+"x1",end = " ")
    for i,j in enumerate(fx[1:-1]):
        sign = "-" if j < 0 else "+"
        print("{} {}x{}".format(sign, abs(j),i+2),end = " ")
    for i,j in enumerate(sorted([x for x in aux if x not in saveBonus])):
        print("+ 0x{}".format(abs(j)),end = " ")        
    for i,j in enumerate(sorted(saveBonus)):
        print("- Mx{}".format(abs(j)),end = " ")   
    print(" --> ", fx[-1])

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