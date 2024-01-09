#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Emily Henry
CS 3950
Module 8 - Final Project
May 4, 2022
"""

import pandas as pd

weatherDF = pd.read_csv(r"/Users/emily/Desktop/EmpireMonth Weather.csv")

DunesDF = pd.read_csv(r"/Users/emily/Desktop/Sleeping Bear Dunes NL Visitation by Month(1).csv")

WDF = pd.DataFrame(weatherDF)
DDF = pd.DataFrame(DunesDF)


WDF = WDF.replace("Avg. Temperature °C (°F)", "Avg. Temperature °F")
WDF = WDF.replace("Min. Temperature °C (°F)", "Min. Temperature °F")
WDF = WDF.replace("Max. Temperature °C (°F)", "Max. Temperature °F")


WDF = WDF.drop(index=[0,2,4], axis = 0)

WDF = WDF.reset_index(drop=True)

WDF.iat[0,0] ="Avg. Temperature °F"
WDF.iat[1,0] = "Min. Temperature °F"
WDF.iat[2,0] = "Max. Temperature °F"
WDF = WDF.replace("("," ")
WDF = WDF.replace(")"," ")
WDF.drop(index =[4],  axis = 0,inplace=True)
WDF = WDF.set_index("Unnamed: 0")

print(WDF)

DDF = DDF.replace(",","",regex=True)
DDF["JAN"] = pd.to_numeric(DDF["JAN"], downcast="integer")
DDF["FEB"] = pd.to_numeric(DDF["FEB"], downcast="integer")
DDF["MAR"] = pd.to_numeric(DDF["MAR"], downcast="integer")
DDF["APR"] = pd.to_numeric(DDF["APR"], downcast="integer")
DDF["MAY"] = pd.to_numeric(DDF["MAY"], downcast="integer")
DDF["JUN"] = pd.to_numeric(DDF["JUN"], downcast="integer")
DDF["JUL"] = pd.to_numeric(DDF["JUL"], downcast="integer")
DDF["AUG"] = pd.to_numeric(DDF["AUG"], downcast="integer")
DDF["SEP"] = pd.to_numeric(DDF["SEP"], downcast="integer")
DDF["OCT"] = pd.to_numeric(DDF["OCT"], downcast="integer")
DDF["NOV"] = pd.to_numeric(DDF["NOV"], downcast="integer")
DDF["DEC"] = pd.to_numeric(DDF["DEC"], downcast="integer")
print(DDF.describe())
print(DDF.head())
DEC = DDF['DEC']
JAN = DDF['JAN']
FEB = DDF['FEB']
MAR = DDF['MAR']
APR = DDF['APR']
MAY = DDF['MAY']
JUN = DDF['JUN']
JUL = DDF['JUL']
AUG = DDF['AUG']
SEP = DDF['SEP']
OCT = DDF['OCT']
NOV = DDF['NOV']

DFWINT = pd.concat([DEC,JAN,FEB],ignore_index = True)
DFSPRNG = pd.concat([MAR,APR,MAY],ignore_index = True)
DFSUMMER = pd.concat([JUN,JUL,AUG],ignore_index=True)
DFFALL = pd.concat([SEP,OCT,NOV],ignore_index=True)

#DATA = {"WINTER":DFWINT,"SPRING":DFSPRNG,"SUMMER":DFSUMMER,"FALL":DFFALL}



DFWINT= pd.DataFrame(DFWINT)
DFSPRNG = pd.DataFrame(DFSPRNG)
DFSUMMER = pd.DataFrame(DFSUMMER)
DFFALL = pd.DataFrame(DFFALL)



DDF2 = pd.concat([DFWINT,DFSPRNG,DFSUMMER,DFFALL],axis=1)
DDF2.columns = ["WINTER", "SPRING", "SUMMER", "FALL"]
print(DDF2)

import scipy.stats as stats
# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(DDF2["WINTER"],DDF2["SPRING"],DDF2["SUMMER"],DDF2["FALL"])
print("F VALUE= ",fvalue,"\nP VALUE = ", pvalue)

import statsmodels.api as sm
from statsmodels.formula.api import ols

DDF2_melt = pd.melt(DDF2.reset_index(), id_vars=['index'], value_vars=['WINTER','SPRING','SUMMER','FALL'])


DDF2_melt = DDF2_melt.rename(columns={"variable":"Seasons"})
print(DDF2_melt.columns)
print(DDF2)

import matplotlib.pyplot as plt
import seaborn as sns
ax = sns.boxplot(x='Seasons', y='value', data=DDF2_melt, color='#99c2a2')
ax = sns.swarmplot(x="Seasons", y="value", data=DDF2_melt, color='#7d0013',size=3)
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(Seasons)', data=DDF2_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

print(WDF.January)









