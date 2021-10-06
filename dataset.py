import pickle
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def get_data_dictionary(mode):
	"""
	Returns the data labels for corresponding mode
  
	Parameters:
	mode (str): type of data (train/val/test)
  
	Returns:
	list: dictionaries having params answer_type, img_id, label, 
		  question_id, question_type, sent
  
	"""
	path = "data/qas/"+mode+"_vqa.pkl"
	return pickle.load(open(path,"rb"))


def load_image_from_dictionary(data_dict, mode):
	"""
	Returns the dictionary of image arrays
  
	Parameters:
	data_dict : data dictionary of corresponding mode
	mode (str): type of data (train/val/test)
  
	Returns:
	dict: img_id as key and the img array as value
  
	"""

	img_dict={}
	for data in data_dict:
		if data["img_id"] not in img_dict:
			img_dict[data["img_id"]]=img_to_array(load_img("data/images/"+mode+"/"+data["img_id"]+".jpg"))
	return img_dict