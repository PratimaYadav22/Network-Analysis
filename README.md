# Network-Analysis
Online Social Network Analysis

**Introduction**
We wanted to explore the fascinating world of network dynamics and structure by simulating a smallworld network using the Watts-Strogatz model. This model is especially good at helping us understand 
networks that naturally show high clustering and short path lengths, characteristics often seen in social, 
technological, and biological networks.
Our main objective was to replicate the behavior of real-world networks by using the Watts-Strogatz 
model to simulate urban transportation systems. We focused on analyzing key measures like degree 
distribution, clustering coefficient, and average path length. These metrics would help us uncover insights 
into the network's connectivity and community structure, ultimately guiding us in understanding 
strategic hubs and efficient pathways in these real-world networks.
We also wanted to see how network properties evolved as more nodes were incrementally added. 
Observing this gradual growth gave us valuable insights into the network's topology, showing how it 
influences resilience and community formation.
Additionally, by employing the Girvan-Newman algorithm, we aimed to identify clusters within the 
network and analyze their structure and connectivity. This method allowed us to categorize clusters 
based on density, enabling us to define strategic areas like Service and Maintenance, Targeted Marketing, 
and Expansion Planning.
Overall, this structured approach helped us understand the unique properties of small-world networks 
while also offering practical insights applicable to various types of real-world networks, from 
transportation and logistics to social networks. With this project, we hoped to deepen our understanding 
of network theory and contribute to more effective network design and management.
Online Social Network Analysis
**Data Collection:**
The Divvy bike-sharing dataset, available through the City of Chicago's open data portal, is a treasure 
trove of urban cycling information. It holds a wealth of records from over 21 million trips made between 
2013 and 2019, providing a comprehensive snapshot of urban mobility trends Divvy Dataset. This dataset 
offers us rich details on trip data, such as station names and IDs for the starting and ending points, as 
well as trip IDs, allowing us to understand the movement patterns of the city's residents and tourists.
In our analysis, we leveraged the Watts-Strogatz small-world network model to simulate the gradual 
addition of nodes and edges. This approach let us mirror the intricate patterns found in real-world 
networks, balancing high clustering coefficients and short path lengths.
Deciding on the network size required a nuanced approach that combined research insights and practical 
considerations. Studies on small-world and urban networks often suggest starting with a medium-sized 
network that can grow incrementally, in line with the Watts-Strogatz model's characteristics. By carefully 
choosing the initial nodes, nearest neighbors, and the increment sizes, we were able to observe changes 
in clustering, path length, and degree distribution over time.
To ensure computational efficiency, we selected an initial size that could be expanded incrementally 
without overwhelming our resources. This allowed us to run analyses like betweenness centrality and 
clustering coefficient calculations while ensuring that our observations could be carried out promptly.
Our approach remained consistent with our initial plan of simulating a large dataset to uncover network 
metrics. We used the Watts-Strogatz model to replicate realistic network structures and maintained 
incremental growth patterns, which helped us identify strategic hubs.
After generating the simulated data, we measured critical network metrics like clustering coefficient and 
average path length to evaluate the network's efficiency and connectivity. Applying the Girvan-Newman 
algorithm allowed us to detect clusters, which were then categorized into strategic areas like service, 
marketing, and expansion. Using the Watts-Strogatz model helped us accurately simulate network 
growth patterns, aligning with our initial vision and reflecting real-world network characteristics.
Online Social Network Analysis
**Project Process:**
In We began by setting out to simulate a large Divvy dataset using a small-world network model. Our goal 
was to identify distinct communities that would provide insights into areas such as service and 
maintenance, marketing, and expansion planning. Throughout this journey, we encountered challenges 
building realistic networks and identifying meaningful clusters, but eventually, we managed to create a 
framework that delivered practical and actionable insights.
It all started with understanding the structure and relationships embedded in the Divvy dataset. Every 
trip was recorded as a pair of stations: the starting point and the destination. Our aim was to simulate 
this network using a small-world model that mirrored the real-world travel patterns found in the data. 
We carefully examined the dataset to identify the appropriate station pairs and set up the network 
model.
When it came to generating the network, we initially relied on the built-in watts_strogatz_graph function 
from NetworkX. Unfortunately, this approach didn't accommodate specific edge creation based on the 
trip pairs, resulting in a graph that didn’t align with the real-world structure. Previously our code was:
To resolve this, we recognized that manually modeling the network was essential to ensure accurate edge 
relationships. Rather than using a generic network generation function, we designed a custom approach 
that incorporated actual trip pairs from the dataset, ensuring the network structure reflected real-world 
data while still maintaining the key characteristics of small-world networks like high clustering and short 
path lengths referring watts_strogatz_graph function . We constructed a ring lattice structure, mapped 
station pairs based on trip counts, and used modular arithmetic to establish nearest neighbors. We then 
added a rewiring mechanism to introduce some randomness while ensuring that meaningful edge 
weights were maintained. Code snippet after the resolution:
Online Social Network Analysis
Next, we turned to network analysis and calculated important metrics. We focused on the clustering 
coefficient to assess how well the network formed tightly connected clusters, a vital characteristic of 
small-world networks. We also calculated the average path length to evaluate how efficiently nodes were 
connected, revealing the network's ability to enable quick communication between different regions. 
Lastly, we visualized the degree distribution to understand the structure and connectivity patterns of the 
nodes. This revealed the classic small-world pattern, where most nodes had moderate connections while 
a few acted as highly connected hubs, demonstrating the network's resilience.
After successfully simulating the network, we used the Girvan-Newman algorithm to detect distinct 
communities. However, tuning the parameters to accurately identify significant clusters required careful 
adjustment. We eventually evaluated the clusters based on density and size, categorizing them into 
actionable insights for service and maintenance, marketing, and expansion planning. The clusters aligned 
with areas of high ridership, highlighting potential hubs for targeted marketing or expansion.
Visualizing each iteration of the network was also crucial. We labeled nodes with their respective station 
IDs, and used different shades to distinguish clusters, revealing their unique characteristics and spatial 
relationships. This visualization approach helped us grasp the network's structure, making it easier to 
identify interconnectedness and clustering patterns.
Despite the challenges we faced, this custom small-world network model accurately represented the 
Divvy dataset. It provided realistic insights into service, marketing, and expansion opportunities, 
underscoring the value of custom modeling in complex networks and highlighting areas for further 
exploration and refinement.
Online Social Network Analysis
**Project Result:**
Our work on this project provided us with valuable insights into the properties of networks and confirmed 
our expectations about how small-world networks behave when generated using the Watts-Strogatz 
model.
We focused on the clustering coefficient, a measure of how tightly connected a community is. The WattsStrogatz model is designed to generate networks with high clustering coefficients, where nodes tend to 
form closely-knit communities. Our implementation showed results consistent with this pattern. By 
manually creating the small-world network, we maintained high clustering while incorporating 
occasional long-range connections(output snippet attached). This combination of tightly connected 
clusters and strategic long-range edges is a hallmark of the small-world model.
Next, we examined the average path length, a metric that indicates how efficiently nodes are connected. 
Small-world networks are expected to have relatively short and consistent path lengths, which our model 
confirmed(output snippet attached). As new nodes were added incrementally, the network's efficiency 
remained stable, validating the small-world properties and ensuring quick travel between nodes.
Online Social Network Analysis
When we visualized the network's degree distribution, the results showed the characteristic left-skewed 
pattern typical of small-world networks. Most nodes had a moderate number of connections, with a 
small minority serving as highly connected hubs(output snippet attached). This distribution illustrated 
how the network balanced connectivity across its nodes, demonstrating the network's resilience.
Online Social Network Analysis
Lastly, we applied the Girvan-Newman algorithm for community detection. It accurately identified 
community structures that matched known network patterns. Each detected cluster was analyzed for its 
density, leading to valuable insights in areas like service and maintenance, targeted marketing (with the 
aid of betweenness centrality), and expansion planning(output snippet attached).
Below is the output file:
output.txt
Online Social Network Analysis
**Discussion of project:**
After spending considerable time on this project, we believe it was highly productive and met our initial 
goals. Our deep exploration of small-world networks provided us with a comprehensive understanding 
of their structure and practical applications. By using a combination of network metrics and community 
detection techniques, we gained a clearer picture of how real-world networks behave and evolve over 
time.
One key learning was about network growth dynamics. We learned how the properties of small-world 
networks significantly influence growth and connectivity. By manually creating the small-world structure, 
we could see how these networks support both high clustering and long-range connections, which 
demonstrated the clear benefits of small-world properties in enhancing connectivity and efficiency. This 
insight has obvious applications in real-world scenarios.
The community analysis process was another eye-opener. Using these techniques, we could effectively 
identify distinct clusters and categorize them into strategic areas such as maintenance, marketing, and 
expansion planning. This provided a clear framework for understanding how clusters form and can be 
leveraged for practical purposes.
In summary, this project solidified our understanding of network analysis and highlighted the practical 
side of network theory in the real world. With these insights, future projects can build on these 
foundations, refining the analysis and developing even more precise applications.
**Future Work:**
With additional time to work on this project, there are several areas we could explore further to deepen 
our understanding and broaden practical applications. One improvement would involve developing 
predictive models to simulate future network growth and changes based on historical data. This 
approach would assist in planning network expansions or identifying potential bottlenecks, allowing for 
a proactive response to emerging challenges.
Another promising avenue lies in enhancing visualizations. By creating interactive visualizations to 
dynamically explore various metrics and cluster characteristics, stakeholders could gain a more intuitive 
understanding of network properties. This would help make the data more accessible and valuable to a 
broader audience. We could also benefit from extended analysis with different network generation 
models, such as the Barabási-Albert preferential attachment model or the Erdős-Rényi random graph 
model. Comparing these with the Watts-Strogatz model would offer a more comprehensive view of 
network dynamics, revealing unique insights that each model brings to the table.
Finally, implementing multiple community detection algorithms beyond Girvan-Newman—like Louvain 
or Infomap—could help uncover different clustering patterns and identify the most effective methods for 
this specific network. Exploring these advanced algorithms would ensure that we capture the most 
accurate representation of network clusters possible.
Online Social Network Analysis
**References:**
NetworkX: https://networkx.github.io/documentation/stable/index.html
Matplotlib: https://matplotlib.org/stable/index.html
Gephi: https://gephi.org/users/
Divvy Dataset: https://data.cityofchicago.org/Transportation/Divvy-Trips/fg6s-gzvg/about_data
Girvan-Newman Algorithm: https://ieeexplore.ieee.org/document/6859714
Watts-Strogatz Small-World Network Model: https://chih-ling-hsu.github.io/2020/05/15/watts-strogatz
These resources were instrumental in developing and understanding the network metrics, analysis techniques, 
and simulation approaches used throughout the project.
