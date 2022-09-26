import pandas as pd
import numpy as np
import csv



target = "sectors_datasets.csv"

sectors_all = pd.DataFrame()

for i in range(1,51):

    Sector = pd.DataFrame()

    Threat_Category = ['Criminal', 'Criminal', 'Governmental', 'Governmental', 'Commercial', 'Individual', 'Individual']

    ID = [i for j in range(len(Threat_Category))]
    Sector["Dataset_ID"] = ID
    Sector['Threat Category'] = Threat_Category

    Threat_Actor = ['Organized Crime', 'Other Criminals', 'APTs', 'Other Governments', 'Competitors', 'Anarchist Insider', 'Anarchist Outsider']
    Sector['Threat Actor'] = Threat_Actor


    Sector['IT'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Healthcare'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Finance'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Consumer Discretionary'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Communication Services'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Industrials'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Consumer Staples'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Energy'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Utilities'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Real Estate'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Materials'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Government'] = np.random.randint(1, 6, size=len(Sector))
    Sector['SLED'] = np.random.randint(1, 6, size=len(Sector))
    Sector['Other Critical'] = np.random.randint(1, 6, size=len(Sector))

    sectors_all = pd.concat([sectors_all, Sector])

sectors_all.reset_index(inplace=True, drop=True)
sectors_all.head()
sectors_all.tail()

sectors_all.to_csv(target,index = False)


