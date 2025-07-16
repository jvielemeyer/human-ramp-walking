import numpy as np
import matplotlib.pyplot as plt
import os


def plot_moment_power(ankleM, ankleP, kneeM, kneeP, hipM, hipP, ankleM_std,ankleP_std, kneeM_std, kneeP_std, hipM_std, hipP_std):
    transp = 0.2
    line = 2 #linewidth
    length_vector = 101

    ankleM_level = np.mean(np.array([ankleM[2][1],ankleM[5][1]]),axis = 0)
    ankleM_level_std=np.mean(np.array([ankleM_std[2][1],ankleM_std[5][1]]),axis = 0)
    kneeM_level = np.mean(np.array([kneeM[2][1],kneeM[5][1]]),axis = 0)
    kneeM_level_std=np.mean(np.array([kneeM_std[2][1],kneeM_std[5][1]]),axis = 0)
    hipM_level = np.mean(np.array([hipM[2][1],hipM[5][1]]),axis = 0)
    hipM_level_std=np.mean(np.array([hipM_std[2][1],hipM_std[5][1]]),axis = 0)
    ankleP_level = np.mean(np.array([ankleP[2][1],ankleP[5][1]]),axis = 0)
    ankleP_level_std=np.mean(np.array([ankleP_std[2][1],ankleP_std[5][1]]),axis = 0)
    kneeP_level = np.mean(np.array([kneeP[2][1],kneeP[5][1]]),axis = 0)
    kneeP_level_std=np.mean(np.array([kneeP_std[2][1],kneeP_std[5][1]]),axis = 0)
    hipP_level = np.mean(np.array([hipP[2][1],hipP[5][1]]),axis = 0)
    hipP_level_std=np.mean(np.array([hipP_std[2][1],hipP_std[5][1]]),axis = 0)

    plt.rc ('font', size = 15)
    plt.rc ('axes', labelsize = 15)
    plt.rc ('xtick', labelsize = 15)
    plt.rc ('ytick', labelsize = 15)
    plt.rc ('legend', fontsize = 10)
    fig1, axs = plt.subplots(3,2)#,figsize=(16, 16))

    #-----------Moments
    axs[0,0].plot(hipM[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,0].plot(hipM[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,0].plot(hipM_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,0].plot(hipM[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,0].plot(hipM[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,0].fill_between(range(length_vector), hipM_level-hipM_level_std, hipM_level+hipM_level_std,color ='k', alpha = transp)

    axs[1,0].plot(kneeM[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,0].plot(kneeM[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,0].plot(kneeM_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,0].plot(kneeM[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,0].plot(kneeM[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,0].fill_between(range(length_vector), kneeM_level-kneeM_level_std, kneeM_level+kneeM_level_std,color ='k', alpha = transp)

    axs[2,0].plot(ankleM[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,0].plot(ankleM[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,0].plot(ankleM_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,0].plot(ankleM[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,0].plot(ankleM[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,0].fill_between(range(length_vector), ankleM_level-ankleM_level_std, ankleM_level+ankleM_level_std,color ='k', alpha = transp)


    #------------------Power

    axs[0,1].plot(hipP[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,1].plot(hipP[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,1].plot(hipP_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,1].plot(hipP[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,1].plot(hipP[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,1].fill_between(range(length_vector), hipP_level-hipP_level_std, hipP_level+hipP_level_std,color ='k', alpha = transp)

    axs[1,1].plot(kneeP[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,1].plot(kneeP[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,1].plot(kneeP_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,1].plot(kneeP[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,1].plot(kneeP[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,1].fill_between(range(length_vector), kneeP_level-kneeP_level_std, kneeP_level+kneeP_level_std,color ='k', alpha = transp)

    axs[2,1].plot(ankleP[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,1].plot(ankleP[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,1].plot(ankleP_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,1].plot(ankleP[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,1].plot(ankleP[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,1].fill_between(range(length_vector), ankleP_level-ankleP_level_std, ankleP_level+ankleP_level_std,color ='k', alpha = transp)

    for i in range(0,3):
        axs[i,0].axis([0, 100, -1.5, 2])
        axs[i,1].axis([0, 100, -3.8, 6])
        for j in range(0,2):
            axs[i,j].axhline(y=0, color='k', linestyle='-',alpha = 0.5)


    axs[0,0].legend(["ramp 10° up","ramp 7.5° up","level mean $\pm$ std","ramp 7.5° down","ramp 10° down"])
    axs[0,0].set(ylabel='Hip Moment [Nm/kg]')
    axs[1,0].set(ylabel='Knee Moment [Nm/kg]')
    axs[2,0].set(xlabel='gait cycle [%]', ylabel='Ankle Moment [Nm/kg]')
    axs[0,1].set(ylabel='Hip Power [W/kg]')
    axs[1,1].set(ylabel='Knee Power [W/kg]')
    axs[2,1].set(xlabel='gait cycle [%]', ylabel='Ankle Power [W/kg]')
    plt.draw()
    plt.show()

def plot_angles(head, thorax, shoulder_ipsi,shoulder_contra, elbow_ipsi, elbow_contra, hip_ipsi, hip_contra, knee_ipsi, knee_contra, ankle_ipsi, ankle_contra, head_std, thorax_std, shoulder_ipsi_std,shoulder_contra_std, elbow_ipsi_std, elbow_contra_std, hip_ipsi_std, hip_contra_std, knee_ipsi_std, knee_contra_std, ankle_ipsi_std, ankle_contra_std):
    transp = 0.2
    line = 2 #linewidth
    length_vector = 101

     #--------------mean over level up and level down:
    #[0] ramp 10 up, [1] ramp 10 down, (2) level up, (3) ramp 75 down, [4] ramp 75 up, [5] level down
    head_level = np.mean(np.array([head[2][1],head[5][1]]),axis = 0)
    head_level_std=np.mean(np.array([head_std[2][1],head_std[5][1]]),axis = 0)
    thorax_level = np.mean(np.array([thorax[2][1],thorax[5][1]]),axis = 0)
    thorax_level_std=np.mean(np.array([thorax_std[2][1],thorax_std[5][1]]),axis = 0)
    shoulder_ipsi_level = np.mean(np.array([shoulder_ipsi[2][1],shoulder_ipsi[5][1]]),axis = 0)
    shoulder_ipsi_level_std=np.mean(np.array([shoulder_ipsi_std[2][1],shoulder_ipsi_std[5][1]]),axis = 0)
    shoulder_contra_level = np.mean(np.array([shoulder_contra[2][1],shoulder_contra[5][1]]),axis = 0)
    shoulder_contra_level_std=np.mean(np.array([shoulder_contra_std[2][1],shoulder_contra_std[5][1]]),axis = 0)
    elbow_ipsi_level = np.mean(np.array([elbow_ipsi[2][1],elbow_ipsi[5][1]]),axis = 0)
    elbow_ipsi_level_std=np.mean(np.array([elbow_ipsi_std[2][1],elbow_ipsi_std[5][1]]),axis = 0)
    elbow_contra_level = np.mean(np.array([elbow_contra[2][1],elbow_contra[5][1]]),axis = 0)
    elbow_contra_level_std=np.mean(np.array([elbow_contra_std[2][1],elbow_contra_std[5][1]]),axis = 0)
    hip_ipsi_level = np.mean(np.array([hip_ipsi[2][1],hip_ipsi[5][1]]),axis = 0)
    hip_ipsi_level_std=np.mean(np.array([hip_ipsi_std[2][1],hip_ipsi_std[5][1]]),axis = 0)
    hip_contra_level = np.mean(np.array([hip_contra[2][1],hip_contra[5][1]]),axis = 0)
    hip_contra_level_std=np.mean(np.array([hip_contra_std[2][1],hip_contra_std[5][1]]),axis = 0)
    knee_ipsi_level = np.mean(np.array([knee_ipsi[2][1],knee_ipsi[5][1]]),axis = 0)
    knee_ipsi_level_std=np.mean(np.array([knee_ipsi_std[2][1],knee_ipsi_std[5][1]]),axis = 0)
    knee_contra_level = np.mean(np.array([knee_contra[2][1],knee_contra[5][1]]),axis = 0)
    knee_contra_level_std=np.mean(np.array([knee_contra_std[2][1],knee_contra_std[5][1]]),axis = 0)
    ankle_ipsi_level = np.mean(np.array([ankle_ipsi[2][1],ankle_ipsi[5][1]]),axis = 0)
    ankle_ipsi_level_std=np.mean(np.array([ankle_ipsi_std[2][1],ankle_ipsi_std[5][1]]),axis = 0)
    ankle_contra_level = np.mean(np.array([ankle_contra[2][1],ankle_contra[5][1]]),axis = 0)
    ankle_contra_level_std=np.mean(np.array([ankle_contra_std[2][1],ankle_contra_std[5][1]]),axis = 0)

    #-----------------------------------------
    plt.rc ('font', size = 12)
    plt.rc ('axes', labelsize = 12)
    plt.rc ('xtick', labelsize = 10)
    plt.rc ('ytick', labelsize = 10)
    plt.rc ('legend', fontsize = 10)
    nmbx = 3
    nmby = 4
    fig1, axs = plt.subplots(nmbx,nmby) #,figsize=(20, 16))

    axs[0,0].plot(head[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,0].plot(head[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,0].plot(head_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,0].plot(head[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,0].plot(head[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,0].fill_between(range(length_vector), head_level-head_level_std, head_level+head_level_std,color ='k', alpha = transp)

    axs[0,1].plot(thorax[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,1].plot(thorax[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,1].plot(thorax_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,1].plot(thorax[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,1].plot(thorax[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,1].fill_between(range(length_vector), thorax_level-thorax_level_std, thorax_level+thorax_level_std,color ='k', alpha = transp)

    axs[1,0].plot(shoulder_ipsi[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,0].plot(shoulder_ipsi[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,0].plot(shoulder_ipsi_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,0].plot(shoulder_ipsi[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,0].plot(shoulder_ipsi[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,0].fill_between(range(length_vector), shoulder_ipsi_level-shoulder_ipsi_level_std, shoulder_ipsi_level+shoulder_ipsi_level_std,color ='k', alpha = transp)

    axs[1,1].plot(shoulder_contra[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,1].plot(shoulder_contra[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,1].plot(shoulder_contra_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,1].plot(shoulder_contra[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,1].plot(shoulder_contra[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,1].fill_between(range(length_vector), shoulder_contra_level-shoulder_contra_level_std, shoulder_contra_level+shoulder_contra_level_std,color ='k', alpha = transp)

    axs[2,0].plot(elbow_ipsi[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,0].plot(elbow_ipsi[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,0].plot(elbow_ipsi_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,0].plot(elbow_ipsi[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,0].plot(elbow_ipsi[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,0].fill_between(range(length_vector), elbow_ipsi_level-elbow_ipsi_level_std, elbow_ipsi_level+elbow_ipsi_level_std,color ='k', alpha = transp)

    axs[2,1].plot(elbow_contra[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,1].plot(elbow_contra[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,1].plot(elbow_contra_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,1].plot(elbow_contra[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,1].plot(elbow_contra[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,1].fill_between(range(length_vector), elbow_contra_level-elbow_contra_level_std, elbow_contra_level+elbow_contra_level_std,color ='k', alpha = transp)

    axs[0,2].plot(hip_ipsi[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,2].plot(hip_ipsi[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,2].plot(hip_ipsi_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,2].plot(hip_ipsi[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,2].plot(hip_ipsi[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,2].fill_between(range(length_vector), hip_ipsi_level-hip_ipsi_level_std, hip_ipsi_level+hip_ipsi_level_std,color ='k', alpha = transp)

    axs[0,3].plot(hip_contra[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[0,3].plot(hip_contra[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[0,3].plot(hip_contra_level,color = (0,0,0), linewidth = line)  #level, black
    axs[0,3].plot(hip_contra[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[0,3].plot(hip_contra[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[0,3].fill_between(range(length_vector), hip_contra_level-hip_contra_level_std, hip_contra_level+hip_contra_level_std,color ='k', alpha = transp)

    axs[1,2].plot(knee_ipsi[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,2].plot(knee_ipsi[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,2].plot(knee_ipsi_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,2].plot(knee_ipsi[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,2].plot(knee_ipsi[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,2].fill_between(range(length_vector), knee_ipsi_level-knee_ipsi_level_std, knee_ipsi_level+knee_ipsi_level_std,color ='k', alpha = transp)

    axs[1,3].plot(knee_contra[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[1,3].plot(knee_contra[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[1,3].plot(knee_contra_level,color = (0,0,0), linewidth = line)  #level, black
    axs[1,3].plot(knee_contra[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[1,3].plot(knee_contra[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[1,3].fill_between(range(length_vector), knee_contra_level-knee_contra_level_std, knee_contra_level+knee_contra_level_std,color ='k', alpha = transp)

    axs[2,2].plot(ankle_ipsi[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,2].plot(ankle_ipsi[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,2].plot(ankle_ipsi_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,2].plot(ankle_ipsi[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,2].plot(ankle_ipsi[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,2].fill_between(range(length_vector), ankle_ipsi_level-ankle_ipsi_level_std, ankle_ipsi_level+ankle_ipsi_level_std,color ='k', alpha = transp)

    axs[2,3].plot(ankle_contra[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    axs[2,3].plot(ankle_contra[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    axs[2,3].plot(ankle_contra_level,color = (0,0,0), linewidth = line)  #level, black
    axs[2,3].plot(ankle_contra[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    axs[2,3].plot(ankle_contra[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    axs[2,3].fill_between(range(length_vector), ankle_contra_level-ankle_contra_level_std, ankle_contra_level+ankle_contra_level_std,color ='k', alpha = transp)

#----------------------------------------

    axs[0,0].axis([0, 100, -30, 30])
    axs[0,1].axis([0, 100, -30, 30])
    axs[0,2].axis([0, 100, -20, 60])
    axs[0,3].axis([0, 100, -20, 60])
    axs[1,0].axis([0, 100, -30, 15])
    axs[1,1].axis([0, 100, -30, 15])
    axs[1,2].axis([0, 100, -20, 80])
    axs[1,3].axis([0, 100, -20, 80])
    axs[2,0].axis([0, 100, 20, 65])
    axs[2,1].axis([0, 100, 20, 65])
    axs[2,2].axis([0, 100, -30, 25])
    axs[2,3].axis([0, 100, -30, 25])

    axs[0,0].legend(["ramp 10° up","ramp 7.5° up","level mean $\pm$ std","ramp 7.5° down","ramp 10° down"])
    axs[0,0].set(ylabel='Head Angle [deg]')
    axs[0,1].set(ylabel='Thorax Angle [deg]')
    axs[1,0].set(ylabel='Shoulder Angle ipsi [deg]')
    axs[1,1].set(ylabel='Shoulder Angle contra [deg]')
    axs[2,0].set(xlabel='gait cycle [%]',ylabel='Elbow Angle ipsi [deg]')
    axs[2,1].set(xlabel='gait cycle [%]',ylabel='Elbow Angle contra [deg]')
    axs[0,2].set(ylabel='Hip Angle ipsi [deg]')
    axs[0,3].set(ylabel='Hip Angle contra [deg]')
    axs[1,2].set(ylabel='Knee Angle ipsi [deg]')
    axs[1,3].set(ylabel='Knee Angle contra [deg]')
    axs[2,2].set(xlabel='gait cycle [%]',ylabel='Ankle Angle ipsi [deg]')
    axs[2,3].set(xlabel='gait cycle [%]',ylabel='Ankle Angle contra [deg]')
    plt.draw()
    plt.show()



def plot_GRFs(Fx1,Fx2,Fz1, Fz2,Fx1_std,Fx2_std,Fz1_std, Fz2_std):
    transp = 0.2
    line = 2 #linewidth
    length_vector = 101
    number_of_settings = 6 #level_up, level_down, ramp75_up,...
    #----------------mean of both force plates:
    Fx = Fx1
    Fz = Fz1
    Fx_std = Fx1_std
    Fz_std = Fz1_std

    for i in range(0,number_of_settings):
        Fx[i][1] = np.mean(np.array([Fx1[i][1],Fx2[i][1]]),axis = 0)
        Fz[i][1] = np.mean(np.array([Fz1[i][1],Fz2[i][1]]),axis = 0)
        Fx_std[i][1] = np.mean(np.array([Fx1_std[i][1],Fx2_std[i][1]]),axis = 0)
        Fz_std[i][1] = np.mean(np.array([Fz1_std[i][1],Fz2_std[i][1]]),axis = 0)


   #--------------mean over level up and level down: überschreibe level up
  #[0] ramp 10 up, [1] ramp 10 down, (2) level up, (3) ramp 75 down, [4] ramp 75 up, [5] level down
    Fx[2][1] = np.mean(np.array([Fx[2][1],Fx[5][1]]),axis = 0)
    Fz[2][1] = np.mean(np.array([Fz[2][1],Fz[5][1]]),axis = 0)
    Fx_std[2][1] = np.mean(np.array([Fx_std[2][1],Fx_std[5][1]]),axis = 0)
    Fz_std[2][1] = np.mean(np.array([Fz_std[2][1],Fz_std[5][1]]),axis = 0)

    plt.rc ('font', size = 15)
    plt.rc ('axes', labelsize = 15)
    plt.rc ('xtick', labelsize = 15)
    plt.rc ('ytick', labelsize = 15)
    plt.rc ('legend', fontsize = 15)
    fig2 = plt.figure(2) #,figsize=(12, 12))
    plt.plot(Fx[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    plt.plot(Fx[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    plt.plot(Fx[2][1],color = (0,0,0), linewidth = line)  #level, black
    plt.plot(Fx[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    plt.plot(Fx[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    plt.fill_between(range(length_vector), Fx[2][1]-Fx_std[2][1], Fx[2][1]+Fx_std[2][1],color ='k', alpha = transp)
    plt.plot(Fz[0][1],color = (0,0,0.9), linewidth = line) #10 up, dark blue
    plt.plot(Fz[4][1],color = (0,0.7,1), linewidth = line) #7.5 up, light blue
    plt.plot(Fz[2][1],color = (0,0,0), linewidth = line) #level, black
    plt.plot(Fz[3][1],color = (1,0.5,0.4), linewidth = line) #7.5 down, light red
    plt.plot(Fz[1][1],color = (0.8,0,0.2), linewidth = line) #10 down, dark red

    plt.fill_between(range(length_vector), Fz[2][1]-Fz_std[2][1], Fz[2][1]+Fz_std[2][1],color ='k', alpha = transp)
    plt.axhline(y=0, color='k', linestyle='-',alpha = 0.5)

    plt.axis([0, 100, -0.25, 1.5])

    plt.legend(["ramp 10° up","ramp 7.5° up","level mean $\pm$ std","ramp 7.5° down","ramp 10° down"])
    plt.xlabel('contact time [%]')
    plt.ylabel('GRF [BW]')
    plt.draw()
    plt.show()


