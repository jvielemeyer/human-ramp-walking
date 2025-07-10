import numpy as np
import os
import matplotlib.pyplot as plt


#--------------------------------------------------------------------
def calc_kin():
    ListeAnkleAI = []
    ListeAnkleAC = []
    ListeAnkleM = []
    ListeAnkleP = []
    ListeKneeAI = []
    ListeKneeAC = []
    ListeKneeM = []
    ListeKneeP = []
    ListeHipAI = []
    ListeHipAC = []
    ListeHipM = []
    ListeHipP = []
    ListeHead = []
    ListeShoulderI = []
    ListeShoulderC = []
    ListeElbowI = []
    ListeElbowC = []
    ListeThorax = []
    folder_prev = []
    prob = 0

    rootdir = os.path.normpath('./Data_Level_2')

    for subdir, dirs, files in os.walk(rootdir):
        folder = subdir
        for file in files:
            folder = str(subdir.split('/')[-1])
            filename = os.fsdecode(file)
            if filename.endswith(".npz"):
                loaded_data = np.load(os.path.join(subdir, filename))
                if ListeAnkleAI == [] or folder != folder_prev:
                    prob = loaded_data['prob']
                    ListeAnkleAI.append(str(prob)+ '_' + folder)
                    ListeAnkleAC.append(str(prob)+ '_' + folder)
                    ListeAnkleM.append(str(prob)+ '_' + folder)
                    ListeAnkleP.append(str(prob)+ '_' + folder)
                    #-----------------
                    ListeKneeAI.append(str(prob)+ '_' + folder)
                    ListeKneeAC.append(str(prob)+ '_' + folder)
                    ListeKneeM.append(str(prob)+ '_' + folder)
                    ListeKneeP.append(str(prob)+ '_' + folder)
                    #-----------------
                    ListeHipAI.append(str(prob)+ '_' + folder)
                    ListeHipAC.append(str(prob)+ '_' + folder)
                    ListeHipM.append(str(prob)+ '_' + folder)
                    ListeHipP.append(str(prob)+ '_' + folder)
                    #-----------------
                    ListeHead.append(str(prob)+ '_' + folder)
                    #ListeNeck.append(str(prob)+ '_' + folder)
                    ListeThorax.append(str(prob)+ '_' + folder)
                    #-----------------
                    ListeShoulderI.append(str(prob)+ '_' + folder)
                    ListeShoulderC.append(str(prob)+ '_' + folder)
                    ListeElbowI.append(str(prob)+ '_' + folder)
                    ListeElbowC.append(str(prob)+ '_' + folder)
                # else:
                ListeAnkleAI.append(loaded_data['ankleAx']) #ipsi
                ListeAnkleAC.append(loaded_data['ankleAx_contra']) #contra
                ListeAnkleM.append(loaded_data['ankleMx'])
                ListeAnkleP.append(loaded_data['anklePz'])
                ListeKneeAI.append(loaded_data['kneeAx'])
                ListeKneeAC.append(loaded_data['kneeAx_contra'])
                ListeKneeM.append(loaded_data['kneeMx'])
                ListeKneeP.append(loaded_data['kneePz'])
                ListeHipAI.append(loaded_data['hipAx'])
                ListeHipAC.append(loaded_data['hipAx_contra'])
                ListeHipM.append(loaded_data['hipMx'])
                ListeHipP.append(loaded_data['hipPz'])
                #-----------
                ListeHead.append(loaded_data['headAx'])
                ListeThorax.append(loaded_data['thoraxAx'])
                ListeShoulderI.append(loaded_data['shoulderAx'])
                ListeShoulderC.append(loaded_data['shoulderAx_contra'])
                ListeElbowI.append(loaded_data['elbowAx'])
                ListeElbowC.append(loaded_data['elbowAx_contra'])
                folder_prev = folder
            else:
                continue

    #-------------------------mean of trials
    # create new list with tupels [experimental condition, mean of all trials of this subject in this condition]

    index_start=0
    AnkleI_Angle = []
    AnkleC_Angle = []
    Ankle_Moment = []
    Ankle_Power = []
    KneeI_Angle = []
    KneeC_Angle = []
    Knee_Moment = []
    Knee_Power = []
    HipI_Angle = []
    HipC_Angle = []
    Hip_Moment = []
    Hip_Power = []
    Head_Angle = []
    Neck_Angle = []
    Thorax_Angle = []
    ShoulderI_Angle = []
    ShoulderC_Angle = []
    ElbowI_Angle = []
    ElbowC_Angle = []

    for index in range(0,len(ListeAnkleAI)):
        if isinstance(ListeAnkleAI[index], str): #yes string
            if index > 0:
                AnkleI_Angle.append([str(ListeAnkleAI[index_start]),np.nanmean(ListeAnkleAI[index_start+1:index-1],axis=0)])
                AnkleC_Angle.append([str(ListeAnkleAC[index_start]),np.nanmean(ListeAnkleAC[index_start+1:index-1],axis=0)])
                Ankle_Moment.append([str(ListeAnkleM[index_start]),np.nanmean(ListeAnkleM[index_start+1:index-1],axis=0)])
                Ankle_Power.append([str(ListeAnkleP[index_start]),np.nanmean(ListeAnkleP[index_start+1:index-1],axis=0)])
                KneeI_Angle.append([str(ListeKneeAI[index_start]),np.nanmean(ListeKneeAI[index_start+1:index-1],axis=0)])
                KneeC_Angle.append([str(ListeKneeAC[index_start]),np.nanmean(ListeKneeAC[index_start+1:index-1],axis=0)])
                Knee_Moment.append([str(ListeKneeM[index_start]),np.nanmean(ListeKneeM[index_start+1:index-1],axis=0)])
                Knee_Power.append([str(ListeKneeP[index_start]),np.nanmean(ListeKneeP[index_start+1:index-1],axis=0)])
                HipI_Angle.append([str(ListeHipAI[index_start]),np.nanmean(ListeHipAI[index_start+1:index-1],axis=0)])
                HipC_Angle.append([str(ListeHipAC[index_start]),np.nanmean(ListeHipAC[index_start+1:index-1],axis=0)])
                Hip_Moment.append([str(ListeHipM[index_start]),np.nanmean(ListeHipM[index_start+1:index-1],axis=0)])
                Hip_Power.append([str(ListeHipP[index_start]),np.nanmean(ListeHipP[index_start+1:index-1],axis=0)])
                Head_Angle.append([str(ListeHead[index_start]),np.nanmean(ListeHead[index_start+1:index-1],axis=0)])
                Thorax_Angle.append([str(ListeThorax[index_start]),np.nanmean(ListeThorax[index_start+1:index-1],axis=0)])
                ShoulderI_Angle.append([str(ListeShoulderI[index_start]),np.nanmean(ListeShoulderI[index_start+1:index-1],axis=0)])
                ShoulderC_Angle.append([str(ListeShoulderC[index_start]),np.nanmean(ListeShoulderC[index_start+1:index-1],axis=0)])
                ElbowI_Angle.append([str(ListeElbowI[index_start]),np.nanmean(ListeElbowI[index_start+1:index-1],axis=0)])
                ElbowC_Angle.append([str(ListeElbowC[index_start]),np.nanmean(ListeElbowC[index_start+1:index-1],axis=0)])
                index_start = index
        elif index == len(ListeAnkleAI)-1: #last element
            AnkleI_Angle.append([str(ListeAnkleAI[index_start]),np.nanmean(ListeAnkleAI[index_start+1:index],axis=0)])
            AnkleC_Angle.append([str(ListeAnkleAC[index_start]),np.nanmean(ListeAnkleAC[index_start+1:index],axis=0)])
            Ankle_Moment.append([str(ListeAnkleM[index_start]),np.nanmean(ListeAnkleM[index_start+1:index],axis=0)])
            Ankle_Power.append([str(ListeAnkleP[index_start]),np.nanmean(ListeAnkleP[index_start+1:index],axis=0)])
            KneeI_Angle.append([str(ListeKneeAI[index_start]),np.nanmean(ListeKneeAI[index_start+1:index],axis=0)])
            KneeC_Angle.append([str(ListeKneeAC[index_start]),np.nanmean(ListeKneeAC[index_start+1:index],axis=0)])
            Knee_Moment.append([str(ListeKneeM[index_start]),np.nanmean(ListeKneeM[index_start+1:index],axis=0)])
            Knee_Power.append([str(ListeKneeP[index_start]),np.nanmean(ListeKneeP[index_start+1:index],axis=0)])
            HipI_Angle.append([str(ListeHipAI[index_start]),np.nanmean(ListeHipAI[index_start+1:index],axis=0)])
            HipC_Angle.append([str(ListeHipAC[index_start]),np.nanmean(ListeHipAC[index_start+1:index],axis=0)])
            Hip_Moment.append([str(ListeHipM[index_start]),np.nanmean(ListeHipM[index_start+1:index],axis=0)])
            Hip_Power.append([str(ListeHipP[index_start]),np.nanmean(ListeHipP[index_start+1:index],axis=0)])
            Head_Angle.append([str(ListeHead[index_start]),np.nanmean(ListeHead[index_start+1:index],axis=0)])
            Thorax_Angle.append([str(ListeThorax[index_start]),np.nanmean(ListeThorax[index_start+1:index],axis=0)])
            ShoulderI_Angle.append([str(ListeShoulderI[index_start]),np.nanmean(ListeShoulderI[index_start+1:index],axis=0)])
            ShoulderC_Angle.append([str(ListeShoulderC[index_start]),np.nanmean(ListeShoulderC[index_start+1:index],axis=0)])
            ElbowI_Angle.append([str(ListeElbowI[index_start]),np.nanmean(ListeElbowI[index_start+1:index],axis=0)])
            ElbowC_Angle.append([str(ListeElbowC[index_start]),np.nanmean(ListeElbowC[index_start+1:index],axis=0)])
    #-------------------------find trials of the same setup of all different probands
    list_trials = []
    #---------------
    AnkleI_A_mean = []
    AnkleC_A_mean = []
    Ankle_M_mean = []
    Ankle_P_mean = []
    KneeI_A_mean = []
    KneeC_A_mean = []
    Knee_M_mean = []
    Knee_P_mean = []
    HipI_A_mean = []
    HipC_A_mean = []
    Hip_M_mean = []
    Hip_P_mean = []
    Head_mean = []
    Thorax_mean= []
    ShoulderI_mean = []
    ShoulderC_mean = []
    ElbowI_mean = []
    ElbowC_mean = []
    #--------
    AnkleI_A_std = []
    AnkleC_A_std = []
    Ankle_M_std = []
    Ankle_P_std = []
    KneeI_A_std = []
    KneeC_A_std = []
    Knee_M_std = []
    Knee_P_std = []
    HipI_A_std = []
    HipC_A_std = []
    Hip_M_std = []
    Hip_P_std = []
    Head_std = []
    Thorax_std= []
    ShoulderI_std = []
    ShoulderC_std = []
    ElbowI_std = []
    ElbowC_std = []
    #-------------
    count = 0

    #-----create list with setups/conditions
    for n in range(0,len(AnkleI_Angle)):
        name = AnkleI_Angle[n][0]
        trial = name[6:len(name)]
        if count == 0:
            trial_0 = trial
        elif trial == trial_0:
            count = 0 #initialize again
        list_trials.append(count)
        count +=1
    #------count how many probands:
    count_prob = [i for i,x in enumerate(list_trials) if x==0]

    #------------------------------------build mean over the probands in each setup/condition (e.g. eben up)
    for k in range(0,int(len(AnkleI_Angle)/len(count_prob))):
        Idx = [i for i,x in enumerate(list_trials) if x==k]
        name = AnkleI_Angle[k][0] #the same for all joints? if not, create this variable for all joints
        #------------------mean
        AnkleI_A_mean.append([name[6:len(name)],np.nanmean([AnkleI_Angle[i][1] for i in Idx],axis=0)])
        AnkleC_A_mean.append([name[6:len(name)],np.nanmean([AnkleC_Angle[i][1] for i in Idx],axis=0)])
        Ankle_M_mean.append([name[6:len(name)],np.nanmean([Ankle_Moment[i][1] for i in Idx],axis=0)])
        Ankle_P_mean.append([name[6:len(name)],np.nanmean([Ankle_Power[i][1] for i in Idx],axis=0)])
        KneeI_A_mean.append([name[6:len(name)],np.nanmean([KneeI_Angle[i][1] for i in Idx],axis=0)])
        KneeC_A_mean.append([name[6:len(name)],np.nanmean([KneeC_Angle[i][1] for i in Idx],axis=0)])
        Knee_M_mean.append([name[6:len(name)],np.nanmean([Knee_Moment[i][1] for i in Idx],axis=0)])
        Knee_P_mean.append([name[6:len(name)],np.nanmean([Knee_Power[i][1] for i in Idx],axis=0)])
        HipI_A_mean.append([name[6:len(name)],np.nanmean([HipI_Angle[i][1] for i in Idx],axis=0)])
        HipC_A_mean.append([name[6:len(name)],np.nanmean([HipC_Angle[i][1] for i in Idx],axis=0)])
        Hip_M_mean.append([name[6:len(name)],np.nanmean([Hip_Moment[i][1] for i in Idx],axis=0)])
        Hip_P_mean.append([name[6:len(name)],np.nanmean([Hip_Power[i][1] for i in Idx],axis=0)])
        Head_mean.append([name[6:len(name)],np.nanmean([Head_Angle[i][1] for i in Idx],axis=0)])
        Thorax_mean.append([name[6:len(name)],np.nanmean([Thorax_Angle[i][1] for i in Idx],axis=0)])
        ShoulderC_mean.append([name[6:len(name)],np.nanmean([ShoulderC_Angle[i][1] for i in Idx],axis=0)])
        ShoulderI_mean.append([name[6:len(name)],np.nanmean([ShoulderI_Angle[i][1] for i in Idx],axis=0)])
        ElbowC_mean.append([name[6:len(name)],np.nanmean([ElbowC_Angle[i][1] for i in Idx],axis=0)])
        ElbowI_mean.append([name[6:len(name)],np.nanmean([ElbowI_Angle[i][1] for i in Idx],axis=0)])
        ###------------------std
        AnkleI_A_std.append([name[6:len(name)],np.nanstd([AnkleI_Angle[i][1] for i in Idx],axis=0)])
        AnkleC_A_std.append([name[6:len(name)],np.nanstd([AnkleC_Angle[i][1] for i in Idx],axis=0)])
        Ankle_M_std.append([name[6:len(name)],np.nanstd([Ankle_Moment[i][1] for i in Idx],axis=0)])
        Ankle_P_std.append([name[6:len(name)],np.nanstd([Ankle_Power[i][1] for i in Idx],axis=0)])
        KneeI_A_std.append([name[6:len(name)],np.nanstd([KneeI_Angle[i][1] for i in Idx],axis=0)])
        KneeC_A_std.append([name[6:len(name)],np.nanstd([KneeC_Angle[i][1] for i in Idx],axis=0)])
        Knee_M_std.append([name[6:len(name)],np.nanstd([Knee_Moment[i][1] for i in Idx],axis=0)])
        Knee_P_std.append([name[6:len(name)],np.nanstd([Knee_Power[i][1] for i in Idx],axis=0)])
        HipI_A_std.append([name[6:len(name)],np.nanstd([HipI_Angle[i][1] for i in Idx],axis=0)])
        HipC_A_std.append([name[6:len(name)],np.nanstd([HipC_Angle[i][1] for i in Idx],axis=0)])
        Hip_M_std.append([name[6:len(name)],np.nanstd([Hip_Moment[i][1] for i in Idx],axis=0)])
        Hip_P_std.append([name[6:len(name)],np.nanstd([Hip_Power[i][1] for i in Idx],axis=0)])
        Head_std.append([name[6:len(name)],np.nanstd([Head_Angle[i][1] for i in Idx],axis=0)])
        Thorax_std.append([name[6:len(name)],np.nanstd([Thorax_Angle[i][1] for i in Idx],axis=0)])
        ShoulderC_std.append([name[6:len(name)],np.nanstd([ShoulderC_Angle[i][1] for i in Idx],axis=0)])
        ShoulderI_std.append([name[6:len(name)],np.nanstd([ShoulderI_Angle[i][1] for i in Idx],axis=0)])
        ElbowC_std.append([name[6:len(name)],np.nanstd([ElbowC_Angle[i][1] for i in Idx],axis=0)])
        ElbowI_std.append([name[6:len(name)],np.nanstd([ElbowI_Angle[i][1] for i in Idx],axis=0)])

    return AnkleI_A_mean, AnkleC_A_mean, Ankle_M_mean, Ankle_P_mean, KneeI_A_mean, KneeC_A_mean, Knee_M_mean, Knee_P_mean, HipI_A_mean, HipC_A_mean, Hip_M_mean, Hip_P_mean, Head_mean, Thorax_mean, ShoulderI_mean, ShoulderC_mean, ElbowI_mean, ElbowC_mean, AnkleI_A_std, AnkleC_A_std,Ankle_M_std, Ankle_P_std, KneeI_A_std, KneeC_A_std, Knee_M_std, Knee_P_std, HipI_A_std, HipC_A_std, Hip_M_std, Hip_P_std, Head_std, Thorax_std, ShoulderI_std, ShoulderC_std,ElbowI_std, ElbowC_std, ListeAnkleAI, ListeAnkleAC, ListeAnkleM, ListeAnkleP, ListeKneeAI, ListeKneeAC, ListeKneeM, ListeKneeP, ListeHipAI, ListeHipAC, ListeHipM, ListeHipP, ListeHead, ListeThorax, ListeShoulderI, ListeShoulderC, ListeElbowI, ListeElbowC
#----------------------------------------------------------------------------

def calc_dyn():
    ListeGRFx1 = []
    ListeGRFx2 = []
    ListeGRFz1 = []
    ListeGRFz2 = []
    folder_prev = []
    prob = 0

    rootdir = os.path.normpath('./Data_Level_2')


    for subdir, dirs, files in os.walk(rootdir):
        folder = subdir

        for file in files:
            folder = str(subdir.split('/')[-1])
            filename = os.fsdecode(file)
            if filename.endswith(".npz"):
                loaded_data = np.load(os.path.join(subdir, filename))
                if ListeGRFx1 == [] or folder != folder_prev:
                    prob = loaded_data['prob']
                    ListeGRFx1.append(str(prob)+ '_' + folder)
                    ListeGRFx2.append(str(prob)+ '_' + folder)
                    ListeGRFz1.append(str(prob)+ '_' + folder)
                    ListeGRFz2.append(str(prob)+ '_' + folder)
                ListeGRFx1.append(loaded_data['GRFx1'])
                ListeGRFx2.append(loaded_data['GRFx2'])
                ListeGRFz1.append(loaded_data['GRFz1'])
                ListeGRFz2.append(loaded_data['GRFz2'])
                folder_prev = folder
            else:
                continue
    #-------------------------mean of trials
    # create new list with tupels [experimental condition, mean of all trials of this subject in this condition]

    index_start=0
    GRFx1 = []
    GRFx2 = []
    GRFz1 = []
    GRFz2 = []

    for index in range(0,len(ListeGRFx1)):
        if isinstance(ListeGRFx1[index], str): #yes string
            if index > 0:
                GRFx1.append([str(ListeGRFx1[index_start]),np.nanmean(ListeGRFx1[index_start+1:index-1],axis=0)])
                GRFx2.append([str(ListeGRFx2[index_start]),np.nanmean(ListeGRFx2[index_start+1:index-1],axis=0)])
                GRFz1.append([str(ListeGRFz1[index_start]),np.nanmean(ListeGRFz1[index_start+1:index-1],axis=0)])
                GRFz2.append([str(ListeGRFz2[index_start]),np.nanmean(ListeGRFz2[index_start+1:index-1],axis=0)])
                index_start = index
        elif index == len(ListeGRFx1)-1: #last element
            GRFx1.append([str(ListeGRFx1[index_start]),np.nanmean(ListeGRFx1[index_start+1:index],axis=0)])
            GRFx2.append([str(ListeGRFx2[index_start]),np.nanmean(ListeGRFx2[index_start+1:index-1],axis=0)])
            GRFz1.append([str(ListeGRFz1[index_start]),np.nanmean(ListeGRFz1[index_start+1:index-1],axis=0)])
            GRFz2.append([str(ListeGRFz2[index_start]),np.nanmean(ListeGRFz2[index_start+1:index-1],axis=0)])

    #-------------------------find trials of the same setup of all different probands
    list_trials = []
    #---------------
    GRFx1_mean = []
    GRFx2_mean = []
    GRFz1_mean = []
    GRFz2_mean = []
    #--------
    GRFx1_std = []
    GRFx2_std = []
    GRFz1_std = []
    GRFz2_std = []
    #-------------
    count = 0

    #-----create list with setups/conditions
    for n in range(0,len(GRFx1)):
        name = GRFx1[n][0]
        trial = name[6:len(name)]
        if count == 0:
            trial_0 = trial
        elif trial == trial_0:
            count = 0 #initialize again
        list_trials.append(count)
        count +=1
    #------count how many probands:
    count_prob = [i for i,x in enumerate(list_trials) if x==0]

    #------------------------------------build mean over the probands in each setup/condition (e.g. eben up)

    for k in range(0,int(len(GRFx1)/len(count_prob))):
        Idx = [i for i,x in enumerate(list_trials) if x==k]
        name = GRFx1[k][0] #the same for all joints? if not, create this variable for all joints
        #------------------mean
        GRFx1_mean.append([name[6:len(name)],np.nanmean([GRFx1[i][1] for i in Idx],axis=0)])
        GRFx2_mean.append([name[6:len(name)],np.nanmean([GRFx2[i][1] for i in Idx],axis=0)])
        GRFz1_mean.append([name[6:len(name)],np.nanmean([GRFz1[i][1] for i in Idx],axis=0)])
        GRFz2_mean.append([name[6:len(name)],np.nanmean([GRFz2[i][1] for i in Idx],axis=0)])
        ###------------------std
        GRFx1_std.append([name[6:len(name)],np.nanstd([GRFx1[i][1] for i in Idx],axis=0)])
        GRFx2_std.append([name[6:len(name)],np.nanstd([GRFx2[i][1] for i in Idx],axis=0)])
        GRFz1_std.append([name[6:len(name)],np.nanstd([GRFz1[i][1] for i in Idx],axis=0)])
        GRFz2_std.append([name[6:len(name)],np.nanstd([GRFz2[i][1] for i in Idx],axis=0)])

    return GRFx1_mean,GRFx2_mean, GRFz1_mean, GRFz2_mean,GRFx1_std,GRFx2_std, GRFz1_std, GRFz2_std

#---------------------------------------------------------------
def calc_VPPmean():
    ListeVPP1 = []
    ListeVPP2 = []
    ListeR1 = []
    ListeR2 = []
    folder_prev = []
    prob = 0

    rootdir = os.path.normpath('./Data_Level_2')

    for subdir, dirs, files in os.walk(rootdir):
        folder = subdir

        for file in files:
            folder = str(subdir.split('/')[-1])
            filename = os.fsdecode(file)
            if filename.endswith(".npz"):
                loaded_data = np.load(os.path.join(subdir, filename))
                if ListeVPP1 == [] or folder != folder_prev:
                    prob = loaded_data['prob']
                    ListeVPP1.append(str(prob)+ '_' + folder)
                    ListeVPP2.append(str(prob)+ '_' + folder)
                    ListeR1.append(str(prob)+ '_' + folder)
                    ListeR2.append(str(prob)+ '_' + folder)
                ListeVPP1.append(loaded_data['VPP1'])
                ListeVPP2.append(loaded_data['VPP2'])
                ListeR1.append(loaded_data['R2_1'])
                ListeR2.append(loaded_data['R2_2'])
                folder_prev = folder
            else:
                continue

    #-------------------------mean of trials
    # create new list with tupels [experimental condition, mean of all trials of this subject in this condition]

    index_start=0
    VPP1 = []
    VPP2 = []
    R1 = []
    R2 = []

    for index in range(0,len(ListeVPP1)):
        if isinstance(ListeVPP1[index], str): #yes string
            if index > 0:
                VPP1.append([str(ListeVPP1[index_start]),np.nanmean(ListeVPP1[index_start+1:index-1],axis=0)])
                VPP2.append([str(ListeVPP2[index_start]),np.nanmean(ListeVPP2[index_start+1:index-1],axis=0)])
                R1.append([str(ListeR1[index_start]),np.nanmean(ListeR1[index_start+1:index-1],axis=0)])
                R2.append([str(ListeR2[index_start]),np.nanmean(ListeR2[index_start+1:index-1],axis=0)])
                index_start = index
        elif index == len(ListeVPP1)-1: #last element
            VPP1.append([str(ListeVPP1[index_start]),np.nanmean(ListeVPP1[index_start+1:index],axis=0)])
            VPP2.append([str(ListeVPP2[index_start]),np.nanmean(ListeVPP2[index_start+1:index-1],axis=0)])
            R1.append([str(ListeR1[index_start]),np.nanmean(ListeR1[index_start+1:index-1],axis=0)])
            R2.append([str(ListeR2[index_start]),np.nanmean(ListeR2[index_start+1:index-1],axis=0)])

    #-------------------------find trials of the same setup of all different probands
    list_trials = []
    #---------------
    VPP1_mean = []
    VPP2_mean = []
    R1_mean = []
    R2_mean = []
    #--------
    VPP1_std = []
    VPP2_std = []
    R1_std = []
    R2_std = []
    #-------------
    count = 0

    #-----create list with setups/conditions
    for n in range(0,len(VPP1)):
        name = VPP1[n][0]
        trial = name[6:len(name)]
        if count == 0:
            trial_0 = trial
        elif trial == trial_0:
            count = 0 #initialize again
        list_trials.append(count)
        count +=1
    #------count how many probands:
    count_prob = [i for i,x in enumerate(list_trials) if x==0]

    #------------------------------------build mean over the probands in each setup/condition (e.g. level up)

    for k in range(0,int(len(VPP1)/len(count_prob))):
        Idx = [i for i,x in enumerate(list_trials) if x==k]
        name = VPP1[k][0] #the same for all joints? if not, create this variable for all joints
        #------------------mean

        VPP1_mean.append([name[6:len(name)],np.nanmean([VPP1[i][1] for i in Idx],axis=0)])
        VPP2_mean.append([name[6:len(name)],np.nanmean([VPP2[i][1] for i in Idx],axis=0)])
        R1_mean.append([name[6:len(name)],np.nanmean([R1[i][1] for i in Idx],axis=0)])
        R2_mean.append([name[6:len(name)],np.nanmean([R2[i][1] for i in Idx],axis=0)])
        ###------------------std
        VPP1_std.append([name[6:len(name)],np.nanstd([VPP1[i][1] for i in Idx],axis=0)])
        VPP2_std.append([name[6:len(name)],np.nanstd([VPP2[i][1] for i in Idx],axis=0)])
        R1_std.append([name[6:len(name)],np.nanstd([R1[i][1] for i in Idx],axis=0)])
        R2_std.append([name[6:len(name)],np.nanstd([R2[i][1] for i in Idx],axis=0)])

    return VPP1_mean,VPP2_mean, R1_mean, R2_mean, VPP1_std,VPP2_std, R1_std, R2_std, VPP1, R1, VPP2, R2, ListeVPP1, ListeVPP2

def calc_speed_mean():
    Listespeed = []
    folder_prev = []
    prob = 0

    rootdir = os.path.normpath('./Data_Level_2')


    for subdir, dirs, files in os.walk(rootdir):
        folder = subdir

        for file in files:
            folder = str(subdir.split('/')[-1])
            filename = os.fsdecode(file)
            if filename.endswith(".npz"):
                loaded_data = np.load(os.path.join(subdir, filename))
                if Listespeed == [] or folder != folder_prev:
                    prob = loaded_data['prob']
                    Listespeed.append(str(prob)+ '_' + folder)
                Listespeed.append(loaded_data['gait_speed'])
                folder_prev = folder
            else:
                continue
    #-------------------------mean of trials
    # create new list with tupels [experimental condition, mean of all trials of this subject in this condition]

    index_start=0
    speed = []


    for index in range(0,len(Listespeed)):
        if isinstance(Listespeed[index], str): #yes string
            if index > 0:
                speed.append([str(Listespeed[index_start]),np.nanmean(Listespeed[index_start+1:index-1],axis=0)])
                index_start = index
        elif index == len(Listespeed)-1: #last element
            speed.append([str(Listespeed[index_start]),np.nanmean(Listespeed[index_start+1:index],axis=0)])

    #-------------------------find trials of the same setup of all different probands
    list_trials = []
    #---------------
    speed_mean = []

    #--------
    speed_std = []

    #-------------
    count = 0

    #-----create list with setups/conditions
    for n in range(0,len(speed)):
        name = speed[n][0]
        trial = name[6:len(name)]
        if count == 0:
            trial_0 = trial
        elif trial == trial_0:
            count = 0 #initialize again
        list_trials.append(count)
        count +=1
    #------count how many probands:
    count_prob = [i for i,x in enumerate(list_trials) if x==0]

    #------------------------------------build mean over the probands in each setup/condition (e.g. eben up)

    for k in range(0,int(len(speed)/len(count_prob))):
        Idx = [i for i,x in enumerate(list_trials) if x==k]
        name = speed[k][0] #the same for all joints? if not, create this variable for all joints
        #------------------mean
        speed_mean.append([name[6:len(name)],np.nanmean([abs(speed[i][1]) for i in Idx],axis=0)])

        ###------------------std
        speed_std.append([name[6:len(name)],np.nanstd([abs(speed[i][1]) for i in Idx],axis=0)])


    return speed_mean,speed_std





