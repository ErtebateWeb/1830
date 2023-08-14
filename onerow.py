import pandas as pd

# خواندن فایل اکسل
df = pd.read_excel('1830-out.xlsx')

# انتخاب سطر اول برای هر راننده و حذف سطرهای تکراری
df_unique = df.drop_duplicates(subset='driver', keep='first')

# ذخیره کردن فایل اکسل با سطرهای منحصر به فرد برای هر راننده
df_unique.to_excel('1830-out-lite.xlsx', index=False)
