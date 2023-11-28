#Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его 
# в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd 
import numpy as np
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

#Создаем новые столбцы с помощью двоичного кодирования:
data["robot"] = np.where(data["whoAmI"].str.contains("robot"), 1, 0)
data["human"] = np.where(data["whoAmI"].str.contains("human"), 1, 0)

print(data)