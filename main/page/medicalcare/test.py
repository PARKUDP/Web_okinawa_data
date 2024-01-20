import pandas as pd

# データ取得関数
def get_data():
    read_file = pd.read_csv("main/key.csv")
    medical_data = read_file['医療']
    medical_data.fillna("None", inplace=True)
    medical_data_list = medical_data.tolist()
    if "None" in medical_data_list:
        medical_data_list.remove("None")
    
    return medical_data_list

if __name__ == "__main__":
    print(len(get_data()))