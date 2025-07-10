import numpy as np
import matplotlib.pyplot as plt
import os #to get file name instead of whole file path
from tkinter import filedialog

import calcInput #readIni, button_get_entries, calc_forces_cop_com, load_data
import calcButtons #show_calc, show_calc1, button_res_save, button_res_both, button_res_single, nextVPP, prevVPP, save_figures, plot_input, plot_kin, plot_vpp

#--------------------------------

#if only one file: kinematic and kinetic, if two files: kinetic (dyn):
def readData (preadin): #dyn
    path = './Data_Level_1'
    #path = filedialog.askopenfilenames()
    pathlist = [os.path.join(root, name)
        for root, dirs, files in os.walk(path)
        for name in files
        if name.endswith((".txt"))]
    preadin.files = sorted(pathlist) #sorted alphabetically


def getData (pres,pstart,pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b,ListeFiles,ListeVPP): #initialization
    #----------------read in all entries:
    calcInput.button_get_entries(pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b)
    #------------------------calculate kin data
    if pstart.number_files.get() == 2: #additionally data kin
        import_file_path_kin = preadin.file_kin
    import_file_path = preadin.files

    for k in range(0,len(import_file_path)): #read in for each file
        directory = os.path.split(import_file_path[k])[0]
        foldername = directory.split('/')[-1]
        if pstart.number_files.get() == 1:
            calcInput.load_data(preadin, pres, pkinetic, import_file_path,k)
        else:
            calcInput.load_data_dyn(preadin, pres, pkinetic, import_file_path,k)
            calcInput.load_data_kin(preadin, pres, pkinetic, import_file_path_kin,k)
            self.ListeFiles_kin.append(import_file_path_kin[k])
        calcButtons.button_res_save(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(import_file_path[k])[0:-4],foldername,k,0,ListeVPP)
        pres.ListeFiles.append(import_file_path[k])
    #--------------initialisation gui page
    if pstart.number_files.get() == 1:
        calcInput.load_data(preadin, pres, pkinetic, import_file_path,0)
    else:
        calcInput.load_data_dyn(preadin, pres, pkinetic, import_file_path,0)
        calcInput.load_data_kin(preadin, pres, pkinetic, import_file_path_kin,0)

    calcButtons.button_res_single(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(import_file_path[0])[0:-4])

def readin_kinematics(preadin,DataKin, DataKin_2): #model output, trajectories (DataKin_2)
    #---------------------lower body
    preadin.LAnkleAngle = DataKin[:,[20,21,22]]
    preadin.LAnkleForce = DataKin[:,[23,24,25]]
    preadin.LAnkleMoment = DataKin[:,[26,27,28]]
    preadin.LAnklePower = DataKin[:,[29,30,31]]

    preadin.RAnkleAngle = DataKin[:,[221,222,223]]
    preadin.RAnkleForce = DataKin[:,[224,225,226]]
    preadin.RAnkleMoment = DataKin[:,[227,228,229]]
    preadin.RAnklePower = DataKin[:,[230,231,232]]

    preadin.LHipAngle = DataKin[:,[101,102,103]]
    preadin.LHipForce = DataKin[:,[104,105,106]]
    preadin.LHipMoment = DataKin[:,[107,108,109]]
    preadin.LHipPower = DataKin[:,[110,111,112]]

    preadin.RHipAngle = DataKin[:,[302,303,304]]
    preadin.RHipForce = DataKin[:,[305,306,307]]
    preadin.RHipMoment = DataKin[:,[308,309,310]]
    preadin.RHipPower = DataKin[:,[311,312,313]]

    preadin.LKneeAngle = DataKin[:,[113,114,115]]
    preadin.LKneeForce = DataKin[:,[116,117,118]]
    preadin.LKneeMoment = DataKin[:,[119,120,121]]
    preadin.LKneePower = DataKin[:,[122,123,124]]

    preadin.RKneeAngle = DataKin[:,[314,315,316]]
    preadin.RKneeForce = DataKin[:,[317,318,319]]
    preadin.RKneeMoment = DataKin[:,[320,321,322]]
    preadin.RKneePower = DataKin[:,[323,324,325]]

    #---------------------------------upper body
    preadin.HeadAngle = DataKin[:,[98,99,100]]
    preadin.NeckAngle = DataKin[:,[125,126,127]]

    preadin.LShoulderAngle = DataKin[:,[152,153,154]]
    preadin.RShoulderAngle = DataKin[:,[353,354,355]]

    preadin.LElbowAngle = DataKin[:,[41,42,43]]
    preadin.RElbowAngle = DataKin[:,[242,243,244]]

    preadin.ThoraxAngle = DataKin[:,[185,186,187]]


    #hip
    preadin.LHip = np.multiply(DataKin_2[:,[71,72,73]],1/1000) #LASI, in m, 0 = y, 1 = x(walking direction), 2 = z(vertical)
    preadin.RHip = np.multiply(DataKin_2[:,[74,75,76]],1/1000) #RASI, in m
    preadin.MHip = (preadin.LHip+preadin.RHip)/2 #midpoint between left and right hip
    #take left one (same value for right and left)


def calc_joints(tdto,preadin,pres,foot):
    gaitcycle = range(tdto[0],tdto[4])
    new_length = 101
    pres.HeadAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.HeadAngle[gaitcycle,0]))
    pres.HeadAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.HeadAngle[gaitcycle,1]))
    pres.HeadAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.HeadAngle[gaitcycle,2]))
    pres.ThoraxAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.ThoraxAngle[gaitcycle,0]))
    pres.ThoraxAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.ThoraxAngle[gaitcycle,1]))
    pres.ThoraxAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.ThoraxAngle[gaitcycle,2]))
    if int(foot) == 0: #left foot in contact
        #--------------------Angle, horizontal (x) in walking direction (sagittal), y and z (vertical):
        #ipsi
        pres.ipsiAnkleAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,0]))
        pres.ipsiKneeAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,0]))
        pres.ipsiHipAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,0]))
        pres.ipsiShoulderAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,0]))
        pres.ipsiElbowAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,0]))
        pres.ipsiAnkleAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,1]))
        pres.ipsiKneeAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,1]))
        pres.ipsiHipAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,1]))
        pres.ipsiShoulderAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,1]))
        pres.ipsiElbowAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,1]))
        pres.ipsiAnkleAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,2]))
        pres.ipsiKneeAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,2]))
        pres.ipsiHipAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,2]))
        pres.ipsiShoulderAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,2]))
        pres.ipsiElbowAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,2]))
        #contra
        pres.contraAnkleAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,0]))
        pres.contraKneeAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,0]))
        pres.contraHipAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,0]))
        pres.contraShoulderAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,0]))
        pres.contraElbowAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,0]))
        pres.contraAnkleAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,1]))
        pres.contraKneeAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,1]))
        pres.contraHipAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,1]))
        pres.contraShoulderAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,1]))
        pres.contraElbowAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,1]))
        pres.contraAnkleAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,2]))
        pres.contraKneeAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,2]))
        pres.contraHipAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,2]))
        pres.contraShoulderAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,2]))
        pres.contraElbowAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,2]))
        #-----------------------Force, x,y,z, ipsi
        pres.ipsiAnkleForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleForce[gaitcycle,0]))
        pres.ipsiKneeForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeForce[gaitcycle,0]))
        pres.ipsiHipForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipForce[gaitcycle,0]))
        pres.ipsiAnkleForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleForce[gaitcycle,1]))
        pres.ipsiKneeForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeForce[gaitcycle,1]))
        pres.ipsiHipForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipForce[gaitcycle,1]))
        pres.ipsiAnkleForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleForce[gaitcycle,2]))
        pres.ipsiKneeForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeForce[gaitcycle,2]))
        pres.ipsiHipForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipForce[gaitcycle,2]))
        #--------------------Moment, x,y,z
        #ipsi
        pres.ipsiAnkleMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleMoment[gaitcycle,0])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeMoment[gaitcycle,0])),1/1000)
        pres.ipsiHipMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipMoment[gaitcycle,0])),1/1000)
        pres.ipsiAnkleMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleMoment[gaitcycle,1])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeMoment[gaitcycle,1])),1/1000)
        pres.ipsiHipMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipMoment[gaitcycle,1])),1/1000)
        pres.ipsiAnkleMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleMoment[gaitcycle,2])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeMoment[gaitcycle,2])),1/1000)
        pres.ipsiHipMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipMoment[gaitcycle,2])),1/1000)
        #----------------------------power vertical (z), also x and y
        #ipsi
        pres.ipsiAnklePower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnklePower[gaitcycle,0]))
        pres.ipsiKneePower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneePower[gaitcycle,0]))
        pres.ipsiHipPower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipPower[gaitcycle,0]))
        pres.ipsiAnklePower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnklePower[gaitcycle,1]))
        pres.ipsiKneePower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneePower[gaitcycle,1]))
        pres.ipsiHipPower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipPower[gaitcycle,1]))
        pres.ipsiAnklePower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnklePower[gaitcycle,2]))
        pres.ipsiKneePower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneePower[gaitcycle,2]))
        pres.ipsiHipPower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipPower[gaitcycle,2]))

    else:
        #Angle, horizontal (x) in walking direction (sagittal) and y,z
        #ipsi
        pres.ipsiAnkleAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,0]))
        pres.ipsiKneeAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,0]))
        pres.ipsiHipAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,0]))
        pres.ipsiShoulderAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,0]))
        pres.ipsiElbowAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,0]))
        pres.ipsiAnkleAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,1]))
        pres.ipsiKneeAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,1]))
        pres.ipsiHipAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,1]))
        pres.ipsiShoulderAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,1]))
        pres.ipsiElbowAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,1]))
        pres.ipsiAnkleAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleAngle[gaitcycle,2]))
        pres.ipsiKneeAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeAngle[gaitcycle,2]))
        pres.ipsiHipAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipAngle[gaitcycle,2]))
        pres.ipsiShoulderAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RShoulderAngle[gaitcycle,2]))
        pres.ipsiElbowAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RElbowAngle[gaitcycle,2]))
        #contra
        pres.contraAnkleAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,0]))
        pres.contraKneeAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,0]))
        pres.contraHipAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,0]))
        pres.contraShoulderAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,0]))
        pres.contraElbowAngle_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,0]))
        pres.contraAnkleAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,1]))
        pres.contraKneeAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,1]))
        pres.contraHipAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,1]))
        pres.contraShoulderAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,1]))
        pres.contraElbowAngle_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,1]))
        pres.contraAnkleAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LAnkleAngle[gaitcycle,2]))
        pres.contraKneeAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LKneeAngle[gaitcycle,2]))
        pres.contraHipAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LHipAngle[gaitcycle,2]))
        pres.contraShoulderAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LShoulderAngle[gaitcycle,2]))
        pres.contraElbowAngle_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.LElbowAngle[gaitcycle,2]))
        #-----------------------Force, x,y,z, ipsi
        pres.ipsiAnkleForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleForce[gaitcycle,0]))
        pres.ipsiKneeForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeForce[gaitcycle,0]))
        pres.ipsiHipForce_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipForce[gaitcycle,0]))
        pres.ipsiAnkleForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleForce[gaitcycle,1]))
        pres.ipsiKneeForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeForce[gaitcycle,1]))
        pres.ipsiHipForce_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipForce[gaitcycle,1]))
        pres.ipsiAnkleForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleForce[gaitcycle,2]))
        pres.ipsiKneeForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeForce[gaitcycle,2]))
        pres.ipsiHipForce_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipForce[gaitcycle,2]))
        #--------------------Moment, x,y,z
        #ipsi
        pres.ipsiAnkleMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleMoment[gaitcycle,0])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeMoment[gaitcycle,0])),1/1000)
        pres.ipsiHipMoment_x = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipMoment[gaitcycle,0])),1/1000)
        pres.ipsiAnkleMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleMoment[gaitcycle,1])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeMoment[gaitcycle,1])),1/1000)
        pres.ipsiHipMoment_y = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipMoment[gaitcycle,1])),1/1000)
        pres.ipsiAnkleMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnkleMoment[gaitcycle,2])),1/1000) #change from mm to m
        pres.ipsiKneeMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneeMoment[gaitcycle,2])),1/1000)
        pres.ipsiHipMoment_z = np.multiply(np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipMoment[gaitcycle,2])),1/1000)
        #-------------------------------------------------power vertical (z):
        #ipsi
        pres.ipsiAnklePower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnklePower[gaitcycle,0]))
        pres.ipsiKneePower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneePower[gaitcycle,0]))
        pres.ipsiHipPower_x = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipPower[gaitcycle,0]))
        pres.ipsiAnklePower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnklePower[gaitcycle,1]))
        pres.ipsiKneePower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneePower[gaitcycle,1]))
        pres.ipsiHipPower_y = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipPower[gaitcycle,1]))
        pres.ipsiAnklePower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RAnklePower[gaitcycle,2]))
        pres.ipsiKneePower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RKneePower[gaitcycle,2]))
        pres.ipsiHipPower_z = np.interp(np.linspace(1,len(gaitcycle),new_length),np.linspace(1,len(gaitcycle),len(gaitcycle)),np.squeeze(preadin.RHipPower[gaitcycle,2]))





