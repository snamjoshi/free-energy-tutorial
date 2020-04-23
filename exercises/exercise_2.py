import numpy as np
import matplotlib.pyplot as plt

""" Initialization """
obs = 2
obs_noise = 1
prior_mean = 3
prior_var = 1
likely_size = [prior_mean]
t_max = 5

# Posterior probability range 
v_min = 0.01
v_max = 5
v_step = 0.01
v_range = np.arange(v_min, v_max, v_step)

""" Calculations """
for i in range(1, int(t_max / v_step) - 1):
    euler_update = likely_size[i - 1] + v_step * ((prior_mean - likely_size[i - 1]) / prior_var + (obs - np.power(likely_size[i - 1], 2)) / obs_noise * (2 * likely_size[i - 1]))
    likely_size.append(euler_update)

""" Plots """
plt.plot(v_range, likely_size)
plt.ylim(0, 3, 1)
plt.xlim(0, 5, 1)
plt.ylabel('Likely Size (phi)')
plt.xlabel('Time')
plt.show()

