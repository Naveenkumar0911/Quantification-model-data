import numpy as np
import pandas as pd


output_target = "threat_output_datasets.csv"
input_target = "threat_input_datasets.csv"

input_threat_all = pd.DataFrame()
threat_all = pd.DataFrame()

skip = 0

for i in range(1,51):

        Generic_Threat = pd.DataFrame()

        Threat_Category = ['Criminal', 'Criminal', 'Governmental',
                        'Governmental', 'Commercial', 'Individual', 'Individual']
        
        ID = [i for j in range(len(Threat_Category))]
        Generic_Threat['Dataset_ID'] = ID
        Generic_Threat['Threat Category'] = Threat_Category

        Threat_Actor = ['Organized Crime','Other Criminals','APTs','Other Governments','Competitors','Anarchist Insider','Anarchist Outsider']
        Generic_Threat['Threat Actor'] = Threat_Actor


        Generic_Threat['Technology'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Expertise'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Resources'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Access'] = np.random.randint(1, 11, size=len(Generic_Threat))
        Generic_Threat['Capable_Sub-Total'] = Generic_Threat['Technology'] + \
            Generic_Threat['Expertise'] + \
            Generic_Threat['Resources'] + Generic_Threat['Access']
        Generic_Threat['Generally'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Specifically'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Motivated_Sub-Total'] = Generic_Threat['Generally'] + \
            Generic_Threat['Specifically']
        Generic_Threat['Low-Conscious'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Perception-Conscious'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Timing-Sensitivity'] = np.random.randint(
            1, 11, size=len(Generic_Threat))
        Generic_Threat['Willing_Sub-Total'] = Generic_Threat['Low-Conscious'] + \
            Generic_Threat['Perception-Conscious'] + \
            Generic_Threat['Timing-Sensitivity']
        Generic_Threat['Threat Severity'] = Generic_Threat['Capable_Sub-Total'] + \
            Generic_Threat['Motivated_Sub-Total'] + Generic_Threat['Willing_Sub-Total']

        input_threat_all = pd.concat([input_threat_all, Generic_Threat])

        values = Generic_Threat['Threat Severity'].values

        Intent = pd.read_csv('intent_datasets.csv')
        Intent = Intent.loc[Intent['Dataset_ID'] == i]     # Getting all the rows which have dataset ID as i

        del Intent['Dataset_ID']

        Threat_Intent = pd.DataFrame()

        Threat_Intent['Threat Category'] = Intent["Threat Category"]
        Threat_Intent['Threat Actor'] = Intent["Threat Actor"]
        Threat_Intent['Ransom'] = Intent["CC1"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Service degradation'] = Intent["CC2"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['IP Theft'] = Intent["CC3"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Reputation hit'] = Intent["CC4"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Low quality Product'] = Intent["CC5"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Data Loss'] = Intent["CC6"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Privacy Breach'] = Intent["CC7"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['OT Failure'] = Intent["CC8"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Resource Theft'] = Intent["CC9"].replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])
        Threat_Intent['Threat Severity'] = values


        Sector = pd.read_csv("sectors_datasets.csv")
        Sector = Sector.loc[Sector['Dataset_ID'] == i]
        del Sector['Dataset_ID']
        Sector = Sector.replace(to_replace=[1,2,3,4,5], value=[0.67,0.8,1,1.2,1.33])

        Threat_model= pd.DataFrame()


        ID = [i for j in range(len(Threat_Actor)+1)]
        Threat_model['Threat Actor'] = Threat_Intent["Threat Actor"]



        Threat_model['Ransom'] = Threat_Intent["Ransom"] * \
            values * Sector["IT"]
        Threat_model['Service degradation'] = Threat_Intent['Service degradation'] * \
            values * Sector["IT"]
        Threat_model["IP Theft"] = Threat_Intent["IP Theft"] * \
            values * Sector["IT"]
        Threat_model['Reputation hit'] = Threat_Intent['Reputation hit'] * \
            values * Sector["IT"]
        Threat_model['Low quality Product'] = Threat_Intent['Low quality Product'] * \
            values * Sector["IT"]
        Threat_model['Data Loss'] = Threat_Intent['Data Loss'] * \
            values * Sector["IT"]
        Threat_model['Privacy Breach'] = Threat_Intent['Privacy Breach'] * \
            values * Sector["IT"]
        Threat_model['OT Failure'] = Threat_Intent['OT Failure'] * \
            values * Sector["IT"]
        Threat_model['Resource Theft'] = Threat_Intent['Resource Theft'] * \
            values * Sector["IT"]

        Threat_model.reset_index(inplace=True, drop=True)
        cols = []
        for i in range(1,len(Threat_model.columns)):
            cols.append(Threat_model.columns[i])
        
        Threat_model[cols] = Threat_model[cols].mask(Threat_model[cols] > 90, 90)

        total_values = ["Total"]
        for i in range(1, len(Threat_model.columns)):
            column = Threat_model[Threat_model.columns[i]]
            total_values.append(column.max())

        Threat_model.loc[len(Threat_Actor)+1] = total_values

        Threat_model.insert(loc=0, column="Dataset_ID", value=ID)

        threat_all = pd.concat([threat_all, Threat_model])
        



input_threat_all.reset_index(inplace=True, drop=True)
input_threat_all.head()
input_threat_all.tail()
input_threat_all.to_csv(input_target, index = False)



threat_all.reset_index(inplace=True, drop=True)
threat_all.head()
threat_all.tail()
threat_all.to_csv(output_target,index=False)


