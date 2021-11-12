
def get_quiz(disaster):
    import pymysql
    conn = pymysql.connect(host='localhost',user='void',password='v1234',db='pompeii',charset='utf8')
# conn=pymysql.connect(host='localhost',user='root',password='',db='',charset='utf-8');
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    first_sql='SELECT * FROM qna where disaster=%s'
    cursor.execute(first_sql,(disaster))
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


# rows=get_quiz('flood')
# print(rows[0])
# for row in rows:
#     print(row)
