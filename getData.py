def Input(filename):
    data = open(filename, "r").read().splitlines()
    
    ## biến phụ
    aux = []

    ## cơ sở
    base, saveBase = [], []

    ## biến giả có thể thêm
    bonus, saveBonus = [], []


    ### lấy thông tin của f(x)
    fx = data[0].split()
    for index, value in enumerate(fx[:-1]):
        fx[index] = float(value)


    ### lấy thông tin của ràng buộc
    const = [value.split() for _, value in enumerate(data[1:])]
    for index, value in enumerate(const):
        for sub_index, sub_value in enumerate(value[:-2]):
            value[sub_index] = float(sub_value)
        ### tách a_i, b_i thành 2 phần [thông tin của a_i, thông tin của b_i]
        const[index] = [const[index][:-2], [const[index][-2:][0], float(const[index][-2:][1])]]


    ### chuyển về dạng đơn hình
    for index, value in enumerate(const):
        
        
        ## Kiểm tra b[i] có âm hay không
        if value[1][1] < 0:
            const[index][1][0] = "<=" if const[index][1][0] == ">=" else const[index][1][0]
            const[index][1][1] =  -const[index][1][1]
            const[index][0] = [-element for element in const[index][0]]
        
        if value[1][0] == "=":
            bonus.append(index)
        if value[1][0] == "<=":
            # thêm biến phụ
            for sub_index, _ in enumerate(const):
                const[sub_index][0].append(0)
            const[index][0][-1], const[index][1][0] = 1, "="
            base.append(len(const[index][0]))
            saveBase.append(len(const[index][1]))
        if value[1][0] == ">=":
            # thêm biến phụ
            for sub_index, _ in enumerate(const):
                const[sub_index][0].append(0)
            const[index][0][-1], const[index][1][0] = -1, "="
            bonus.append(index)
            aux.append(len(const[index][0]))

    ## kiểm tra biến giả (M)
    if len(base) != len(data[1:]):
        while len(base) < len(data[1:]) or len(bonus):
            for index, value in enumerate(const):
                const[index][0].append(0)
            const[bonus[0]][0][-1] = 1
            base.append(len(const[bonus[0]][0]))
            bonus = bonus[1:] if len(bonus) > 0 else []
            saveBonus.append(saveBonus[-1] + 1 if len(saveBonus) else len(const[0][0]))
 
    return base, const, saveBonus, aux