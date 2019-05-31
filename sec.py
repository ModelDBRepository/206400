from neuron import h, nrn
import neuron

import params


class NewSection(nrn.Section):
    
    def __init__(self, SectionName='noName'):
        '''  Inherited from NEURON class Section'''
        nrn.Section.__init__(self, name = SectionName)    # Using the init of the parent
        self.SectionName = SectionName
        self.voltage = []
    
    def set_geom(self, length=1, diameter=1, nseg=1):
        '''Set length, diameter and nseg.'''
        self.L = length
        self.diam = diameter
        self.nseg = nseg
    
    def set_memb(self):
        '''Set cytoplasmic resistivity and membrane conductance.'''
        self.Ra = params.r_a
        self.cm = params.c_m
            
    def set_passive(self):
        '''Set passive membrane properties.'''
        self.insert("pas")
        for seg in self:
            seg.pas.g = params.gpas
            seg.pas.e = params.E_pas
    
    def set_na3(self, gna_max):
        ''' Insert the high-threshold sodium conductance.'''
        self.insert("na3")   
        for seg in self:
            na_channel = seg.na3
            na_channel.gbar = gna_max
            na_channel.sh = params.na3_shm #vshift of activation curve
            na_channel.shx = params.na3_shh #vshift of inactivation curve
            seg.ena = params.E_na
       
    def set_nax(self, gna_max, E_na=params.E_na): 
        ''' Insert the high-threshold sodium conductance.'''
        self.insert("nax")   
        for seg in self:
            na_channel = seg.nax
            na_channel.gbar = gna_max
            na_channel.sh = params.nax_shm #vshift of activation curve
            na_channel.shx = params.nax_shh #vshift of inactivation curve
            seg.ena = params.E_na        
            
                
    def set_active_k(self, gk_max): 
        ''' Insert active potassium conductance.'''
        self.insert("kdr")  
        for seg in self:
            k_channel = seg.kdr
            k_channel.gbar = gk_max
            seg.ek = params.E_k
         

    def set_recording(self, location): 
        self.rec_v = h.Vector()     
        self.rec_v.record(self(location)._ref_v)
        
