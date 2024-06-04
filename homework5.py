immutable_var = ("Hello", 3, 'a')
print('Immutable tuple:', immutable_var)
#immutable_var[0] = "Bye"               #Элементы кортежа нельзя изменять, так как кортеж - это нреизменяемая коллекция
mutable_list = [1, 2, 3, "Hello"]
mutable_list[0] = 45
print('Mutable list:', mutable_list)

