import pandas as pandas
import numpy as np 
import h5py as h5
from scipy.interpolate import RegularGridInterpolator as rgi 

extmapfile=h5.File('../Data/stilism_cube.h5','r')

extmapgroup=extmapfile['stilism']

extmap=extmapgroup['cube_datas']

extmap=np.array(extmap[:,:,:])

x = np.linspace(-1997.5, 1997.5, 800)
y = np.linspace(-1997.5, 1997.5, 800)
z = np.linspace(-297.5, 297.5, 120)

def ext_calc(l, b, d, npoints=100):
	t = np.linspace(0, 1, npoints)
	star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	
	if star_pos[0] > 1997.5:
		d = 1997.49/(np.cos(b*np.pi/180)*np.cos(l*np.pi/180))
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	if star_pos[0] < -1997.5:
		d = -1997.49/(np.cos(b*np.pi/180)*np.cos(l*np.pi/180))
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	if star_pos[1] > 1997.5:
		d = 1997.49/np.cos(b*np.pi/180)*np.sin(l*np.pi/180)
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	if star_pos[1] < -1997.5:
		d = -1997.49/np.cos(b*np.pi/180)*np.sin(l*np.pi/180)
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	if star_pos[2] > 297.5:
		d = 297.49/np.sin(b*np.pi/180)
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	if star_pos[2] < -297.5:
		d = -297.49/np.sin(b*np.pi/180)
		star_pos = d*np.array([np.cos(b*np.pi/180)*np.cos(l*np.pi/180),np.cos(b*np.pi/180)*np.sin(l*np.pi/180),np.sin(b*np.pi/180)])
	
	interpolation_points=np.array([star_pos[0]*t,star_pos[1]*t,star_pos[2]*t]).transpose()

	interpolator=rgi((x,y,z), extmap)

	interpolated_vals=interpolator(interpolation_points)

	extout=sum(interpolated_vals)*(d/npoints)
    
	return extout
    