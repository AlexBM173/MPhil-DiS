import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import seaborn as sns

with open("ps1.pkl", "rb") as f:
    data = pickle.load(f)

print(data)

hist = pd.DataFrame.hist(data=data, column="vx")
plt.savefig("vx_hist.png")

hist = pd.DataFrame.hist(data=data, column="vy")
plt.savefig("vy_hist.png")

hist = pd.DataFrame.hist(data=data, column="vz")
plt.savefig("vz_hist.png")

hist = pd.DataFrame.hist(data=data, column="R2")
plt.savefig("R2_hist.png")

hist = pd.DataFrame.hist(data=data, column="p")
plt.savefig("p_hist.png")
plt.clf()

pairplot = sns.pairplot(data=data, vars=["vx","vy"], kind="scatter", diag_kind="hist")
plt.savefig("vx_vy_pairplot.png")
plt.clf()

pairplot = sns.pairplot(data=data)
plt.savefig("all_pairplot.png")
plt.clf()

scatter = sns.scatterplot(data=data, x="vx", y="vy", s=20, color="k", alpha=1)
histplot = sns.histplot(data=data, x="vx", y="vy", bins=35, pthresh=0.1, cmap="plasma", cbar=True)
kdeplot = sns.kdeplot(data=data, x="vx", y="vy", levels=5, color="k", fill=False)
plt.rcParams.update({'font.size': 20})
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel("vx", fontsize=20)
plt.ylabel("vy", fontsize=20)
plt.xticks([-3,-2,-1,0,1,2,3], fontsize=15)
plt.yticks([-3,-2,-1,0,1,2,3], fontsize=15)
plt.title("KDE plot of vx and vy", fontsize=20)
plt.savefig("vx_vy_kde.png", dpi=600, bbox_inches="tight")
plt.clf()