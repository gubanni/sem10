import input_data
from write_data import write_data


def push_data():
    dct_uch = input_data.input_data_uch()
    dct_cl = input_data.input_data_cl()
    dct_adr = input_data.input_data_adr()
    
   
    write_data(dct_uch, "name.json")
    write_data(dct_adr, "adress.json")
    write_data(dct_cl, "class.json")
    

