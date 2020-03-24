'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    # implement here
        # implement here
    #如果字符长度等于1，则只有1种组合方式
    if len(digitarray) == 1:
        return 1
    
    #设字符长度相同长的列表，储存字符变化数
    list_dym = [0]*len(digitarray)
    
    #遍历字符长度
    for i in range(len(digitarray)):
        #在第0个字符位置，查看前2个字符数字是否符合以下条件
        if i == 0:
            #符合0开头，或者大于2的开头，或者等于2但个位数大于5的字符，有且只有1种组合方式
            if int(digitarray[i]) == 0 or int(digitarray[i]) > 2 or (int(digitarray[i])==2 and int(digitarray[i+1])>5):
                list_dym[0] = 1
                list_dym[1] = 1
            #否则有2种组合方式
            else:
                list_dym[0] = 1
                list_dym[1] = 2
        #从第2个字符位置开始，查看是否有组成符合以下条件的字符数字
        if i >= 2:
            #第i个字符位置一定至少有前一个字符位置组合方式数
            list_dym[i] = list_dym[i-1]
            #如果第i个字符位置和前一个字符位置可以组合符合条件的数字，则加上第i-2个字符位置个数
            if int(digitarray[i-1])==1 or (int(digitarray[i-1])==2 and int(digitarray[i])<=5):
                list_dym[i] += list_dym[i-2]
    #返回最后一位储存列表数字
    return list_dym[-1]
