import numpy as np
import matplotlib.pyplot as plt

""" Initialization """
obs = 2
obs_noise = 1
prior_mean = 3
prior_var = 1
t_max = 5

likely_size = [prior_mean]
prior_pe = [0]
obs_pe = [0]

# Posterior probability range 
v_min = 0.01
v_max = 5
v_step = 0.01
v_range = np.arange(v_min, v_max, v_step)

""" Calculations """
for i in range(1, int(t_max / v_step) - 1):
    likely_size_update = likely_size[i - 1] + v_step * (-prior_pe[i - 1] + obs_pe[i - 1] * (2 * likely_size[i - 1]))
    prior_pe_update = prior_pe[i - 1] + v_step * (likely_size[i - 1] - prior_mean - prior_var * prior_pe[i - 1])
    obs_pe_update = obs_pe[i - 1] + v_step * (obs - np.power(likely_size[i - 1], 2) - obs_noise * obs_pe[i - 1])

    likely_size.append(likely_size_update)
    prior_pe.append(prior_pe_update)
    obs_pe.append(obs_pe_update)

plt.plot(v_range, likely_size)
plt.plot(v_range, prior_pe)
plt.plot(v_range, obs_pe)
plt.ylim(-2, 3, 1)
plt.xlim(0, 5, 1)
plt.ylabel('Activity')
plt.xlabel('Time')
plt.legend(['Likely Size', 'Prior PE', 'Signal PE'], loc = 'upper right')
plt.show()




