import pandas as pd
import pingouin as pg

# データの定義
data1 = [3.814, 3.792, 3.786, 3.822, 3.814, 3.854, 3.874, 3.929, 4.061, 4.057, 4.121]
data2 = [3.731, 3.73, 3.773, 3.781, 3.765, 3.683, 3.784, 3.818, 3.829, 3.925, 3.972]
data3 = [3.617, 3.595, 3.623, 3.603, 3.673, 3.696, 3.741, 3.719, 3.729, 3.851, 3.887]
data4 = [3.491, 3.581, 3.602, 3.579, 3.57, 3.58, 3.592, 3.677, 3.706, 3.718, 3.751]
data5 = [3.399, 3.314, 3.513, 3.48, 3.534, 3.499, 3.521, 3.647, 3.654, 3.665, 3.724]
data6 = [3.206, 3.081, 3.241, 3.097, 3.116, 3.196, 3.439, 3.512, 3.486, 3.522, 3.641]

# データをデータフレームにまとめる
df = pd.DataFrame({
    'Time1': data1,
    'Time2': data2,
    'Time3': data3,
    'Time4': data4,
    'Time5': data5,
    'Time6': data6
})

# データをlong形式に変換
df_long = pd.melt(df, var_name='Time', value_name='Score')

# 被験者の識別子を追加（この場合は一つのデータ群(撮像条件)に11個のデータ（11人の被験者）がある）
df_long['Subject'] = df_long.groupby('Time').cumcount() + 1

# Repeated Measures ANOVAの実行
aov = pg.rm_anova(dv='Score', within='Time', subject='Subject', data=df_long, detailed=True)

# 結果を表示
print(aov)
