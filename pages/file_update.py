import pandas as pd
import urllib.request as urllib2  
import json
import os

current_dir = os.path.dirname(__file__)
data_key_path = os.path.join(current_dir, 'data','key.csv')

# 医療関連のデータのキーを取得する関数
def medical_key():
    read_file = pd.read_csv(data_key_path)
    medical_data = read_file['医療']
    medical_data.fillna("None", inplace=True)
    medical_data_list = medical_data.tolist()
    medical_data_list = [name for name in medical_data if name != "None"]
    return medical_data_list

# 避難場所のデータのキーを取得する関数
def hinann_key():
    read_file = pd.read_csv(data_key_path)
    hinann_data = read_file['避難']
    hinann_data.fillna("None", inplace=True)
    hinann_data_list = hinann_data.tolist()
    hinann_data_list = [name for name in hinann_data if name != "None"]
    return hinann_data_list

# 文化のデータのキーを取得する関数
def culture_key():
    read_file = pd.read_csv(data_key_path)
    culture_data = read_file['文化']
    culture_data.fillna("None", inplace=True)
    culture_data_list = culture_data.tolist()
    culture_data_list = [name for name in culture_data if name != "None"]
    
    return culture_data_list

# 避難場所のデータのキーを取得する関数
def Aed_key():
    read_file = pd.read_csv(data_key_path)
    Aed_data = read_file['AED']
    Aed_data.fillna("None", inplace=True)
    Aed_data_list = Aed_data.tolist()
    Aed_data_list = [name for name in Aed_data if name != "None"]
    
    return Aed_data_list

def get_data(resources, filename):
    all_data = []
    for resource in resources:
        response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
        data = json.loads(response.read()).get('result').get('records')
        all_data.extend(data)
    return pd.DataFrame(all_data)


def main(zyouki):
    if(zyouki == "medicalcare"):
        medical_path = os.path.join(current_dir, 'data','medicalcare.csv')
        resources = medical_key()
        data = get_data(resources, "medicalcare")
        data.to_csv(medical_path, index=False)
    elif(zyouki == "hinann"):
        hinanan_path = os.path.join(current_dir, 'data','hinann.csv')
        resources = hinann_key()
        data = get_data(resources, "hinann")
        data.to_csv(hinanan_path, index=False)

    elif(zyouki == "culture"):
        culture_path = os.path.join(current_dir, 'data','culture.csv')
        resources = culture_key()
        data = get_data(resources, "culture")
        data.to_csv(culture_path, index=False)

    elif(zyouki == "Aed"):
        Aed_path = os.path.join(current_dir, 'data','Aed.csv')
        resources = Aed_key()
        data = get_data(resources, "Aed")
        data.to_csv(Aed_path, index=False)
