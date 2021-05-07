# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:33:06 2020

@author: David
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("crime.csv", encoding="latin-1")
tmp = df.head(1000)
df.columns.values

"""
Leitfragen 1/3
"""

"""Welche Straftaten sind am häufigsten?"""
plot = sns.countplot(x="OFFENSE_CODE_GROUP",
              data = df,
              order = df['OFFENSE_CODE_GROUP'].value_counts().index)
plt.setp(plot.get_xticklabels(), rotation=90)


table = df.groupby(["OFFENSE_CODE_GROUP"]).INCIDENT_NUMBER.count().to_frame()
table = table.sort_values('INCIDENT_NUMBER', ascending=False)


"""Wie hat sich die Zahl der schweren Straftaten im Laufe der Jahre entwickelt?"""
#table = df.groupby(["UCR_PART", "YEAR"], as_index=False).INCIDENT_NUMBER.count()
#table.set_index("UCR_PART").T.plot(kind='bar', stacked=True)

table = df.groupby(["UCR_PART", "YEAR"]).INCIDENT_NUMBER.count()
table.T.plot(kind='bar', stacked=True)

table = df[df['UCR_PART'] == "Part One"]
#table = table.groupby(["YEAR"], as_index=False).INCIDENT_NUMBER.count()
plot = sns.countplot(x="YEAR",
              data = table)


"""Warum ist die Gesamtzahl 2015 und 2018 (so) niedrig?"""
min(df['OCCURRED_ON_DATE'])
max(df['OCCURRED_ON_DATE'])


"""In welchen Stadtgebieten werden, aufgeschlüsselt nach Jahr, die meisten
Straftaten begangen?"""
table = df.groupby(["DISTRICT", "YEAR"],  as_index=False).INCIDENT_NUMBER.count()
table = table.sort_values(['YEAR', 'INCIDENT_NUMBER'], ascending=False)

plot = sns.catplot(
    data=table, kind="bar",
    x="DISTRICT", y="INCIDENT_NUMBER", hue="YEAR")


"""In welchen Stadtgebieten werden die meisten schweren Straftaten ('Part One')
begangen?"""
table = df[df['UCR_PART'] == "Part One"]
plot = sns.countplot(x="DISTRICT", 
                     data = table,
                     order = table['INCIDENT_NUMBER'].value_counts().index)


"""Welche Arten von schweren Straftaten ('Part One') treten in dem Stadtgebiet 'B2' am
häufigsten auf? """
filtered = df[(df['UCR_PART'] == "Part One") & (df['DISTRICT'] == "B2")]

plot = sns.countplot(x="OFFENSE_CODE_GROUP",
              data = filtered,
              order = filtered['OFFENSE_CODE_GROUP'].value_counts().index)
plt.setp(plot.get_xticklabels(), rotation=90)



"""
Leitfragen 2/3
"""

"""
3. Existieren (a) Uhrzeiten, (b) Tage oder (c) Monate an denen mehr
schwere Verbrechen ('Part One') stattfinden?
• Finden Straftaten eher nachts oder tagsüber statt?
• Wann werden somit die meisten Polizisten benötigt?
"""
filtered = df[df['UCR_PART'] == "Part One"]

plot = sns.countplot(x="HOUR",
              data = filtered)

plot = sns.countplot(x="DAY_OF_WEEK",
              data = filtered)

plot = sns.countplot(x="MONTH",
              data = filtered)




"""
4. Welche leichten Straftaten ('Part Tree') benötigen (vermutlich)
Verkehrspolizisten?
• Welches sind die 5 Straßen, in denen die meisten Verkehrspolizisten benötigt
werden?
"""
filtered = df[df['UCR_PART'] == "Part Three"]

table = filtered.groupby(["OFFENSE_CODE_GROUP"]).INCIDENT_NUMBER.count().to_frame()
table = table.sort_values('INCIDENT_NUMBER', ascending=False)

plot = sns.countplot(x="OFFENSE_CODE_GROUP",
              data = filtered,
              order = filtered['OFFENSE_CODE_GROUP'].value_counts().index)
plt.setp(plot.get_xticklabels(), rotation=90)


filtered.OFFENSE_CODE_GROUP.unique()
filtered = filtered[filtered['OFFENSE_CODE_GROUP'].isin(["Motor Vehicle Accident Response", 'License Plate Related Incidents'])]
table = filtered.groupby(["STREET"]).INCIDENT_NUMBER.count().to_frame()
table = table.sort_values('INCIDENT_NUMBER', ascending=False)
table[0:5]



"""
5. Wie hat sich die Anzahl der Schießereien in den letzten Jahren
entwickelt?
• In welchem Bezirk finden die meisten Schießereien statt?
• In welcher Straße finden die meisten Schießereien statt?
• Zu welchen Uhrzeiten finden die meisten Schießereien statt?
"""

df.SHOOTING.unique()
filtered = df[df['SHOOTING'] == "Y"]


plot = sns.countplot(x="DISTRICT",
              data = filtered,
              order = filtered['DISTRICT'].value_counts().index)

plot = sns.countplot(x="STREET",
              data = filtered,
              order = filtered['STREET'].value_counts().iloc[:10].index)
plt.setp(plot.get_xticklabels(), rotation=90)

plot = sns.countplot(x="HOUR",
              data = filtered,
              order = filtered['HOUR'].value_counts().index)
