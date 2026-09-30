import numpy as np
import matplotlib.pyplot as plt
import csv


def read_csv_to_numpy(file_path):
    # Read data from the second temperature scan
    
    column1 = []
    column2 = []
    column3 = []
    column4 = []

    # Open the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Convert the row values to appropriate types and append to the lists
            column1.append(float(row[0]))
            column2.append(float(row[1]))
            column3.append(float(row[2]))
            column4.append(float(row[3]))

    # Convert the lists to NumPy arrays
    array1 = np.array(column1)
    array2 = np.array(column2)
    array3 = np.array(column3)
    array4 = np.array(column4)

    return array1, array2, array3, array4


file_path = "20260824_Transmission_log.csv"

timestamp, input_power, output_power, temperature = read_csv_to_numpy(file_path)


# Only plot the data when the laser was locked:
lock_idx = np.arange(0, len(timestamp))
input_power = input_power[lock_idx]
output_power = output_power[lock_idx]

timestamp -= timestamp[0]
hours = timestamp/60/60
days = hours/24
days_temp = np.copy(days)
days = days[lock_idx]
lockidx_temp = temperature[lock_idx]

#input_power /= np.mean(input_power)
#output_power /= np.mean(output_power)
norm_power = output_power/input_power
#norm_power /= np.max(norm_power)

plt.figure()
plt.subplot(311)
plt.plot(days, input_power/np.mean(input_power), '.', label="input power")
plt.plot(days, output_power/np.mean(output_power), '.', label="output power")
plt.grid()
plt.legend()
plt.xlabel("time / days")
#plt.ylabel("opt. power / mW")
plt.ylabel("normalised power / a.u.")
plt.subplot(312)
z = np.polyfit(days, norm_power, 1)
p = np.poly1d(z)
plt.plot(days, norm_power, '.', label="std = " + str(np.round(np.std(norm_power)*100, 3)) + "%")
#plt.plot(norm_power, '.')
plt.plot(days, p(days), label="linear fit; slope = " + str(np.round(z[0]*100, 4)) + "%/day")
#plt.ylim((0.995, 1.005))
plt.legend()
plt.grid()
plt.xlabel("time / days")
plt.ylabel("transmission")
plt.subplot(313)
plt.plot(days_temp, temperature, label="min: " + str(np.round(np.min(temperature), 1)) +
         "C; max: " + str(np.round(np.max(temperature), 1)) + "C")
plt.grid()
plt.legend()
plt.xlabel("time / days")
plt.ylabel("temperature / C")
plt.show()
