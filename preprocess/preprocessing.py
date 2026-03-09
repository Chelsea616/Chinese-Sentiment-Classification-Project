import pandas as pd
from sklearn.model_selection import train_test_split
import re


partial_prefixes = ['补标', '#补标#', '标一下','已看']
date_prefix_pattern = re.compile(r'^\d{6,8}$')
date_chinese_pattern = re.compile(r'^\s*\d{4}年(\d{1,2}月)?(\d{1,2}[日号])?[\s，。！？…]*$')
def is_meaningless_comment(text):
    text = str(text).strip()
    if len(text) < 3:
        return True
    for prefix in partial_prefixes:
        if re.fullmatch(fr'{prefix}[\s，。！？…]*', text):
            return True
    if re.fullmatch(r'\d{6,8}', text):
        return True

    if date_prefix_pattern.fullmatch(text):
        return True

    if date_chinese_pattern.fullmatch(text):
        return True

    return False

df = pd.read_csv('DMSC.csv', encoding='utf-8')
target_movies = ['何以笙箫默', '湄公河行动','七月与安生']
df = df[df['Movie_Name_CN'].str.strip().isin(target_movies)]


df = df[['Comment', 'Star']]


df['Comment'] = df['Comment'].astype(str).str.strip()
df = df[~df['Comment'].apply(is_meaningless_comment)].copy()

# 4. create labels（0=negative，1=positive）
def label_rating(star):
    if star <= 3:
        return 0
    else:
        return 1

df['text'] = df['Comment']
df['label'] = df['Star'].apply(label_rating)
df = df[['text', 'label']]

# 5. split（8:2）
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])

# 6. savve
train_df.to_csv('data/train_pinggu.csv', index=False, encoding='utf-8-sig')
test_df.to_csv('data/test_pinggu.csv', index=False, encoding='utf-8-sig')
