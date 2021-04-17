import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# /home/vins/Workspace/Py/data_files
df_monthly = pd.read_csv('/home/vins/Workspace/Py/data_files/salesmonthly.csv')
df_monthly["total"] = df_monthly["M01AB"] + df_monthly["M01AE"] + df_monthly["N02BA"] + df_monthly["N02BE"] + \
                      df_monthly["N05B"] + df_monthly["N05C"] + df_monthly["R03"] + df_monthly["R06"]
# df_monthly.to_excel("/home/vins/Workspace/Py/data_files/monthly_sales_v1.xlsx")
df = df_monthly[['datum', 'total']]
year_list = df.datum
total_list = df.total

# /home/vins/Workspace/Py/data_files
df_monthly = pd.read_csv('/home/vins/Workspace/Py/data_files/salesmonthly.csv')
df_monthly["total"] = df_monthly["M01AB"] + df_monthly["M01AE"] + df_monthly["N02BA"] + df_monthly["N02BE"] + \
                      df_monthly["N05B"] + df_monthly["N05C"] + df_monthly["R03"] + df_monthly["R06"]
# df_monthly.to_excel("/home/vins/Workspace/Py/data_files/monthly_sales_v1.xlsx")
df = df_monthly[['datum', 'total']]
year_list = df.datum
total_list = df.total

# print(year_list)
# print(total_list)

plt.xlabel('year_list')
plt.ylabel('total_list')

plt.plot(year_list, total_list, color='red', marker='*')
plt.show()
# df

# fig, axes = plt.subplots(8, 1, figsize=(10, 30), sharex=True)
# for name, ax in zip(['M01AB','M01AE','N02BA','N02BE', 'N05B','N05C','R03','R06'], axes):
#  sns.boxplot(data=df_daily, x='Month', y=name, ax=ax)

# df

# fig, axes = plt.subplots(8, 1, figsize=(10, 30), sharex=True)
# for name, ax in zip(['M01AB','M01AE','N02BA','N02BE', 'N05B','N05C','R03','R06'], axes):
#  sns.boxplot(data=df_daily, x='Month', y=name, ax=ax)
