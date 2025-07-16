import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_kin_single_lower(ankleA,ankleM,ankleP, kneeA, kneeM, kneeP, hipA, hipM, hipP):

    length_vector = 101
    plt.rc ('font', size = 15)
    plt.rc ('axes', labelsize = 15)
    plt.rc ('xtick', labelsize = 15)
    plt.rc ('ytick', labelsize = 15)
    plt.rc ('legend', fontsize = 10)
    fig1, axs = plt.subplots(3,3,figsize=(16, 16))

    colo = ["b","g","y","m","k","r","c","b","g","y","m","k","r"]
    for index in range(0,len(ankleA)):
        if isinstance(ankleA[index], str):
            name = str(ankleA[index])

        if not isinstance(ankleA[index], str): #no string
            axs[0,0].plot(ankleA[index], color = colo[int(name[3:5])-1])
            axs[1,0].plot(kneeA[index],color = colo[int(name[3:5])-1])
            axs[2,0].plot(hipA[index],color = colo[int(name[3:5])-1])
            axs[0,1].plot(ankleM[index],color = colo[int(name[3:5])-1])
            axs[1,1].plot(kneeM[index],color = colo[int(name[3:5])-1])
            axs[2,1].plot(hipM[index],color = colo[int(name[3:5])-1])
            axs[0,2].plot(ankleP[index],color = colo[int(name[3:5])-1])
            axs[1,2].plot(kneeP[index],color = colo[int(name[3:5])-1])
            axs[2,2].plot(hipP[index],color = colo[int(name[3:5])-1])

    axs[0,0].set(ylabel='Ankle Angle [deg]')
    axs[1,0].set(ylabel='Knee Angle [deg]')
    axs[2,0].set(xlabel='gait cycle [%]', ylabel='Hip Angle [deg]')
    axs[0,1].set(ylabel='Ankle Moment [Nm/kg]')
    axs[1,1].set(ylabel='Knee Moment [Nm/kg]')
    axs[2,1].set(xlabel='gait cycle [%]', ylabel='Hip Moment [Nm/kg]')
    axs[0,2].set(ylabel='Ankle Power [W/kg]')
    axs[1,2].set(ylabel='Knee Power [W/kg]')
    axs[2,2].set(xlabel='gait cycle [%]', ylabel='Hip Power [W/kg]')
    plt.show()

def plot_kin_single_upper(head, thorax, shoulder_ipsi,shoulder_contra, elbow_ipsi, elbow_contra):
    length_vector = 101
    plt.rc ('font', size = 15)
    plt.rc ('axes', labelsize = 15)
    plt.rc ('xtick', labelsize = 15)
    plt.rc ('ytick', labelsize = 15)
    plt.rc ('legend', fontsize = 10)
    fig1, axs = plt.subplots(3,2)#,figsize=(16, 16))

    colo = ["b","g","y","m","k","r","c","b","g","y","m","k","c"]
    for index in range(0,len(head)):
        if isinstance(head[index], str):
            name = str(head[index])
        if not isinstance(head[index], str): #no string
            axs[0,0].plot(head[index],color = colo[int(name[3:5])-1])
            axs[0,1].plot(thorax[index],color = colo[int(name[3:5])-1])
            axs[1,0].plot(shoulder_ipsi[index],color = colo[int(name[3:5])-1])
            axs[2,0].plot(elbow_ipsi[index],color = colo[int(name[3:5])-1])
            axs[1,1].plot(shoulder_contra[index],color = colo[int(name[3:5])-1])
            axs[2,1].plot(elbow_contra[index],color = colo[int(name[3:5])-1])



    axs[0,0].set(ylabel='Head Angle [deg]')
    axs[0,1].set(ylabel='Thorax Angle [deg]')
    axs[1,0].set(ylabel='Shoulder ipsi Angle [deg]')
    axs[2,0].set(xlabel='gait cycle [%]', ylabel='Elbow ipsi Angle [deg]')
    axs[1,1].set(ylabel='Shoulder contra Angle [deg]')
    axs[2,1].set(xlabel='gait cycle [%]', ylabel='Elbow contra Angle [deg]')
    plt.show()

def scatterplot_VPP(VPP_mean, VPP):
    #take VPP relative to body height
    plt.rc ('font', size = 12)
    plt.rc ('axes', labelsize = 12)
    plt.rc ('xtick', labelsize = 10)
    plt.rc ('ytick', labelsize = 10)
    plt.rc ('legend', fontsize = 10)
    plt.figure(figsize=(12,12))
    transp = 0.5
    for index in range(0,len(VPP)):
        if isinstance(VPP[index], str): #yes string
            name = VPP[index]
            if "level" in name:
                clr = "k" #black
            elif "75_up" in name:
                clr = (0,0.7,1) #light blue
            elif "75_down" in name:
                clr = (1,0.5,0.4) #light red
            elif "10_up" in name:
                clr = (0,0,0.9) #dark blue
            elif "10_down" in name:
                clr = (0.8,0,0.2) #dark red
            else:
                clr = "w"
        else:
            v = VPP[index]


            plt.plot(v[0],v[1],'o',color = clr, alpha = transp)
    setup = ["ramp 10° up","ramp 7.5° up", "level","ramp 7.5° down","ramp 10° down"]
    k=0
    order = [0,4,2,3,1]
    m_level = (VPP_mean[2][1] + VPP_mean[5][1])/2
    for i in order:
        name = VPP_mean[i][0]
        if "level" in name:
            clr = (0,0,0) #black
        elif "75_up" in name:
            clr = (0,0.7,1) #light blue
        elif "75_down" in name:
            clr = (1,0.5,0.4) #light red
        elif "10_up" in name:
            clr = (0,0,0.9) #dark blue
        elif "10_down" in name:
            clr = (0.8,0,0.2) #dark red

        if i == 2:
            m = m_level
        else:
            m = VPP_mean[i][1]
        #print(m)
        plt.plot(m[0],m[1],'o',color = clr, markersize=15, mec = 'w', label = setup[k]) #mec = markeredgecolor
        k=k+1

    plt.plot(0,0,'+',color = 'k', markersize=15, label = 'CoM')
    #plt.plot(0,0,'+',color = 'k', markersize=15, label = 'hip')
    plt.xlabel('VPPx [m]')
    plt.ylabel('VPPz [m]')
    plt.legend()
    plt.axis('scaled')
    plt.xlim(-0.3, 0.3)
    plt.ylim(-0.1,1.2)

    plt.show()



















