from os import listdir
from os.path import isfile, join
import pickle
from PIL import Image
import tqdm
import numpy as np
import sys
import argparse

class Data:
	def __init__(self):
		pass

	def create(self,path,size):

		if path[-1]!="/" or path[-1]!="\\":
			path+="/"

		"""
			Convert images of a size to a pickle file

			Required parameters :
			path : the path of the size
			size : imgs will be converted to size*size imgs
		"""
		try:
			onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		except Exception as e:
			print(e)
			quit()

		print("Number of pictures :",len(onlyfiles))

		if path[-1] != "/" or path[-1]!="\\":
			path = path +"/"

		dataset = []

		print("Creating the dataset..")
		for i in tqdm.trange(len(onlyfiles)):
			img = Image.open(path+onlyfiles[i]).convert("RGB")
			img = img.resize((size, size), Image.ANTIALIAS)
			dataset.append(np.asarray(img))
		
		dataset = np.array(dataset)
		print("Shape of the dataset :",dataset.shape)
		pickle.dump(dataset, open('dataset.pkl', 'wb'))
		


	def load(self):
		"""
			Load the dataset
		"""
		return pickle.load(open('dataset.pkl', 'rb'))

if __name__ == "__main__":

	#Define the parser and all its arguments
	parser = argparse.ArgumentParser(description="Creating a new dataset")

	parser.add_argument("-p", "--path",
	                    help="Folder path")

	parser.add_argument("-s", "--size",type=int,
	                    help="Size of the image")

	args = parser.parse_args()

	#Execute the different tasks according to the parameters
	if args.path and args.size:
		data = Data()
		data.create(args.path,args.size)
	else:
		print("Must add a path and a size")
