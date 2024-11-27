from scipy import stats

print(stats.norm.cdf(0))
ttest_result = stats.ttest_rel([1,2,3,4,5],[5,6,7,8,7])
print(ttest_result)
if ttest_result.pvalue > .05:
    print("Reject null hypothesis")
else:
    print("Accept null hypothesis")
