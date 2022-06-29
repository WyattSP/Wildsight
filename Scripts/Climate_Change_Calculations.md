#The Cost of Coal to Climate Change Emissions Calculations

I have tried to include all sources of information and calculations used in the *The Cost of Coal to Climate Change* Arc Story. Errors or inconsistencies may be present. If errors are found or more accurate information exists I encourage you contact me.

Calculations will be broken down by section as appearing in the article.

kt = kilotonnes
mt = million tonnes

##Mining

Sources for Elk Valley emissions from [1]. Report stats that a portion of GHG emission reductions were from temporary operational disruptions related to COVID-19. It is not clear from the report if reductions in GHG emissions for 2020 under key performance indicators was due to these COVID-19 disruptions. I encourage the company to reach out for clarification so inconsistencies can be corrected.

Total GHG emissions for Scope 1 and Scope 2 appear to be combined for all operations (Coal, Copper, Zinc, etc). As such emission estimates in this report will represent an upper or maximum estimate for Scope 1 and Scope 2 emissions. As stated in [1], GHG emissions associated with Scope 2 emissions, totalling 213 kt is primarily from CdA and Quebrada Blanca (QB) operations. As such, 213 kt was subtracted from the total Scope 1 and Scope 2 GHG emissions reported in [1].

Total emissions are also reported in [1] which includes the emissions associated with the use of coal product sold.

Total Emissions (Scope 1) = 2,582 kt CO<sub>2</sub>e

Total Emissions (Scope 3) = 64,000 kt CO<sub>2</sub>e  

Within this section, Total Emissions (Scope 1) was rounded to 2,600 kt.

##Transportation

###Rail

Estimates for rail transportation from [2].

Total emissions per year = 3,101,936 tonnes CO<sub>2</sub>e
Carloads = 2,782,220

CO<sub>2</sub>e emitted per train car load = Total emissions per year/Carloads
CO<sub>2</sub>e emitted per train car load  = 3,101,936 tonnes CO<sub>2</sub>e/2,782,220
CO<sub>2</sub>e emitted per train car load = 1.115 tonnes CO<sub>2</sub>e

A train car can transport approximately 105 tonnes of coal. Teck Coal Limited exports approximately 25 million tonnes of coal per year (2020).  

Train loads per year = 25,000,000 tonnes of coal / 105 tonnes of coal per train car
Train loads per year = 238,095

Total emissions from rail transport = carloads per year * CO<sub>2</sub>e emitted per train car load
Total emissions from rail transport = 238,096 carloads per year * 1.115 tonnes CO<sub>2</sub>e
Total emissions from rail transport = 265,452 tonnes CO<sub>2</sub>e (0.27 mt CO<sub>2</sub>e)

###Ship

Estimate numbers taken from [3]

Bulk carrier estimated to carry 80,000 tonnes of cargo.

####Low Estimate

11 grams CO<sub>2</sub>e * 10,000 km = 110,000 grams CO<sub>2</sub>e per tonne of cargo
110,000 grams CO<sub>2</sub>e = 0.11 tonnes CO<sub>2</sub>e
0.11 tonnes CO<sub>2</sub>e per tonne of cargo * 25,000,000 tonnes of coal = 2,750,000 CO<sub>2</sub>e
2.75 mt CO<sub>2</sub>e emitted for the transportation of 25 mt of coal

####High Estimate

42 grams CO<sub>2</sub>e * 10,000 km = 420,000 grams CO<sub>2</sub>e per tonne of cargo
420,000 grams CO<sub>2</sub>e = 0.42 tonnes CO<sub>2</sub>e
0.42 tonnes CO<sub>2</sub>e per tonne of cargo * 25,000,000 tonnes of coal = 10,500,000 CO<sub>2</sub>e
10.5 mt CO<sub>2</sub>e emitted for the transportation of 25 mt of coal

##Steel-Making

Total estimate taken from [1]

##Total Emissions

Mining: 2.6 Mt CO<sub>2</sub>e
Rail Transportation: 0.27 Mt CO<sub>2</sub>e
Shipping: 2.75 - 10.5 Mt CO<sub>2</sub>e
Steel Manufacturing: 64 Mt CO<sub>2</sub>e

Total Calculated Emissions: 69.62 - 77.37 Mt CO<sub>2</sub>e per year

#Pi Chart

```python
import plotly.offline
import plotly.graph_objs as go

e_labels = ['Mining (2.6 Mt CO<sub>2</sub>)','Rail Transport (0.27 Mt CO<sub>2</sub>)','Shipping (10.5 Mt CO<sub>2</sub>)','Steel-Making (64 Mt CO<sub>2</sub>)']
emissions = [2.6,0.27,10.5,64]

figE= go.Figure(data=[go.Pie(labels=e_labels, values=emissions, pull=[0, 0, 0, 0.2],textinfo='label+percent')])
figE.update_layout(showlegend=False)
plotly.offline.plot(figE)
```

##References

[1] https://www.teck.com/media/2020-Sustainability-Report-Climate-Change.pdf
[2] https://investor.cpr.ca/key-metrics/default.aspx 
[3] https://www.nature.com/articles/news.2008.574
