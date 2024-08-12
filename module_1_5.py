immutable_var = 1, 2, 'e', True
print('Immutable Tuple:', immutable_var)
mutable_list = [1, 2, 'x', 'y', True]
mutable_list[0] = 5
mutable_list.append(85)
mutable_list.insert(1, 't')
print('Mutable_list:', mutable_list)
 # нельзя изменять данные внутри кортежа, так как кортеж - это неизменяемая упор. коллекция данных. При его изменении
 # будет интерпритироваться ошибка
 