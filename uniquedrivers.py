import pandas as pd

# خواندن فایل اول
df1 = pd.read_excel('1830-out-lite.xlsx')

# خواندن فایل دوم
df2 = pd.read_excel('140203-taxidata-babol.xlsx')

# استخراج محتوایی از فایل اول که در فایل دوم نباشد
# unique_content = df1[~df1['NATIONALCODE'].isin(df2['NATIONALCODE'])]


# تشخیص محتوایی از فایل اول که در فایل دوم وجود ندارد
unique_records = df1[~df1['NATIONALCODE'].isin(df2['NATIONALCODE'])]

# ذخیره کردن فایل اکسل با محتوای منحصر به فرد
unique_records.to_excel('unique.xlsx', index=False)
