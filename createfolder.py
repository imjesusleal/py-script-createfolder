#!/usr/bin/python3

import os
import shutil
import sys

def main():

	args = sys.argv[1:]
	directory, name, file = args

	try:
		if directory != '':
			os.chdir(directory)
			cwd = os.getcwd()
		else:
			print('Debes especificar al directorio al que quieres ir')
		if name != '':
			if not os.path.exists(name):
				os.makedirs(name)
			else:
				print('Ya existe una carpeta con ese nombre, intenta otro')
		if file != '':
			with open(file, 'w') as f:
				pass
		new_path = os.path.join(cwd, name)
		destination = os.path.join(new_path, file)
		source = os.path.join(cwd, file)
		shutil.move(source, destination)
	except:
		raise AssertionError('Ha ocurrido un error, por favor intentalo de nuevo')


if __name__ == '__main__':
	main()
