from solo_epd_loader import *
import os

startdate = 20220505
path = os.getcwd() + "/data/"
sensor = 'ept'
df_protons, df_electrons, dict_energies = epd_load(sensor=sensor, startdate=startdate, viewing='sun', autodownload=True, only_averages=True)

print("df_protons columns for EPT:")
for column in df_protons.columns:
    print(column)

print("energies dictionary for EPT:")
print(dict_energies)
