import pandas as pd
import sqlite3
import numpy as np


conn = sqlite3.connect('EDA_data.db')

# 创建游标对象
cursor = conn.cursor()

# 查询所有表名
cursor.execute("update data_6 set tag = 1 where id in (SELECT id FROM data_6 WHERE id<10)")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
# 获取查询结果
results = cursor.fetchall()

print(results)

# 关闭游标和连接
cursor.close()
conn.close()
