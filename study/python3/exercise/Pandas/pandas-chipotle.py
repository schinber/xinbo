"""
1 - 开始了解你的数据
探索Chipotle快餐数据
– 将数据集存入一个名为chipo的数据框内  --data
– 查看前10行内容
– 数据集中有多少个列(columns)？
– 打印出全部的列名称
– 数据集的索引是怎样的？
– 被下单数最多商品(item)是什么?
– 在item_name这一列中，一共有多少种商品被下单？
– 在choice_description中，下单次数最多的商品是什么？
– 一共有多少商品被下单？
– 将item_price转换为浮点数
– 在该数据集对应的时期内，收入(revenue)是多少？
– 在该数据集对应的时期内，一共有多少订单？
– 每一单(order)对应的平均总价是多少？
————————————————
版权声明：本文为CSDN博主「王大阳_」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43746433/article/details/90454463
"""
import pandas as pd

data = pd.read_csv(r'F:\Python\data_center\Pandas_exercises_master/\chipotle.tsv', sep='\t')
print(data)
print