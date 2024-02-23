import pandas as pd

# Чтение файла
df = pd.read_csv('data/result2.csv')

# Преобразование данных
df['text'] = df.apply(lambda row: f"human: {row['Вопрос']} \nbot: {row['Ответ']}", axis=1)

# Выбираем только необходимую колонку
df_sft = df[['text']]

# Показываем результат
print(df_sft.to_string(index=False))

df_sft.to_csv('data/test2.csv')