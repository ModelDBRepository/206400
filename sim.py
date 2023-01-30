# -*- coding: iso-8859-1 -*-


from numpy import * # zeros, where, diff
from matplotlib.pyplot import *

import params
import model


import neuron
from neuron import hclass, h, nrn
import pylab as pyl


class Simulation(object):
    def __init__(self, recordingList):
        ''' Stimulation with one electrode and registration of voltage at several other.'''
        self.recordingList = recordingList 


    def run_neuron(self):
        h('celsius = {0}'.format(params.temperature))
        neuron.h.finitialize(params.v_init)
        neuron.h.fcurrent() 
        while h.t < params.tstop:
            h.fadvance()    
        self.get_recording()       

    
    def insert_IClamp(self, location = params.electrodeLocation, delay=params.delay, amp = params.amp, dur = params.dur):
        self.stim = h.IClamp(location)
        self.stim.delay = delay
        self.stim.amp = amp
        self.stim.dur = dur
        
    def get_recording(self):
        self.times = array(self.rec_t)     # alternativ to `list(rec_t)`: `numpy.array(rec_t)`
        for compartment in self.recordingList:
            compartment.voltage = []
            compartment.voltage.append(compartment.rec_v)

    def set_time_recording(self):
        self.rec_t = h.Vector()
        self.rec_t.record(h._ref_t)   



