from esdl.esdl_handler import EnergySystemHandler
import requests, os, pandas as pd

def read_inputs(Assets, ESDL):
    in_ctm = {}

    esh = EnergySystemHandler()                            
    es: esdl.EnergySystem = esh.load_file(ESDL)  
    eassets = es.eAllContents()                

    assets = tuple(Assets.keys())

    for easset in eassets:                                 
        for asset in assets:                                 
            if isinstance(easset, asset):
                if isinstance(Assets[asset], list):
                    for csvfile in Assets[asset]:
                        if easset.name in csvfile:
                            pass 
                else:
                    df = pd.read_csv('Profiles/%s'%Assets[asset])
                    df = df.drop('CTMref_w', axis = 1)
                    df = df[df['CTMref_r'].notnull()]
                    df_override = df[df['Overrideval'].notnull()]
                    df = df[~df['Overrideval'].notnull()]

                    for indx in df.index:
                        df_i = df.loc[indx].dropna()
                        easset_contnt = easset
                        try:
                            for i in df_i[:-1]:
                                easset_contnt = easset_contnt.eGet(i)
                            in_ctm[df_i[-1]] = float(easset_contnt)
                        except AttributeError:
                            pass   

                    for indx in df_override.index: 
                        df_i = df_override.loc[indx].dropna()
                        easset_contnt = easset
                        for i in df_i[:-3]:
                            easset_contnt = easset_contnt.eGet(i)
                            
                        if str(easset_contnt) == df_i[-3]: 
                            in_ctm[df_i[-2]] = float(df_i[-1])
    return in_ctm


def write_inputs(Assets, ESDL, sessionID, url):

    profiles = Assets.values()
    csvfiles = []
    for item in profiles:
        if isinstance(item, list):
            for csvfile in item:
                csvfiles.append(csvfile)
        else:
            csvfiles.append(item)
    
    outputs = []

    for csv in csvfiles:
        df = pd.read_csv('Profiles/%s'%csv)
        CTM_refs = df['CTMref_w'][df['CTMref_w'].notnull()]
        

        for ctmref in CTM_refs:
            outputs.append(ctmref) 

    requestJSON = {"SessionID": sessionID, "inputs": {}, "outputs": outputs}
    output = requests.post(url, json=requestJSON)
    output = output.json()['output_values']

    esh = EnergySystemHandler()
    es: esdl.EnergySystem = esh.load_file(ESDL)
    eassets = es.eAllContents()

    assets = tuple(Assets.keys())

    for easset in eassets: 
        for asset in assets:  
            if isinstance(easset, asset):  
                if isinstance(Assets[asset], list):   
                    for csvfile in Assets[asset]:
                        if easset.name.lower() in csvfile.lower(): 
    
                            df = pd.read_csv('./ESDL/Profiles/%s'%csvfile)
                            df = df[df['CTMref_w'].notnull()]
                            df = df.drop('CTMref_r', axis = 1)
                            df_override = df[df['Overrideval'].notnull()]
                            df = df[~df['Overrideval'].notnull()]
                            
                            for indx in df_override.index:
                                df_i = df_override.loc[indx].dropna()
                                if output[df_i['CTMref_w']] == df_i['Overrideval']:
                                    att = easset
                                    for i in df_i[:-5]:
                                        att = getattr(att, i)
                                    setattr(att, df_i[-4], df_i[-3])

                            for indx in df.index:
                                df_i = df.loc[indx].dropna()
                                if df_i['CTMref_w'] in output.keys():
                                    att = easset
                                    for i in df_i[:-2]:
                                        att = getattr(att, i)
                                    setattr(att, df_i[-2], output[df_i['CTMref_w']])
                
                else:
                    df = pd.read_csv('Profiles/%s'%Assets[asset])
                    df = df[df['CTMref_w'].notnull()]
                    df = df.drop('CTMref_r', axis = 1)
                    df_override = df[df['Overrideval'].notnull()]
                    df = df[~df['Overrideval'].notnull()]
                    
                    for indx in df.index:
                        df_i = df.loc[indx].dropna()
                        if df_i['CTMref_w'] in output.keys():
                            att = easset
                            for i in df_i[:-3]:
                                att = getattr(att, i)
                            setattr(att, df_i[-2], output[df_i['CTMref_w']])
                    
                    for indx in df_override.index:
                        df_i = df_override.loc[indx].dropna()
                        if output[df_i['CTMref_w']] == df_i['Overrideval']:
                            att = easset
                            for i in df_i[:-5]:
                                att = getattr(att, i)
                            setattr(att, df_i[-4], df_i[-3])
                            

    esh.save()
