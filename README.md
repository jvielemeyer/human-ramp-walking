# Calculation


The file main_calculation.py creates a GUI. The GUI is developed to calculate the Virtual Pivot Point (VPP) easily. If there are problems, please contact me (johanna.vielemeyer@uni-jena.de) or optimize the code by yourself.


## You need:
1. software: python3
	- packages:
		- configparser
		- matplotlib.pyplot
		- numpy
		- os
		- scipy
		- tkinter
2. code files:
	- _main_calculation.py_
	- initialization files
		- _anthropometrics.ini_
		- _measurement_system.ini_
	- folder “calculation” includes
 		- *\_\_init__.py*
		- _calcButtons.py_
		- _calcCoM.py_
		- _calcInput.py_
		- _calcPlot.py_
		- _calcReadInData.py_
		- _calcSave.py_
		- _calcVPP.py_
3. data folder: “Data_Level_1”
	- raw data in .txt
 	- here you find an example (all trials of one participant)
	- the whole dataset can be found at the figshare repository; please download the folder from there and save it as "Data_Level_1" in the main folder, where _main_calculation.py_ is stored
	
      
## Start 

Start in terminal with the following input:

`cd location of main_calculation.py`

`python3 main_calculation.py`

## Explanation

- _main_calculation.py_ creates VPP calculation tool GUI
- everything is prepared for the analysis, it is not necessary (but easily possible) to change parameters in the GUI and in the ini-files
- short explanation of the VPP calculation tool GUI (for long version, see the file _Documentation_gui.pdf_)
	1. first page: 
		- click on “skip configurations” if you do NOT want to change input parameters (recommended) or
		- click on “adjust configuration” if you want to change parameters
	2. result page
		- you get VPP (x,z) position and R² for each single file you loaded in (with “prev” and “next” you can switch between the results of the single files)
		- “plot VPP” creates VPP plot in a CoM-centered coordinate frame for the chosen trial
		- “plot GRF, CoP, CoM” creates single curves of the x and z component of the parameters for the first and second contact (single and double support phases are illustrated separately) for the chosen trial
		- “plot joints” creates single curves of head and thorax angle; shoulder and elbow angle of ipsi- and contralateral join; hip, knee, and ankle joint angle/moment/power for the ipsi- and contralateral joint for the chosen trial
	3. the program creates 
		- _VPP_Data.csv_ with all VPP data in one file
		- folder “Data_Level_2” with compressed data (.npz) for visualization


# Visualization

## You need:
1.  software: python3
	- packages:
		- matplotlib.pyplot
		- numpy
		- os
2. code files:
	- _main_visualization.py_
	- folder “visualization” includes
		- _mean_calc.py_ (calculate mean values over trials and subjects)
		- _plot_all.py_ (plot routine to plot all single trials)
		- _plot_means.py_ (plot mean curves over trials and subjects)
3. data folder: “Data_Level_2”
	- data compressed as .npz
 	- could be created by VPP calculation tool GUI, see paragraph “calculation”, or can be downloaded from the figshare repository
  	- note: you need at least one file for each setting to create the plots
      
## Start in terminal with the following input:

`cd location of main_visualization.py`

`python3 main_visualization.py`

_main_visualization.py_ contains (please uncomment the part that you need in the main file):
1. kinematics
	- calculate mean values
	- plot mean values (angles, moments, power)
	- plot single trials (upper body, lower body)
2. kinetics
	- calculate mean values
	- plot mean values
3. VPP
	- calculate mean values
	- scatter plot
4. walking speed
	- calculate mean values


