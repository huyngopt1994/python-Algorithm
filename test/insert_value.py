def insert_val_at(index, my_list, value):
	if 0 <= index < len(my_list)-1:

		my_list.insert(index, value)
		return my_list
	else:
		return False
