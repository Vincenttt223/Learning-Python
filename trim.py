def trim(s):
    if s == '':
        return s  # 首先判断str s 是否为''
    while s[0] == ' ':  # 如果有Str前空格
        s = s[1:]  # 删除空格 直到没有空格
        if s == '':  # 判断是否全是空格 是的话就返回s 然后Break 不然会出现 IndexError: string index out of range 因为还要判断Str后面是否存在空格
            return s
            break
    while s[-1] == ' ':  # 同上 删除Str后空格
        s = s[:-1]
    return s
