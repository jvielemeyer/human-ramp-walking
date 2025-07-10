import csv
import numpy as np
import matplotlib.pyplot as plt
import os



#save data in csv, rubric = VPP, ankle, hip,...
def button_save_data(Liste,filename,rubric):
   # fullpath = str(rubric) + "_" + str(filename) + ".csv"
    fullpath = "VPP_Data.csv"
    with open(fullpath,'w') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        for index in range(0,len(Liste)):
            writer.writerow(Liste[index])
#-------------------------------------------------------------------------------

def data_save_npz(pres,file_name,folder,
    AnkleAngle_ipsi_x, AnkleAngle_ipsi_y,AnkleAngle_ipsi_z,
    AnkleAngle_contra_x, AnkleAngle_contra_y,AnkleAngle_contra_z,
    AnkleMoment_x, AnkleMoment_y, AnkleMoment_z,
    AnklePower_x, AnklePower_y, AnklePower_z,
    KneeAngle_ipsi_x, KneeAngle_ipsi_y, KneeAngle_ipsi_z,
    KneeAngle_contra_x, KneeAngle_contra_y, KneeAngle_contra_z,
    KneeMoment_x, KneeMoment_y, KneeMoment_z,
    KneePower_x, KneePower_y, KneePower_z,
    HipAngle_ipsi_x, HipAngle_ipsi_y, HipAngle_ipsi_z,
    HipAngle_contra_x, HipAngle_contra_y, HipAngle_contra_z,
    HipMoment_x, HipMoment_y, HipMoment_z,
    HipPower_x, HipPower_y, HipPower_z,
    ShoulderAngle_ipsi_x,ShoulderAngle_ipsi_y,ShoulderAngle_ipsi_z,
    ShoulderAngle_contra_x,ShoulderAngle_contra_y,ShoulderAngle_contra_z,
    ElbowAngle_ipsi_x,ElbowAngle_ipsi_y,ElbowAngle_ipsi_z,
    ElbowAngle_contra_x,ElbowAngle_contra_y,ElbowAngle_contra_z,
    HeadAngle_x,HeadAngle_y,HeadAngle_z,
    ThoraxAngle_x,ThoraxAngle_y,ThoraxAngle_z,
    Fx1, Fx2,Fy1, Fy2, Fz1, Fz2,
    COPx1, COPx2,COPy1, COPy2, COPz1, COPz2,
    COMx1, COMx2,COMy1, COMy2, COMz1, COMz2,
    VPP1, VPP2, r1, r2,
    speed):
    newpath = r'Data_Level_2' + "/" + file_name[0:5] + "/" +folder
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    np.savez(newpath  + "/" + str(file_name) + ".npz", prob=file_name[0:5] ,folder=folder,
        ankleAx=AnkleAngle_ipsi_x, ankleAy=AnkleAngle_ipsi_y, ankleAz=AnkleAngle_ipsi_z,
        ankleAx_contra=AnkleAngle_contra_x, ankleAy_contra=AnkleAngle_contra_y, ankleAz_contra=AnkleAngle_contra_z,
        ankleMx=AnkleMoment_x, ankleMy=AnkleMoment_y, ankleMz=AnkleMoment_z,
        anklePx=AnklePower_x, anklePy=AnklePower_y, anklePz=AnklePower_z,
        kneeAx=KneeAngle_ipsi_x, kneeAy=KneeAngle_ipsi_y, kneeAz=KneeAngle_ipsi_z,
        kneeAx_contra=KneeAngle_contra_x, kneeAy_contra=KneeAngle_contra_y, kneeAz_contra=KneeAngle_contra_z,
        kneeMx=KneeMoment_x, kneeMy=KneeMoment_y, kneeMz=KneeMoment_z,
        kneePx=KneePower_x, kneePy=KneePower_y, kneePz=KneePower_z,
        hipAx=HipAngle_ipsi_x, hipAy=HipAngle_ipsi_y, hipAz=HipAngle_ipsi_z,
        hipAx_contra=HipAngle_contra_x, hipAy_contra=HipAngle_contra_y, hipAz_contra=HipAngle_contra_z,
        hipMx=HipMoment_x, hipMy=HipMoment_y, hipMz=HipMoment_z,
        hipPx=HipPower_x, hipPy=HipPower_y, hipPz=HipPower_z,
        shoulderAx=ShoulderAngle_ipsi_x, shoulderAy=ShoulderAngle_ipsi_y, shoulderAz=ShoulderAngle_ipsi_z,
        shoulderAx_contra=ShoulderAngle_contra_x, shoulderAy_contra=ShoulderAngle_contra_y, shoulderAz_contra=ShoulderAngle_contra_z,
        elbowAx=ElbowAngle_ipsi_x, elbowAy=ElbowAngle_ipsi_y, elbowAz=ElbowAngle_ipsi_z,
        elbowAx_contra=ElbowAngle_contra_x, elbowAy_contra=ElbowAngle_contra_y, elbowAz_contra=ElbowAngle_contra_z,
        headAx=HeadAngle_x, headAy=HeadAngle_y, headAz=HeadAngle_z,
        thoraxAx=ThoraxAngle_x, thoraxAy=ThoraxAngle_y, thoraxAz=ThoraxAngle_z,
        GRFx1 = Fx1, GRFx2 = Fx2, GRFy1 = Fy1, GRFy2 = Fy2, GRFz1 = Fz1, GRFz2 = Fz2,
        CoPx1 = COPx1, CoPx2 = COPx2, CoPy1 = COPy1, CoPy2 = COPy2, CoPz1 = COPz1, CoPz2 = COPz2,
        CoMx1 = COMx1, CoMx2 = COMx2, CoMy1 = COMy1, CoMy2 = COMy2, CoMz1 = COMz1, CoMz2 = COMz2,
        VPP1 = VPP1, VPP2 = VPP2, R2_1 = r1, R2_2 = r2,
        gait_speed = speed)

#------------------------------------------------
def save_VPP_mean(VPP1_mean,VPP2_mean, R1_mean, R2_mean, VPP1_std,VPP2_std, R1_std, R2_std):
    #------------------create list:
    order = [2,4,0,5,3,1]
    ListeVPP_table = [""]
    Liste_names = [""]
    Liste_var = [["VPPx [m]"],["VPPz [m]"],["R_squared"]]
    Liste_mean = []
    Liste_std = []

    for index in order: #header
        Liste_names.extend([VPP1_mean[index][0]])
    ListeVPP_table.append(Liste_names)

    for i in range(0,len(Liste_var)): #0,1,2: VPPx, VPPz, R2
        ListeVPP_table.append("")
        ListeVPP_table.append(Liste_var[i])
        Liste_mean.extend(["mean"])
        Liste_std.extend(["std"])
        for index in order:
            mean1 = VPP1_mean[index][1]
            std1 = VPP1_std[index][1]
            if i == 2:
                mean1 = R1_mean[index][1]
                std1 = R1_std[index][1]
                Liste_mean.extend([mean1]) #i=0 x, i=1 z, i=2 R^2
                Liste_std.extend([std1])
            else:
                Liste_mean.extend([mean1[i]]) #i=0 x, i=1 z, i=2 R^2
                Liste_std.extend([std1[i]])

        ListeVPP_table.extend([Liste_mean[i*(len(Liste_names)):len(Liste_names)+i*len(Liste_names)]])
        ListeVPP_table.extend([Liste_std[i*(len(Liste_names)):len(Liste_names)+i*len(Liste_names)]])

   # fullpath = str(rubric) + "_" + str(filename) + ".csv"
    fullpath = "VPP_mean.csv"
    with open(fullpath, 'w') as csvfile:
        writer=csv.writer(csvfile)
        for index in range(0,len(ListeVPP_table)):
            writer.writerow(ListeVPP_table[index])