import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

if __name__ == '__main__':
    sixty = pd.read_csv('../data/combined_cleaned.csv',dtype={'WINTERPEAKDEMAND': np.float64, 'SUMMERPEAKDEMAND': np.float64},index_col='Unnamed: 0')
    df = sixty[sixty['DATAYEAR'] < 2018]

    COAL = []
    NATURALGAS = []
    OIL = []
    HYDRO = []
    GEOTHERMAL = []
    WIND = []
    SOLAR = []
    NUCLEAR = []
    OTHER = []
    YEAR = []



    for i in range(1990,2018):
        df = sixty[sixty['DATAYEAR'] == i]
        COAL.append(df.MW_COAL.sum())
        NATURALGAS.append(df.MW_NATURAL_GAS.sum())
        OIL.append(df.MW_OIL.sum())
        HYDRO.append(df.MW_HYDROELECTRIC.sum())
        GEOTHERMAL.append(df.MW_GEOTHERMAL.sum())
        WIND.append(df.MW_WIND.sum())
        SOLAR.append(df.MW_SOLAR.sum())
        NUCLEAR.append(df.MW_NUCLEAR.sum())
        OTHER.append(df.MW_OTHER.sum())
        YEAR.append(i)

    dct_MW = {'COAL':COAL,'NATURALGAS':NATURALGAS,'OIL':OIL,'HYDRO':HYDRO,'WIND':WIND,'SOLAR':SOLAR,'NUCLEAR':NUCLEAR}

    dct_gen_plot = {}
    for item in dct_MW.items():
        dct_gen_plot[item[0]] = list([item[1][0],item[1][16],item[1][27]])
    years = list([YEAR[0],YEAR[16],YEAR[27]])

    df_mw = pd.DataFrame(dct_gen_plot,columns=list(dct_gen_plot.keys()), index = years)

    fig, ax = plt.subplots(figsize=(20,20))
    df_mw.plot.barh(ax=ax)

    legend = plt.legend(fontsize='x-large')
    plt.setp(legend.get_texts(), color='black')
    ax.set_title('Generation Type by Year',color='black',fontsize=24)
    plt.xticks(fontsize=20)
    plt.xlabel('Total Megawatt Hours',fontsize=24)
    plt.yticks(fontsize=20)
    plt.savefig('../images/gen_by_year.png',dpi=60)

    ##########################

    type_agg = df.groupby(['DATAYEAR']).agg({'is_0':'sum','is_1':'sum','is_2':'sum','is_3':'sum'})
    type_agg = type_agg.reset_index()
    type_agg['TOTAL'] = type_agg['is_0'] + type_agg['is_1'] + type_agg['is_2'] + type_agg['is_3']
    type_agg = type_agg.rename(columns={'is_0':'Other','is_1':'Municipal','is_2':'Cooperative','is_3':'Retail Power Marketer'})

    pct_muni = []
    pct_coop = []
    pct_rpm = []
    pct_other = []


    for i in range(1990,2018):
        df2 = type_agg[type_agg['DATAYEAR'] == i]
        pct_muni.append(df2.Municipal.mean()/df2.TOTAL.mean())
        pct_coop.append(df2.Cooperative.mean()/df2.TOTAL.mean())
        pct_rpm.append(df2['Retail Power Marketer'].mean()/df2.TOTAL.mean())
        pct_other.append(df2.Other.mean()/df2.TOTAL.mean())
        YEAR.append(i)
        
    dct_gen_plot = {'Other':pct_other,'Municipal':pct_muni,'Cooperative':pct_coop,'Retail Power Marketer':pct_rpm}
    for item in dct_gen_plot.items():
        dct_gen_plot[item[0]] = list([item[1][0],item[1][16],item[1][27]])
    years = list([YEAR[0],YEAR[16],YEAR[27]])

    labels = list(dct_gen_plot.keys())
    sizes_1 = list([dct_gen_plot['Other'][0],dct_gen_plot['Municipal'][0],dct_gen_plot['Cooperative'][0],dct_gen_plot['Retail Power Marketer'][0]])
    sizes_2 = list([dct_gen_plot['Other'][1],dct_gen_plot['Municipal'][1],dct_gen_plot['Cooperative'][1],dct_gen_plot['Retail Power Marketer'][1]])
    sizes_3 = list([dct_gen_plot['Other'][2],dct_gen_plot['Municipal'][2],dct_gen_plot['Cooperative'][2],dct_gen_plot['Retail Power Marketer'][2]])
    explode = (0,.1,0,0)

    fig, ax = plt.subplots(3,1,figsize=(12,30))
    
    ax.flatten()[0].pie(sizes_1, labels=labels,explode=explode,autopct='%1.1f%%',textprops={'fontsize': 18})
    ax.flatten()[1].pie(sizes_2, labels=labels,explode=explode,autopct='%1.1f%%',textprops={'fontsize': 18})
    ax.flatten()[2].pie(sizes_3, labels=labels,explode=explode,autopct='%1.1f%%',textprops={'fontsize': 18})
    ax.flatten()[0].set_title(years[0],fontsize=24)
    ax.flatten()[1].set_title(years[1],fontsize=24)
    ax.flatten()[2].set_title(years[2],fontsize=24)
    plt.savefig('../images/ownershiptypes.png',dpi=60)
