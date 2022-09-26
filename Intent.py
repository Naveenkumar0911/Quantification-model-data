import pandas as pd
import numpy as np
import csv


target = "intent_datasets.csv"

    
intent_all = pd.DataFrame()
for i in range(1, 51):

    
    Intent = pd.DataFrame()

    

    Threat_Category = ['Criminal', 'Criminal', 'Governmental',
                        'Governmental', 'Commercial', 'Individual', 'Individual']

    ID = [i for j in range(len(Threat_Category))]
    
    Intent["Dataset_ID"] = ID

    Intent['Threat Category'] = Threat_Category

    Threat_Actor = ['Organized Crime', 'Other Criminals', 'APTs',
                    'Other Governments', 'Competitors', 'Anarchist Insider', 'Anarchist Outsider']
    Intent['Threat Actor'] = Threat_Actor

    Intent['CC1'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC2'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC3'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC4'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC5'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC6'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC7'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC8'] = np.random.randint(1, 6, size=len(Intent))
    Intent['CC9'] = np.random.randint(1, 6, size=len(Intent))
    intent_all = pd.concat([intent_all, Intent])

intent_all.reset_index(inplace=True, drop=True)
intent_all.head()
intent_all.tail()

intent_all.to_csv(target, index = False)
