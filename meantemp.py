import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameters to modify in the dashboard
THRESHOLD = 2.00
COM = 14
WINDOW_SIZE = 15
WINDOW_SIZE_BOLL = 20
PROPVOTE = 0.8
NUM_STD_DEV = 3

# EWMA parameters
ewma_30_min = 60
ewma_60_min = 90
ewma_120_min = 120


# def majority_vote(arr):
#     return 1 if np.mean(arr) > 0.5 else 0


def majority_vote(data, proportional_vote=0.7):
    num_samples = len(data)
    num_off_body = np.sum(data)
    prop_off_body = num_off_body / num_samples

    return 1 if prop_off_body >= proportional_vote else 0


def find_consecutive_drops(temp_data, threshold):
    # print(type(temp_data))
    # for i,val in enumerate(temp_data):
    #     print(val,end="\n")
    #     if i>=20:
    #         break

    running_sum = [0]
    for i in range(1, len(temp_data)):
        diff = temp_data[i] - temp_data[i - 1]

        if diff < 0 and running_sum[-1] + diff < 0:
            running_sum.append(running_sum[-1] + diff)
        else:
            running_sum.append(0)
        # if i<=20:
        #     print(diff)
        #     print(running_sum[-1])

    off_body_temp = [1 if abs(rs) >= threshold else 0 for rs in running_sum]

    # Apply majority voting over a rolling window
    off_body = []
    for i in range(len(off_body_temp) - WINDOW_SIZE + 1):
        off_body.append(majority_vote(off_body_temp[i:i + WINDOW_SIZE], proportional_vote=PROPVOTE))

    # Padding the end of the off_body array to match the length of the input data
    off_body.extend([0] * (WINDOW_SIZE - 1))
    return off_body


def plot_off_body_periods(ax, off_body_periods):
    for i in range(len(off_body_periods) - 1):
        if off_body_periods[i]:
            ax.axvspan(i, i + 1, alpha=0.2, color='red')
            # if off_body[i]==1 than it drow vertical line between i to i+1 thick


def bollinger_bands(temp_data, window_size, num_std_dev):
    temp_series = pd.Series(temp_data)
    # print(type(temp_series))
    # print(temp_series[:20])
    moving_avg = temp_series.rolling(window=window_size).mean()
    # print(type(moving_avg))
    # print(moving_avg[:20])
    std_dev = temp_series.rolling(window=window_size).std()
    # print(std_dev[:25])

    lower_band = moving_avg - num_std_dev * std_dev
    upper_band = moving_avg + num_std_dev * std_dev
    # print(type(lower_band))
    return lower_band, upper_band


# Read the dataset
data = pd.read_csv('/home/omkar/Panda/sampal_temp.csv')
print(data.head(10))

mean_temperature = data['MeanTemperature'].ewm(com=COM).mean().values
# mean_temperature = data['MeanTemperature'].values
mean_accelerometer_composite = data['MeanAccelerometerComposite'].values

# Calculate EWMAs
ewma_30 = data['MeanTemperature'].ewm(span=ewma_30_min).mean().values
ewma_60 = data['MeanTemperature'].ewm(span=ewma_60_min).mean().values
ewma_120 = data['MeanTemperature'].ewm(span=ewma_120_min).mean().values


off_body_periods = find_consecutive_drops(mean_temperature, THRESHOLD)
# print(off_body_periods[:])
lower_band, upper_band = bollinger_bands(mean_temperature, WINDOW_SIZE_BOLL, NUM_STD_DEV)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
# it create 3 parallel subploat having same x axis

# Plot temperature data with Bollinger Bands
ax1.plot(mean_temperature, label='Original Temperature Data', alpha=0.5)
ax1.plot(lower_band, label='Lower Bollinger Band', linestyle='--', color='green')
ax1.plot(upper_band, label='Upper Bollinger Band', linestyle='--', color='red')
ax1.set_ylabel('Temperature')

plot_off_body_periods(ax1, off_body_periods)
ax1.legend()
ax1.set_title('Temperature Data and Bollinger Bands')



# Plot accelerometer data
ax2.plot(mean_accelerometer_composite, label='Accelerometer Composite', alpha=0.5)
ax2.set_xlabel('Time (minutes)')
ax2.set_ylabel('Accelerometer Composite')
plot_off_body_periods(ax2, off_body_periods)
ax2.legend()
ax2.set_title('Accelerometer Data')



ax3.plot(data['MeanTemperature'], label='Raw Temperature Data', alpha=0.5)
ax3.plot(ewma_30, label=f'30-minute EWMA', color='green')
ax3.plot(ewma_60, label=f'60-minute EWMA', color='orange')
ax3.plot(ewma_120, label=f'120-minute EWMA', color='blue')
plot_off_body_periods(ax3, off_body_periods)

ax3.set_xlabel('Time (minutes)')
ax3.set_ylabel('Temperature')

ax3.legend()
ax3.set_title('Temperature Data and EWMAs')


plt.tight_layout()
plt.show()