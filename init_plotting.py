
import pylab as pyl
import matplotlib

"""Scripts for preparing nice plots."""

def init_plotting(font_size=12):
    matplotlib.rc('font', family='sans-serif') 
    matplotlib.rc('font', **{'sans-serif' : 'Arial','family' : 'sans-serif'})
    matplotlib.rc('text', usetex='false') 
    matplotlib.rcParams.update({'font.size': font_size})
    pyl.rcParams['axes.labelsize'] = pyl.rcParams['font.size']
    pyl.rcParams['xtick.labelsize'] = pyl.rcParams['font.size']
    pyl.rcParams['ytick.labelsize'] = pyl.rcParams['font.size']
    pyl.rcParams['xtick.major.size'] = 3
    pyl.rcParams['xtick.minor.size'] = 3
    pyl.rcParams['xtick.major.width'] = 0.75
    pyl.rcParams['xtick.minor.width'] = 0.75
    pyl.rcParams['ytick.major.width'] = 0.75
    pyl.rcParams['ytick.minor.width'] = 0.75
    pyl.rcParams['xtick.major.pad'] = 2
    pyl.rcParams['ytick.major.pad'] = 2
    pyl.rcParams['axes.linewidth'] = 0.75
    matplotlib.rc('pdf', fonttype=42) 


def set_axes_bottom_left():
    pyl.gca().spines['right'].set_color('none')
    pyl.gca().spines['top'].set_color('none')
    pyl.gca().xaxis.set_ticks_position('bottom')
    pyl.gca().yaxis.set_ticks_position('left')
    pyl.gca().yaxis.set_tick_params(which='both',right='off', width=0.75, length=3)
    pyl.gca().xaxis.set_tick_params(which='both', top='off', width=0.75, length=3)
