"""
Dictionary of masking parameters for keplerian_mask experiments.
January 2024 (for addressing ApJL referee question)
"""


mask_dict = {}

mask_dict['fiducial'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

########################################
#### VARYING EMISSION SURFACE SLOPE ####
########################################

mask_dict['zr_25'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.25,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['zr_50'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.50,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

################################################################
#### VARYING EMISSION SURFACE SLOPE WITH HIGHER INCLINATION ####
################################################################

mask_dict['zr_25_inc45'] =         {
                                'image': None,
                                'inc': 45.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.25,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['zr_50_inc45'] =         {
                                'image': None,
                                'inc': 45.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.50,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

##########################################
#### VARYING LINE WIDTH NORMALIZATION ####
##########################################

mask_dict['dV0_100'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 100.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['dV0_600'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 600.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

#############################
#### VARYING INCLINATION ####
#############################

mask_dict['inc_45'] =         {
                                'image': None,
                                'inc': 45.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['inc_70'] =         {
                                'image': None,
                                'inc': 70.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': 0.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

##################################
#### VARYING LINE WIDTH SLOPE ####
##################################

mask_dict['dVq_05'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': -0.5,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['dVq_10'] =         {
                                'image': None,
                                'inc': 20.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': -1.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

##########################################################
#### VARYING LINE WIDTH SLOPE WITH HIGHER INCLINATION ####
##########################################################

mask_dict['dVq_05_inc45'] =         {
                                'image': None,
                                'inc': 45.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': -0.5,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

mask_dict['dVq_10_inc45'] =         {
                                'image': None,
                                'inc': 45.0,
                                'PA': 0.0,
                                'mstar': 1.0,
                                'dist': 150.0,
                                'vlsr': 5.e3,
                                'zr': 0.0,
                                'dV0': 300.0,
                                'dVq': -1.0,
                                'r_min': 0.0,
                                'r_max': 4.0,
                                'restfreqs': ['230.580GHz'],
                                'estimate_rms': False,
                                }

