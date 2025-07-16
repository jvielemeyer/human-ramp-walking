import numpy as np #for calculation
from scipy import signal #for filter
from scipy.signal import butter #for butterworth filter
import os #to get file name instead of whole file path
import matplotlib.pyplot as plt

from calculation import calcReadInData,calcInput,calcVPP, calcSave,calcPlot
# import calcReadInData #readData, getData, readin_kinematics, calc_joints
# import calcInput #readIni, button_get_entries, calc_forces_cop_com, load_data
# import calcVPP #VPP_calculation, R_mod
# import calcSave #button_save_data, data_save_npz, save_VPP_mean
# import calcPlot #button_plot_input, VPP_plot, VPP_plot_show, plot_joints



def show_calc(preadin,pres):
    preadin.lower()
    pres.lift()

def show_calc1(pres,pstart,pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b,ListeFiles,ListeVPP):
    calcReadInData.getData(pres,pstart,pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b,ListeFiles,ListeVPP)
    show_calc(preadin,pres)


def button_res_save(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name,foldername,k,p,ListeVPP):
    plot=p
    button_res_both(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name,plot)
    #-----------------------------------------VPP
    pres.ListeVPP.append([file_name,1,pres.VPP_calc1[0],pres.VPP_calc1[1],pres.r_mod1])
    pres.ListeVPP.append([file_name,2,pres.VPP_calc2[0],pres.VPP_calc2[1],pres.r_mod2])
    calcSave.button_save_data(pres.ListeVPP,foldername,"VPP") #save in csv, name after foldername
    #---------------------------------------------Kinematics
    calcReadInData.calc_joints(pres.tdto,preadin,pres,pres.foot_td)

    #---------------------SAVE (COMPRESS) DATA IN .NPZ
    calcSave.data_save_npz(pres,file_name,foldername,
            pres.ipsiAnkleAngle_x,pres.ipsiAnkleAngle_y, pres.ipsiAnkleAngle_z,
            pres.contraAnkleAngle_x,pres.contraAnkleAngle_y, pres.contraAnkleAngle_z,
            pres.ipsiAnkleMoment_x,pres.ipsiAnkleMoment_y, pres.ipsiAnkleMoment_z,
            pres.ipsiAnklePower_x, pres.ipsiAnklePower_y, pres.ipsiAnklePower_z,
            pres.ipsiKneeAngle_x,  pres.ipsiKneeAngle_y, pres.ipsiKneeAngle_z,
            pres.contraKneeAngle_x,  pres.contraKneeAngle_y, pres.contraKneeAngle_z,
            pres.ipsiKneeMoment_x, pres.ipsiKneeMoment_y, pres.ipsiKneeMoment_z,
            pres.ipsiKneePower_x, pres.ipsiKneePower_y, pres.ipsiKneePower_z,
            pres.ipsiHipAngle_x,  pres.ipsiHipAngle_y,  pres.ipsiHipAngle_z,
            pres.contraHipAngle_x,  pres.contraHipAngle_y,  pres.contraHipAngle_z,
            pres.ipsiHipMoment_x, pres.ipsiHipMoment_y, pres.ipsiHipMoment_z,
            pres.ipsiHipPower_x, pres.ipsiHipPower_y, pres.ipsiHipPower_z,
            pres.ipsiShoulderAngle_x, pres.ipsiShoulderAngle_y, pres.ipsiShoulderAngle_z,
            pres.contraShoulderAngle_x, pres.contraShoulderAngle_y, pres.contraShoulderAngle_z,
            pres.ipsiElbowAngle_x, pres.ipsiElbowAngle_y, pres.ipsiElbowAngle_z,
            pres.contraElbowAngle_x, pres.contraElbowAngle_y,pres.contraElbowAngle_z,
            pres.HeadAngle_x, pres.HeadAngle_y, pres.HeadAngle_z,
            pres.ThoraxAngle_x, pres.ThoraxAngle_y, pres.ThoraxAngle_z,
            pres.Fx1_norm, pres.Fx2_norm,pres.Fy1_norm, pres.Fy2_norm, pres.Fz1_norm, pres.Fz2_norm,
            pres.COPx1_norm, pres.COPx2_norm,pres.COPy1_norm, pres.COPy2_norm, pres.COPz1_norm, pres.COPz2_norm,
            pres.COMx1_norm, pres.COMx2_norm, pres.COMy1_norm, pres.COMy2_norm,pres.COMz1_norm,pres.COMz2_norm,
            pres.VPP_calc1, pres.VPP_calc2,pres.r_mod1,pres.r_mod2,
            pres.speed)

def button_res_both(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name,plot):
    [tdto, tt, COM, direction,sign_x] = calcInput.calc_forces_cop_com(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name)

    sos = butter(4, 50,  'lowpass', output='sos',fs = preadin.Frequ_video)
    VPP_init=[0, 0.2]

    for index in range(0,4,2): #0,2
        if direction == 0:
            pres.CoM_dir = COM[:,[1,2]] #only x and z
            pres.Hip_dir = preadin.MHip[:,[1,2]]
        else:
            pres.CoM_dir = np.transpose(np.array([sign_x*COM[:,1],COM[:,2]]))  #Com with changed direction (fits to CoP)
            pres.Hip_dir = np.transpose(np.array([sign_x*preadin.MHip[:,1],preadin.MHip[:,2]]))

        #----------------------------------------------calc VPP
        #center_of_coord = pres.Hip_dir #VPP in hip centered coordinate frame
        center_of_coord = pres.CoM_dir #VPP in CoM centered coordinate frame
        align = 0 #vertical aligned
        #align = 1 #trunk aligned
        if (index < 2): #1st contact
            pres.VPP_calc1 = calcVPP.VPP_calculation(pres.CoPx1[tt[index]:tt[index+1]],pres.CoPz1[tt[index]:tt[index+1]], center_of_coord[tt[index]:tt[index+1]], pres.Fx1[tt[index]:tt[index+1]], pres.Fz1[tt[index]:tt[index+1]], VPP_init,preadin.ThoraxAngle[tt[index]:tt[index+1],1],align,file_name)
            pres.r_mod1 = calcVPP.R_mod(pres.CoPx1[tt[index]:tt[index+1]], pres.CoPz1[tt[index]:tt[index+1]],center_of_coord[tt[index]:tt[index+1]], pres.Fx1[tt[index]:tt[index+1]], pres.Fz1[tt[index]:tt[index+1]],preadin.ThoraxAngle[tt[index]:tt[index+1],1],align, pres.VPP_calc1,1)

        else: #2nd contact
            pres.VPP_calc2 = calcVPP.VPP_calculation(pres.CoPx2[tt[index]:tt[index+1]],pres.CoPz2[tt[index]:tt[index+1]], center_of_coord[tt[index]:tt[index+1]], pres.Fx2[tt[index]:tt[index+1]], pres.Fz2[tt[index]:tt[index+1]], VPP_init,preadin.ThoraxAngle[tt[index]:tt[index+1],1],align,file_name)
            pres.r_mod2 = calcVPP.R_mod(pres.CoPx2[tt[index]:tt[index+1]],pres.CoPz2[tt[index]:tt[index+1]], center_of_coord[tt[index]:tt[index+1]], pres.Fx2[tt[index]:tt[index+1]], pres.Fz2[tt[index]:tt[index+1]],preadin.ThoraxAngle[tt[index]:tt[index+1],1], align, pres.VPP_calc2, 2)

        pres.CoM =COM
        pres.tdto = tdto
        pres.tt = tt

def button_res_single(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name):
        plot = 0
        button_res_both(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,file_name,plot)
        pres.VPPx1.set(np.round(pres.VPP_calc1[0],3))
        pres.VPPz1.set(np.round(pres.VPP_calc1[1],3))
        pres.R2_1.set(round(pres.r_mod1,3))
        pres.label_file['text'] = file_name
        pres.l_VPPx1['text'] = pres.VPPx1.get()
        pres.l_VPPz1['text'] = pres.VPPz1.get()
        pres.l_R2_1['text'] = pres.R2_1.get()
        pres.VPPx2.set(np.round(pres.VPP_calc2[0],3))
        pres.VPPz2.set(np.round(pres.VPP_calc2[1],3))
        pres.R2_2.set(round(pres.r_mod2,3))
        pres.label_file['text'] = file_name
        pres.l_VPPx2['text'] = pres.VPPx2.get()
        pres.l_VPPz2['text'] = pres.VPPz2.get()
        pres.l_R2_2['text'] = pres.R2_2.get()

#--------------------------------------------Buttons on page pres
def nextVPP(pres,pstart,preadin,pkinematic1, pkinematic2a,pkinematic2b, pkinetic,ListeFiles):
        pres.lift()
        if pres.count < (len(ListeFiles)-1):
            pres.count = pres.count + 1
        else:
            pres.count=0
        calcReadInData.calc_joints(pres.tdto,preadin,pres,pres.foot_td)
        if pstart.number_files.get() == 1:
            calcInput.load_data(preadin, pres, pkinetic,ListeFiles,pres.count)
        else:
            calcInput.load_data_dyn(preadin, pres, pkinetic, ListeFiles,pres.count)
            calcInput.load_data_kin(preadin, pres, pkinetic, ListeFiles_kin,pres.count)
        file_path = ListeFiles[pres.count]
        button_res_single(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(file_path)[0:-4])
        show_calc(preadin,pres)


def prevVPP(pres,pstart,preadin, pkinematic1, pkinematic2a,pkinematic2b, pkinetic,ListeFiles):
        pres.lift()
        if pres.count > 0:
            pres.count = pres.count - 1
        else:
            pres.count=len(ListeFiles)-1
        calcReadInData.calc_joints(pres.tdto,preadin,pres,pres.foot_td)
        if pstart.number_files.get() == 1:
            calcInput.load_data(preadin, pres, pkinetic, ListeFiles,pres.count)
        else:
            calcInput.load_data_dyn(preadin, pres, pkinetic, ListeFiles,pres.count)
            calcInput.load_data_kin(preadin, pres, pkinetic, ListeFiles_kin,pres.count)
        file_path = ListeFiles[pres.count]
        button_res_single(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(file_path)[0:-4])
        show_calc(preadin,pres)


def save_figures(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin):
        # if pstart.number_files.get() == 2: #additionally data kin
        #    import_file_path_kin = self.file_kin
        import_file_path = preadin.files
        directory = os.path.split(import_file_path[0])[0]
        foldername = directory.split('/')[-1]
        for k in range(0,len(import_file_path)): #read in for each file
          #  if pstart.number_files == 1:
            calcInput.load_data(preadin, pres, pkinetic, import_file_path,k)
           # else:
            #    calcInput.load_data_dyn(preadin, pres, pkinetic, import_file_path,k)
             #   calcInput.load_data_kin(preadin, pres, pkinetic, import_file_path_kin,k)
            button_res_save(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(import_file_path[k])[0:-4],foldername,k,2,pres.ListeVPP)

def plot_input(pres):
    pres.p_var = 1
    calcPlot.button_plot_input(pres.CoPx1,pres.CoPx2,pres.CoPz1,pres.CoPz2, pres.CoM_dir, pres.Fx1, pres.Fx2, pres.Fz1, pres.Fz2,pres.p_var,pres.tdto) #pres.CoM[:,[1,2]]

def plot_kin(pres):
    pres.p_kin = 1
    calcPlot.plot_joints(pres.p_kin,pres)


def plot_vpp(pres,pstart,pkinematic1,pkinematic2a,pkinematic2b,preadin):
    #center_of_coord = pres.Hip_dir
    center_of_coord = pres.CoM_dir
    align = 0 #vertical aligned
    #align = 1 #trunk aligned

    pres.p_vpp = 1
    file_path = pres.ListeFiles[pres.count]
    button_res_both(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin,os.path.basename(file_path)[0:-4],pres.p_vpp)
    tt = pres.tt
    index = 0; #VPP1
    calcPlot.VPP_plot_show(pres.p_vpp,pres.Fx1[tt[index]:tt[index+1]], pres.Fz1[tt[index]:tt[index+1]],center_of_coord[tt[index]:tt[index+1]],pres.CoPx1[tt[index]:tt[index+1]],pres.CoPz1[tt[index]:tt[index+1]],preadin.ThoraxAngle[tt[index]:tt[index+1],1],align, pres.VPP_calc1,os.path.basename(file_path)[0:-4],1)
    #VPP2
    index = 2; #VPP2
    calcPlot.VPP_plot_show(pres.p_vpp,pres.Fx2[tt[index]:tt[index+1]], pres.Fz2[tt[index]:tt[index+1]],center_of_coord[tt[index]:tt[index+1]],pres.CoPx2[tt[index]:tt[index+1]],pres.CoPz2[tt[index]:tt[index+1]],preadin.ThoraxAngle[tt[index]:tt[index+1],1],align, pres.VPP_calc2,os.path.basename(file_path)[0:-4],2)
    plt.show()







