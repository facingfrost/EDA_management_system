import pandas as pd
import sqlite3
import numpy as np



def df_to_sqlite(df,table_name):
    conn = sqlite3.connect('EDA_data.db')
    primary_key = pd.DataFrame(np.array(range(len(df))), columns=["id"])
    tag = pd.DataFrame(np.array([0 for i in range(len(df))]), columns=["tag"])
    primary_key.index = df.index
    tag.index = df.index
    df = pd.concat([primary_key,df,tag],axis=1,sort=False)
    print(df)
    df.to_sql(table_name, conn, if_exists='replace', index=True)
    conn.close()


def extract_tables_names():
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('EDA_data.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 查询所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # 获取查询结果
    tables = cursor.fetchall()

    # 打印所有表名
    table_names = []
    for table in tables:
        table_names.append(table[0])

    # 关闭游标和连接
    cursor.close()
    conn.close()
    return table_names



def sqlite_to_df(table_name):
    with sqlite3.connect('EDA_data.db') as con:
        c = con.cursor()
        packs = pd.read_sql("SELECT * FROM "+table_name, con=con)
        # 输出提取出的表的信息
        # 表的大小
        # print(packs.shape)
        # 表中的数据类型
        # print(packs.dtypes)
        # 前几行数据
        # print(packs.head())
        return packs

def label_artifact(table_name,idx):
    conn = sqlite3.connect('EDA_data.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 查询所有表名
    cursor.execute("update "+table_name+" set tag = 1 where id in (SELECT id FROM "+table_name+" WHERE id>="+str(idx)+" and id<"+str(idx+40)+")")
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

def label_not_artifact(table_name,idx):
    conn = sqlite3.connect('EDA_data.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 查询所有表名
    cursor.execute("update "+table_name+" set tag = 0 where id in (SELECT id FROM "+table_name+" WHERE id>="+str(idx)+" and id<"+str(idx+40)+")")
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

if __name__ == "__main__":
    label_artifact("data_6",10)