# Network-Analysis
Online Social Network Analysis

**Introduction:**

- Simulated a small-world network using the Watts-Strogatz model to study urban transportation systems. 
- Goal was to analyze degree distribution, clustering coefficient, and average path length, and observe network growth by adding nodes. 
Using the Girvan-Newman algorithm, we identified and categorized clusters for strategic areas like Service and Maintenance, Targeted Marketing, and Expansion Planning. 

This project provided insights into network connectivity, community structure, and resilience, enhancing our understanding of small-world networks for real-world applications.

**Data Collection:**

- The Divvy bike-sharing dataset from the City of Chicago's open data portal includes over 21 million trips made between 2013 and 2019, offering detailed trip data such as station names, IDs, and trip IDs. We used the Watts-Strogatz small-world network model to simulate node and edge additions, reflecting real-world network patterns with high clustering and short path lengths.
- Starting with a medium-sized network, we incrementally grew it to observe changes in clustering, path length, and degree distribution. This approach ensured computational efficiency, allowing for timely analysis of metrics like betweenness centrality and clustering coefficient.
- By simulating large datasets, we measured critical network metrics to evaluate efficiency and connectivity. Using the Girvan-Newman algorithm, we detected clusters and categorized them into strategic areas like service, marketing, and expansion. This method accurately simulated network growth and real-world characteristics.

**Project Process:**

- Initiated the project by simulating the Divvy dataset through a small-world network model to uncover distinct communities that could enhance our understanding of service, marketing, and expansion strategies.
- This process involved transforming raw data on trip pairs into a realistic network model using a customized approach instead of the standard watts_strogatz_graph function, allowing for more precise reflection of real-world travel patterns.
- By manually modeling network connections based on actual trip data, we maintained essential small-world characteristics such as high clustering and short path lengths, thereby enhancing the network's utility for practical insights. Through rigorous network analysis and the application of the Girvan-Newman algorithm, identified meaningful communities that directly informed strategic decisions in areas like marketing and expansion, demonstrating the effectiveness of our tailored approach despite initial challenges.

**Project Result:**

This project simulates a small-world network model to analyze and uncover efficient pathways and strategic community structures within the network. By integrating tightly connected clusters and strategic long-range edges, we've replicated hallmark traits of small-world networks, applicable in various strategic analyses.

Key Findings:

- Average Path Length: Confirms the small-world network characteristic of short path lengths, demonstrating quick and efficient travel between nodes, with stability as new nodes are added.

![apl](https://github.com/user-attachments/assets/75458abd-4d42-48ad-9a6c-3caa7b0b67a3)

- Degree Distribution: Shows a left-skewed pattern typical of small-world networks where most nodes have moderate connections, but a few act as highly connected hubs, providing a balance that enhances the network's resilience (output snippet attached).

![degree_1](https://github.com/user-attachments/assets/58a5c637-ce2b-42fc-aae4-edba97207cbc)

- Focusing on the clustering coefficient, a measure of how tightly connected a community is. The Watts Strogatz model is designed to generate networks with high clustering coefficients, where nodes tend to form closely-knit communities. Our implementation showed results consistent with this pattern. By manually creating the small-world network, we maintained high clustering while incorporating occasional long-range connections(output snippet attached). This combination of tightly connected clusters and strategic long-range edges is a hallmark of the small-world model.

![CC_FINAL](https://github.com/user-attachments/assets/fcd56d2b-16a9-4f6d-8a4d-826fa5d99354)

- Community Detection: Using the Girvan-Newman algorithm, we detected communities that conformed to expected network patterns. We analyzed clusters for density and utilized betweenness centrality for targeted marketing, service, and maintenance insights, and expansion planning (output snippet attached).

![clusters](https://github.com/user-attachments/assets/ece6e562-7d8a-45b0-829d-730286b6730a)


**Future Work:**

- One improvement would involve developing predictive models to simulate future network growth and changes based on historical data. This approach would assist in planning network expansions or identifying potential bottlenecks, allowing for a proactive response to emerging challenges.
- Another promising avenue lies in enhancing visualizations.

**References:**

- NetworkX: https://networkx.github.io/documentation/stable/index.html
- Matplotlib: https://matplotlib.org/stable/index.html
- Gephi: https://gephi.org/users/
- Divvy Dataset: https://data.cityofchicago.org/Transportation/Divvy-Trips/fg6s-gzvg/about_data
- Girvan-Newman Algorithm: https://ieeexplore.ieee.org/document/6859714
- Watts-Strogatz Small-World Network Model: https://chih-ling-hsu.github.io/2020/05/15/watts-strogatz

These resources were instrumental in developing and understanding the network metrics, analysis techniques, and simulation approaches used throughout the project.
