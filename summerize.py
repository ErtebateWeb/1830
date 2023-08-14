import pandas as pd

# خواندن فایل اکسل
df = pd.read_excel('1830.xlsx')

# محاسبه تعداد مسیرهای هر راننده
count_per_driver = df.groupby('driver')['code'].count().reset_index()
count_per_driver.columns = ['driver', 'تعداد مسیرها']

# محاسبه مجموع مسافت طی شده هر راننده
sum_distance_per_driver = df.groupby('driver')['distance'].sum().reset_index()
sum_distance_per_driver.columns = ['driver', 'مجموع مسافت طی شده']

# محاسبه مجموع هزینه هر راننده
sum_price_per_driver = df.groupby('driver')['price'].sum().reset_index()
sum_price_per_driver.columns = ['driver', 'مجموع هزینه']

# اضافه کردن ستون‌های جدید به فایل اکسل
df = pd.merge(df, count_per_driver, on='driver', how='left')
df = pd.merge(df, sum_distance_per_driver, on='driver', how='left')
df = pd.merge(df, sum_price_per_driver, on='driver', how='left')

# ذخیره کردن فایل اکسل با ستون‌های جدید
df.to_excel('1830-out.xlsx', index=False)
