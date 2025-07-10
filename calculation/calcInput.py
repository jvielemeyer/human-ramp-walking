import csv
import numpy as np
import matplotlib.pyplot as plt
import configparser #to read ini-file
import json #to read list in ini file

import calcReadInData #readData, getData, readin_kinematics, calc_joints
import calcCoM #Com_calc

#--------------------------------------------
#read in initialization file:
def readIni (preadin,pres,pkinetic,pkinematic1,pkinematic2a,pkinematic2b):
    # ini_file=filedialog.askopenfilename()
    ini_measure = "measurement_system.ini"
    ini_anthro = "anthropometrics.ini"
    config = configparser.ConfigParser()
    config.read(ini_measure)
    config.read(ini_anthro)
    preadin.Mass = np.multiply(json.loads(config.get("ANTHRO","mass")),9.81) #from kg to N
    pres.p_var = 0 # no plot of input variables at initialisation
    pres.p_vpp = 0
    pres.p_kin = 0

    pkinetic.frequ_grf.set(config.get("KINETICS", 'frequ_grf'))
    pkinetic.unit.set(config.get("KINETICS", 'unit_cop'))
    pkinetic.col_fx1.set(config.get("KINETICS", 'col_fx1'))
    pkinetic.col_fz1.set(config.get("KINETICS", 'col_fz1'))
    pkinetic.col_copx1.set(config.get("KINETICS", 'col_copx1'))
    pkinetic.col_copz1.set(config.get("KINETICS", 'col_copz1'))
    pkinetic.col_fx2.set(config.get("KINETICS", 'col_fx2'))
    pkinetic.col_fz2.set(config.get("KINETICS", 'col_fz2'))
    pkinetic.col_copx2.set(config.get("KINETICS", 'col_copx2'))
    pkinetic.col_copz2.set(config.get("KINETICS", 'col_copz2'))
    pkinetic.col_fx3.set(config.get("KINETICS", 'col_fx3'))
    pkinetic.col_fz3.set(config.get("KINETICS", 'col_fz3'))
    pkinetic.col_copx3.set(config.get("KINETICS", 'col_copx3'))
    pkinetic.col_copz3.set(config.get("KINETICS", 'col_copz3'))
    pkinetic.fac_fx.set(config.get("KINETICS", 'fac_fx'))
    pkinetic.fac_fz.set(config.get("KINETICS", 'fac_fz'))


    pkinetic.combo_pm_fx1.set(config.get("KINETICS", 'pm_fx1'))
    pkinetic.combo_pm_fz1.set(config.get("KINETICS", 'pm_fz1'))
    pkinetic.combo_pm_fx2.set(config.get("KINETICS", 'pm_fx2'))
    pkinetic.combo_pm_fz2.set(config.get("KINETICS", 'pm_fz2'))
    pkinetic.combo_pm_fx3.set(config.get("KINETICS", 'pm_fx3'))
    pkinetic.combo_pm_fz3.set(config.get("KINETICS", 'pm_fz3'))
    pkinetic.combo_pm_copx2.set(config.get("KINETICS", 'pm_copx2'))

    pkinematic1.frequ_video.set(config.get("KINEMATICS", 'frequ_video'))
    pkinematic1.frequ_cut.set(config.get("KINEMATICS", 'frequ_cut'))

    pkinematic2a.mal_lat_lx.set(config.get("KINEMATICS", 'mal_lat_lx'))
    pkinematic2a.mal_lat_lz.set(config.get("KINEMATICS", 'mal_lat_lz'))
    pkinematic2a.mal_lat_rx.set(config.get("KINEMATICS", 'mal_lat_rx'))
    pkinematic2a.mal_lat_rz.set(config.get("KINEMATICS", 'mal_lat_rz'))
    pkinematic2a.mal_med_lx.set(config.get("KINEMATICS", 'mal_med_lx'))
    pkinematic2a.mal_med_lz.set(config.get("KINEMATICS", 'mal_med_lz'))
    pkinematic2a.mal_med_rx.set(config.get("KINEMATICS", 'mal_med_rx'))
    pkinematic2a.mal_med_rz.set(config.get("KINEMATICS", 'mal_med_rz'))
    pkinematic2a.toe_lx.set(config.get("KINEMATICS", 'toe_lx'))
    pkinematic2a.toe_lz.set(config.get("KINEMATICS", 'toe_lz'))
    pkinematic2a.toe_rx.set(config.get("KINEMATICS", 'toe_rx'))
    pkinematic2a.toe_rz.set(config.get("KINEMATICS", 'toe_rz'))
    pkinematic2a.knee_lx.set(config.get("KINEMATICS", 'knee_lx'))
    pkinematic2a.knee_lz.set(config.get("KINEMATICS", 'knee_lz'))
    pkinematic2a.knee_rx.set(config.get("KINEMATICS", 'knee_rx'))
    pkinematic2a.knee_rz.set(config.get("KINEMATICS", 'knee_rz'))
    pkinematic2a.hip_lx.set(config.get("KINEMATICS", 'hip_lx'))
    pkinematic2a.hip_lz.set(config.get("KINEMATICS", 'hip_lz'))
    pkinematic2a.hip_rx.set(config.get("KINEMATICS", 'hip_rx'))
    pkinematic2a.hip_rz.set(config.get("KINEMATICS", 'hip_rz'))
    pkinematic2a.shoulder_lx.set(config.get("KINEMATICS", 'shoulder_lx'))
    pkinematic2a.shoulder_lz.set(config.get("KINEMATICS", 'shoulder_lz'))
    pkinematic2a.shoulder_rx.set(config.get("KINEMATICS", 'shoulder_rx'))
    pkinematic2a.shoulder_rz.set(config.get("KINEMATICS", 'shoulder_rz'))

    pkinematic2b.com_x.set(config.get("MODEL_OUTPUT", 'com_x'))
    pkinematic2b.com_z.set(config.get("MODEL_OUTPUT", 'com_z'))

    preadin.keyword_dyn.set(config.get("READIN", 'keyword_dyn'))
    preadin.keyword_kin.set(config.get("READIN", 'keyword_kin'))
    preadin.keyword_kin_end.set(config.get("READIN", 'keyword_kin_end'))
    preadin.dist_keyword_dyn.set(config.get("READIN", 'dist_keyword_dyn'))
    preadin.dist_keyword_kin.set(config.get("READIN", 'dist_keyword_kin'))

#----------------------------------------------------
def button_get_entries(pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b):
    #general
    preadin.Frequ_grf=pkinetic.frequ_grf.get()
    preadin.Frequ_video=pkinematic1.frequ_video.get()
    preadin.Frequ_cut=pkinematic1.frequ_cut.get()
    preadin.Nb_kmp = 3
    preadin.Keyword_dyn=preadin.keyword_dyn.get()
    preadin.Dist_keyword_dyn=preadin.dist_keyword_dyn.get()
    preadin.Dist_keyword_dyn_end=preadin.dist_keyword_dyn_end.get()
    preadin.Keyword_kin=preadin.keyword_kin.get()
    preadin.Dist_keyword_kin=preadin.dist_keyword_kin.get()
    preadin.Dist_keyword_kin_end=preadin.dist_keyword_kin_end.get()
    preadin.Keyword_kin_end=preadin.keyword_kin_end.get()

    #kinetics
    preadin.Col_fx1=pkinetic.col_fx1.get()
    preadin.Col_fz1=pkinetic.col_fz1.get()
    preadin.Col_copx1=pkinetic.col_copx1.get()
    preadin.Col_copz1=pkinetic.col_copz1.get()
    preadin.Pm_fx1=pkinetic.pm_fx1.get()
    preadin.Pm_fz1=pkinetic.pm_fz1.get()
    preadin.Pm_copx1=pkinetic.pm_copx1.get()
    preadin.Col_fx2=pkinetic.col_fx2.get()
    preadin.Col_fz2=pkinetic.col_fz2.get()
    preadin.Col_copx2=pkinetic.col_copx2.get()
    preadin.Col_copz2=pkinetic.col_copz2.get()
    preadin.Pm_fx2=pkinetic.pm_fx2.get()
    preadin.Pm_fz2=pkinetic.pm_fz2.get()
    preadin.Pm_copx2=pkinetic.pm_copx2.get()
    preadin.Col_fx3=pkinetic.col_fx3.get()
    preadin.Col_fz3=pkinetic.col_fz3.get()
    preadin.Col_copx3=pkinetic.col_copx3.get()
    preadin.Col_copz3=pkinetic.col_copz3.get()
    preadin.Pm_fx3=pkinetic.pm_fx3.get()
    preadin.Pm_fz3=pkinetic.pm_fz3.get()
    preadin.Pm_copx3=pkinetic.pm_copx3.get()

    preadin.Fac_fx=pkinetic.fac_fx.get()
    preadin.Fac_fz=pkinetic.fac_fz.get()

    #kinematics
    pkinematic2a.Mal_lat_lx= pkinematic2a.mal_lat_lx.get()
    pkinematic2a.Mal_lat_lz= pkinematic2a.mal_lat_lz.get()
    pkinematic2a.Mal_lat_rx= pkinematic2a.mal_lat_rx.get()
    pkinematic2a.Mal_lat_rz= pkinematic2a.mal_lat_rz.get()
    pkinematic2a.Mal_med_lx= pkinematic2a.mal_med_lx.get()
    pkinematic2a.Mal_med_lz= pkinematic2a.mal_med_lz.get()
    pkinematic2a.Mal_med_rx= pkinematic2a.mal_med_rx.get()
    pkinematic2a.Mal_med_rz= pkinematic2a.mal_med_rz.get()
    pkinematic2a.Toe_lx= pkinematic2a.toe_lx.get()
    pkinematic2a.Toe_lz= pkinematic2a.toe_lz.get()
    pkinematic2a.Toe_rx= pkinematic2a.toe_rx.get()
    pkinematic2a.Toe_rz= pkinematic2a.toe_rz.get()
    pkinematic2a.Knee_lx= pkinematic2a.knee_lx.get()
    pkinematic2a.Knee_lz= pkinematic2a.knee_lz.get()
    pkinematic2a.Knee_rx= pkinematic2a.knee_rx.get()
    pkinematic2a.Knee_rz= pkinematic2a.knee_rz.get()
    pkinematic2a.Hip_lx= pkinematic2a.hip_lx.get()
    pkinematic2a.Hip_lz= pkinematic2a.hip_lz.get()
    pkinematic2a.Hip_rx= pkinematic2a.hip_rx.get()
    pkinematic2a.Hip_rz= pkinematic2a.hip_rz.get()
    pkinematic2a.Shoulder_lx= pkinematic2a.shoulder_lx.get()
    pkinematic2a.Shoulder_lz= pkinematic2a.shoulder_lz.get()
    pkinematic2a.Shoulder_rx= pkinematic2a.shoulder_rx.get()
    pkinematic2a.Shoulder_rz= pkinematic2a.shoulder_rz.get()

    pkinematic2a.Mal_lat = [pkinematic2a.Mal_lat_lx, pkinematic2a.Mal_lat_lz, pkinematic2a.Mal_lat_rx, pkinematic2a.Mal_lat_rz]
    pkinematic2a.Mal_med = [pkinematic2a.Mal_med_lx, pkinematic2a.Mal_med_lz, pkinematic2a.Mal_med_rx, pkinematic2a.Mal_med_rz]
    pkinematic2a.Toe = [pkinematic2a.Toe_lx, pkinematic2a.Toe_lz, pkinematic2a.Toe_rx, pkinematic2a.Toe_rz]
    pkinematic2a.Knee = [pkinematic2a.Knee_lx, pkinematic2a.Knee_lz, pkinematic2a.Knee_rx, pkinematic2a.Knee_rz]
    pkinematic2a.Hip = [pkinematic2a.Hip_lx, pkinematic2a.Hip_lz, pkinematic2a.Hip_rx, pkinematic2a.Hip_rz]
    pkinematic2a.Shoulder = [pkinematic2a.Shoulder_lx, pkinematic2a.Shoulder_lz, pkinematic2a.Shoulder_rx, pkinematic2a.Shoulder_rz]

    #------------
    pkinematic2b.Com_x= pkinematic2b.com_x.get()
    pkinematic2b.Com_z= pkinematic2b.com_z.get()
    pkinematic2b.Com = [pkinematic2b.Com_x, pkinematic2b.Com_z]

def calc_forces_cop_com(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin, file_name):
    if pstart.com_output.get() == 2:
        COM=calcCoM.Com_calc(pres.DataKin, pkinematic2a.Mal_lat, pkinematic2a.Mal_med, pkinematic2a.Toe, pkinematic2a.Knee, pkinematic2a.Hip, pkinematic2a.Shoulder,preadin)
    else:
        COM = pres.DataKin[:,pkinematic2b.Com_x-1:pkinematic2b.Com_z+1] #x-1: include y component
        if (pkinematic1.unit.get() == 1):
            COM=np.multiply(COM,1/1000)

    calcReadInData.readin_kinematics(preadin,pres.DataKin, pres.DataKin_2)

    tdto = np.sort(np.round(pres.DataTdto[:,3]*preadin.Frequ_video-pres.offset)).astype(np.int32)  #changed from float to integer
    tdto_index = np.argsort(np.round(pres.DataTdto[:,3]*preadin.Frequ_video-pres.offset)).astype(np.int32)
    Events_Foot = np.array(pres.foot)[tdto_index]
    Events_TD = np.array(pres.TD)[tdto_index] # 0 = TO, 1 = TD

    #------find first TO (= first zero), after this 4 events relevant:
    if (Events_TD[0] == 0):
        events_index = np.arange(0,4)
    else:
        events_index = np.arange(1,5) #order foot, 1= right, 0 = left (1,1,0,0 = r, r, l, l in the air, e.g. first contact left, second contact right)

    #---------------------------find first TD of gait cycle and determine leg
    if Events_TD[0] == 1:
        pres.foot_td = Events_Foot[0]
    else:
        pres.foot_td = Events_Foot[1]

    prob = int(file_name[3:5])-1

    #---------read in all 3 force plates (a, b, c) and normalize it to length of CoM

    Fx_a_short = np.interp(np.linspace(1,len(pres.Fx[:,0]),len(COM)),np.linspace(1,len(pres.Fx[:,0]),len(pres.Fx[:,0])),pres.Fx[:,0])/preadin.Mass[prob]*preadin.Fac_fx
    Fx_b_short = np.interp(np.linspace(1,len(pres.Fx[:,1]),len(COM)),np.linspace(1,len(pres.Fx[:,1]),len(pres.Fx[:,1])),pres.Fx[:,1])/preadin.Mass[prob]*preadin.Fac_fx
    Fx_c_short = np.interp(np.linspace(1,len(pres.Fx[:,2]),len(COM)),np.linspace(1,len(pres.Fx[:,2]),len(pres.Fx[:,2])),pres.Fx[:,2])/preadin.Mass[prob]*preadin.Fac_fx
    Fy_a_short = np.interp(np.linspace(1,len(pres.Fy[:,0]),len(COM)),np.linspace(1,len(pres.Fy[:,0]),len(pres.Fy[:,0])),pres.Fy[:,0])/preadin.Mass[prob]*preadin.Fac_fx
    Fy_b_short = np.interp(np.linspace(1,len(pres.Fy[:,1]),len(COM)),np.linspace(1,len(pres.Fy[:,1]),len(pres.Fy[:,1])),pres.Fy[:,1])/preadin.Mass[prob]*preadin.Fac_fx
    Fy_c_short = np.interp(np.linspace(1,len(pres.Fy[:,2]),len(COM)),np.linspace(1,len(pres.Fy[:,2]),len(pres.Fy[:,2])),pres.Fy[:,2])/preadin.Mass[prob]*preadin.Fac_fx
    Fz_a_short = np.interp(np.linspace(1,len(pres.Fz[:,0]),len(COM)),np.linspace(1,len(pres.Fz[:,0]),len(pres.Fz[:,0])),pres.Fz[:,0])/preadin.Mass[prob]*preadin.Fac_fz
    Fz_b_short = np.interp(np.linspace(1,len(pres.Fz[:,1]),len(COM)),np.linspace(1,len(pres.Fz[:,1]),len(pres.Fz[:,1])),pres.Fz[:,1])/preadin.Mass[prob]*preadin.Fac_fz
    Fz_c_short = np.interp(np.linspace(1,len(pres.Fz[:,2]),len(COM)),np.linspace(1,len(pres.Fz[:,2]),len(pres.Fz[:,2])),pres.Fz[:,2])/preadin.Mass[prob]*preadin.Fac_fz
    CoPx_a_short = np.interp(np.linspace(1,len(pres.CoPx[:,0]),len(COM)),np.linspace(1,len(pres.CoPx[:,0]),len(pres.CoPx[:,0])),pres.CoPx[:,0])
    CoPx_b_short = np.interp(np.linspace(1,len(pres.CoPx[:,1]),len(COM)),np.linspace(1,len(pres.CoPx[:,1]),len(pres.CoPx[:,1])),pres.CoPx[:,1])
    CoPx_c_short = np.interp(np.linspace(1,len(pres.CoPx[:,2]),len(COM)),np.linspace(1,len(pres.CoPx[:,2]),len(pres.CoPx[:,2])),pres.CoPx[:,2])
    CoPy_a_short = np.interp(np.linspace(1,len(pres.CoPy[:,0]),len(COM)),np.linspace(1,len(pres.CoPy[:,0]),len(pres.CoPy[:,0])),pres.CoPy[:,0])
    CoPy_b_short = np.interp(np.linspace(1,len(pres.CoPy[:,1]),len(COM)),np.linspace(1,len(pres.CoPy[:,1]),len(pres.CoPy[:,1])),pres.CoPy[:,1])
    CoPy_c_short = np.interp(np.linspace(1,len(pres.CoPy[:,2]),len(COM)),np.linspace(1,len(pres.CoPy[:,2]),len(pres.CoPy[:,2])),pres.CoPy[:,2])
    CoPz_a_short = np.interp(np.linspace(1,len(pres.CoPz[:,0]),len(COM)),np.linspace(1,len(pres.CoPz[:,0]),len(pres.CoPz[:,0])),pres.CoPz[:,0])
    CoPz_b_short = np.interp(np.linspace(1,len(pres.CoPz[:,1]),len(COM)),np.linspace(1,len(pres.CoPz[:,1]),len(pres.CoPz[:,1])),pres.CoPz[:,1])
    CoPz_c_short = np.interp(np.linspace(1,len(pres.CoPz[:,2]),len(COM)),np.linspace(1,len(pres.CoPz[:,2]),len(pres.CoPz[:,2])),pres.CoPz[:,2])


    #---------------------------------------------
    tt = tdto[events_index]

    if (COM[tt[3],1]-COM[tt[2],1]) > 0: #check walking direction with Comx
        direction = 0 # walking direction is already positive
    else:
        direction = 1

    #---------find max of Fz as key value -> if max_a lays between TO1 and TD2, then Fz_a = Fz_1 (and Fz_b = Fz_2), else Fz_b and Fz_c are 1 and 2 (search in whole contact (TD to TO of the same leg))
    m = [i for i,value in enumerate(Fz_b_short) if value > 0.7]
    if  (m[0] <= tt[1]):
        if (CoPx_b_short[tt[1]]-CoPx_b_short[tt[0]]) > 0: #COP forwards
            sign_x = 1
        else: #COP moves backwards -> mirror Fx and COPx on y-axis
            sign_x = -1
        pres.Fx1 = sign_x*Fx_b_short
        pres.Fy1 = sign_x*Fy_b_short #same sign for x and y
        pres.Fz1 = Fz_b_short
        pres.CoPx1 = sign_x*CoPx_b_short
        pres.CoPy1 = sign_x*CoPy_b_short
        pres.CoPz1 = CoPz_b_short
        if sign_x == -1:
            pres.Fx2 = sign_x*Fx_c_short
            pres.Fy2 = sign_x*Fy_c_short
            pres.Fz2 = Fz_c_short
            pres.CoPx2 = sign_x*CoPx_c_short
            pres.CoPy2 = sign_x*CoPy_c_short
            pres.CoPz2 = CoPz_c_short
        elif sign_x == 1: # flip order of forces
            pres.Fx2 = sign_x*Fx_a_short
            pres.Fy2 = sign_x*Fy_a_short
            pres.Fz2 = Fz_a_short
            pres.CoPx2 = sign_x*CoPx_a_short
            pres.CoPy2 = sign_x*CoPy_a_short
            pres.CoPz2 = CoPz_a_short
    elif (m[0] >= tt[1] and  m[0] <= tt[3]):
        if (CoPx_b_short[tt[3]]-CoPx_b_short[tt[2]]) > 0: #COP forwards
            sign_x = 1
        else: #COP moves backwards -> mirror Fx and COPx on y-axis
            sign_x = -1
        pres.Fx2 = sign_x*Fx_b_short
        pres.Fy2 = sign_x*Fy_b_short
        pres.Fz2 = Fz_b_short
        pres.CoPx2 = sign_x*CoPx_b_short
        pres.CoPy2 = sign_x*CoPy_b_short
        pres.CoPz2 = CoPz_b_short
        if sign_x == -1:
            pres.Fx1 = sign_x*Fx_a_short
            pres.Fy1 = sign_x*Fy_a_short
            pres.Fz1 = Fz_a_short
            pres.CoPx1 = sign_x*CoPx_a_short
            pres.CoPy1 = sign_x*CoPy_a_short
            pres.CoPz1 = CoPz_a_short
        elif sign_x == 1: # flip order of forces
            pres.Fx1 = sign_x*Fx_c_short
            pres.Fy1 = sign_x*Fy_c_short
            pres.Fz1 = Fz_c_short
            pres.CoPx1 = sign_x*CoPx_c_short
            pres.CoPy1 = sign_x*CoPy_c_short
            pres.CoPz1 = CoPz_c_short
    else:
        pres.Fx1 = []
        pres.Fy1 = []
        pres.Fz1 = []
        pres.Fx2 = []
        pres.Fy2 = []
        pres.Fz2 = []
        pres.CoPx1 = []
        pres.CoPy1 = []
        pres.CoPz1 = []
        pres.CoPx2 = []
        pres.CoPy2 = []
        pres.CoPz2 = []
        print('error')

    #------------------------------------------normalize to stance time
    stance1 = len(range(tdto[0],tdto[3]))
    stance2 = len(range(tdto[2],tdto[5]))
    gait_cycle = len(range(tdto[0],tdto[4]))
    new_length = 101
    x = range(0,new_length)


    #-------------------length single support phase normalized to 100
    ssp1_beg = int((len(range(tdto[0],tdto[1]))*100)/len(range(tdto[0],tdto[3])))
    ssp1_end = int((len(range(tdto[0],tdto[2]))*100)/len(range(tdto[0],tdto[3])))
    ssp2_beg = int((len(range(tdto[2],tdto[3]))*100)/len(range(tdto[2],tdto[5])))
    ssp2_end = int((len(range(tdto[2],tdto[4]))*100)/len(range(tdto[2],tdto[5])))

    pres.Fx1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.Fx1[tdto[0]:tdto[3]])
    pres.Fx2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.Fx2[tdto[2]:tdto[5]])
    pres.Fy1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.Fy1[tdto[0]:tdto[3]])
    pres.Fy2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.Fy2[tdto[2]:tdto[5]])
    pres.Fz1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.Fz1[tdto[0]:tdto[3]])
    pres.Fz2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.Fz2[tdto[2]:tdto[5]])

    pres.COPx1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.CoPx1[tdto[0]:tdto[3]])
    pres.COPx2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.CoPy2[tdto[2]:tdto[5]])
    pres.COPy1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.CoPy1[tdto[0]:tdto[3]])
    pres.COPy2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.CoPy2[tdto[2]:tdto[5]])
    pres.COPz1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),pres.CoPz1[tdto[0]:tdto[3]])
    pres.COPz2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),pres.CoPz2[tdto[2]:tdto[5]])

    pres.COMx1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),np.squeeze(COM[tdto[0]:tdto[3],1]))
    pres.COMx2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),COM[tdto[2]:tdto[5],1])
    pres.COMy1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),np.squeeze(COM[tdto[0]:tdto[3],0]))
    pres.COMy2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),COM[tdto[2]:tdto[5],0])
    pres.COMz1_norm = np.interp(np.linspace(1,stance1,new_length),np.linspace(1,stance1,stance1),COM[tdto[0]:tdto[3],2])
    pres.COMz2_norm = np.interp(np.linspace(1,stance2,new_length),np.linspace(1,stance2,stance2),COM[tdto[2]:tdto[5],2])

    pres.speed = abs(((COM[tdto[4],1]-COM[tdto[0],1])/gait_cycle)*preadin.Frequ_video)#(Comx(TD3) - Comx(TD1))/(td3-td1) * frequency
    return tdto, tt, COM, direction, sign_x

#------------------------------------------------------------------
def load_data(preadin,pres, pkinetic, import_file_path,k):
    with open(import_file_path[k]) as datatxt: #to find start and end of data
        try:
            lines=datatxt.readlines()
        except:
            lines = []
            print("error at " + import_file_path[k])
        for i in range(0,len(lines)):
            l=(lines[i]).rstrip("\n").split("\t")
            if str(l).find(preadin.Keyword_dyn) != -1: #kinetics: search entered keyword in data file
                start_kinetics=i + preadin.Dist_keyword_dyn; #kinetics: search line of keyword + entered distance=start line of kinetic data
            if str(l).find(preadin.Keyword_kin) != -1: #kinematics
                end_kinetics=i - preadin.Dist_keyword_dyn_end;
                start_kinematics=i + preadin.Dist_keyword_kin; #kinematics: search line of keyword + entered distance=start line of kinematic data
            if str(l).find(preadin.Keyword_kin_end) != -1:
                end_kinematics=i - preadin.Dist_keyword_kin_end;
        length_footer = len(lines)-end_kinematics-2

    DataDyn=np.loadtxt(import_file_path[k], skiprows=start_kinetics,  max_rows=end_kinetics - start_kinetics)
    try:
        pres.DataKin=np.genfromtxt(import_file_path[k],delimiter="\t",skip_header=start_kinematics,skip_footer=length_footer) #model output
        pres.DataKin_2=np.genfromtxt(import_file_path[k],delimiter="\t",skip_header=end_kinematics+4) # trajectories
    except: #error
        print(import_file_path[k])
        exit()
    lines_start = 14
    try:
        pres.DataTdto=np.genfromtxt(import_file_path[k],delimiter="\t",skip_header=3,skip_footer=len(lines)-lines_start) #read from header
    except: #error
        print(import_file_path[k])
        exit()
    ################Events
    #save which foot (left, right) and which event (TD, TO)
    # file = open(import_file_path[k])
    events = open(import_file_path[k]).readlines()
    #in this lines, there are the events
    foot = []
    TD = []
    for ii in range(3,lines_start-4):
        a = events[ii].split()
        foot = np.append(foot, a.count('Right')) # 1 = right foot, 0 = left foot
        TD = np.append(TD, a.count('Strike')) # 1= TD (Foot strike), 0 = TO (Foot off)

    pres.foot = foot
    pres.TD = TD
    pres.offset = DataDyn[0,0] #it doesn't start at 1, but at e.g. 317, this is the offset

    # consider entered sign
    if (preadin.Pm_fx1 == "+"):
        sign = 1
    else: sign = -1
    #readin correct column for GRF and COP (first force plate):
    pres.Fx = np.transpose(sign*np.array([DataDyn[:,preadin.Col_fx1-1]]))
    pres.Fy = np.transpose(sign*np.array([DataDyn[:,preadin.Col_fx1-2]]))
    if (preadin.Pm_fz1 == "+"):
        sign = 1
    else: sign = -1
    pres.Fz = np.transpose(sign*np.array([DataDyn[:,preadin.Col_fz1-1]]))
    if (preadin.Pm_copx1 == "+"):
        sign = 1
    else: sign = -1
    pres.CoPx = np.transpose(sign*np.array([DataDyn[:,preadin.Col_copx1-1]]))
    pres.CoPy = np.transpose(sign*np.array([DataDyn[:,preadin.Col_copx1-2]]))
    pres.CoPz = np.transpose(np.array([DataDyn[:,preadin.Col_copz1-1]]))

    if (preadin.Pm_fx2 == "+"):
        sign = 1
    else: sign = -1
    pres.Fx = np.append(pres.Fx, sign*np.transpose([DataDyn[:,preadin.Col_fx2-1]]), axis = 1)
    pres.Fy = np.append(pres.Fy, sign*np.transpose([DataDyn[:,preadin.Col_fx2-2]]), axis = 1)
    if (preadin.Pm_fz2 == "+"):
        sign = 1
    else: sign = -1
    pres.Fz = np.append(pres.Fz, sign*np.transpose([DataDyn[:,preadin.Col_fz2-1]]), axis = 1)
    if (preadin.Pm_copx2 == "+"):
        sign = 1
    else: sign = -1
    pres.CoPx = np.append(pres.CoPx, sign*np.transpose([DataDyn[:,preadin.Col_copx2-1]]), axis = 1)
    pres.CoPy = np.append(pres.CoPy, sign*np.transpose([DataDyn[:,preadin.Col_copx2-2]]), axis = 1)
    pres.CoPz = np.append(pres.CoPz, np.transpose([DataDyn[:,preadin.Col_copz2-1]]), axis = 1)

    if (preadin.Pm_fx3 == "+"):
        sign = 1
    else: sign = -1
    pres.Fx = np.append(pres.Fx, sign*np.transpose([DataDyn[:,preadin.Col_fx3-1]]), axis = 1)
    pres.Fy = np.append(pres.Fy, sign*np.transpose([DataDyn[:,preadin.Col_fx3-2]]), axis = 1)
    if (preadin.Pm_fz3 == "+"):
        sign = 1
    else: sign = -1
    pres.Fz = np.append(pres.Fz, sign*np.transpose([DataDyn[:,preadin.Col_fz3-1]]), axis = 1)
    if (preadin.Pm_copx3 == "+"):
        sign = 1
    else: sign = -1
    pres.CoPx = np.append(pres.CoPx, sign*np.transpose([DataDyn[:,preadin.Col_copx3-1]]), axis = 1)
    pres.CoPy = np.append(pres.CoPy, sign*np.transpose([DataDyn[:,preadin.Col_copx3-2]]), axis = 1)
    pres.CoPz = np.append(pres.CoPz, np.transpose([DataDyn[:,preadin.Col_copz3-1]]), axis = 1)

    #if CoP1 was measured in mm, convert to meter:
    if (pkinetic.unit.get() == 1):
        pres.CoPx=np.multiply(pres.CoPx,1/1000)
        pres.CoPy=np.multiply(pres.CoPy,1/1000)
        pres.CoPz=np.multiply(pres.CoPz,1/1000)