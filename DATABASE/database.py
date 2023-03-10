# 导入所需的库
import pymysql
import invoke_vehicle_model as invoke
# 连接配置
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='199899', 
                    #    db='data',#调用data数据库
                       port= 3306,
                       charset='utf8')
       

# 游标1
cur = conn.cursor()
#游标2
# cur2 = conn.cursor()

# 希望建立一个data数据库，不确定以前是否建立过，先进行删除
# sql = 'DROP DATABASE data;'
# cur.execute(sql)

# 创建数据库（创建完后不屏蔽会报错）
# sql1 = "CREATE DATABASE data;"
# cur.execute(sql1)

#调用data数据库
sql2 = "USE data;"
cur.execute(sql2)

#删除data数据库的表parameter
# sql3 = "DROP TABLE IF EXISTS parameter"
# cur.execute(sql3)

# 创建表名为parameter的数据表（创建完后不屏蔽会报错）
# `Torque_FL[N·m]` double, `Torque_FR[N·m]` double, `Torque_RL[N·m]` double, `Torque_RR[N·m]` double, `delta_f[deg]` double, `Mu` double, `X0[m]` double,`Y0[m]` double, `Vx[m/s]` double, `Vy[m/s]` double, `Vz[m/s]` double, `ax[g]` double, `ay[g]` double, `az[g]` double, `Yaw[rad]` double, `Pitch[rad]` double, `Roll[rad]` double, `RollRate[rad/s]` double,  `PitchRate[rad/s]` double, `YawRate[rad/s]` double, `RollAcceleration[rad/s^2]` double, `PitchAcceleration[rad/s^2]` double, `YawAcceleration[rad/s^2]` double,  `Fx_fl[N]` double, `Fx_fr[N]` double, `Fx_rl[N]` double, `Fx_rr[N]` double, `Fy_fl[N]` double, `Fy_fr[N]` double, `Fy_rl[N]` double, `Fy_rr[N]` double, `Fz_fl[N]` double, `Fz_fr[N]` double, `Fz_rl[N]` double, `Fz_rr[N]` double, `beta[rad]` double, `d_beta[rad/s]` double, `Omega_fl[rad/s]` double, `Omega_fr[rad/s]` double, `Omega_rl[rad/s]` double, `Omega_rr[rad/s]` double, Sx_fl double, Sx_fr double, Sx_rl double, Sx_rr double, `time_t[s]` double
sql4 = "create table parameter( `Torque_FL[N·m]` double,\
                                 `Torque_FR[N·m]` double, \
                                 `Torque_RL[N·m]` double, \
                                 `Torque_RR[N·m]` double, \
                                 `delta_f[deg]` double, \
                                 `Mu` double,\
                                 `X0[m]` double,\
                                 `Y0[m]` double,\
                                 `Vx[m/s]` double, \
                                 `Vy[m/s]` double, \
                                 `Vz[m/s]` double, \
                                 `ax[g]` double, \
                                 `ay[g]` double, \
                                 `az[g]` double, \
                                 `Yaw[rad]` double, \
                                 `Pitch[rad]` double, \
                                 `Roll[rad]` double,\
                                 `RollRate[rad/s]` double, \
                                 `PitchRate[rad/s]` double, \
                                 `YawRate[rad/s]` double,\
                                 `RollAcceleration[rad/s^2]` double,\
                                 `PitchAcceleration[rad/s^2]` double, \
                                 `YawAcceleration[rad/s^2]` double, \
                                 `Fx_fl[N]` double, \
                                 `Fx_fr[N]` double, \
                                 `Fx_rl[N]` double, \
                                 `Fx_rr[N]` double, \
                                 `Fy_fl[N]` double, \
                                 `Fy_fr[N]` double, \
                                 `Fy_rl[N]` double, \
                                 `Fy_rr[N]` double,\
                                 `Fz_fl[N]` double, \
                                 `Fz_fr[N]` double, \
                                 `Fz_rl[N]` double, \
                                 `Fz_rr[N]` double, \
                                 `beta[rad]` double,\
                                 `d_beta[rad/s]` double, \
                                 `Omega_fl[rad/s]` double, \
                                 `Omega_fr[rad/s]` double, \
                                 `Omega_rl[rad/s]` double, \
                                 `Omega_rr[rad/s]` double, \
                                 `Sx_fl` double, \
                                 `Sx_fr` double, \
                                 `Sx_rl` double, \
                                 `Sx_rr` double, \
                                 `time_t[s]` float\
                                 );"
cur.execute(sql4)

# 修改指定字段 alter table 表名 change 原字段名字 新的字段名字 字段类型
# abc = "alter table parameter change a d int"
# cur.execute(abc)

# 在表中追加数据
# sql4 = 'insert into name(salary_id, employer_name, salary_amount, actual_salary) values (%s,%s,%s,%s)'
# cur.execute(sql4,(100,'王哈哈', 200, 300))
# cur.execute(sql4,(200,'哈哈', 100, 300))
# conn.commit()#添加数据改变了原来表的结构，因此要用此语句，才能真正在mysql中添加新的数据



# cur.execute('select * from data')#在data的表里面查询所有内容
# 游标2
# cur2.execute('desc data')#输出数据结构

# result = cur.fetchall()
# 游标2
# result2 = cur2.fetchall()

# print(result)
# print(result2)

# # 查找result中的数据
# sql5 = "select * from name where employer_name = '王哈哈' ;"
# cur.execute(sql5)
# row = cur.fetchone() # 获取单条数据
# print(row)

# sql6 = "select * from name ;"
# cur.execute(sql6)
# row1 = cur.fetchall()#获取所有数据
# print(row1)

# sql7 = "select * from name where employer_name = '李哈哈' or employer_name = '哈哈' ;"
# cur.execute(sql7)
# row2 = cur.fetchall() # 获取单条数据
# print(row2)

# #删除数据表
# sql8 = "delete from name where employer_name = '王哈哈' ;"
# cur.execute(sql8)
# conn.commit()

# #修改数据表中的数据
# sql9 = "update name set employer_name = '哈哈' where employer_name = '李哈哈' ;" #将employer_name下的所有李哈哈都改为哈哈
# cur.execute(sql9)
# conn.commit()#提交到数据库

# sql10 ='delete from parameter where `Vx[m/s]` < 16 '
# cur.execute(sql10)
# conn.commit()

cur.close()
conn.close()