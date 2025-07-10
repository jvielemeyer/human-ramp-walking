#VPP calculation Software by Johanna Vielemeyer
#johanna.vielemeyer@uni-jena.de
#github-link
#------------------------------------------------------
#---------------PREAMBLE-------------------------------
#------------------------------------------------------
from tkinter import font
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import sys
import os
import numpy as np #for calculation
from numpy import genfromtxt #to get NaN for empty columns
import matplotlib.pyplot as plt #to create plots


#-------------------import functions from other files

sys.path.append(os.path.normpath('./calculation/'))
import calcButtons #show_calc, show_calc1, button_res_save, button_res_both, button_res_single, nextVPP, prevVPP, save_figures, plot_input, plot_kin, plot_vpp
import calcInput #readIni, button_get_entries, calc_forces_cop_com, load_data
import calcReadInData #readData, getData,readin_kinematics, calc_joints


#------------------------------------------------------------------------
#----------FIRST PART: CREATE GUI-----------------------------------------
#-------------------------------------------------------------------------
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

#--------------------------------------------------------------------------
class PageStart(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=50)
        self.normal_font=font.Font(self, family='Arial', size=12)

        self.number_files = tk.IntVar()
        self.com_output = tk.IntVar()

        #---------------------------------------------------------header
        self.label_header=tk.Label(self, text= 'VPP calculation tool',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)

        #----------------------------------------------------how many files
        self.label_number_files=tk.Label(self, text= 'Kinematic and kinetic data are saved in ',font=self.normal_font,bg='white', anchor='nw')
        self.label_number_files.place(relx=0.1, rely=0.3, relwidth=0.7, relheight=0.05)
        self.radio_number_files_1=tk.Radiobutton(self, text="one file", variable=self.number_files, value =1, font=self.normal_font, anchor='w',bg='white', activeforeground="dim gray")
        self.radio_number_files_2=tk.Radiobutton(self, text="two separate files", variable=self.number_files, value =2, font=self.normal_font, anchor='w',bg='white', activeforeground="dim gray")
        self.radio_number_files_1.place(relx=0.55, rely=0.3, relwidth=0.2, relheight=0.05)
        self.radio_number_files_2.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.05)
        self.radio_number_files_1.select()

        #-------------------------------------------------------------------Button
        self.browseButton_ini=tk.Button(self, text='Load initialization file(s)...', bg='lightblue', fg='black', font=('helvetica', 12, 'bold'))
        self.browseButton_ini.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.1)
        #all in one data file
        self.browseButton_data=tk.Button(self, text='Load data file(s)...', bg='blue', fg='white', font=('helvetica', 12, 'bold'))
        #two separate data files (the order of the files has to fit)
        self.browseButton_data_dyn=tk.Button(self, text='Load kinetic data files...', bg='blue', fg='white', font=('helvetica', 12, 'bold'))

        self.browseButton_data_kin=tk.Button(self, text='Load kinematic data files...', bg='blue', fg='white', font=('helvetica', 12, 'bold'))

        self.Button_skip=tk.Button(self, text='skip configuration \n calc direct', bg='red', fg='white', font=('helvetica', 12, 'bold'))
        self.Button_skip.place(relx=0.375, rely=0.8, relwidth=0.25, relheight=0.1)

        #option "one file" is shown on start page:
        self.browseButton_data.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        #option two files is shown on start page:
        # self.browseButton_data_dyn.place(relx=0.15, rely=0.5, relwidth=0.34, relheight=0.1)
        # self.browseButton_data_kin.place(relx=0.5, rely=0.5, relwidth=0.35, relheight=0.1)

        
        #--------------------------center of mass as output variable available?
        self.label_com_output=tk.Label(self, text= 'Center of mass (CoM) is already output variable in raw data ',font=self.normal_font,bg='white', anchor='nw')
        self.label_com_output.place(relx=0.1, rely=0.7, relwidth=0.7, relheight=0.05)
        self.radio_com_output_1=tk.Radiobutton(self, text="yes", variable=self.com_output, value =1, font=self.normal_font, anchor='w',bg='white', activeforeground="dim gray")
        self.radio_com_output_2=tk.Radiobutton(self, text="no", variable=self.com_output, value =2, font=self.normal_font, anchor='w',bg='white', activeforeground="dim gray")
        self.radio_com_output_1.place(relx=0.75, rely=0.7, relwidth=0.1, relheight=0.05)
        self.radio_com_output_2.place(relx=0.85, rely=0.7, relwidth=0.1, relheight=0.05)

        self.radio_com_output_1.select() #"yes"  is chosen
        # ------------------------------------------------------------
        self.button_forward =  tk.Button(self, text = ">>", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_forward.place(relx = 0.9, rely = 0.9, relwidth=0.07, relheight=0.07)

#-------------------------------------------------------------------------
#----------------------------Page "Configuration (kinetic data)""
class PageKinetic(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)
        self.container_1=tk.Frame(self, bg='white')
        self.container_1.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)
        self.container_2=tk.Frame(self, bg='white')
        self.container_2.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)
        self.container_3=tk.Frame(self, bg='white')
        self.container_3.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)
        self.container_4=tk.Frame(self, bg='white')
        self.container_4.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

        self.frequ_grf=tk.IntVar()
        self.unit=tk.IntVar()
        self.nb_kmp=tk.IntVar()
        self.mass= []
        self.fac_fx=tk.DoubleVar()
        self.fac_fz=tk.DoubleVar()

        #-----------------------------------------------------header
        self.label_header=tk.Label(self, text= '1. Configuration (kinetic data)',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)

        #----------------------------------------------measurement frequency
        self.label_grf=tk.Label(self, text= 'sample frequency kinetic data in Hz (e.g. 1000 Hz):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_grf.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.05)
        self.entry_frequ_grf=tk.Entry(self, textvariable=self.frequ_grf, justify='left',font=("Arial", 14))

        self.entry_frequ_grf.place(relx=0.65, rely=0.15, relwidth=0.1, relheight=0.05)

        #------------------------------------------------------------unit CoP
        self.label_unit_cop=tk.Label(self, text= 'CoP measured in:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_unit_cop.place(relx=0.1, rely=0.25, relwidth=0.7, relheight=0.05)
        self.radio_unit_cop_mm=tk.Radiobutton(self, text="mm", variable=self.unit, value =1, font=self.normal_font, anchor='w',bg='lightgray', activeforeground="dim gray")
        self.radio_unit_cop_meter=tk.Radiobutton(self, text="m", variable=self.unit, value =0, font=self.normal_font, anchor='w',bg='lightgray', activeforeground="dim gray")
        self.radio_unit_cop_mm.place(relx=0.6, rely=0.25, relwidth=0.15, relheight=0.05)
        self.radio_unit_cop_meter.place(relx=0.75, rely=0.25, relwidth=0.15, relheight=0.05)
        self.radio_unit_cop_mm.select()

        #------------------------------------------order and signs of kinetic data
        self.label_dyn=tk.Label(self, text= 'GRFx  \t \t GRFz \t \t CoPx',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dyn.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.05)

        #--------------------------------------------1st contact
        self.col_fx1=tk.IntVar()
        self.col_fz1=tk.IntVar()
        self.col_copx1=tk.IntVar()
        self.col_copz1=tk.IntVar()
        self.pm_fx1=tk.StringVar()
        self.pm_fz1=tk.StringVar()
        self.pm_copx1=tk.StringVar()


        self.label_fp_1=tk.Label(self.container_1, text= 'Force Plate 1:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_fp_1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_fx1=tk.Entry(self.container_1, textvariable=self.col_fx1, justify='center',font=("Arial", 14))
        self.entry_fx1.place(relx=0.35, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_fz1=tk.Entry(self.container_1, textvariable=self.col_fz1, justify='center',font=("Arial", 14))
        self.entry_fz1.place(relx=0.55, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_copx1=tk.Entry(self.container_1, textvariable=self.col_copx1, justify='center',font=("Arial", 14))
        self.entry_copx1.place(relx=0.75, rely=0, relwidth=0.05, relheight=0.5)

        self.combo_pm_fx1=ttk.Combobox(self.container_1, textvariable=self.pm_fx1, font=("Arial", 14))
        self.combo_pm_fx1['values']=('+', '-')
        self.combo_pm_fx1.current(0) # "+" = 0 as standard
        self.combo_pm_fx1.place(relx=0.3, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_fz1=ttk.Combobox(self.container_1, textvariable=self.pm_fz1, font=("Arial", 14))
        self.combo_pm_fz1['values']=('+', '-')
        self.combo_pm_fz1.current(0)
        self.combo_pm_fz1.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_copx1=ttk.Combobox(self.container_1, textvariable=self.pm_copx1, font=("Arial", 14))
        self.combo_pm_copx1['values']=('+', '-')
        self.combo_pm_copx1.current(0)
        self.combo_pm_copx1.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)

        #----------------------------------2nd contact
        self.col_fx2=tk.IntVar()
        self.col_fz2=tk.IntVar()
        self.col_copx2=tk.IntVar()
        self.col_copz2=tk.IntVar()
        self.pm_fx2=tk.StringVar()
        self.pm_fz2=tk.StringVar()
        self.pm_copx2=tk.StringVar()

        self.label_fp_2=tk.Label(self.container_2, text= 'Force Plate 2:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_fp_2.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_fx2=tk.Entry(self.container_2, textvariable=self.col_fx2, justify='center',font=("Arial", 14))
        self.entry_fx2.place(relx=0.35, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_fz2=tk.Entry(self.container_2, textvariable=self.col_fz2, justify='center',font=("Arial", 14))
        self.entry_fz2.place(relx=0.55, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_copx2=tk.Entry(self.container_2, textvariable=self.col_copx2, justify='center',font=("Arial", 14))
        self.entry_copx2.place(relx=0.75, rely=0, relwidth=0.05, relheight=0.5)

        self.combo_pm_fx2=ttk.Combobox(self.container_2, textvariable=self.pm_fx2, font=("Arial", 14))
        self.combo_pm_fx2['values']=('+', '-')
        self.combo_pm_fx2.current(0)
        self.combo_pm_fx2.place(relx=0.3, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_fz2=ttk.Combobox(self.container_2, textvariable=self.pm_fz2, font=("Arial", 14))
        self.combo_pm_fz2['values']=('+', '-')
        self.combo_pm_fz2.current(0)
        self.combo_pm_fz2.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_copx2=ttk.Combobox(self.container_2, textvariable=self.pm_copx2, font=("Arial", 14))
        self.combo_pm_copx2['values']=('+', '-')
        self.combo_pm_copx2.current(0)
        self.combo_pm_copx2.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)

        #---------------------------------------3rd contact
        self.col_fx3=tk.IntVar()
        self.col_fz3=tk.IntVar()
        self.col_copx3=tk.IntVar()
        self.col_copz3=tk.IntVar()
        self.pm_fx3=tk.StringVar()
        self.pm_fz3=tk.StringVar()
        self.pm_copx3=tk.StringVar()

        self.label_fp_3=tk.Label(self.container_3, text= 'Force Plate 3:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_fp_3.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_fx3=tk.Entry(self.container_3, textvariable=self.col_fx3, justify='center',font=("Arial", 14))
        self.entry_fx3.place(relx=0.35, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_fz3=tk.Entry(self.container_3, textvariable=self.col_fz3, justify='center',font=("Arial", 14))
        self.entry_fz3.place(relx=0.55, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_copx3=tk.Entry(self.container_3, textvariable=self.col_copx3, justify='center',font=("Arial", 14))
        self.entry_copx3.place(relx=0.75, rely=0, relwidth=0.05, relheight=0.5)

        self.combo_pm_fx3=ttk.Combobox(self.container_3, textvariable=self.pm_fx3, font=("Arial", 14))
        self.combo_pm_fx3['values']=('+', '-')
        self.combo_pm_fx3.current(0)
        self.combo_pm_fx3.place(relx=0.3, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_fz3=ttk.Combobox(self.container_3, textvariable=self.pm_fz3, font=("Arial", 14))
        self.combo_pm_fz3['values']=('+', '-')
        self.combo_pm_fz3.current(0)
        self.combo_pm_fz3.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.combo_pm_copx3=ttk.Combobox(self.container_3, textvariable=self.pm_copx3, font=("Arial", 14))
        self.combo_pm_copx3['values']=('+', '-')
        self.combo_pm_copx3.current(0)
        self.combo_pm_copx3.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)


        self.button_forward =  tk.Button(self, text = ">>", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_forward.place(relx = 0.9, rely = 0.9, relwidth=0.07, relheight=0.07)
        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)

        #------------------------------------------------factor forces
        self.label_factor_Fx=tk.Label(self, text= 'Factor GRFx:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_factor_Fx.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.05)
        self.entry_factor_Fx=tk.Entry(self, textvariable=self.fac_fx, justify='left',font=("Arial", 14))
        self.entry_factor_Fx.place(relx=0.3, rely=0.85, relwidth=0.1, relheight=0.05)
        self.fac_fx.set(1.0)
        self.label_factor_Fz=tk.Label(self, text= 'Factor GRFz:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_factor_Fz.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.05)
        self.entry_factor_Fz=tk.Entry(self, textvariable=self.fac_fz, justify='left',font=("Arial", 14))
        self.entry_factor_Fz.place(relx=0.7, rely=0.85, relwidth=0.1, relheight=0.05)
        self.fac_fz.set(1.0)
#-------------------------------------------------------------------------
#-----------------------Page "Configuration (kinematic data)""
class PageKinematic1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)

        self.frequ_video=tk.IntVar()
        self.frequ_cut=tk.IntVar()
        self.unit=tk.IntVar()

        #--------------------------------------------------header
        self.label_header=tk.Label(self, text= '2. Configuration (kinematic data)',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)

        #--------------------------------------------------sample frequency
        self.label_video=tk.Label(self, text= 'sample frequency kinematics in Hz (e.g. 200 Hz):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_video.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.05)
        self.entry_frequ_video=tk.Entry(self, textvariable=self.frequ_video, justify='left',font=("Arial", 14))
        self.entry_frequ_video.place(relx=0.65, rely=0.15, relwidth=0.1, relheight=0.05)

        #----------------------------------------------------cutoff frequency
        self.label_frequ_cut=tk.Label(self, text= 'cut-off frequency kinematics in Hz (e.g. 50 Hz):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_frequ_cut.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.05)
        self.entry_frequ_cut=tk.Entry(self, textvariable=self.frequ_cut, justify='left',font=("Arial", 14))
        self.entry_frequ_cut.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.05)

        #-----------------------------------------------------------unit data
        self.label_unit=tk.Label(self, text= 'data measured in:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_unit.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.05)
        radio_unit_mm=tk.Radiobutton(self, text="mm", variable=self.unit, value =1, font=self.normal_font, anchor='w',bg='lightgray', activeforeground="dim gray")
        radio_unit_meter=tk.Radiobutton(self, text="m", variable=self.unit, value =0, font=self.normal_font, anchor='w',bg='lightgray', activeforeground="dim gray")
        radio_unit_mm.place(relx=0.6, rely=0.35, relwidth=0.15, relheight=0.05)
        radio_unit_meter.place(relx=0.75, rely=0.35, relwidth=0.15, relheight=0.05)
        radio_unit_mm.select()

        #--------------------------------------------------------------button
        self.button_forward =  tk.Button(self, text = ">>", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_forward.place(relx = 0.9, rely = 0.9, relwidth=0.07, relheight=0.07)
        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)
#-------------------------------------------------------------------------
#--------------------------------Page: "marker setup (kinematic data)"
class PageKinematic2a(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)

        self.container_1=tk.Frame(self, bg='white')
        self.container_1.place(relx=0, rely=0.225, relwidth=1, relheight=0.1)
        self.container_2=tk.Frame(self, bg='white')
        self.container_2.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)
        self.container_3=tk.Frame(self, bg='white')
        self.container_3.place(relx=0, rely=0.375, relwidth=1, relheight=0.1)
        self.container_4=tk.Frame(self, bg='white')
        self.container_4.place(relx=0, rely=0.45, relwidth=1, relheight=0.1)
        self.container_5=tk.Frame(self, bg='white')
        self.container_5.place(relx=0, rely=0.525, relwidth=1, relheight=0.1)
        self.container_6=tk.Frame(self, bg='white')
        self.container_6.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)
        self.container_7=tk.Frame(self, bg='white')
        self.container_7.place(relx=0, rely=0.675, relwidth=1, relheight=0.1)
        self.container_8=tk.Frame(self, bg='white')
        self.container_8.place(relx=0, rely=0.75, relwidth=1, relheight=0.1)


        #-------------------------------------------------header
        self.label_header=tk.Label(self, text= '3. Marker setup (kinematic data)',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)
        self.label_marker=tk.Label(self, text= 'left:  \t x \t z \t right: \t x \t z',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_marker.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.05)

        #---------------------------------------single markers
        #mal lat
        self.mal_lat_lx=tk.IntVar()
        self.mal_lat_lz=tk.IntVar()
        self.mal_lat_rx=tk.IntVar()
        self.mal_lat_rz=tk.IntVar()
        self.label_mal_lat=tk.Label(self.container_1, text= 'malleolus lateralis:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_mal_lat.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_mal_lat_lx=tk.Entry(self.container_1, textvariable=self.mal_lat_lx, justify='center',font=("Arial", 14))
        self.entry_mal_lat_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_lat_lz=tk.Entry(self.container_1, textvariable=self.mal_lat_lz, justify='center',font=("Arial", 14))
        self.entry_mal_lat_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_lat_rx=tk.Entry(self.container_1, textvariable=self.mal_lat_rx, justify='center',font=("Arial", 14))
        self.entry_mal_lat_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_lat_rz=tk.Entry(self.container_1, textvariable=self.mal_lat_rz, justify='center',font=("Arial", 14))
        self.entry_mal_lat_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #mal med
        self.mal_med_lx=tk.IntVar()
        self.mal_med_lz=tk.IntVar()
        self.mal_med_rx=tk.IntVar()
        self.mal_med_rz=tk.IntVar()
        self.label_mal_med=tk.Label(self.container_2, text= 'malleolus medialis:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_mal_med.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_mal_med_lx=tk.Entry(self.container_2, textvariable=self.mal_med_lx, justify='center',font=("Arial", 14))
        self.entry_mal_med_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_med_lz=tk.Entry(self.container_2, textvariable=self.mal_med_lz, justify='center',font=("Arial", 14))
        self.entry_mal_med_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_med_rx=tk.Entry(self.container_2, textvariable=self.mal_med_rx, justify='center',font=("Arial", 14))
        self.entry_mal_med_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_mal_med_rz=tk.Entry(self.container_2, textvariable=self.mal_med_rz, justify='center',font=("Arial", 14))
        self.entry_mal_med_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #toe
        self.toe_lx=tk.IntVar()
        self.toe_lz=tk.IntVar()
        self.toe_rx=tk.IntVar()
        self.toe_rz=tk.IntVar()
        self.label_toe=tk.Label(self.container_3, text= 'toe:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_toe.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_toe_lx=tk.Entry(self.container_3, textvariable=self.toe_lx, justify='center',font=("Arial", 14))
        self.entry_toe_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_toe_lz=tk.Entry(self.container_3, textvariable=self.toe_lz, justify='center',font=("Arial", 14))
        self.entry_toe_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_toe_rx=tk.Entry(self.container_3, textvariable=self.toe_rx, justify='center',font=("Arial", 14))
        self.entry_toe_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_toe_rz=tk.Entry(self.container_3, textvariable=self.toe_rz, justify='center',font=("Arial", 14))
        self.entry_toe_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #knee
        self.knee_lx=tk.IntVar()
        self.knee_lz=tk.IntVar()
        self.knee_rx=tk.IntVar()
        self.knee_rz=tk.IntVar()
        self.label_knee=tk.Label(self.container_4, text= 'knee:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_knee.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_knee_lx=tk.Entry(self.container_4, textvariable=self.knee_lx, justify='center',font=("Arial", 14))
        self.entry_knee_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_knee_lz=tk.Entry(self.container_4, textvariable=self.knee_lz, justify='center',font=("Arial", 14))
        self.entry_knee_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_knee_rx=tk.Entry(self.container_4, textvariable=self.knee_rx, justify='center',font=("Arial", 14))
        self.entry_knee_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_knee_rz=tk.Entry(self.container_4, textvariable=self.knee_rz, justify='center',font=("Arial", 14))
        self.entry_knee_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #hip
        self.hip_lx=tk.IntVar()
        self.hip_lz=tk.IntVar()
        self.hip_rx=tk.IntVar()
        self.hip_rz=tk.IntVar()
        self.label_hip=tk.Label(self.container_5, text= 'trochanter major (hip):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_hip.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_hip_lx=tk.Entry(self.container_5, textvariable=self.hip_lx, justify='center',font=("Arial", 14))
        self.entry_hip_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_hip_lz=tk.Entry(self.container_5, textvariable=self.hip_lz, justify='center',font=("Arial", 14))
        self.entry_hip_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_hip_rx=tk.Entry(self.container_5, textvariable=self.hip_rx, justify='center',font=("Arial", 14))
        self.entry_hip_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_hip_rz=tk.Entry(self.container_5, textvariable=self.hip_rz, justify='center',font=("Arial", 14))
        self.entry_hip_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #shoulder
        self.shoulder_lx=tk.IntVar()
        self.shoulder_lz=tk.IntVar()
        self.shoulder_rx=tk.IntVar()
        self.shoulder_rz=tk.IntVar()
        self.label_shoulder=tk.Label(self.container_6, text= 'acromion (shoulder):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_shoulder.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.entry_shoulder_lx=tk.Entry(self.container_6, textvariable=self.shoulder_lx, justify='center',font=("Arial", 14))
        self.entry_shoulder_lx.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_shoulder_lz=tk.Entry(self.container_6, textvariable=self.shoulder_lz, justify='center',font=("Arial", 14))
        self.entry_shoulder_lz.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_shoulder_rx=tk.Entry(self.container_6, textvariable=self.shoulder_rx, justify='center',font=("Arial", 14))
        self.entry_shoulder_rx.place(relx=0.7, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_shoulder_rz=tk.Entry(self.container_6, textvariable=self.shoulder_rz, justify='center',font=("Arial", 14))
        self.entry_shoulder_rz.place(relx=0.8, rely=0, relwidth=0.05, relheight=0.5)

        #------------------------------------------------------------button
        self.button_forward =  tk.Button(self, text = ">>", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_forward.place(relx = 0.9, rely = 0.9, relwidth=0.07, relheight=0.07)
        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)
#---------------------------------------------------------------------------------
#---------if Com is available: position in kinematic file (kinematic data: only Com)
class PageKinematic2b(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)

        self.container_1=tk.Frame(self, bg='white')
        self.container_1.place(relx=0, rely=0.35, relwidth=1, relheight=0.1)
        

        #-------------------------------------------------------header
        self.label_header=tk.Label(self, text= '3. Center of mass (CoM) coordinates \n in kinematic data',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)
        self.label_marker=tk.Label(self, text= '\t x \t z ',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_marker.place(relx=0.3, rely=0.25, relwidth=0.35, relheight=0.05)

        #-------------------------------------------------------center of mass (CoM)
        self.com_x=tk.IntVar()
        self.com_z=tk.IntVar()
        self.label_com=tk.Label(self.container_1, text= 'CoM position:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_com.place(relx=0.1, rely=0, relwidth=0.55, relheight=0.5)
        self.entry_com_x=tk.Entry(self.container_1, textvariable=self.com_x, justify='center',font=("Arial", 14))
        self.entry_com_x.place(relx=0.4, rely=0, relwidth=0.05, relheight=0.5)
        self.entry_com_z=tk.Entry(self.container_1, textvariable=self.com_z, justify='center',font=("Arial", 14))
        self.entry_com_z.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.5)

        #----------------------------------------------------------------button
        self.button_forward =  tk.Button(self, text = ">>", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_forward.place(relx = 0.9, rely = 0.9, relwidth=0.07, relheight=0.07)
        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)
#------------------------------------------------------------------------------------
#--------------------------------------------------Page:"Read in files"
class PageReadin(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)

        #--------------------Variables
        self.keyword_dyn=tk.StringVar()
        self.keyword_kin=tk.StringVar()
        self.keyword_kin_end=tk.StringVar()

        self.dist_keyword_dyn=tk.IntVar()
        self.dist_keyword_dyn_end=tk.IntVar()
        self.dist_keyword_kin=tk.IntVar()
        self.dist_keyword_kin_end=tk.IntVar()

        #--------------------------------------------------------header
        self.label_header=tk.Label(self, text= '4. Read in data',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)

        #---------------------------------------------------------label
        self.label_keyword_dyn=tk.Label(self, text= 'key word in header kinetics (e.g. \'Devices\'):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_keyword_dyn.place(relx=0.05, rely=0.2, relwidth=0.7, relheight=0.05)
        self.label_dist_keyword_dyn=tk.Label(self, text= 'distance (rows) from keyword kinetics to data (e.g. 5 rows):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dist_keyword_dyn.place(relx=0.05, rely=0.3, relwidth=0.7, relheight=0.05)
        self.label_dist_keyword_dyn=tk.Label(self, text= 'distance (rows) from keyword kinematics to end kinetic data:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dist_keyword_dyn.place(relx=0.05, rely=0.4, relwidth=0.7, relheight=0.05)
        self.label_keyword_kin=tk.Label(self, text= 'key word in header kinematics (e.g. \'Trajectories\'):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_keyword_kin.place(relx=0.05, rely=0.5, relwidth=0.7, relheight=0.05)
        self.label_dist_keyword_kin=tk.Label(self, text= 'distance (rows) from keyword kinematics to data:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dist_keyword_kin.place(relx=0.05, rely=0.6, relwidth=0.7, relheight=0.05)
        self.label_dist_keyword_kin_end=tk.Label(self, text= 'distance (rows) from end kinematic data to next word:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dist_keyword_kin_end.place(relx=0.05, rely=0.7, relwidth=0.7, relheight=0.05)
        self.label_dist_keyword_end=tk.Label(self, text= '"next word":',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_dist_keyword_end.place(relx=0.05, rely=0.8, relwidth=0.7, relheight=0.05)
        
        #---------------------------------------------------------------Entry
        self.entry_keyword_dyn=tk.Entry(self, textvariable=self.keyword_dyn, justify='left',font=("Arial", 14))
        self.entry_keyword_dyn.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.05)
        self.entry_keyword_kin=tk.Entry(self, textvariable=self.keyword_kin, justify='left',font=("Arial", 14))
        self.entry_keyword_kin.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.05)
        self.entry_keyword_end=tk.Entry(self, textvariable=self.keyword_kin_end, justify='left',font=("Arial", 14))
        self.entry_keyword_end.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.05)

        #---------------------------Combobox (to choose from given entries)
        self.combo_dist_keyword_dyn=ttk.Combobox(self, textvariable=self.dist_keyword_dyn, font=("Arial", 14))
        self.combo_dist_keyword_dyn['values']=('1', '2', '3', '4', '5', '6', '7','8','9','10')
        self.combo_dist_keyword_dyn.current(0)
        self.combo_dist_keyword_dyn.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.05)
        self.combo_dist_keyword_dyn_end=ttk.Combobox(self, textvariable=self.dist_keyword_dyn_end, font=("Arial", 14))
        self.combo_dist_keyword_dyn_end['values']=('1', '2', '3', '4', '5', '6', '7','8','9','10')
        self.combo_dist_keyword_dyn_end.current(0)
        self.combo_dist_keyword_dyn_end.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.05)
        self.combo_dist_keyword_kin=ttk.Combobox(self, textvariable=self.dist_keyword_kin, font=("Arial", 14))
        self.combo_dist_keyword_kin['values']=('1', '2', '3', '4', '5', '6', '7','8','9','10')
        self.combo_dist_keyword_kin.current(0)
        self.combo_dist_keyword_kin.place(relx=0.7, rely=0.6, relwidth=0.2, relheight=0.05)
        self.combo_dist_keyword_kin_end=ttk.Combobox(self, textvariable=self.dist_keyword_kin_end, font=("Arial", 14))
        self.combo_dist_keyword_kin_end['values']=('1', '2', '3', '4', '5', '6', '7','8','9','10')
        self.combo_dist_keyword_kin_end.current(0)
        self.combo_dist_keyword_kin_end.place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.05)

        #-------------------------------------------------------------Button
        self.button_calc= tk.Button(self, text="calculate VPP", font=self.normal_font,bd=1,bg='white', highlightbackground='black', highlightcolor='navajowhite',activebackground="#e6e3e4")
        self.button_calc.place(relx=0.77, rely=0.9, relwidth=0.2, relheight=0.07)

        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)
#--------------------------------------------------------
#-------------------------------------Page: "Show Results"
class PageResults(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.background=tk.Label(self,bg="white")
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.big_font=font.Font(self, family='Arial', size=25)
        self.normal_font=font.Font(self, family='Arial', size=12)
        self.container_1=tk.Frame(self, bg='white')
        self.container_1.place(relx=0, rely=0.4, relwidth=0.5, relheight=1)
        self.container_2=tk.Frame(self, bg='white')
        self.container_2.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=1)
        self.container_3=tk.Frame(self, bg='white')
        self.container_3.place(relx=0.72, rely=0.4, relwidth=0.25, relheight=1)

        #-------------------------Variable
        self.VPPx1=tk.DoubleVar()
        self.VPPz1=tk.DoubleVar()
        self.R2_1=tk.DoubleVar()
        self.VPPx2=tk.DoubleVar()
        self.VPPz2=tk.DoubleVar()
        self.R2_2=tk.DoubleVar()
        self.CoP=tk.DoubleVar()
        self.Com=tk.DoubleVar()
        self.Fx=tk.DoubleVar()
        self.Fz=tk.DoubleVar()
        self.p_var=tk.DoubleVar()
        self.p_vpp=tk.DoubleVar()
        self.p_kin=tk.DoubleVar()

        #--------------------------------------------------header
        self.label_header=tk.Label(self, text= '5. Results',font=self.big_font,bg='white', anchor='nw')
        self.label_header.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.15)

        #------------------------------------------------first row
        self.label_file=tk.Label(self,font=self.normal_font,bg='lightblue', anchor='nw')
        self.label_file.place(relx=0.05, rely=0.2, relwidth=0.35, relheight=0.05)
        self.label_fp1=tk.Label(self, text= 'Force Plate 1',bg='white',font=self.normal_font, anchor='w')
        self.label_fp1.place(relx=0.3, rely=0.3, relwidth=0.25, relheight=0.05)
        self.label_fp2=tk.Label(self, text= 'Force Plate 2',bg='white',font=self.normal_font, anchor='w')
        self.label_fp2.place(relx=0.5, rely=0.3, relwidth=0.25, relheight=0.05)

        #---------------------------------------------------first column
        self.label_VPPx=tk.Label(self.container_1, text= 'VPPx (m):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_VPPx.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.05)
        self.label_VPPz=tk.Label(self.container_1, text= 'VPPz (m):',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_VPPz.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.05)
        self.label_R2=tk.Label(self.container_1, text= 'R²:',font=self.normal_font,bg='lightgray', anchor='nw')
        self.label_R2.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)

        #---------------------------------------------------------VPP values
        self.l_VPPx1=tk.Label(self.container_1, textvariable= self.VPPx1, font=self.normal_font,bg='lightgray', anchor='center')
        self.l_VPPx1.place(relx=0.55, rely=0, relwidth=0.35, relheight=0.05)
        self.l_VPPz1=tk.Label(self.container_1, textvariable= self.VPPz1,font=self.normal_font,bg='lightgray', anchor='center')
        self.l_VPPz1.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.05)
        self.l_R2_1=tk.Label(self.container_1, textvariable= self.R2_1,font=self.normal_font,bg='lightgray', anchor='center')
        self.l_R2_1.place(relx=0.55, rely=0.2, relwidth=0.35, relheight=0.05)

        self.l_VPPx2=tk.Label(self.container_2, textvariable= self.VPPx2, font=self.normal_font,bg='lightgray', anchor='center')
        self.l_VPPx2.place(relx=0, rely=0, relwidth=0.7, relheight=0.05)
        self.l_VPPz2=tk.Label(self.container_2, textvariable= self.VPPz2,font=self.normal_font,bg='lightgray', anchor='center')
        self.l_VPPz2.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.05)
        self.l_R2_2=tk.Label(self.container_2, textvariable= self.R2_2,font=self.normal_font,bg='lightgray', anchor='center')
        self.l_R2_2.place(relx=0, rely=0.2, relwidth=0.7, relheight=0.05)


        #----------------------------------------------Buttons
        #plot VPP
        self.button_plot_VPP =  tk.Button(self.container_3, text = "plot VPP", font = self.normal_font,bd=1, bg = 'blue',fg='white', highlightbackground='black',activebackground="#e6e3e4")
        self.button_plot_VPP.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        #self.p_vpp = 0

        #plot Input
        self.button_plot = tk.Button(self.container_3, text = "plot GRF, CoP, CoM", font = self.normal_font,bd=1, bg = 'blue',fg='white', highlightbackground='black',activebackground="#e6e3e4")
        self.button_plot.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)
        #self.p_var = 0

        #plot kinematics
        self.button_plot_kin =  tk.Button(self.container_3, text = "plot joints", font = self.normal_font,bd=1, bg = 'blue',fg='white', highlightbackground='black',activebackground="#e6e3e4")
        self.button_plot_kin.place(relx=0, rely=0.2, relwidth=1, relheight=0.05)
        #self.p_kin = 0


        #plot save
        #self.button_save_fig =  tk.Button(self.container_3, text = "save all figures", font = self.normal_font,bd=1,bg = 'blue',fg='white', highlightbackground='black',activebackground="#e6e3e4")
        #self.button_save_fig.place(relx=0, rely=0.5, relwidth=0.7, relheight=0.07)
        #-------------------------------------------
        #button prev, next
        self.button_prev =  tk.Button(self.container_1, text = "<< prev", font = self.normal_font,bd=1,bg = 'lightblue', highlightbackground='black',activebackground="#e6e3e4")
        self.button_prev.place(relx=0.05, rely=0.3, relwidth=0.25, relheight=0.07)
        self.button_next =  tk.Button(self.container_3, text = "next >>", font = self.normal_font,bd=1,bg = 'lightblue', highlightbackground='black',activebackground="#e6e3e4")
        self.button_next.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.07)

        #button back
        self.button_back =  tk.Button(self, text = "<<", font = self.normal_font,bd=1,bg = 'green', highlightbackground='black',activebackground="#e6e3e4")
        self.button_back.place(relx = 0.03, rely = 0.9, relwidth=0.07, relheight=0.07)


#-------------------------------------------------------------------
#-----------PART 2: MAIN VIEW (CALCULATIONS, DATA PROCESSING)--------
#-------------------------------------------------------------------

class MainView(tk.Frame):
    def __init__(self,*args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.normal_font=font.Font(self, family='Arial', size=12)
        self.label_font=font.Font(self, family='Arial', size=30)
        self.entry_font=font.Font(self, family='Arial', size=40)

        #------------------------------------------
        pstart=PageStart(self)
        pkinetic=PageKinetic(self)
        pkinematic1=PageKinematic1(self)
        pkinematic2a=PageKinematic2a(self) #without Com
        pkinematic2b=PageKinematic2b(self) #with Com
        # if pstart.com_output.get() == 2:
        #     pkinematic2=PageKinematic2a(self)
        # else:
        #     pkinematic2=PageKinematic2b(self)
        preadin=PageReadin(self)
        pres=PageResults(self)

        container=tk.Frame(self)
        container.place(relx=0, rely=0, relwidth=1, relheight=1)

        pstart.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pkinetic.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pkinematic1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pkinematic2a.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pkinematic2b.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        preadin.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pres.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #--------------------functions:show pages
        def show_one_file(*args):
            pstart.browseButton_data_dyn.place_forget()
            pstart.browseButton_data_kin.place_forget()
            pstart.browseButton_data.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
            pstart.lift()

        def show_two_files(*args):
            pstart.browseButton_data.place_forget()
            #two separate data files (the order of the files has to fit):
            pstart.browseButton_data_dyn.place(relx=0.15, rely=0.5, relwidth=0.34, relheight=0.1)
            pstart.browseButton_data_kin.place(relx=0.5, rely=0.5, relwidth=0.35, relheight=0.1)
            pstart.lift()
            preadin.label_dist_keyword_dyn.place_forget()
            preadin.combo_dist_keyword_dyn_end.place_forget()

        def show_fp_3(*args): # 3 force plates are default
            pkinetic.container_2.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)
            pkinetic.container_3.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)
            pkinetic.container_4.place_forget()
            pkinetic.lift()

        def show_pkinematic2(*args):
            if pstart.com_output.get() == 2:
                pkinematic2a.lift()
            else:
                pkinematic2b.lift()

        #-----------------initialisation "show pages"
        pstart.radio_number_files_1['command']=show_one_file
        pstart.radio_number_files_2['command']=show_two_files
        show_fp_3()
        pstart.lift() #Start

        #---------------------------------------------------------
        #---------------------------read in data: initialisation
        pres.ListeFiles=[]
        pres.ListeFiles_kin=[]
        pres.ListeVPP=[0]
        pres.ListeVPP[0]=['name of kinetic file','Force plate number' '\t' 'VPPx (m)' '\t'  'VPPz (m)' '\t' 'R^2']
        pres.count = 0

        #----------------------------BUTTONS------------------------
        # green buttons with arrows:
        pstart.button_forward['command']=pkinetic.lift
        pkinetic.button_back['command']=pstart.lift
        pkinetic.button_forward['command']=pkinematic1.lift

        pkinematic2a.button_forward['command']=preadin.lift
        pkinematic2b.button_forward['command']=preadin.lift
        pkinematic1.button_back['command']=pkinetic.lift
        pkinematic2a.button_back['command']=pkinematic1.lift
        pkinematic2b.button_back['command']=pkinematic1.lift

        pkinematic1.button_forward['command']=show_pkinematic2
        preadin.button_back['command']=show_pkinematic2
        pres.button_back['command']=preadin.lift
        #----------------------------------------------
        #lambda: that the buttons just work when pressed and not at initialisation

        pstart.browseButton_data['command']=lambda: calcReadInData.readData(preadin)
        #pstart.browseButton_data_kin['command']=calcReadInData.readData_kin(self)
        pstart.browseButton_data_dyn['command']=lambda: calcReadInData.readData(self)
        pstart.browseButton_ini['command']=lambda: calcInput.readIni(preadin,pres,pkinetic,pkinematic1,pkinematic2a,pkinematic2b)
        pstart.Button_skip['command']=lambda: calcButtons.show_calc1(pres,pstart,pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b,pres.ListeFiles,pres.ListeVPP)
        preadin.button_calc['command']=lambda: calcButtons.show_calc1(pres,pstart,pkinetic,preadin,pkinematic1,pkinematic2a,pkinematic2b,pres.ListeFiles,pres.ListeVPP)
        pres.button_next['command']=lambda: calcButtons.nextVPP(pres,pstart,preadin, pkinematic1, pkinematic2a,pkinematic2b, pkinetic,pres.ListeFiles)
        pres.button_prev['command']=lambda: calcButtons.prevVPP(pres,pstart,preadin, pkinematic1, pkinematic2a,pkinematic2b, pkinetic,pres.ListeFiles)
        #pres.button_save_fig['command']=lambda: calcButtons.save_figures(pres,pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin)
        pres.button_plot['command']=lambda: calcButtons.plot_input(pres)
        pres.button_plot_VPP['command']=lambda: calcButtons.plot_vpp(pres, pstart,pkinematic1, pkinematic2a,pkinematic2b,preadin)
        pres.button_plot_kin['command']=lambda: calcButtons.plot_kin(pres)

#--------------------------------------------------------------------------------
#-------------ROOT MAINLOOP------------------------------------------------------
#--------------------------------------------------------------------------------

if __name__ == "__main__":
    def full(event):
        root.wm_attributes('-fullscreen', True)
    def small(event):
        root.wm_attributes('-fullscreen', False)
        root.wm_geometry("700x500")
    def plot_kill_all():
        plt.close('all')
        root.destroy()

    root=tk.Tk()
    main=MainView(root)
    root.title("VPP calculation tool")
    main.place(relwidth=1, relheight=1, relx=0, rely=0)
    root.wm_geometry("700x500+20+30")
    #delete the following if figures should not be closed with closing main window:
    root.protocol('WM_DELETE_WINDOW', plot_kill_all)
    root.mainloop()

