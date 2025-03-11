#################################################
#### COLLECTION OF OPERATIONS FOR CASA 6.4.1 ####
#################################################
"""
Copy and paste the following into a CASA terminal.
"""

from astropy.io import fits

execfile('./keplerian_mask.py') # also imports numpy as np
execfile('./kepmasks_dict.py') # loads mask_dict

xaxis = np.linspace(7.5, -7.5, 301)[::-1]
yaxis = np.linspace(-7.5, 7.5, 301)
saxis = np.zeros(1)
vaxis = np.arange(0e3, 10.001e3, 50) # offsets

# Iterate through the masks in mask_dict
for key in mask_dict.keys():

    # Make mask
    mask = make_mask(x_axis=xaxis,
                    y_axis=yaxis,
                    s_axis=saxis,
                    v_axis=vaxis,
                    **mask_dict[key])

    # Drop the third axis (dropstokes) & Make velax the first axis
    mask = np.squeeze(mask, axis=2)
    mask = np.moveaxis(mask, -1, 0)

    # Save the mask as a FITS file
    fits_filename    = './masks/'+key+'.fits'
    hdu              = fits.PrimaryHDU(mask.astype(int))
    hdul             = fits.HDUList([hdu])
    hdul.writeto(fits_filename, overwrite=True)
    print(f"Mask saved as {fits_filename}")

