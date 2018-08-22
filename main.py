# -*- coding: utf-8 -*-

# Import external libraries
from hapi import absorptionCoefficient_Lorentz, transmittanceSpectrum, fetch
from numpy import savetxt, shape, array

# Spectral range of interest - um
lmin = 2.0              # min wavelength
lmax = 3.0              # max wavelength
kmin = 10**4/lmax       # min wavenumber
kmax = 10**4/lmin       # max wavenumber

# Molecular species of interest
nmol = 'H2O'

# Fetch the HITRAN data for the molecule of interest
fetch(nmol, 1, 1, kmin, kmax)

# Compute the absorption/extinction coefficient - cm^-1
kmat, abscoeff = absorptionCoefficient_Lorentz(SourceTables = nmol, \
                                               WavenumberStep = 0.5, \
                                               HITRAN_units = False)

# Process the data to be exported
data = array([10**4/kmat * 1000, abscoeff]).T
data = data[::-1]

# Export the processed data
filename = './Data/abscoeff' + nmol + '.txt'
savetxt(filename, data, fmt = ['%.4E', '%.4E'])

# End of file
print('END!')