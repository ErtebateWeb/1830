import pandas as pd

# خواندن فایل اول
df1 = pd.read_excel('1830-out-lite.xlsx')

# خواندن فایل دوم
df2 = pd.read_excel('140204-taxidata-babol.xlsx')

# ادغام دو فایل بر اساس فیلدهای کلیدی
merged_df = pd.merge(df1, df2, on='NATIONALCODE', how='inner')

# ذخیره کردن فایل اکسل ادغام شده
merged_df.to_excel('140205-4-taxidata-babol.xlsx', index=False)
