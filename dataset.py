import pickle

def get_data_dictionary(mode):
    """
    Returns the data labels for corresponding mode
  
    Parameters:
    mode (int): type of data (train/val/test)
  
    Returns:
    list: dictionaries having params answer_type, img_id, label, 
          question_id, question_type, sent
  
    """
    path = "data/qas/"+mode+"_vqa.pkl"
    return pickle.load(open(path,"rb"))