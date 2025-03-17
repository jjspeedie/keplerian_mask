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

##################################
#### MIMICKING SPECIFIC DISKS ####
##################################

mask_dict['PDS70'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                            'image': None,
                            'inc': 51.7,
                            'PA': 160.4,
                            'mstar': 0.875,
                            'dist': 113.,
                            'vlsr': 5.5e3,
                            'zr': 0.25,
                            'dV0': 300.0,
                            'dVq': 0.0,
                            'r_min': 0.0,
                            'r_max': 2.0,
                            'restfreqs': ['230.580GHz'],
                            'estimate_rms': False,
                            'max_dzr': 0.25
                            }

mask_dict['PDS70_max_dzr_0.01'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                        'image': None,
                                        'inc': 51.7,
                                        'PA': 160.4,
                                        'mstar': 0.875,
                                        'dist': 113.,
                                        'vlsr': 5.5e3,
                                        'zr': 0.25,
                                        'dV0': 300.0,
                                        'dVq': 0.0,
                                        'r_min': 0.0,
                                        'r_max': 2.0,
                                        'restfreqs': ['230.580GHz'],
                                        'estimate_rms': False,
                                        'max_dzr': 0.01
                                        }
mask_dict['PDS70_max_dzr_0.25'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                        'image': None,
                                        'inc': 51.7,
                                        'PA': 160.4,
                                        'mstar': 0.875,
                                        'dist': 113.,
                                        'vlsr': 5.5e3,
                                        'zr': 0.25,
                                        'dV0': 300.0,
                                        'dVq': 0.0,
                                        'r_min': 0.0,
                                        'r_max': 2.0,
                                        'restfreqs': ['230.580GHz'],
                                        'estimate_rms': False,
                                        'max_dzr': 0.25
                                        }

mask_dict['PDS70_max_dzr_0.25_fs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.25, 
                                            'frontside_only':True
                                            }

mask_dict['PDS70_max_dzr_0.25_bs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.25, 
                                            'backside_only':True
                                            }

mask_dict['PDS70_zr0.25_max_dzr0.25_min_zr0.0_fs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.25, 
                                            'min_zr': 0.0, 
                                            'frontside_only':True
                                            }

mask_dict['PDS70_zr0.25_max_dzr0.25_min_zr0.0_bs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.25, 
                                            'min_zr': 0.0, 
                                            'backside_only':True
                                            }

mask_dict['PDS70_zr0.25_max_dzr0.0049_min_zr0.245_fs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.0049, 
                                            'min_zr': 0.245, 
                                            'frontside_only':True
                                            }

mask_dict['PDS70_zr0.25_max_dzr0.0049_min_zr0.245_bs'] =       { # Kepler et al. (2019), Rampinelli et al. (2024)
                                            'image': None,
                                            'inc': 51.7,
                                            'PA': 160.4,
                                            'mstar': 0.875,
                                            'dist': 113.,
                                            'vlsr': 5.5e3,
                                            'zr': 0.25,
                                            'dV0': 300.0,
                                            'dVq': 0.0,
                                            'r_min': 0.0,
                                            'r_max': 2.0,
                                            'restfreqs': ['230.580GHz'],
                                            'estimate_rms': False,
                                            'max_dzr': 0.0049, 
                                            'min_zr': 0.245, 
                                            'backside_only':True
                                            }