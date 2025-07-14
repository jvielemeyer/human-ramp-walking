# Calculation


The file main_calculation.py creates a GUI. The GUI is created to calculate the Virtual Pivot Point (VPP) easily. Until now, it is only tested on Linux. If there are problems in other operating systems, please contact me (johanna.vielemeyer@uni-jena.de) or optimize the code by yourself.


## You need:
1. software: python3
	- packages:
		- configparser
		- matplotlib.pyplot
		- numpy
		- os
		- scipy
		- sys
		- tkinter
2. code files:
	- main_calculation.py
	- initialization files
		- anthropometrics.ini
		- measurement_system.ini
	- folder “calculation” includes
		- calcButtons.py
		- calcCoM.py
		- calcInput.py
		- calcPlot.py
		- calcReadInData.py
		- calcSave.py
		- calcVPP.py
3. data folder: “Data_Level_1”
	- raw data in .txt
 	- here you find an example of 3 files
	- the whole dataset can be found at the figshare repository; please download the folder from there and save it as "Data_Level_1" in the main folder, where "main_calculation.py" is stored
	
      
## Start 

Start in terminal with the following input:

`cd *location of main_calculation.py*`

`python3 main_calculation.py`

## Explanation

- main_calculation.py creates VPP calculation tool GUI
- everything is prepared for the analysis, it is not necessary (but easily possible) to change parameters in the GUI and in the ini-files
- short explanation of the VPP calculation tool GUI (for long version, see the document “documentation”)
	1. first page: 
		1. click on “Load initialization file…” to load the files
		2. click on “Load data files…” to load all data files from the folder “Data_Level_1”
		3. click on “skip configuration” if you do not want to change input parameters or click on the green arrow to change input parameters
	2. result page
		- you get VPP (x,z) position and R² for each single file you loaded in (with “prev” and “next” you can switch between the results of the single files)
		- “plot VPP” creates VPP plot in a CoM-centered coordinate frame for the chosen trial
		- “plot GRF, CoP, CoM” creates single curves of the x and z component of the parameters for the first and second contact (single and double support phases are illustrated separately) for the chosen trial
		- “plot joints” creates single curves of head and thorax angle; shoulder and elbow angle of ipsi- and contralateral join; hip, knee, and ankle joint angle/moment/power for the ipsi- and contralateral joint for the chosen trial
	3. the program creates 
		- “VPP_Data.csv” with all VPP data in one file
		- folder “Data_Level_2” with compressed data (.npz) for visualization


# Visualization

## You need:
1.  software: python3
	- packages:
		- matplotlib.pyplot
		- numpy
		- os
		- sys
2. code files:
	- main_visualization.py
	- folder “visualization” includes
		-  “mean_calc.py” (calculate mean values over trials and subjects)
		- “plot_all.py” (plot routine to plot all single trials)
		-  “plot_means.py” (plot  mean curves over trials and subjects)
3. data folder: “Data_Level_2”
	- data compressed as .npz
 	- could be created by VPP calculation tool GUI, see paragraph “calculation”, or can be downloaded from the figshare repository
  	- note: you need at least data of two participants to build mean values for plotting 
      
## Start in terminal with the following input:

`cd *location of main_visualization.py*`

`python3 main_visualization.py`

main_visualization.py contains (please uncomment the part that you need in the main file):
1. kinematics
	- calculate mean values
	- plot mean values (angles, moments, power)
	- plot single trials (upper body, lower body)
2. kinetics
	- calculate mean values
	- plot mean values
3. VPP
	- calculate mean values
	- boxplot
	- scatter plot
4. walking speed
	- calculate mean values


