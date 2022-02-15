from scipy import stats

# probability of getting 5 successes out of twenty for a 50/50

x = stats.binom(20,0.5).pmf(5)

print(x)

stats.geom

