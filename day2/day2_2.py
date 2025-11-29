import pandas as pd


data = {
  "name": {
    "0": "Pavani",
    "1": "Rahul",
    "2": "Sita",
    "3": "Ajay",
    "4": "Teja",
    "5": "Kiran",
    "6": "Mahi",
    "7": "Riya",
    "8": "Sai",
    "9": "Arjun",
    "10": "Niki",
    "11": "Manu",
    "12": "Loki",
    "13": "Ramu",
    "14": "Rosh",
    "15": "Diya",
    "16": "Mona",
    "17": "Kavi",
    "18": "Sona",
    "19": "Raju"
  },

  "age": {
    "0": 19,
    "1": 20,
    "2": 18,
    "3": 21,
    "4": 20,
    "5": 19,
    "6": 18,
    "7": 20,
    "8": 21,
    "9": 19,
    "10": 20,
    "11": 18,
    "12": 21,
    "13": 20,
    "14": 19,
    "15": 18,
    "16": 20,
    "17": 21,
    "18": 20,
    "19": 18
  },

  "city": {
    "0": "Hyderabad",
    "1": "Vizag",
    "2": "Hyd",
    "3": "Vzg",
    "4": "Vizag",
    "5": "Hyderabad",
    "6": "Hyd",
    "7": "Vizag",
    "8": "Hyderabad",
    "9": "Vzg",
    "10": "Vizag",
    "11": "Hyd",
    "12": "Hyderabad",
    "13": "Vizag",
    "14": "Hyd",
    "15": "Vizag",
    "16": "Hyderabad",
    "17": "Vzg",
    "18": "Vizag",
    "19": "Hyd"
  },

  "department": {
    "0": "CSE",
    "1": "ECE",
    "2": "MECH",
    "3": "CIVIL",
    "4": "CSE",
    "5": "EEE",
    "6": "CSE",
    "7": "IT",
    "8": "MECH",
    "9": "ECE",
    "10": "CSE",
    "11": "CIVIL",
    "12": "IT",
    "13": "MECH",
    "14": "EEE",
    "15": "ECE",
    "16": "CSE",
    "17": "IT",
    "18": "CIVIL",
    "19": "EEE"
  },

  "scholarship": {
    "0": True,
    "1": False,
    "2": True,
    "3": True,
    "4": 0,
    "5": True,
    "6": True,
    "7": "f",
    "8": True,
    "9": False,
    "10": 1,
    "11": False,
    "12": True,
    "13": True,
    "14": False,
    "15": True,
    "16": False,
    "17": True,
    "18": False,
    "19": "t",
  }
}


df = pd.DataFrame(data)
# df ["city"].str.contains("hyd",case=False)
df["city"]=df ["city"].str.replace(r"hyd.*","Hyderabad",case=False,regex=True)
df["city"]=df ["city"].str.replace(r"vzg.*","vizag",case=False,regex=True)
def clean_bool(x):
    c=str(x).strip().lower()
    if c in ["true","1","yes","t""true"]:
        return 1
    if c in ["f","0","no","no","false"]:
        return 0
df["scholarship"]=df["scholarship"].apply(clean_bool)
print(df)
