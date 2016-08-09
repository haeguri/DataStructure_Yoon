data_num = [10, 100, 1000, 10000, 100000]

def get_ratio(dn):
    total = pow(dn, 2) + dn

    pow_ratio = (pow(dn, 2) / total) * 100
    alone_ratio = (dn / total) * 100

    print("데이터 개수가 {0}개 일 때, n^2+n에서 n이 차지하는 비율은 고작 {1}".format(dn, round(alone_ratio, 3)))

for num in data_num:
    get_ratio(num)