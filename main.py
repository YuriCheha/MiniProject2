import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


user_data = pd.read_csv('3_user_data.csv')
logs = pd.read_csv('3_logs.csv')
user_data.info()


logs.describe()

#Какой клиент совершил больше всего успешных операций?
success_counts = logs.loc[logs.success == True].client.value_counts()
max_num = success_counts.max()
max_success_users = success_counts.loc[success_counts == max_num]
max_success_users
max_success_users.index.sort_values()

#С какой платформы было совершено наибольшее количество успешных операций?
logs.loc[logs.success == True].platform.value_counts().idxmax()

#Какую платформу предпочитают премиальные клиенты?
premium_logs = logs.merge(user_data, on = 'client')
premium_logs.loc[premium_logs.premium == True].platform.value_counts().idxmax()

#Визуализируйте распределение возраста клиентов в зависимости от типа клиента
sns.displot(data=premium_logs, x='age', hue='premium', kde=True, kind='hist', stat='density', common_norm=False, bins=14)

#Постройте график распределения числа успешных операций
success_count = logs.loc[logs.success == True].client.value_counts()
success_count = success_count.rename('successes')
sns.countplot(x=success_count)

#Визуализируйте число успешных операций, сделанных на платформе computer, в зависимости от возраста
plt.figure(figsize=(12,8))
sns.countplot(data=premium_logs.loc[(premium_logs.platform == 'computer') & (premium_logs.success == True)], x = 'age')











