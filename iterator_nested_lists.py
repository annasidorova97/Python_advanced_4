nested_list = [
	'd',
	'f',
	['a', 'b', ['k', 'j'], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, some_list):
		self.list = some_list
		self.current_value = ''

	def __iter__(self):
		self.main_cursor = 0
		return self

	def __next__(self):
		if self.main_cursor >= len(self.list):
			raise StopIteration
		if not isinstance(self.list[self.main_cursor], list):
			self.current_value = self.list[self.main_cursor]
			self.main_cursor += 1
			return self.current_value
		else:
			self.list = self.list[self.main_cursor] + self.list[self.main_cursor+1:]
			self.main_cursor = 0
			return self.__next__()


for item in FlatIterator(nested_list):
	print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

