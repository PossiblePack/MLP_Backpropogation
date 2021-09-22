from random import randrange
import numpy as np
from flood_dataset import *

def crossvalidation_split(data, folds):
	dataset_split = []
	dataset_copy = list(data)
	fold_size = int(len(data) / folds)
	for i in range(folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

