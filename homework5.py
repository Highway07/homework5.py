immutable_var = tuple([1,'hand',False])
print('immutable_tuple:',immutable_var)
#Кортежи-не изменяемый объект,он не поддерживает обращение по элементам  immutable_var[0] = 3
print(immutable_var)

mutable_list = [1,2,True,'hand']
mutable_list[2] = 'Modified'
print(mutable_list)