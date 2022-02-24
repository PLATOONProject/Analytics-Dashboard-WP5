from pandas import read_pickle

data_cds = read_pickle("code/meteo_cds.pkl")
print(data_cds.to_json())