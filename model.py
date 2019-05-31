from __future__ import division
import numpy as np

from neuron import h, nrn
import neuron
import pylab as pyl

import params
import sec
import sim
import init_plotting


class NewNeuron(object):
    
    def __init__(self, Lhill):
        ''' create a new neuron'''
        self.makeSoma()
        self.makeDend()
        self.makeHill(Lhill)
        self.makeAis()
        self.makeAxon()
        
#-------- generate compartments and connect them together --------------    
    def makeSoma(self):
        self.soma = sec.NewSection("soma")
        self.soma.set_memb()
        self.soma.set_geom(length=params.L_soma, diameter=params.diam_soma, nseg=params.nseg_soma)
        self.soma.set_passive()
        self.soma.set_na3(gna_max=params.gna_soma)
        self.soma.set_active_k(gk_max=params.gk_soma)
        
    def makeDend(self): #dendrite
        self.dend = sec.NewSection("dend")
        self.dend.set_memb()
        self.dend.set_geom(length=params.L_dend, diameter=params.diam_dend, nseg=params.nseg_dend)
        self.dend.set_passive()
        self.dend.set_na3(gna_max=params.gna_dend)
        self.dend.set_active_k(gk_max=params.gk_dend)
        #connect it
        self.dend.connect(self.soma,0,1) #connect dend(1), soma(0)

    def makeHill(self, Lhill):
        self.hill = sec.NewSection("hill")
        self.hill.set_geom(length=Lhill, diameter=params.diam_hill, nseg=params.nseg_hill)
        self.hill.set_memb()
        self.hill.set_passive()
        self.hill.set_na3(gna_max=params.gna_hill)
        self.hill.set_active_k(gk_max=params.gk_hill)
        #connect it
        self.hill.connect(self.soma,1,0) #connect hill(0), soma(1)

        
    def makeAis(self):
        self.ais = sec.NewSection("ais")
        self.ais.set_memb()
        self.ais.set_geom(length=params.L_ais, diameter=params.diam_ais, nseg=params.nseg_ais)
        self.ais.set_passive()
        self.ais.set_nax(gna_max=params.gna_ais)
        self.ais.set_active_k(gk_max=params.gk_ais)
        #connect it
        self.ais.connect(self.hill,1,0) #connect hill(1), ais(0)


    def makeAxon(self):
        self.axon = sec.NewSection("axon")
        self.axon.set_memb()
        self.axon.set_geom(length=params.L_axon, diameter=params.diam_axon, nseg=params.nseg_axon)
        self.axon.set_passive()
        self.axon.set_nax(gna_max=params.gna_axon)
        self.axon.set_active_k(gk_max=params.gk_axon)
        #connect it
        self.axon.connect(self.ais,1,0) #connect ais(1), axon(0)


#------------------ insert simulation ----------------------------------   
    def insert_simulation(self, location):
        self.simulation = sim.Simulation(h.allsec())
        self.simulation.set_time_recording() 
        for sec in self.simulation.recordingList:    
            sec.set_recording(location)
    
            
#---------------- plot the output --------------------------------------   

    def plot_soma_ais(self, stim_list):
        '''Plot Voltage and dV/dt of soma & AIS for different stimulus strength'''
        #Prepare the plot
        init_plotting.init_plotting(font_size=10)
        fig1 = pyl.figure(1)
        fig1_1 = fig1.add_subplot(221)
        init_plotting.set_axes_bottom_left()
        fig1_2 = fig1.add_subplot(223)
        init_plotting.set_axes_bottom_left()
        
        self.insert_simulation(location=0.5)
        colors=["orangered","darkred","gold"]

        for index, item in enumerate(stim_list):
            print "Iinj =", item, "nA"
            self.simulation.insert_IClamp(location = self.soma(0.5), delay=params.delay, amp = item, dur = params.dur)
            self.simulation.run_neuron()
            
            time = self.simulation.times
            vtrace=np.array(self.soma.voltage).flatten()
            vtraceAIS=np.array(self.ais.voltage).flatten()

            fig1_1.plot(time, vtrace, color=colors[index])
            fig1_1.plot(time, vtraceAIS, color =colors[index], linestyle="dashed")

            dv= self.dv_dt(vtrace) 
            dvAIS= self.dv_dt(vtraceAIS)
            
            fig1_2.plot(vtrace[: len(dv)], dv, color=colors[index])
            fig1_2.plot(vtraceAIS[: len(dvAIS)], dvAIS,linestyle="dashed", color=colors[index]) 

        fsize = 10
        fig1_1.set_xlabel("Time [ms]", fontsize=fsize)
        fig1_1.set_ylabel("Voltage [mV]", fontsize=fsize)
        fig1_2.set_xlabel("Voltage [mV]", fontsize=fsize)    
        fig1_2.set_ylabel("dV/dt [V/s]", fontsize=fsize)   
        
        #format the plot    
        pyl.figure(1)
        fig1_1.set_xlim(95,115)
        fig1_1.set_ylim(-90,60)
        xtick_positions = range(-80,61,20) 
        xtick_labels = [-80, "", -40, "", 0, "",40,""]
        ytick_positions = range(-100, 701,100) 
        ytick_labels = ["", 0, "", 200, "",400, "",600,""]
        xtick_positions_t = [95,100,105,110,115] 
        xtick_labels_t = [0,"",10,"",20]
        fig1_1.set_xticks(xtick_positions_t, minor=False)
        fig1_1.set_xticklabels(xtick_labels_t)
        fig1_1.set_yticks(xtick_positions, minor=False)
        fig1_1.set_yticklabels(xtick_labels)
        fig1_2.set_xticks(xtick_positions, minor=False)
        fig1_2.set_xticklabels(xtick_labels)
        fig1_2.set_yticks(ytick_positions, minor=False)
        fig1_2.set_yticklabels(ytick_labels)
        fig1_1.set_title("Iinj = 0.5 nA (yellow), 0.8 nA (red), 1.3 nA (orange) \n Soma (solid) and AIS (dashed)")

        pyl.show()

   
#--------------------- helper functions --------------------------------
    def dv_dt(self, vtrace): 
        '''2-point first order finite difference to estimate dV/dt '''
        dt = params.h.dt
        dv = []
        for i in range(1, len(vtrace)-2): 
            dv.append((vtrace[i+1]-vtrace[i-1])/(2*dt))
        return dv
