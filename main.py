from os.path import exists
from search_data import creating
from file_writing import writing_scv
from file_writing import writing_txt


path = 'phone.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()
    