#Các thư viện cần thiết
import numpy as np
import pandas as pd

#Các thư viện dùng để trực quan hóa dữ liệu
import matplotlib.pyplot as plt
import seaborn as sns



def bootstrapping(N, M, x):
    upper_bound = 0
    lower_bound = 0
    mean_bootstrap = []

    for _ in range(M):
        #create a sample width size is N, can overlap
        new_df = df.sample(n= N,replace=True)
        #save mean bootstrap
        mean_bootstrap.append(float(new_df.mean(axis=0)))


    dict = {'Mean Bootstrap': mean_bootstrap}
    mean_bootstrap = pd.DataFrame(dict)

    sorted_df = mean_bootstrap.sort_values(by='Mean Bootstrap', ascending=True)
    lower_bound = sorted_df.iloc[round(M*x)]
    upper_bound = sorted_df.iloc[round(M*(1-x))]

    return mean_bootstrap, lower_bound, upper_bound

            


original_samples = [81, 32, 49, 54, 44, 74, 98, 42, 54, 51, 69, 49, 43, 5, 1, 5, 35, 55, 4, 20, 25, 34, 31, 65, 46, 92, 2, 4, 41, 38]
df = pd.DataFrame(original_samples)
mean_bootstrap, lower_bound, upper_bound = bootstrapping(10,201,0.05) # n, M, x%

# histogram
sns.histplot(mean_bootstrap['Mean Bootstrap'], kde=True ,color = 'navy', bins=50)

# khoang tin cay
print(int(lower_bound))
print(int(upper_bound))

plt.show()

