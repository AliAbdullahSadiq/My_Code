from scipy.special import comb

probability = comb(100, 80) * (0.25 ** 80) * (0.75 ** 20)
print(probability)
