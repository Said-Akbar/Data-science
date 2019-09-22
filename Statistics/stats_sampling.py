# 21/09/2019 DataQuest Statistics, mission 1 sampling
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv("wnba.csv")
wnba =file.copy()

def plot_sample(ns=100):
    avg_list = []

    for i in range(ns): # get 100 samples of size 10 and measure their mean
        avg_list.append(wnba['PTS'].sample(n=10, random_state=i).mean())
    pop_mean_pts=wnba['PTS'].mean()
    fig, ax = plt.subplots()
    ax.scatter(x=range(ns),y=avg_list)
    ax.set_ylim([100,300])
    ax.axhline(pop_mean_pts)
    plt.title("Random sampling from population")
    plt.show()

def most_points_position(): # finds which position has the greatest points per game
    wnba['Pts_per_game'] = wnba['PTS']/wnba['Games Played']
    strata = {}
    position_most_points = ''
    pos_pts = 0
    for i in wnba['Pos'].unique():
        strata[i] = wnba[wnba['Pos']==i]
    for i in strata:
        sample = strata[i].sample(n=10, random_state=0)
        avg = sample['Pts_per_game'].mean()
        if avg > pos_pts:
            pos_pts =avg
            position_most_points = i
    return position_most_points

def stratified_sample_plot(): # stratify based on number of games
    group1 = wnba[wnba['Games Played']<=12]
    group2 = wnba[(wnba['Games Played']>12) & (wnba['Games Played']<=22)]
    group3 = wnba[wnba['Games Played']>22]
    avg_list = []
    for i in range(100):
        a=group1['PTS'].sample(n=1, random_state=i)
        b=group2['PTS'].sample(n=2, random_state=i)
        c=group3['PTS'].sample(n=7, random_state=i)
        avg_list.append(pd.concat([a,b,c]).mean())
    plt.scatter(range(1,101), avg_list)
    plt.axhline(wnba['PTS'].mean())
    plt.title("Stratified sampling")
    plt.show()
#stratified_sample_plot()
def clustered_sampling(): #clustered sampling for wnba dataset
    clusters = pd.Series(wnba["Team"].unique()).sample(4,random_state=0)
    cluster = pd.DataFrame()
    for i in clusters:
        cluster=pd.concat([cluster,wnba[wnba["Team"]==i]])
    sampling_error_height = wnba['Height'].mean()-cluster['Height'].mean()
    sampling_error_age = wnba['Age'].mean()-cluster['Age'].mean()
    sampling_error_BMI = wnba['BMI'].mean()-cluster['BMI'].mean()
    sampling_error_points = wnba['PTS'].mean()-cluster['PTS'].mean()
    return sampling_error_points

def main():
    plot_sample()
    print('Most points scored from the position:',most_points_position())
    stratified_sample_plot()
    print("Sampling error (clustered sampling):",clustered_sampling())

if __name__ == "__main__":
    main()
