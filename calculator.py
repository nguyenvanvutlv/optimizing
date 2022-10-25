from sklearn.utils import column_or_1d


def sol(fx, order, const, answer_start, saveBonus, target):
    """
     max -> âm nhỏ nhất
     min -> dương lớn nhất
    """
    for i in saveBonus:
        fx[i-1] = -1

    table = []
    for index, element in enumerate(const):
        table.append([-1 if order[index] in saveBonus else 0] + [order[index], element[1][1]] + element[0])
    for index, element in enumerate(table):
        print(element)
    
    while True:
        ## khởi tạo delta
        result = [0] * (len(fx) + 1)


        ## tính f(x) = sum(cj * P/a)
        result[0] = sum([element[0] * element[2] for index, element in enumerate(table)])

        ## tính delta_i của mỗi x = sum(cj * aj - xj)
        for index, element in enumerate(result[1:]):
            result[index+1] = sum([j[0] * j[3 + index] for i,j in enumerate(table)]) - fx[index]
        print(result)

        ## tìm cột xoay chọn giá trị âm nhỏ nhất nếu max hoặc giá trị dương lớn nhất nếu min từ delta_i
        """
            value_rotate: giá trị để chọn max hoặc min
            index_find_rotate: chỉ số cột để xoay
            column: ô để xoay
        """
        value_rotate = min(result[1:]) if target == "max" else max(result[1:])
        index_find_rotate = [index for index, element in enumerate(result) if element == value_rotate][0]
        current_lambda = [None if element[2 + index_find_rotate] <= 0 else (element[2] / element[2 + index_find_rotate]) for index, element in enumerate(table)]
        column = [index for index, element in enumerate(current_lambda) if element == min(current_lambda)][0]
        

        old_base = table[column][1]

        ## tính toán lại bảng mới
        table[column][1] = index_find_rotate
        table[column][0] = fx[index_find_rotate - 1]
        for index, element in enumerate(table[column][2:]):
            table[column][index+2] /= table[column][index_find_rotate + 2]

        for index, element in enumerate(table):
            if index == column:
                continue
            ### fix
        
        for element in table:
            print(element)
        print()
        print()

        break
