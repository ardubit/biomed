# https://www.statology.org/kl-divergence-python/

from scipy.special import rel_entr

# P = [.05, .1, .2, .05, .15, .25, .08, .12]
# Q = [.3, .1, .2, .1, .1, .02, .08, .1]

P = [.1, .1, .1, .1, .1, .1, .1, .1]
Q = [1.12, 1.12, .12, .12, .12, .12, .12, .12]

# calculate (P || Q) KL divergence between the two distributions
kl1 = sum(rel_entr(P, Q))

# KL divergence is not a symmetric metric.
kl2 = sum(rel_entr(Q, P))

print('KL1 \n', kl1)
print('KL2 \n', kl2)