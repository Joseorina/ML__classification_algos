#Implementing Random Selection
import random
N = 10000
d = 10
ads_selected =[]
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward + reward
    
#Visualizing the result- Histogram
plt.hist(ads_selected)
plt.title('HIstogram ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()