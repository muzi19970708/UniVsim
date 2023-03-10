import DOF14 as DF
import csv
import pymysql

# 连接配置
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='199899', 
                       db='data',#调用data数据库
                       port= 3306,
                       charset='utf8')

cur = conn.cursor()
       
List_X0 = []
List_Y0 = []
List_Vx = []
List_Vy = []
List_Vz = []
List_ax = []
List_ay = []
List_az = []
List_Yaw = []
List_Pitch = []
List_Roll = []
List_RollRate = []
List_PitchRate= []
List_YawRate = []
List_RollAcceleration = []
List_PitchAcceleration = []
List_YawAcceleration = []
List_Fx_fl = []
List_Fx_fr = []
List_Fx_rl = []
List_Fx_rr = []
List_Fy_fl = []
List_Fy_fr = []
List_Fy_rl = []
List_Fy_rr = []
List_Fz_fl = []
List_Fz_fr = []
List_Fz_rl = []
List_Fz_rr = []
List_beta = []
List_d_beta = []
List_Omega_fl = []
List_Omega_fr = []
List_Omega_rl = []
List_Omega_rr = []
List_Sx_fl = []
List_Sx_fr = []
List_Sx_rl = []
List_Sx_rr = []
List_time = []
DF.DOF14_P.Mt =1590  #change the weight of vehicle(the operation should be in front of DF.vehicle_model_14degrees_reset())
DF.DOF14_P.Vx0=2
DF.DOF14_P.Vy0=0
DF.vehicle_model_14degrees_initialize()

while DF.DOF14_Y.time_t < 10:  #terminate condition of running 
    DF.vehicle_model_14degrees_step(400,400,400,400,10,0.8)
    List_X0.append(DF.DOF14_Y.X_ground)
    List_Y0.append(DF.DOF14_Y.Y_ground)
    List_Vx.append(DF.DOF14_Y.Vx)
    List_Vy.append(DF.DOF14_Y.Vy)
    List_Vz.append(DF.DOF14_Y.Vz)
    List_ax.append(DF.DOF14_Y.ax)
    List_ay.append(DF.DOF14_Y.ay)
    List_az.append(DF.DOF14_Y.az)
    List_Yaw.append(DF.DOF14_Y.Yaw)
    List_Pitch.append(DF.DOF14_Y.Pitch)
    List_Roll.append(DF.DOF14_Y.Roll)
    List_RollRate.append(DF.DOF14_Y.RollRate)
    List_PitchRate.append(DF.DOF14_Y.PitchRate)
    List_YawRate.append(DF.DOF14_Y.YawRate)
    List_RollAcceleration.append(DF.DOF14_Y.RollAcceleration)
    List_PitchAcceleration.append(DF.DOF14_Y.PitchAcceleration)
    List_YawAcceleration.append(DF.DOF14_Y.YawAcceleration)
    List_Fx_fl.append(DF.DOF14_Y.Fx_fl)
    List_Fx_fr.append(DF.DOF14_Y.Fx_fr)
    List_Fx_rl.append(DF.DOF14_Y.Fx_rl)
    List_Fx_rr.append(DF.DOF14_Y.Fx_rr)
    List_Fy_fl.append(DF.DOF14_Y.Fy_fl)
    List_Fy_fr.append(DF.DOF14_Y.Fy_fr)
    List_Fy_rl.append(DF.DOF14_Y.Fy_rl)
    List_Fy_rr.append(DF.DOF14_Y.Fy_rr)
    List_Fz_fl.append(DF.DOF14_Y.Fz_fl)
    List_Fz_fr.append(DF.DOF14_Y.Fz_fr)
    List_Fz_rl.append(DF.DOF14_Y.Fz_rl)
    List_Fz_rr.append(DF.DOF14_Y.Fz_rr)
    List_beta.append(DF.DOF14_Y.beta)
    List_d_beta.append(DF.DOF14_Y.d_beta)
    List_Omega_fl.append(DF.DOF14_Y.Omega_fl)
    List_Omega_fr.append(DF.DOF14_Y.Omega_fr)
    List_Omega_rl.append(DF.DOF14_Y.Omega_rl)
    List_Omega_rr.append(DF.DOF14_Y.Omega_rr)
    List_Sx_fl.append(DF.DOF14_Y.Sx_fl)
    List_Sx_fr.append(DF.DOF14_Y.Sx_fr)
    List_Sx_rl.append(DF.DOF14_Y.Sx_rl)
    List_Sx_rr.append(DF.DOF14_Y.Sx_rr)
    List_time.append(DF.DOF14_Y.time_t)
    
    sql1 = 'insert into parameter(`X0[m]`,`Y0[m]`,`Vx[m/s]`,`Vy[m/s]`,`Vz[m/s]`, `ax[g]` , `ay[g]` , `az[g]` , `Yaw[rad]` , `Pitch[rad]` , `Roll[rad]` , \
        `RollRate[rad/s]` ,  `PitchRate[rad/s]` , `YawRate[rad/s]` , \
        `RollAcceleration[rad/s^2]`,`PitchAcceleration[rad/s^2]` , \
        `YawAcceleration[rad/s^2]` ,  `Fx_fl[N]` , `Fx_fr[N]` , `Fx_rl[N]` , `Fx_rr[N]` , `Fy_fl[N]` , `Fy_fr[N]` , `Fy_rl[N]` , \
        `Fy_rr[N]` , `Fz_fl[N]` , `Fz_fr[N]` , `Fz_rl[N]` , `Fz_rr[N]` , `beta[rad]` , `d_beta[rad/s]` , `Omega_fl[rad/s]` , `Omega_fr[rad/s]` , \
        `Omega_rl[rad/s]` , `Omega_rr[rad/s]` , `Sx_fl` , `Sx_fr` , `Sx_rl` , `Sx_rr` ,`time_t[s]`) \
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql1,(DF.DOF14_Y.X_ground ,DF.DOF14_Y.Y_ground ,DF.DOF14_Y.Vx , DF.DOF14_Y.Vy , DF.DOF14_Y.Vz ,DF.DOF14_Y.ax , DF.DOF14_Y.ay , DF.DOF14_Y.az ,DF.DOF14_Y.Yaw , DF.DOF14_Y.Pitch, DF.DOF14_Y.Roll, \
                      DF.DOF14_Y.RollRate,  DF.DOF14_Y.PitchRate, DF.DOF14_Y.YawRate, \
                      DF.DOF14_Y.RollAcceleration,\
                      DF.DOF14_Y.PitchAcceleration, DF.DOF14_Y.YawAcceleration,\
                      DF.DOF14_Y.Fx_fl, DF.DOF14_Y.Fx_fr, DF.DOF14_Y.Fx_rl, DF.DOF14_Y.Fx_rr,\
                      DF.DOF14_Y.Fy_fl, DF.DOF14_Y.Fy_fr, DF.DOF14_Y.Fy_rl, DF.DOF14_Y.Fy_rr ,\
                      DF.DOF14_Y.Fz_fl, DF.DOF14_Y.Fz_fr, DF.DOF14_Y.Fz_rl, DF.DOF14_Y.Fz_rr,\
                      DF.DOF14_Y.beta, DF.DOF14_Y.d_beta, \
                      DF.DOF14_Y.Omega_fl, DF.DOF14_Y.Omega_fr, DF.DOF14_Y.Omega_rl, DF.DOF14_Y.Omega_rr,\
                      DF.DOF14_Y.Sx_fl, DF.DOF14_Y.Sx_fr, DF.DOF14_Y.Sx_rl, DF.DOF14_Y.Sx_rr, DF.DOF14_Y.time_t))
    conn.commit()#添加数据改变了原来表的结构，因此要用此语句，才能真正在mysql中添加新的数据
   
print(DF.DOF14_Y.out_Mt)
print(DF.DOF14_P.Vx0)


# with open("test_Vx_1.csv", "w") as fp:   #data record
#         for value in List_Vx:
#             fp.write(f"{value}\n")

# 删除Vx[m/s]这一列的所有数据
# sql ='delete from parameter where `Vy[m/s]`  '
# cur.execute(sql)
# conn.commit()

cur.close()
conn.close()