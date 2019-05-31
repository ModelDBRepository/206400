from neuron import h

#--------------------- morphology --------------------------------------
# soma
L_soma = 40         
diam_soma = 20      
nseg_soma = 5  
   
# hill 
diam_hill = 1
nseg_hill = 5

# ais
L_ais = 30
diam_ais = 1
nseg_ais = 11

# axon
L_axon = 1000
diam_axon = 1
nseg_axon = 51

# dendrite
L_dend = 900     
diam_dend = 6
nseg_dend = 21

#--------------------- simulation control ------------------------------
h.dt = 0.025
tstop = 120
v_init = -70 

#-----------------------------------------------------------------------
#-----------------reversal potentials etc.------------------------------
#-----------------------------------------------------------------------
V_rest = v_init 
E_na   = 55  
E_k    =-90  
E_pas = v_init

temperature = 37.

#-------------------passive properties----------------------------------
r_a = 150      # Ohm*cm; 
c_m = 1   # microF/cm^2
r_m = 10000  # Ohm*cm^2
gpas = 1./r_m  # S/cm^2 

#---------------------active properties---------------------------------
# all conductance densities in S/cm^2 
#defaults
gna = 0.02 
gka = 0
gkdr =0.05

# soma
gna_soma =gna
gk_soma = gkdr

# dend
gna_dend = gna
gk_dend = gk_soma

# hill
gna_hill = 2*gna
gk_hill = 5*gkdr

# ais
gna_ais = 5 *gna
gk_ais = 5*gkdr

# axon
gna_axon = 2*gna
gk_axon = 2.5*gkdr

# VSHIFT of activation & inactivation curves
#somato-dendritic channels
na3_shm = 5
na3_shh = na3_shm
#axonal channels
nax_shm = -5
nax_shh = nax_shm

#----------------------- input -----------------------------------------
recording_location=0.5 
electrodeLocation = "soma(.5)"
delay = 100.
dur = 15
amp = 0

