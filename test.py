#Các thư viện cần thiết
import numpy as np
import pandas as pd

#Các thư viện dùng để trực quan hóa dữ liệu
import matplotlib.pyplot as plt
import seaborn as sns



def bootstrapping(df, N, M, x):
    upper_bound = 0
    lower_bound = 0
    mean_bootstrap = []

    for _ in range(M):
        #create a sample width size is N, can overlap
        new_df = df.sample(n= N,replace=True)
        #save mean bootstrap
        mean_bootstrap.append(float(new_df.mean(axis=0)))


    dict = {'Mean Bootstrap (Explains concepts)': mean_bootstrap}
    mean_bootstrap = pd.DataFrame(dict)

    #Sắp xếp lai cái giá trị trong mean_bootstrap theo thứ tự tăng dần
    sorted_df = mean_bootstrap.sort_values(by='Mean Bootstrap (Explains concepts)', ascending=True)
    lower_bound = sorted_df.iloc[round(M*x)]
    upper_bound = sorted_df.iloc[round(M*(1-x))]
    mean_line = sorted_df.mean()

    return mean_bootstrap, lower_bound, upper_bound, mean_line

            

#init original sample
# original_samples = [81, 32, 49, 54, 44, 74, 98, 42, 54, 51, 69, 49, 43, 5, 1, 5, 35, 55, 4, 20, 25, 34, 31, 65, 46, 92, 2, 4, 41, 38]
# df = pd.DataFrame(original_samples)

# Read file csv to data frame
df = pd.read_csv('../bootstrap-sampling-method/StudentsPerformance.csv', delimiter=',')

# Get first 1000 rows BMI that has HeartDisease are 'Yes'
df_explain_concept = df['math score']


mean_bootstrap, lower_bound, upper_bound, mean_line = bootstrapping(df_explain_concept, 333,6666,0.05) # dataframe, n, M, x%

#  histogram
sns.histplot(mean_bootstrap['Mean Bootstrap (Explains concepts)'], kde=True ,color = 'brown', bins=20)

# khoảng tin cậy
lower_bound = float("{:.2f}".format(float(lower_bound)))
upper_bound = float( "{:.2f}".format(float(upper_bound)))
mean_line = float( "{:.2f}".format(float(mean_line)))

print('Giới hạn dưới: ' + str(lower_bound))
print('Giới hạn trên: '  + str(upper_bound))
print('Mean: '  + str(mean_line))

plt.axvline(lower_bound, 0,20)
plt.axvline(upper_bound, 0,20)
plt.axvline(mean_line, 0,20, color = 'k', linestyle = '--')

plt.text(lower_bound, 700, str(lower_bound), fontsize=10)
plt.text(upper_bound, 700, str(upper_bound), fontsize=10)
plt.text(mean_line-0.05, 700, "Mean: " + str(mean_line), fontsize=10)

plt.show()


