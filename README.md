# OctTB_HGCAL_Simulation
This Repository is contain the code needed to generate sim samples with HGCAL TB geometry (CMSSW_10_6_0_pre4) 

This does not work after running scram b 
For this to work, you should follow the instructions give in this gDoc [1] and make sure you have same scripts as to this directory
[1]https://docs.google.com/document/d/1zAFqpzQOyw8Z0EhdXiE8CaVq7JZ0pNujxyCJL55VvOk/edit?usp=sharing


## Instructions to run the reconstruction machinery (including general interaction mode + condor job submission)

Read the README.md file present in the "GenSimOctober2018_ProtoWorkflow"

# important points to remember
Sequence of the steps to set up the environment
cd CMSSW_*/src
cmsenv
./setup.sh //// Need	to change the directory path in	setup.sh to your working area
export PYTHONPATH=<path to GenSimOctober2018_ProtoWorkflow>:$PYTHONPATH
pip install --user luigi   // to install needed luigi packages

// You should change the path of simulated samples in the simulateSamples.py file 