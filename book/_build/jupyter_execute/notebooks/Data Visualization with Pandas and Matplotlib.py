# Data Visualization with Pandas and Matplotlib

# import library 
import pandas as pd 
import matplotlib.pyplot as plt 

# display plot in the notebook 
%matplotlib inline 

# set figuresize and fontsize 
plt.rcParams['figure.figsize'] = (8,6) 
plt.rcParams['font.size'] = 14 

# read data 
drink_cols = ["country", 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv("../data/drinks.csv", header=0, names=drink_cols, na_filter=False)

## Data Exploration

# examine first few rows 
drinks.head() 

# observations and columns 
drinks.shape

# data structure 
drinks.info() 

# numerical summary 
drinks.describe() 

##  Histogram: show the distribution of a numerical variable

# sort the beer columns and split it into 3 groups 
drinks.beer.sort_values().values

# compare with histogram 
drinks.beer.plot(kind="hist", bins=3);

# try more bins 
drinks.beer.plot(kind="hist", bins=20); 

# add title and labels 
drinks.beer.plot(kind="hist", bins=20, title="Histogram of Beer Servings")
plt.xlabel("Beer Survings") 
plt.ylabel("Frequency")
# show plot 
plt.show() 

# compare with density plot(smooth version of a histogram) 
drinks.beer.plot(kind="density", xlim=(0, 500));

## Scatter Plot: show the relationship between two numerical variables

# select the beer and wine columns and sort by beer 
drinks[["beer", "wine"]].sort_values(by="beer").values

# comapre with scatter plot 
drinks.plot(kind="scatter", x="beer", y="wine"); 

# add transparency 
drinks.plot(kind='scatter', x="beer", y="wine", alpha=0.3); 

# vary point color by spirit servings 
drinks.plot(kind="scatter", x="beer", y="wine", c="spirit", colormap="Blues"); 

# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']]); 

# increase figure size 
# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']], figsize=(10,8)); 

##  Bar Plot: show a numerical comparison across different categories

# count the number of countries in each continent 
drinks.continent.value_counts()

# compare with bar plot 
drinks.continent.value_counts().plot(kind="bar"); 

# calculate the mean alcohol amounts for each continent 
drinks.groupby('continent').mean() 

# side-by-side bar plots 
drinks.groupby('continent').mean().plot(kind='bar'); 

# drop the liters column
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar'); 

# stacked bar plots 
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True); 

## Box Plot: show quartiles (and outliers) for one or more numerical variables
__Five-Number Summary__
* min = minimum value
* 5% = first quartile (Q1) = median of the lower half of the data
* 50% = second quartile (Q2) = median of the data
* 75% = third quartile (Q3) = median of the upper half of the data
* max = maximum value
(More useful than mean and standard deviation for describing skewed distributions)
* Interquartile Range (IQR) = Q3 - Q1

__Outliers__ 
* below Q1 - 1.5 * IQR
* above Q3 + 1.5 * IQR

# sort the spirit column 
drinks.spirit.sort_values().values 

# show five-number summary of spirit 
drinks.spirit.describe() 

# compare with boxplot 
drinks.spirit.plot(kind='box');  

# include multiple variables 
drinks.drop('liters', axis=1).plot(kind='box'); 

## Line Plot: show the trend of a numerical variable over time

# read ufo data 
ufo = pd.read_csv("../data/ufo.csv")
ufo['Time'] = pd.to_datetime(ufo.Time) 
ufo['Year'] = ufo.Time.dt.year 

# examine first few rows  
ufo.head() 

# observations and columns 
ufo.shape 

# data structure 
ufo.info() 

# numerical summary 
ufo.describe()  

# count the number of ufo reports each year (and sort by year)
ufo.Year.value_counts().sort_index() 

# compare with line plot 
ufo.Year.value_counts().sort_index().plot();

# don't use a line plot when there is no logical ordering 
drinks.continent.value_counts().plot(kind='line'); 

## Grouped Box Plots: show one box plot for each group

# remainder: boxplot of beer survings 
drinks.beer.plot(kind='box'); 

# boxplot of beer survings group by continent 
drinks.boxplot(column='beer', by='continent'); 

# boxplot of all numerical columns group by continent 
drinks.boxplot(by='continent'); 

## Grouped Histograms: show one histogram for each group

# remainder: histogram of beer survings 
drinks.beer.plot(kind='hist', bins=20); 

# histogram of beer  survings group by continent 
drinks.hist(column='beer', by='continent'); 

# share the x-axis 
drinks.hist(column='beer', by='continent', sharex=True); 

# share the x and y axis 
drinks.hist(column='beer', by='continent', sharex=True, sharey=True); 

# change the layout 
drinks.hist(column='beer', by='continent', sharex=True, layout=(2, 3));

 ## Assorted Functionality

# saving a plot to a file 
drinks.beer.plot(kind='hist', bins=20, title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Freequency")
plt.savefig("beer_survings.png") # .png, .tiff, .pdf, .jpeg 

# list available plot style 
plt.style.available

# use plot style: ggplot 
plt.style.use('ggplot')

# histogram of beer survings in ggplot style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

# use plot style: ggplot 
plt.style.use('seaborn') 

# histogram of beer survings in seaborn style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

# use plot style: ggplot 
plt.style.use('fivethirtyeight') 

# histogram of beer survings in fivethirtyeight style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")