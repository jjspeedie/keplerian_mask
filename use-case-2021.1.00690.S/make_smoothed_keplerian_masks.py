'''
ALMA Program ID: 2021.1.00690.S (PI: R. Dong)
reducer: J. Speedie

Quick script to make spectrally smoothed Keplerian/anti-Keplerian masks from
existing (top hat) ones.
'''

import sys, os
import numpy as np
from astropy.io import fits
from scipy.ndimage import gaussian_filter


molecule         = '12CO'
robust           = 'robust0.0' # 'robust1.5' # 'robust0.0'
vres_version     = 'v12' # 'v12'
extension        = '.clean.keplerian_mask.fits'
new_extension    = '.clean.smooth_keplerian_mask.fits'
sigma_channels   = 5 # width of gaussian filter in units of number of channels

maskname         = '../cvpost_copy/images_lines/'+molecule+'/'+vres_version+'_'+robust+'/ABAur_'+molecule+extension
new_maskname     = '../cvpost_copy/images_lines/'+molecule+'/'+vres_version+'_'+robust+'/ABAur_'+molecule+new_extension

if not os.path.isfile(new_maskname):
    print("Creating a copy of mask: "+new_maskname)
    os.system('cp '+maskname+' '+new_maskname)

hdul = fits.open(new_maskname)

print("Data shape: ", hdul[0].data.shape)

print("Smoothing along the velocity axis by "+str(sigma_channels)+" channels...")

for y_ind in np.arange(0, hdul[0].data.shape[1], 1):
    hdul[0].data[:, y_ind, :] = gaussian_filter(hdul[0].data[:, y_ind, :], sigma=sigma_channels)

for x_ind in np.arange(0, hdul[0].data.shape[2], 1):
    hdul[0].data[:, :, x_ind] = gaussian_filter(hdul[0].data[:, :, x_ind], sigma=sigma_channels)

hdul.writeto(new_maskname, overwrite=True)

hdul.close()
print("Done!")






sys.exit()
