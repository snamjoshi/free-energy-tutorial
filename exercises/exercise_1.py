import numpy as np
import matplotlib.pyplot as plt

""" Methods """
def likelihood_function(v):
    return np.power(v, 2)

def normal_dist(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi * sigma))) * np.exp(-(np.power(x - mu, 2) / (2 * sigma))) 

def likelihood(u, v_p, mu_u):
    return normal_dist(u, v_p, mu_u)

def prior(v, v_p, sigma_p):
    return normal_dist(v, v_p, sigma_p)

def posterior(likelihood, prior, evidence):
    return (likelihood * prior) / evidence

""" Initialization """
obs = 2
obs_noise = 1
prior_mean = 3
prior_var = 1

# Posterior probability range
v_min = 0.01
v_max = 5
v_step = 0.01
v_range = np.arange(v_min, v_max, v_step)

""" Calculations """
likelihood_prob = likelihood(obs, likelihood_function(v_range), obs_noise)
prior_prob = prior(v_range, prior_mean, prior_var)
evidence_prob = np.sum(likelihood_prob * prior_prob * v_step)
posterior_prob = (likelihood_prob * prior_prob) / evidence_prob

""" Plots """
# Note, y-axis is incorrect for likelihood function plot

figs, axs = plt.subplots(2, 2)
axs[0, 0].plot(v_range, prior_prob)
axs[0, 0].set_title('Prior')
axs[0, 1].plot(v_range, likelihood_prob)
axs[0, 1].set_title('Likelihood')
axs[1, 0].plot(v_range, posterior_prob)
axs[1, 0].set_title('Posterior')
axs[1, 1].plot(v_range, likelihood_function(v_range))
axs[1, 1].set_title('Likelihood Function')

for ax in axs.flat:
    ax.set(xlabel = 'Food Size', ylabel = 'Probability')
    ax.label_outer()
    
plt.show()

""" Workspace """
# def evidence(likelihood, prior, postp_min, postp_max):
#     return integrate.quad(lambda x: likelihood * prior, min, max)

