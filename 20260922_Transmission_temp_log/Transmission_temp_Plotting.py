import numpy as np
import matplotlib.pyplot as plt
import csv

file_path = "Transmission_temp_log.csv"

weed_out = False # Toggle to produce the plot that helps us weed out bad data.

# Read in the data:
data = np.loadtxt(file_path, delimiter=',').T
timestamp = data[0]
central_temp = data[1]
tran_plus = data[2]
tran_minus = data[3]
tran_max = data[4]
amb_temp = data[5]
air_pressure = data[6]

timestamp -= timestamp[0]
timestamp = timestamp/60/60

# Weed out the data:
idx = np.arange(len(timestamp))
include = np.ones(len(timestamp), dtype=bool)
include[:13] = False
include[127:146] = False
include[421:434] = False
include[861:887] = False
include[1047:1061] = False
include[1122:1130] = False
include[1649:1666] = False
include[1710] = False
include[1899:1912] = False
include[1957:1974] = False
include[2470:2555] = False
include[2625:2650] = False
include[2726:2766] = False
include[2877:2952] = False
include[3038:3060] = False
include[3068] = False
include[3096:3111] = False
include[3269:3280] = False
include[3289:3303] = False
include[3430:3446] = False
include[3456] = False
include[3460:3480] = False
include[3508:3523] = False
include[3721] = False
include[3729:3740] = False
include[4512:4531] = False
include[4582:4613] = False
include[4691:4715] = False
include[4910:4934] = False
include[5018] = False
include[5032:5037] = False
include[5104:5120] = False
include[5135:5158] = False
include[5184:5203] = False
include[5319:5324] = False
include[5496:5525] = False
include[6334:6347] = False
include[6436:6448] = False
include[6516:6541] = False
include[7445:7457] = False
include[7810:9290] = False
include[9401:9534] = False
include[9823:9856] = False

if weed_out:
    plt.figure()
    plt.plot(idx[include], tran_plus[include], '.')
    #plt.plot(idx[include], tran_minus[include], '.')
    #plt.plot(idx[include], tran_max[include], '.')
    #plt.plot(idx[include], central_temp[include], '.')
    plt.grid()
    plt.show()

# Plot the data:
if not weed_out:
    plt.figure()
    
    ax1 = plt.subplot(411)
    plt.plot(timestamp[include], tran_plus[include], '.', label="tran_plus")
    plt.plot(timestamp[include], tran_minus[include], '.', label="tran_minus")
    plt.plot(timestamp[include], tran_max[include], '.', label="tran_max")
    plt.legend()
    plt.ylabel("transmission")
    plt.grid()
    
    ax2 = plt.subplot(412, sharex=ax1)
    plt.plot(timestamp[include], central_temp[include], '.')
    plt.ylabel("central temperature / C")
    plt.grid()
    
    ax3 = plt.subplot(413, sharex=ax1)
    plt.plot(timestamp, amb_temp, '.')
    plt.ylabel("ambient temperature / C")
    plt.grid()
    
    ax4 = plt.subplot(414, sharex=ax1)
    plt.plot(timestamp, air_pressure, '.')
    plt.ylabel("air pressure / hPa")
    plt.xlabel("time / hours")
    plt.grid()
    
    # Hide x-axis tick labels on upper plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)
    
    plt.show()
    
    plt.figure()
    sc = plt.scatter(air_pressure[include], central_temp[include], c=timestamp[include], cmap='viridis')
    #plt.plot(air_pressure[include], central_temp[include], '.')
    plt.grid()
    plt.xlabel("air pressure / hPa")
    plt.ylabel("resonance temperature / C")
    cbar = plt.colorbar(sc)
    cbar.set_label("time / hours")
    plt.show()
