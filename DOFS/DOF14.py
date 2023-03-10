# -*- coding:utf-8 -*-
#  Copyright (c). All Rights Reserved.
#  Institution: Changchun Univ. of Tech.
#  Leader: Bin Zhao
#  Member: Hewei Li & Xinyue Chen & Zhenxing Ding & Xiangjin Liu & Qingxuan Wang & Yongle Gao & Ze Wang & Junming Zhang
#  Creator: Xiangjin Liu
#  Description: how to invoke DLL file and difine the interface with DLL files including struct and function.
#  Update Date: 2023-03-10, Xiangjin Liu : the result of simulation is accurater
import ctypes

invoker = ctypes.WinDLL("DOF14_win64.dll", winmode=0)

#invoke interface of function
DOF14_initialize = invoker.DOF14_initialize
DOF14_step = invoker.DOF14_step
DOF14_terminate = invoker.DOF14_terminate


"""
user-difine data types

typedef double real_T;
typedef unsigned char uint8_T;
"""
real_T = ctypes.c_double
uint8_T = ctypes.c_ubyte

class P_DOF14_T(ctypes.Structure):
    """
    the goal is matching data struct between python with DLL
    
    real_T InitialSpeed[3];              /* Variable: InitialSpeed
                                            * Referenced by: '<S10>/Integrator2'
                                            */
    real_T Jw;                           /* Variable: Jw
                                            * Referenced by: '<S10>/车轮有效转动惯量'
                                            */
    real_T Jx;                           /* Variable: Jx
                                            * Referenced by: '<S38>/车身绕X轴等效转动惯量'
                                            */
    real_T Jy;                           /* Variable: Jy
                                            * Referenced by: '<S38>/车身绕Y轴等效转动惯量'
                                            */
    real_T Jz;                           /* Variable: Jz
                                            * Referenced by: '<S38>/车身绕Z轴等效转动惯量'
                                            */
    real_T L0[4];                        /* Variable: L0
                                            * Referenced by: '<S15>/L0'
                                            */
    real_T L1[4];                        /* Variable: L1
                                            * Referenced by: '<S15>/轮胎初始变化偏移量'
                                            */
    real_T L2[4];                        /* Variable: L2
                                            * Referenced by: '<S15>/L2'
                                            */
    real_T M;                            /* Variable: M
                                            * Referenced by: '<S38>/簧上质量'
                                            */
    real_T Mt;                           /* Variable: Mt
                                            * Referenced by: '<S38>/整车质量'
                                            */
    real_T Mu;                           /* Variable: Mu
                                            * Referenced by:
                                            *   '<S47>/簧下质量'
                                            *   '<S38>/车轮质量'
                                            *   '<S26>/簧下质量'
                                            */
    real_T Rw[4];                        /* Variable: Rw
                                            * Referenced by:
                                            *   '<S10>/Integrator2'
                                            *   '<S24>/轮胎有效滚动半径'
                                            */
    real_T Vx0;                          /* Variable: Vx0
                                            * Referenced by: '<S17>/Vx0'
                                            */
    real_T Vy0;                          /* Variable: Vy0
                                            * Referenced by: '<S17>/Vy0'
                                            */
    real_T X0;                           /* Variable: X0
                                        * Referenced by: '<Root>/Constant1'
                                        */
    real_T Y0;                           /* Variable: Y0
                                        * Referenced by: '<Root>/Constant2'      
                                        */                                  
    real_T a;                            /* Variable: a
                                            * Referenced by:
                                            *   '<S8>/质心到前轴距离'
                                            *   '<S38>/质心距离前轴纵向投影距离'
                                            *   '<S26>/质心距离前轴纵向投影距离'
                                            */
    real_T b;                            /* Variable: b
                                            * Referenced by:
                                            *   '<S8>/质心到后轴距离'
                                            *   '<S38>/质心距离后轴纵向投影距离'
                                            *   '<S26>/质心距离后轴纵向投影距离'
                                            */
    real_T b_slf;                        /* Variable: b_slf
                                            * Referenced by:
                                            *   '<S47>/左前悬架侧倾角阻尼'
                                            *   '<S26>/左前悬架侧倾角阻尼'
                                            */
    real_T b_slr;                        /* Variable: b_slr
                                            * Referenced by:
                                            *   '<S47>/左后悬架侧倾角阻尼'
                                            *   '<S26>/左后悬架侧倾角阻尼'
                                            */
    real_T b_srf;                        /* Variable: b_srf
                                            * Referenced by:
                                            *   '<S47>/右前悬架侧倾角阻尼'
                                            *   '<S26>/右前悬架侧倾角阻尼'
                                            */
    real_T b_srr;                        /* Variable: b_srr
                                            * Referenced by:
                                            *   '<S47>/右后悬架侧倾角阻尼'
                                            *   '<S26>/右后悬架侧倾角阻尼'
                                            */
    real_T c;                            /* Variable: c
                                            * Referenced by:
                                            *   '<S8>/轮距'
                                            *   '<S38>/轮距'
                                            *   '<S26>/轮距'
                                            */
    real_T g;                            /* Variable: g
                                            * Referenced by:
                                            *   '<S47>/重力时间常数'
                                            *   '<S38>/重力加速度'
                                            *   '<S26>/重力时间常数'
                                            */
    real_T hrcf;                         /* Variable: hrcf
                                            * Referenced by: '<S17>/F_roll_ center'
                                            */
    real_T hrcr;                         /* Variable: hrcr
                                            * Referenced by: '<S17>/R_roll_ center'
                                            */
    real_T k_slf;                        /* Variable: k_slf
                                            * Referenced by:
                                            *   '<S47>/左前悬架侧倾角刚度'
                                            *   '<S26>/左前悬架侧倾角刚度'
                                            */
    real_T k_slr;                        /* Variable: k_slr
                                            * Referenced by:
                                            *   '<S47>/左后悬架侧倾角刚度'
                                            *   '<S26>/左后悬架侧倾角刚度'
                                            */
    real_T k_srf;                        /* Variable: k_srf
                                            * Referenced by:
                                            *   '<S47>/右前悬架侧倾角刚度'
                                            *   '<S26>/右前悬架侧倾角刚度'
                                            */
    real_T k_srr;                        /* Variable: k_srr
                                            * Referenced by:
                                            *   '<S47>/右后悬架侧倾角刚度'
                                            *   '<S26>/右后悬架侧倾角刚度'
                                            */
    real_T k_tlf;                        /* Variable: k_tlf
                                            * Referenced by:
                                            *   '<S12>/Gain'
                                            *   '<S47>/左前轮垂向刚度'
                                            *   '<S26>/左前轮垂向刚度'
                                            */
    real_T k_tlr;                        /* Variable: k_tlr
                                            * Referenced by:
                                            *   '<S47>/左后轮垂向刚度'
                                            *   '<S26>/左后轮垂向刚度'
                                            */
    real_T k_trf;                        /* Variable: k_trf
                                            * Referenced by:
                                            *   '<S47>/右前轮垂向刚度'
                                            *   '<S26>/右前轮垂向刚度'
                                            */
    real_T k_trr;                        /* Variable: k_trr
                                            * Referenced by:
                                            *   '<S47>/右后轮垂向刚度'
                                            *   '<S26>/右后轮垂向刚度'
                                            */
    real_T steerRatio;                   /* Variable: steerRatio
                                            * Referenced by: '<Root>/Gain1'
                                            */
    real_T BandLimitedWhiteNoise1_Cov;
                                    /* Mask Parameter: BandLimitedWhiteNoise1_Cov
                                        * Referenced by: '<S2>/Output'
                                        */
    real_T BandLimitedWhiteNoise1_seed;
                                    /* Mask Parameter: BandLimitedWhiteNoise1_seed
                                    * Referenced by: '<S2>/White Noise'
                                    */
    real_T SAE_Value;                    /* Expression: 1
                                            * Referenced by: '<S17>/SAE'
                                            */
    real_T Original_Value;               /* Expression: 0
                                            * Referenced by: '<S17>/Original'
                                            */
    real_T Gain_Gain;                    /* Expression: 1/3.6
                                            * Referenced by: '<S17>/Gain'
                                            */
    real_T Integrator1_UpperSat;         /* Expression: 100
                                            * Referenced by: '<S17>/Integrator1'
                                            */
    real_T Integrator1_LowerSat;         /* Expression: -100
                                            * Referenced by: '<S17>/Integrator1'
                                            */
    real_T Gain1_Gain;                   /* Expression: 1/3.6
                                            * Referenced by: '<S17>/Gain1'
                                            */
    real_T Integrator4_UpperSat;         /* Expression: 100
                                            * Referenced by: '<S17>/Integrator4'
                                            */
    real_T Integrator4_LowerSat;         /* Expression: -100
                                            * Referenced by: '<S17>/Integrator4'
                                            */
    real_T Integrator2_IC;               /* Expression: 0
                                            * Referenced by: '<S17>/Integrator2'
                                            */
    real_T Integrator2_UpperSat;         /* Expression: 100
                                            * Referenced by: '<S17>/Integrator2'
                                            */
    real_T Integrator2_LowerSat;         /* Expression: -100
                                            * Referenced by: '<S17>/Integrator2'
                                            */
    real_T Integrator3_IC;               /* Expression: 0
                                            * Referenced by: '<S17>/Integrator3'
                                            */
    real_T Integrator3_IC_l;             /* Expression: 0
                                            * Referenced by: '<S37>/Integrator3'
                                            */
    real_T Integrator1_IC;               /* Expression: 0
                                            * Referenced by: '<S15>/Integrator1'
                                            */
    real_T Integrator2_IC_b;             /* Expression: 0
                                            * Referenced by: '<S15>/Integrator2'
                                            */
    real_T Integrator_IC;                /* Expression: 0
                                            * Referenced by: '<S15>/Integrator'
                                            */
    real_T Integrator_UpperSat;          /* Expression: 50
                                            * Referenced by: '<S15>/Integrator'
                                            */
    real_T Integrator_LowerSat;          /* Expression: -50
                                            * Referenced by: '<S15>/Integrator'
                                            */
    real_T UnitDelay_InitialCondition;   /* Expression: 0
                                            * Referenced by: '<S15>/Unit Delay'
                                            */
    real_T TransferFcn2_A;               /* Computed Parameter: TransferFcn2_A
                                            * Referenced by: '<S6>/Transfer Fcn2'
                                            */
    real_T TransferFcn2_C;               /* Computed Parameter: TransferFcn2_C
                                            * Referenced by: '<S6>/Transfer Fcn2'
                                            */
    real_T TransferFcn1_A;               /* Computed Parameter: TransferFcn1_A
                                            * Referenced by: '<S6>/Transfer Fcn1'
                                            */
    real_T TransferFcn1_C;               /* Computed Parameter: TransferFcn1_C
                                            * Referenced by: '<S6>/Transfer Fcn1'
                                            */
    real_T TransferFcn3_A;               /* Computed Parameter: TransferFcn3_A
                                            * Referenced by: '<S6>/Transfer Fcn3'
                                            */
    real_T TransferFcn3_C;               /* Computed Parameter: TransferFcn3_C
                                            * Referenced by: '<S6>/Transfer Fcn3'
                                            */
    real_T TransferFcn4_A;               /* Computed Parameter: TransferFcn4_A
                                            * Referenced by: '<S6>/Transfer Fcn4'
                                            */
    real_T TransferFcn4_C;               /* Computed Parameter: TransferFcn4_C
                                            * Referenced by: '<S6>/Transfer Fcn4'
                                            */
    real_T Gain2_Gain;                   /* Expression: 1/57.3
                                            * Referenced by: '<Root>/Gain2'
                                            */
    real_T Gain_Gain_p;                  /* Expression: -1
                                            * Referenced by: '<S4>/Gain'
                                            */
    real_T Gain1_Gain_f[4];              /* Expression: ones(1,4)
                                            * Referenced by: '<S4>/Gain1'
                                            */
    real_T Constant1_Value;              /* Expression: 0
                                            * Referenced by: '<S10>/Constant1'
                                            */
    real_T MY_Value;                     /* Expression: 1
                                            * Referenced by: '<S16>/MY'
                                            */
    real_T MY1_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY1'
                                            */
    real_T MY2_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY2'
                                            */
    real_T MY3_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY3'
                                            */
    real_T MY4_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY4'
                                            */
    real_T MY5_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY5'
                                            */
    real_T MY6_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY6'
                                            */
    real_T MY7_Value;                    /* Expression: 1
                                            * Referenced by: '<S16>/MY7'
                                            */
    real_T Cd_Value;                     /* Expression: 0.3
                                            * Referenced by: '<S17>/Cd'
                                            */
    real_T Am2_Value;                    /* Expression: 1.55
                                            * Referenced by: '<S17>/A(m^2)'
                                            */
    real_T IC_Value[4];                  /* Expression: ones(4,1)
                                            * Referenced by: '<S1>/IC'
                                            */
    real_T WhiteNoise_Mean;              /* Expression: 0
                                            * Referenced by: '<S2>/White Noise'
                                            */
    real_T WhiteNoise_StdDev;            /* Computed Parameter: WhiteNoise_StdDev
                                            * Referenced by: '<S2>/White Noise'
                                            */
    real_T Gain_Gain_b;                  /* Expression: 1
                                            * Referenced by: '<S3>/Gain'
                                            */
    real_T Gain1_Gain_e;                 /* Expression: 1
                                            * Referenced by: '<S3>/Gain1'
                                            */
    real_T Gain_Gain_h;                  /* Expression: 1/57.3
                                            * Referenced by: '<S14>/Gain'
                                            */
    real_T TransferFcn_A;                /* Computed Parameter: TransferFcn_A
                                            * Referenced by: '<S10>/Transfer Fcn'
                                            */
    real_T TransferFcn_C;                /* Computed Parameter: TransferFcn_C
                                            * Referenced by: '<S10>/Transfer Fcn'
                                            */
    real_T TransferFcn1_A_d;             /* Computed Parameter: TransferFcn1_A_d
                                            * Referenced by: '<S10>/Transfer Fcn1'
                                            */
    real_T TransferFcn1_C_d;             /* Computed Parameter: TransferFcn1_C_d
                                            * Referenced by: '<S10>/Transfer Fcn1'
                                            */
    real_T TransferFcn2_A_d;             /* Computed Parameter: TransferFcn2_A_d
                                            * Referenced by: '<S10>/Transfer Fcn2'
                                            */
    real_T TransferFcn2_C_i;             /* Computed Parameter: TransferFcn2_C_i
                                            * Referenced by: '<S10>/Transfer Fcn2'
                                            */
    real_T TransferFcn3_A_g;             /* Computed Parameter: TransferFcn3_A_g
                                            * Referenced by: '<S10>/Transfer Fcn3'
                                            */
    real_T TransferFcn3_C_b;             /* Computed Parameter: TransferFcn3_C_b
                                            * Referenced by: '<S10>/Transfer Fcn3'
                                            */
    real_T Integrator_IC_a;              /* Expression: 0
                                            * Referenced by: '<Root>/Integrator'
                                            */
    real_T Integrator1_IC_o;             /* Expression: 0
                                            * Referenced by: '<Root>/Integrator1'
                                            */
    uint8_T OriginalorSAE_CurrentSetting;
                                /* Computed Parameter: OriginalorSAE_CurrentSetting
                                * Referenced by: '<S17>/Original or SAE'
                                */
    """
    _fields_ = [
        ("initialSpeed", real_T*3),
        ("Jw", real_T),
        ("Jx", real_T),
        ("Jy", real_T),
        ("Jz", real_T),
        ("L0", real_T*4),
        ("L1", real_T*4),
        ("L2", real_T*4),
        ("M", real_T),
        ("Mt", real_T),
        ("Mu", real_T),
        ("Rw", real_T*4),
        ("Vx0", real_T),
        ("Vy0", real_T),
        ("X0", real_T),
        ("Y0", real_T),
        ("a", real_T),
        ("b", real_T),
        ("b_slf", real_T),
        ("b_slr", real_T),
        ("b_srf", real_T),
        ("b_srr", real_T),
        ("c", real_T),
        ("g", real_T),
        ("hrcf", real_T),
        ("hrcr", real_T),
        ("k_slf", real_T),
        ("k_slr", real_T),
        ("k_srf", real_T),
        ("k_srr", real_T),
        ("k_tlf", real_T),
        ("k_tlr", real_T),
        ("k_trf", real_T),
        ("k_trr", real_T),
        ("steerRatio", real_T),
        ("BandLimitedWhiteNoise1_Cov", real_T),
        ("BandLimitedWhiteNoise1_seed", real_T),
        ("SAE_Value", real_T),
        ("Original_Value", real_T),
        ("Gain_Gain", real_T),
        ("Integrator1_UpperSat", real_T),
        ("Integrator1_LowerSat", real_T),
        ("Gain1_Gain", real_T),
        ("Integrator4_UpperSat", real_T),
        ("Integrator4_LowerSat", real_T),
        ("Integrator2_IC", real_T),
        ("Integrator2_UpperSat", real_T),
        ("Integrator2_LowerSat", real_T),
        ("Integrator3_IC", real_T),
        ("Integrator3_IC_l", real_T),
        ("Integrator1_IC", real_T),
        ("Integrator2_IC_b", real_T),
        ("Integrator_IC", real_T),
        ("Integrator_UpperSat", real_T),
        ("Integrator_LowerSat", real_T),
        ("UnitDelay_InitialCondition", real_T),
        ("TransferFcn2_A", real_T),
        ("TransferFcn2_C", real_T),
        ("TransferFcn1_A", real_T),
        ("TransferFcn1_C", real_T),
        ("TransferFcn3_A", real_T),
        ("TransferFcn3_C", real_T),
        ("TransferFcn4_A", real_T),
        ("TransferFcn4_C", real_T),
        ("Gain2_Gain", real_T),
        ("Gain_Gain_p", real_T),
        ("Gain1_Gain_f", real_T*4),
        ("Constant1_Value", real_T),
        ("MY_Value", real_T),
        ("MY1_Value", real_T),
        ("MY2_Value", real_T),
        ("MY3_Value", real_T),
        ("MY4_Value", real_T),
        ("MY5_Value", real_T),
        ("MY6_Value", real_T),
        ("MY7_Value", real_T),
        ("Cd_Value", real_T),
        ("Am2_Value", real_T),
        ("IC_Value", real_T*4),
        ("WhiteNoise_Mean", real_T),
        ("WhiteNoise_StdDev", real_T),
        ("Gain_Gain_b", real_T),
        ("Gain1_Gain_e", real_T),
        ("Gain_Gain_h", real_T),
        ("TransferFcn_A", real_T),
        ("TransferFcn_C", real_T),
        ("TransferFcn1_A_d", real_T),
        ("TransferFcn1_C_d", real_T),
        ("TransferFcn2_A_d", real_T),
        ("TransferFcn2_C_i", real_T),
        ("TransferFcn3_A_g", real_T),
        ("TransferFcn3_C_b", real_T),
        ("Integrator_IC_a", real_T),
        ("Integrator1_IC_o", real_T),
        ("OriginalorSAE_CurrentSetting", uint8_T),


    ]
class ExtU_DOF14_T(ctypes.Structure):
    """
typedef struct {
  real_T Torque_FL;                    /* '<Root>/Torque_FL' unit:N/m */
  real_T Torque_FR;                    /* '<Root>/Torque_FR' unit:N/m */
  real_T Torque_RL;                    /* '<Root>/Torque_RL' unit:N/m */
  real_T Torque_RR;                    /* '<Root>/Torque_RR' unit:N/m*/
  real_T delta_f;                      /* '<Root>/delta_f' unit:rad*/
  real_T Mu;                           /* '<Root>/Mu' */
} ExtU_DOF14_T;
    """
    _fields_ = [
        ("Torque_FL", real_T),
        ("Torque_FR", real_T),
        ("Torque_RL", real_T),
        ("Torque_RR", real_T),
        ("delta_f", real_T),
        ("Mu", real_T),
    ]


class ExtY_DOF14_T(ctypes.Structure):
    """

typedef struct {
  real_T X_ground;                     /* '<Root>/X_ground' unit:m */
  real_T Y_ground;                     /* '<Root>/Y_ground' unit:m*/
  real_T Vx;                           /* '<Root>/Vx' unit:m/s */
  real_T Vy;                           /* '<Root>/Vy' unit:m/s*/
  real_T Vz;                           /* '<Root>/Vz' unit:g*/
  real_T ax;                           /* '<Root>/ax' unit:g*/
  real_T ay;                           /* '<Root>/ay' unit:g*/
  real_T az;                           /* '<Root>/az' unit:g*/
  real_T Yaw;                          /* '<Root>/Yaw' unit:rad*/
  real_T Pitch;                        /* '<Root>/Pitch' unit:rad*/
  real_T Roll;                         /* '<Root>/Roll' unit:rad*/
  real_T RollRate;                     /* '<Root>/RollRate' rad/s*/
  real_T PitchRate;                    /* '<Root>/PitchRate' unit:rad/s*/
  real_T YawRate;                      /* '<Root>/YawRate' unit:rad/s*/
  real_T RollAcceleration;            /* '<Root>/RollAcceeleration' unit:rad/s2*/
  real_T PitchAcceleration;            /* '<Root>/PitchAcceleration' unit:rad/s2*/
  real_T YawAcceleration;              /* '<Root>/YawAcceleration' unit:rad/s2*/
  real_T Fx_fl;                        /* '<Root>/Fx_fl' unit:N*/
  real_T Fx_fr;                        /* '<Root>/Fx_fr' unit:N*/
  real_T Fx_rl;                        /* '<Root>/Fx_rl' unit:V*/
  real_T Fx_rr;                        /* '<Root>/Fx_rr' unit:V*/
  real_T Fy_fl;                        /* '<Root>/Fy_fl' unit:V*/
  real_T Fy_fr;                        /* '<Root>/Fy_fr' unit:V*/
  real_T Fy_rl;                        /* '<Root>/Fy_rl' unit:V*/
  real_T Fy_rr;                        /* '<Root>/Fy_rr' unit:V*/
  real_T Fz_fl;                        /* '<Root>/Fz_fl' unit:V*/
  real_T Fz_fr;                        /* '<Root>/Fz_fr' unit:V*/
  real_T Fz_rl;                        /* '<Root>/Fz_rl' unit:V*/
  real_T Fz_rr;                        /* '<Root>/Fz_rr' unit:V*/
  real_T Omega_fl;                     /* '<Root>/Omega_fl' unit:rad/s*/
  real_T Omega_fr;                     /* '<Root>/Omega_fr' unit:rad/s*/
  real_T Omega_rl;                     /* '<Root>/Omega_rl' unit:rad/s*/
  real_T Omega_rr;                     /* '<Root>/Omega_rr' unit:rad/s*/
  real_T Sx_fl;                        /* '<Root>/Sx_fl' */
  real_T Sx_fr;                        /* '<Root>/Sx_fr' */
  real_T Sx_rl;                        /* '<Root>/Sx_rl' */
  real_T Sx_rr;                        /* '<Root>/Sx_rr' */
  real_T beta;                         /* '<Root>/beta' unit:rad*/
  real_T d_beta;                       /* '<Root>/d_beta' unit:rad/s*/
  real_T time_t;                       /* '<Root>/time_t' s*/
  real_T out_Mt;                       /* '<Root>/out_Mt' kg*/
} ExtY_DOF14_T;
    """
    _fields_ = [
        ("X_ground", real_T),
        ("Y_ground", real_T),
        ("Vx", real_T),
        ("Vy", real_T),
        ("Vz", real_T),
        ("ax", real_T),
        ("ay", real_T),
        ("az", real_T),
        ("Yaw", real_T),
        ("Pitch", real_T),
        ("Roll", real_T),
        ("RollRate", real_T),
        ("PitchRate", real_T),
        ("YawRate", real_T),
        ("RollAcceleration", real_T),
        ("PitchAcceleration", real_T),
        ("YawAcceleration", real_T),
        ("Fx_fl", real_T),
        ("Fx_fr", real_T),
        ("Fx_rl", real_T),
        ("Fx_rr", real_T),
        ("Fy_fl", real_T),
        ("Fy_fr", real_T),
        ("Fy_rl", real_T),
        ("Fy_rr", real_T),
        ("Fz_fl", real_T),
        ("Fz_fr", real_T),
        ("Fz_rl", real_T),
        ("Fz_rr", real_T),
        ("Omega_fl", real_T),
        ("Omega_fr", real_T),
        ("Omega_rl", real_T),
        ("Omega_rr", real_T),
        ("Sx_fl", real_T),
        ("Sx_fr", real_T),
        ("Sx_rl", real_T),
        ("Sx_rr", real_T),
        ("beta", real_T),
        ("d_beta", real_T),
        ("time_t", real_T),
        ("out_Mt", real_T)
    ]



"""
/* External inputs (root import signals with default storage) */
ExtU_DOF14_T DOF14_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_DOF14_T DOF14_Y;
"""
DOF14_U = ExtU_DOF14_T.in_dll(invoker, "DOF14_U")
DOF14_Y = ExtY_DOF14_T.in_dll(invoker, "DOF14_Y")
DOF14_P = P_DOF14_T.in_dll(invoker, "DOF14_P")

def vehicle_model_14degrees_step(moment_FL:float,moment_FR:float,moment_RL:float,moment_RR:float,delta_f:float,Mu:float,):
    '''
    input data to vehicle model
    '''
    DOF14_U.Torque_FL = moment_FL
    DOF14_U.Torque_FR = moment_FR
    DOF14_U.Torque_RL = moment_RL
    DOF14_U.Torque_RR = moment_RR


    DOF14_U.delta_f = delta_f
    DOF14_U.Mu = Mu


    DOF14_step()


def vehicle_model_14degrees_initialize():
    '''
    initialize vehicle model
    '''
    DOF14_initialize()


def vehicle_model_14degreees_terminate():
    '''
    terminate runing(it is possibale not to writte)
    '''
    DOF14_terminate()