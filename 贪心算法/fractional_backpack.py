# _*_coding:utf-8_*_
# created by Amuu on 2021/10/20

goods = [(60, 10), (100, 30), (120, 20)]  # 每个商品元组表示（价格，重量）
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def f_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m, total_v


print(f_backpack(goods, 50))
