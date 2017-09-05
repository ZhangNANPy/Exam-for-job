'''n = 7
e_l = [10, 20, 30, 40, 50, 60, 70]
f_l = [[1,2], [3,1], [3,7], [1,4], [1,5], [6,1]]'''
n=5
e_l = [19, 100, 58, 44, 80]
f_l = [[1,2], [2,4], [2,5], [1,3]]

def maxEfficiency(n, e_l, f_l):
    exclusion = {}
    for i in range(1, n+1):
        exclusion[i] = []
        for j in f_l:
            if i in j:
                if i == j[0]:
                    exclusion[i].append(j[1])
                elif i == j[1]:
                    exclusion[i].append(j[0])
    ratio_l = {}
    for i in range(1, n+1):
        ratio = sum(exclusion[i]) / e_l[i - 1]
        if ratio in ratio_l.keys():
            ratio_l[ratio].append(i)
        else:
            ratio_l[ratio] = [i]
    m4use = set([i for i in range(1, n+1)])
    sume = 0
    for i in sorted(list(ratio_l.keys())):
        for m in ratio_l[i]:
            if m in m4use:
                sume += e_l[m-1]
                m4use = m4use - set(exclusion[m])
    return sume

if __name__ == '__main__':
    print(maxEfficiency(n, e_l, f_l))