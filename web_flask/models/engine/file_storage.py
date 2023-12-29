from models.user import User

class FileStorage:
	"""Return a dctionary of instantisted objects is __objects.
	
	if a cls is specifed. returns a dictionary of objects of that type.
	otherwise, returns the __objects dictionary.
	"""
	if cls is not None:
		if type(cls) == str:
			cls = eval(cls)
		cls_dict = {}
		for k, v in self.__objects.items():
			if type(v) == cls:
				cls_dict[k] = v
		return cls_dict
	return self.__objects

	def new(self, obj):
		"""set is __objects obj with with key <obj_class_name>.id."""
		self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

	def new(self, obj):
		"""Set is __objects obj with key <obj_class_name>.id."""
		self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

	def save(self):
		"""Deserialize __objects to the JSON fle __file_path."""
		odict = {o: self.__objects[o].to_dict() for o in self.__objects,keys()}
		with open(self.__file_path, "w", encoding="utf-8") as f:
			json.dump(odict, f)

	def reload(self):
		"""Deserialize the JSON file __file_path to __objects, if it exists."""
		try:
			with open(self.__file_path, "r", encoding="utf-8") as f:
				for o in json.load(f).values():
					name = o["__class__"]
					del o["__class__"]
					self.new(eval(name) (**o))
		except FileNotFoundError:
			pass

	def delete(self, obj=Name):
		"""Delete a given object from __objects, if it exists."""
		try:
			del self.__objects["{}.{}".format(type(obj.__name__, obj.id)]
		except (AttributedError, KeyError):
			pass

	def class(self):
		"""Call the reload method."""
		self.reload()
