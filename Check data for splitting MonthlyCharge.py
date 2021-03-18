#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("Company A - data.csv")


# In[3]:


data.head(10)


# In[4]:


data.drop(['id','customerID'],axis = 1, inplace = True)


# In[5]:


internet = data.loc[:,('InternetService','MonthlyCharges')]
internet.rename(columns={"InternetService": "x"}, inplace = True)

contract = data.loc[:,('Contract','MonthlyCharges')]
contract.rename(columns={"Contract": "x"}, inplace = True)

payment = data.loc[:,('PaymentMethod','MonthlyCharges')]
payment.rename(columns={"PaymentMethod": "x"}, inplace = True)


# In[6]:


frames = [internet, contract, payment]
dat = pd.concat(frames,axis=0,join="outer",ignore_index=False)


# In[7]:


#dat['MonthlyCharges'] = dat['MonthlyCharges'].astype(int)


# In[8]:


sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})


# In[9]:


pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(dat, row="x", hue="x", aspect=20, height=0.8, palette=pal)
g.map(sns.kdeplot, "MonthlyCharges",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=3)
g.map(sns.kdeplot, "MonthlyCharges", clip_on=False, color="w", lw=2, bw_adjust=.5)
g.map(plt.axhline, y=0, lw=2, clip_on=False)
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, 0.2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
g.map(label, "MonthlyCharges")
g.set(ylim=(0, 0.05))

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)


# In[10]:


internet2 = data.loc[:,('InternetService','TotalCharges')]
internet2.rename(columns={"InternetService": "z"}, inplace = True)

contract2 = data.loc[:,('Contract','TotalCharges')]
contract2.rename(columns={"Contract": "z"}, inplace = True)

payment2 = data.loc[:,('PaymentMethod','TotalCharges')]
payment2.rename(columns={"PaymentMethod": "z"}, inplace = True)


# In[11]:


frames2 = [internet2, contract2, payment2]
dat2 = pd.concat(frames2,axis=0,join="outer",ignore_index=False)


# In[12]:


dat2['TotalCharges'] = pd.to_numeric(dat2['TotalCharges'], errors='coerce')


# In[15]:


sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

pal2 = sns.cubehelix_palette(10, rot=-.25, light=.7)
g2 = sns.FacetGrid(dat2, row="z", hue="z", aspect=20, height=0.8, palette=pal)
g2.map(sns.kdeplot, "TotalCharges",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=3)
g2.map(sns.kdeplot, "TotalCharges", clip_on=False, color="w", lw=2, bw_adjust=.5)
g2.map(plt.axhline, y=0, lw=2, clip_on=False)
def label(x, color, label):
    ax2 = plt.gca()
    ax2.text(0, 0.2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax2.transAxes)
g2.map(label, "TotalCharges")
g2.set(ylim=(0, 0.001))

# Set the subplots to overlap
g2.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g2.set_titles("")
g2.set(yticks=[])
g2.despine(bottom=True, left=True)


# In[16]:


internet3 = data.loc[:,('InternetService','tenure')]
internet3.rename(columns={"InternetService": "z1"}, inplace = True)

contract3 = data.loc[:,('Contract','tenure')]
contract3.rename(columns={"Contract": "z1"}, inplace = True)

payment3 = data.loc[:,('PaymentMethod','tenure')]
payment3.rename(columns={"PaymentMethod": "z1"}, inplace = True)


# In[17]:


frames3 = [internet3, contract3, payment3]
dat3 = pd.concat(frames3,axis=0,join="outer",ignore_index=False)


# In[18]:


sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

pal3 = sns.cubehelix_palette(10, rot=-.25, light=.7)
g3 = sns.FacetGrid(dat3, row="z1", hue="z1", aspect=20, height=0.8, palette=pal)
g3.map(sns.kdeplot, "tenure",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=3)
g3.map(sns.kdeplot, "tenure", clip_on=False, color="w", lw=2, bw_adjust=.5)
g3.map(plt.axhline, y=0, lw=2, clip_on=False)
def label(x, color, label):
    ax3 = plt.gca()
    ax3.text(0, 0.2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax3.transAxes)
g3.map(label, "tenure")
g3.set(ylim=(0, 0.05))

# Set the subplots to overlap
g3.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g3.set_titles("")
g3.set(yticks=[])
g3.despine(bottom=True, left=True)


# In[ ]:




