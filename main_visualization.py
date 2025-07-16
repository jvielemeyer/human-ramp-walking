import os
import numpy as np
import matplotlib.pyplot as plt
import warnings

from visualization import plot_means, mean_calc, plot_all

warnings.filterwarnings("ignore")
##############################################################
#-------------1. kinematics (joint angles, moments, power)------
##############################################################
#-------------------calculate mean of kinematics
##first part: mean values over trials and subjects
##second part: all single trials of all subjects
[Ankle_ipsi_A_mean,Ankle_contra_A_mean,Ankle_M_mean, Ankle_P_mean,
Knee_ipsi_A_mean,Knee_contra_A_mean, Knee_M_mean, Knee_P_mean,
Hip_ipsi_A_mean,Hip_contra_A_mean, Hip_M_mean, Hip_P_mean,
Head_mean, Thorax_mean,
Shoulder_ipsi_mean, Shoulder_contra_mean,
Elbow_ipsi_mean, Elbow_contra_mean,
Ankle_ipsi_A_std,Ankle_contra_A_std,Ankle_M_std, Ankle_P_std,
Knee_ipsi_A_std,Knee_contra_A_std,Knee_M_std, Knee_P_std,
Hip_ipsi_A_std,Hip_contra_A_std, Hip_M_std, Hip_P_std,
Head_std,Thorax_std,
Shoulder_ipsi_std, Shoulder_contra_std,
Elbow_ipsi_std, Elbow_contra_std,
Ankle_ipsi_Angle, Ankle_contra_Angle, Ankle_Moment, Ankle_Power,
Knee_ipsi_Angle, Knee_contra_Angle, Knee_Moment, Knee_Power,
Hip_ipsi_Angle, Hip_contra_Angle, Hip_Moment, Hip_Power,
Head_Angle, Thorax_Angle,
ShoulderI_Angle, ShoulderC_Angle,
ElbowI_Angle, ElbowC_Angle] = mean_calc.calc_kin()

###########################################################
## -----------------plot mean values--------------------
# ##---------------------------------plot kinematics of whole body
plot_means.plot_angles(Head_mean, Thorax_mean, Shoulder_ipsi_mean,Shoulder_contra_mean, Elbow_ipsi_mean, Elbow_contra_mean, Hip_ipsi_A_mean, Hip_contra_A_mean, Knee_ipsi_A_mean, Knee_contra_A_mean, Ankle_ipsi_A_mean, Ankle_contra_A_mean, Head_std, Thorax_std, Shoulder_ipsi_std,Shoulder_contra_std, Elbow_ipsi_std, Elbow_contra_std, Hip_ipsi_A_std, Hip_contra_A_std, Knee_ipsi_A_std, Knee_contra_A_std, Ankle_ipsi_A_std, Ankle_contra_A_std)

#plot_means.plot_moment_power(Ankle_M_mean, Ankle_P_mean, Knee_M_mean, Knee_P_mean,Hip_M_mean, Hip_P_mean, Ankle_M_std, Ankle_P_std, Knee_M_std, Knee_P_std,Hip_M_std, Hip_P_std)

##############################################################
#--------------plot single trials for technical validation

# plot_all.plot_kin_single_upper(Head_Angle, Thorax_Angle,
# ShoulderI_Angle, ShoulderC_Angle,
# ElbowI_Angle, ElbowC_Angle)

# plot_all.plot_kin_single_lower(Ankle_ipsi_Angle, Ankle_Moment, Ankle_Power,
# Knee_ipsi_Angle, Knee_Moment, Knee_Power, Hip_ipsi_Angle, Hip_Moment, Hip_Power)



################################################################################
#--------------2. kinetics (ground reaction forces)------------------------------
################################################################################
#---------------------calculate mean of kinetics
[GRFx1_mean,GRFx2_mean, GRFz1_mean, GRFz2_mean,GRFx1_std,GRFx2_std, GRFz1_std, GRFz2_std] = mean_calc.calc_dyn()

#---------------plot kinetics
#plot_means.plot_GRFs(GRFx1_mean,GRFx2_mean, GRFz1_mean, GRFz2_mean,GRFx1_std,GRFx2_std, GRFz1_std, GRFz2_std)


##########################################################################
#-------------------------------3. VPP--------------------------------------
#########################################################################
##------------------calculate mean of VPP
[VPP1_mean,VPP2_mean, R1_mean, R2_mean, VPP1_std,VPP2_std, R1_std, R2_std,VPP1_trials, R1_trials,VPP2_trials, R2_trials, VPP1_all, VPP2_all] = mean_calc.calc_VPPmean()
##"trials": mean over all runs of each trial for each subject
##"mean": mean over all subjects for above "trials"

##------------------------------plot VPP scatter plot

#plot_all.scatterplot_VPP(VPP2_mean, VPP2_all)

#########################################################################
#----------------------------4. walking speed-----------------------------
##########################################################################
#-------calculate mean value of speed
# [speed_mean,speed_std] = mean_calc.calc_speed_mean()
# print(speed_mean)
# print(speed_std)
