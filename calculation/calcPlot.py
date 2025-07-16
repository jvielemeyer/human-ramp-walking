import matplotlib.pyplot as plt
import numpy as np
import math


def button_plot_input(Cop1,Cop2,Copz1,Copz2, Com, Fx_a, Fx_b, Fz_a, Fz_b,p,tdto):


  #--------------------------variables
    stance1 = len(range(tdto[0],tdto[3]))
    stance2 = len(range(tdto[2],tdto[5]))
    x = range(0,101)
    #-------------------length single support phase normalized to 100
    ssp1_beg = int((len(range(tdto[0],tdto[1]))*100)/len(range(tdto[0],tdto[3])))
    ssp1_end = int((len(range(tdto[0],tdto[2]))*100)/len(range(tdto[0],tdto[3])))
    ssp2_beg = int((len(range(tdto[2],tdto[3]))*100)/len(range(tdto[2],tdto[5])))
    ssp2_end = int((len(range(tdto[2],tdto[4]))*100)/len(range(tdto[2],tdto[5])))


    Fx1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),Fx_a[tdto[0]:tdto[3]])
    Fx2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Fx_b[tdto[2]:tdto[5]])
    Fz1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),Fz_a[tdto[0]:tdto[3]])
    Fz2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Fz_b[tdto[2]:tdto[5]])

    COPx1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),Cop1[tdto[0]:tdto[3]])
    COPx2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Cop2[tdto[2]:tdto[5]])
    COPz1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),Copz1[tdto[0]:tdto[3]])
    COPz2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Copz2[tdto[2]:tdto[5]])
    COPx1_zero = COPx1-COPx1[0]
    COPz1_zero = COPz1-COPz1[0]
    COPx2_zero = COPx2-COPx2[0]
    COPz2_zero = COPz2-COPz2[0]

    COMx1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),np.squeeze(Com[tdto[0]:tdto[3],0]))
    COMx2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Com[tdto[2]:tdto[5],0])
    COMz1 = np.interp(np.linspace(1,stance1,101),np.linspace(1,stance1,stance1),Com[tdto[0]:tdto[3],1])
    COMz2 = np.interp(np.linspace(1,stance2,101),np.linspace(1,stance2,stance2),Com[tdto[2]:tdto[5],1])
    #-------------------------------------------create plot

    fig, axs = plt.subplots(3, 2,figsize=(11, 9))

  # order for legend
    axs[0, 0].plot(range(1,ssp1_beg+1),Fx1[1:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[0, 0].plot(range(ssp1_beg,ssp1_end+1),Fx1[ssp1_beg:ssp1_end+1],color='b')

    axs[0, 0].plot(range(ssp2_beg,ssp2_end+1),Fx2[ssp2_beg:ssp2_end+1],color='r')
    axs[0, 0].legend(['1st contact (DSP) ','1st contact (SSP)','2nd contact'])
    #---------------
    axs[0, 0].plot(range(1,ssp2_beg+1),Fx2[1:ssp2_beg+1],alpha = 0.3,color='r')
    axs[0, 0].plot(range(ssp1_end,101),Fx1[ssp1_end:101],alpha = 0.3,color='blue')
    #---
    axs[0, 1].plot(range(1,ssp1_beg+1),Fz1[1:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[0, 1].plot(range(ssp1_beg,ssp1_end+1),Fz1[ssp1_beg:ssp1_end+1],color='b')
    axs[0, 1].plot(range(ssp1_end,101),Fz1[ssp1_end:101],alpha = 0.3,color='blue')
    #---
    axs[1, 0].plot(range(1,ssp1_beg+1),COMx1[1:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[1, 0].plot(range(ssp1_beg,ssp1_end+1),COMx1[ssp1_beg:ssp1_end+1],color='b')
    axs[1, 0].plot(range(ssp1_end,101),COMx1[ssp1_end:101],alpha = 0.3,color='blue')
    #---
    axs[1, 1].plot(range(1,ssp1_beg+1),COMz1[1:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[1, 1].plot(range(ssp1_beg,ssp1_end+1),COMz1[ssp1_beg:ssp1_end+1],color='b')
    axs[1, 1].plot(range(ssp1_end,101),COMz1[ssp1_end:101],alpha = 0.3,color='blue')

    #-----------------
    #delete this for COPx shifted to zero:

    axs[2, 0].plot(range(0,ssp1_beg+1),COPx1[0:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[2, 0].plot(range(ssp1_beg,ssp1_end+1),COPx1[ssp1_beg:ssp1_end+1],color='b')
    axs[2, 0].plot(range(ssp1_end,101),COPx1[ssp1_end:101],alpha = 0.3,color='blue')
    #---
    axs[2, 1].plot(range(0,ssp1_beg+1),COPz1[0:ssp1_beg+1],alpha = 0.3,color='blue')
    axs[2, 1].plot(range(ssp1_beg,ssp1_end+1),COPz1[ssp1_beg:ssp1_end+1],color='b')
    axs[2, 1].plot(range(ssp1_end,101),COPz1[ssp1_end:101],alpha = 0.3,color='blue')
    #----------------

    #take this for COPx shifted to zero:

    # axs[2, 0].plot(range(0,ssp1_beg+1),COPx1_zero[0:ssp1_beg+1],alpha = 0.3,color='blue')
    # axs[2, 0].plot(range(ssp1_beg,ssp1_end+1),COPx1_zero[ssp1_beg:ssp1_end+1],color='b')
    # axs[2, 0].plot(range(ssp1_end,101),COPx1_zero[ssp1_end:101],alpha = 0.3,color='blue')
    # #---
    # axs[2, 1].plot(range(0,ssp1_beg+1),COPz1_zero[0:ssp1_beg+1],alpha = 0.3,color='blue')
    # axs[2, 1].plot(range(ssp1_beg,ssp1_end+1),COPz1_zero[ssp1_beg:ssp1_end+1],color='b')
    # axs[2, 1].plot(range(ssp1_end,101),COPz1_zero[ssp1_end:101],alpha = 0.3,color='blue')

    #--------------------------


    axs[0, 0].plot(range(1,ssp2_beg+1),Fx2[1:ssp2_beg+1],alpha = 0.3,color='r')
    axs[0, 0].plot(range(ssp2_beg,ssp2_end+1),Fx2[ssp2_beg:ssp2_end+1],color='r')
    axs[0, 0].plot(range(ssp2_end,101),Fx2[ssp2_end:101],alpha = 0.3,color='r')
    #---
    axs[0, 1].plot(range(1,ssp2_beg+1),Fz2[1:ssp2_beg+1],alpha = 0.3,color='r')
    axs[0, 1].plot(range(ssp2_beg,ssp2_end+1),Fz2[ssp2_beg:ssp2_end+1],color='r')
    axs[0, 1].plot(range(ssp2_end,101),Fz2[ssp2_end:101],alpha = 0.3,color='r')
    #---
    axs[1, 0].plot(range(1,ssp2_beg+1),COMx2[1:ssp2_beg+1],alpha = 0.3,color='r')
    axs[1, 0].plot(range(ssp2_beg,ssp2_end+1),COMx2[ssp2_beg:ssp2_end+1],color='r')
    axs[1, 0].plot(range(ssp2_end,101),COMx2[ssp2_end:101],alpha = 0.3,color='r')
    #---
    axs[1, 1].plot(range(1,ssp2_beg+1),COMz2[1:ssp2_beg+1],alpha = 0.3,color='r')
    axs[1, 1].plot(range(ssp2_beg,ssp2_end+1),COMz2[ssp2_beg:ssp2_end+1],color='r')
    axs[1, 1].plot(range(ssp2_end,101),COMz2[ssp2_end:101],alpha = 0.3,color='r')
    #---------------------
    #delete this for COPx shifted to zero:

    axs[2, 0].plot(range(0,ssp2_beg+1),COPx2[0:ssp2_beg+1],alpha = 0.3,color='r')
    axs[2, 0].plot(range(ssp2_beg,ssp2_end+1),COPx2[ssp2_beg:ssp2_end+1],color='r')
    axs[2, 0].plot(range(ssp2_end,101),COPx2[ssp2_end:101],alpha = 0.3,color='r')
    #---
    axs[2, 1].plot(range(0,ssp2_beg+1),COPz2[0:ssp2_beg+1],alpha = 0.3,color='r')
    axs[2, 1].plot(range(ssp2_beg,ssp2_end+1),COPz2[ssp2_beg:ssp2_end+1],color='r')
    axs[2, 1].plot(range(ssp2_end,101),COPz2[ssp2_end:101],alpha = 0.3,color='r')
    #-----------------------

    #take this for COPx shifted to zero:

    # axs[2, 0].plot(range(0,ssp2_beg+1),COPx2_zero[0:ssp2_beg+1],alpha = 0.3,color='r')
    # axs[2, 0].plot(range(ssp2_beg,ssp2_end+1),COPx2_zero[ssp2_beg:ssp2_end+1],color='r')
    # axs[2, 0].plot(range(ssp2_end,101),COPx2_zero[ssp2_end:101],alpha = 0.3,color='r')
    # #---
    # axs[2, 1].plot(range(0,ssp2_beg+1),COPz2_zero[0:ssp2_beg+1],alpha = 0.3,color='r')
    # axs[2, 1].plot(range(ssp2_beg,ssp2_end+1),COPz2_zero[ssp2_beg:ssp2_end+1],color='r')
    # axs[2, 1].plot(range(ssp2_end,101),COPz2_zero[ssp2_end:101],alpha = 0.3,color='r')
   # axs[2,0].plot(range(1,101),COPx1_zero)

    axs[2, 0].set_xlim(0,101)

    #take this for COPx shifted to zero:

    #axs[2, 1].set_xlim(0,101)
    # min_all = min(min(COPx1_zero),min(COPx2_zero))
    # max_all = max(max(COPx1_zero),max(COPx2_zero))

    #delete this for COPx shifted to zero:
    min_all = min(min(COPx1),min(COPx2))
    max_all = max(max(COPx1),max(COPx2))

    tol = np.abs(max_all-min_all)*0.1
    axs[2, 0].set_ylim(min_all-tol,max_all+tol)

    #take this for COPx shifted to zero:
    #axs[2, 1].set_ylim(min_all-tol,max_all+tol)

    #--------------------------------------------zero line
    axs[0, 0].axhline(y=0, color='k', linestyle='-')
    axs[0, 1].axhline(y=0, color='k', linestyle='-')
    axs[2, 1].axhline(y=0, color='k', linestyle='-')

    #-----------------------------------------formatting


    axs[0, 0].set(ylabel='GRFx [bw]')
    axs[0, 1].set(ylabel='GRFz [bw]')
    axs[1, 0].set(ylabel='CoMx [m]')
    axs[1, 1].set(ylabel='CoMz [m]')

    #take this for COPx shifted to zero:

    # axs[2, 0].set(xlabel='stance phase (%)', ylabel='CoPx (shifted to zero) [m]')
    # axs[2, 1].set(xlabel='stance phase (%)', ylabel='CoPz (shifted to zero) [m]')

    #delete this for COPx shifted to zero:
    axs[2, 0].set(xlabel='stance phase (%)', ylabel='CoPx (absolute values) [m]')
    axs[2, 1].set(xlabel='stance phase (%)', ylabel='CoPz (absolute values) [m]')
    if (p > 0):
        plt.show()


  #---------------------
def VPP_plot(Force_x, Force_z, Com, COP,COPz,trunk_angle,align, VPP_opt, factor, j,file_name):

    COPx = COP
    plt.figure(j)
    plt.clf()
    if align == 0:
        trunk_angle = np.full([len(COP), 1], 0) #vertical aligned
    COPx_rot = np.full([len(COP), 1], np.nan)
    COPz_rot = np.full([len(COP), 1], np.nan)
    Force_x_rot = np.full([len(COP), 1], np.nan)
    Force_z_rot = np.full([len(COP), 1], np.nan)
    for ii in range(1, len(COPx), 5):  # draw each single force vector in Com-centered coordinate system
        COPx_rot[ii] = (COP[ii]- Com[ii,0])*math.cos(math.radians(trunk_angle[ii])) + (COPz[ii]- Com[ii,1])*math.sin(math.radians(trunk_angle[ii])) #angle in rad
        COPz_rot[ii] = -(COP[ii]- Com[ii,0])*math.sin(math.radians(trunk_angle[ii])) + (COPz[ii]- Com[ii,1])*math.cos(math.radians(trunk_angle[ii]))
        Force_x_rot[ii] = Force_x[ii]*math.cos(math.radians(trunk_angle[ii])) + Force_z[ii]*math.sin(math.radians(trunk_angle[ii]))
        Force_z_rot[ii] = -Force_x[ii]*math.sin(math.radians(trunk_angle[ii])) + Force_z[ii]*math.cos(math.radians(trunk_angle[ii]))

        if Com[0,0] < Com[-1,0]:
            beg = [(COPx_rot[ii]), COPz_rot[ii]]  # begin force vector (in COP)
            ende = [(Force_x_rot[ii] * factor + COPx_rot[ii]), (Force_z_rot[ii] * factor + COPz_rot[ii])]  # end force vector
        else:  #first value of Comx greater than last -> flip VPP plot and VPPx
            beg = [(COPx_rot[len(COPx)-ii]), COPz_rot[len(COPx)-ii]]  # begin force vector (in COP)
            ende = [(Force_x_rot[len(COPx)-ii] * factor + COPx_rot[len(COPx)-ii]), (Force_z_rot[len(COPx)-ii] * factor + COPz_rot[len(COPx)-ii])]  # end force vector

        #take this for color code of vectors:
        #plt.plot([beg[0], ende[0]], [beg[1], ende[1]], color=[1, 0, 0])
        #plt.plot([beg[0], ende[0]], [beg[1], ende[1]], color=[0, 0, 0])
        #plt.plot([beg[0], ende[0]], [beg[1], ende[1]], color=[0, 0, 1])
        plt.plot([beg[0], ende[0]], [beg[1], ende[1]], color=[0, 0, ii/ (len(COPx) - 1)])


    plt.xlabel('horizontal position [m]')
    plt.ylabel('vertical position [m]')
    plt.title(file_name + ', VPP ' + str(j)) # nmb_force_plate)
    #plt.axis([-0.41, 0.41, -1.1, 2.7])


    p1 = plt.plot(0, 0, '+k', markersize=12)  # green cross: COM
    p2 = plt.plot(VPP_opt[0], VPP_opt[1], 'Xr', markersize=10)  # red cross: VPP
    #p2 = plt.plot(VPP_opt[0], VPP_opt[1], 'Xk', markersize=10)  # black cross: VPP
    plt.grid(True)


def VPP_plot_show(plot,Force_x, Force_z, COM, COP,COPz,trunk_angle,align, VPP_calc,file_name,j):
    if plot > 0:
        factor = (VPP_calc[1]+1)*2#1.7 #length of force vectors
        # j = 1
        VPP_plot(Force_x, Force_z, COM, COP,COPz,trunk_angle, align, VPP_calc, factor, j,file_name)
        plt.draw()

def plot_joints(p,pres,):
    x = range(0,101)
    #-------------------------------------------create plot
    if (p > 0):
        fig, axs = plt.subplots(5, 2,figsize=(16, 12))

      #------------------------------------------

        axs[0, 0].plot(x,pres.HeadAngle_z,color='blue')
        axs[0, 1].plot(x,pres.ThoraxAngle_z,color='blue')
        axs[1, 0].plot(x,pres.ipsiShoulderAngle_x,color='blue')
        axs[1, 1].plot(x,pres.contraShoulderAngle_x,color='red')
        axs[1, 1].plot(x,pres.ipsiElbowAngle_x,color='blue')
        axs[1, 0].plot(x,pres.contraElbowAngle_x,color='red')
        axs[2, 0].plot(x,pres.ipsiHipAngle_x,color='blue')
        axs[2, 0].plot(x,pres.contraHipAngle_x,color='red')
        axs[2, 1].plot(x,pres.ipsiHipMoment_x,color='green')

        axs[2, 1].plot(x,pres.ipsiHipPower_z,color='black')
        axs[3, 0].plot(x,pres.ipsiKneeAngle_x,color='blue')
        axs[3, 0].plot(x,pres.contraKneeAngle_x,color='red')
        axs[3, 1].plot(x,pres.ipsiKneeMoment_x,color='green')
        axs[3, 1].plot(x,pres.ipsiKneePower_z,color='black')
        axs[4, 0].plot(x,pres.ipsiAnkleAngle_x,color='blue')
        axs[4, 0].plot(x,pres.contraAnkleAngle_x,color='red')
        axs[4, 1].plot(x,pres.ipsiAnkleMoment_x,color='green')
        axs[4, 1].plot(x,pres.ipsiAnklePower_z,color='black')




        axs[1, 0].legend(['ipsi','contra'])
        axs[2, 1].legend(['Moment','Power'])

        #-----------------------------------------formatting

        axs[0, 0].set(ylabel='Head Angle [deg]')
        axs[0, 1].set(ylabel='Thorax Angle [deg]')
        axs[1, 0].set(ylabel='Shoulder Angle [deg]')
        axs[1, 1].set(ylabel='Elbow Angle [deg]')
        axs[2, 0].set(ylabel='Hip Angle [deg]')
        axs[2, 1].set(ylabel='Hip\n g:Moment [Nm/kg],\n b:Power [W/kg]')
        axs[3, 0].set(ylabel='Knee Angle [deg]')
        axs[3, 1].set(ylabel='Knee\n g:Moment [Nm/kg],\n b:Power [W/kg]')
        axs[4, 0].set(xlabel='gait cycle (%)', ylabel='Ankle Angle [deg]')
        axs[4, 1].set(xlabel='gait cycle (%)',ylabel='Ankle\n g:Moment [Nm/kg],\n b:Power [W/kg]')

        plt.show()
