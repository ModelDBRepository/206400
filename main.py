'''
Run this file to generate voltage and dV/dt traces as shown in Fig 3B and S2 B
of the publication Michalikova et al. (2016).
Vary the parameters Iinj_list and L_hill to change the amplitude of the 
injected current and the distance between the soma and the AIS. 
'''

import model

Iinj_list = [1.3, 0.8, 0.5] #Current clamp amplitude [nA]

L_hill = 100 #100: to generate spikelets, sh-APs and fb-APs (default value: 30)

Nr1 = model.NewNeuron(Lhill=L_hill)

Nr1.plot_soma_ais(stim_list=Iinj_list)

