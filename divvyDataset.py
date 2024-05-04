import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV file to check its structure
file_path = 'Divvy_Trips_20240503_17k.csv'
divvy_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe and its columns
divvy_data.head(), divvy_data.columns

#print(divvy_data)


# Select the first 10 unique stations from both "FROM STATION NAME" and "TO STATION NAME"
unique_stations = pd.unique(divvy_data[['FROM STATION NAME', 'TO STATION NAME']].values.ravel('K'))
selected_stations = unique_stations[:100]

# Generate a Watts-Strogatz small-world network for 10 nodes
# k is the number of nearest neighbors, p is the probability of rewiring each edge
k = 3  # Each node is connected to its three nearest neighbors
p = 0.5  # Rewiring probability

# Degree Distribution
def plot_degree_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]  # Get degrees for all nodes
    fig, ax = plt.subplots(figsize=(7, 7))  # Adjusted for a single histogram
    ax.hist(degrees, bins=range(max(degrees)+1), color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Degree Distribution')
    ax.set_xlabel('Degree')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def calculate_average_path_length(G):
    if nx.is_connected(G):
        # If the graph is connected, calculate the average path length directly
        return nx.average_shortest_path_length(G)
    else:
        # If the graph is disconnected, find the largest connected component and calculate its average path length
        largest_cc = max(nx.connected_components(G), key=len)
        subgraph = G.subgraph(largest_cc)
        return nx.average_shortest_path_length(subgraph)
    
def calculate_clustering_coefficients(G):
    # Calculate the clustering coefficient for each node
    node_clustering = nx.clustering(G)
    
    # Calculate the average clustering coefficient for the whole graph
    average_clustering = nx.average_clustering(G)

    return node_clustering, average_clustering

def calculate_betweenness_centrality(G):
    # Calculate betweenness centrality for each node
    node_betweenness_centrality = nx.betweenness_centrality(G)
    # Calculate the average betweenness centrality
    average_betweenness_centrality = sum(node_betweenness_centrality.values()) / len(node_betweenness_centrality)
    return node_betweenness_centrality, average_betweenness_centrality
    
# Create the Watts-Strogatz model
ws_graph = nx.watts_strogatz_graph(n=len(selected_stations), k=k, p=p)
labels = {i: station for i, station in enumerate(selected_stations)}  # Map nodes to station names

# Draw the Watts-Strogatz graph with labels
plt.figure(figsize=(10, 10))
nx.draw(ws_graph, labels=labels, with_labels=True, node_color='lightblue', node_size=200, edge_color='gray', font_size=9, font_weight='bold')
plt.title("Watts-Strogatz Small-World Network (10 Stations)")

#degree distribution
plot_degree_distribution(ws_graph)

# Assuming ws_graph is your Watts-Strogatz graph
average_path_length = calculate_average_path_length(ws_graph)
print("Average path length:", average_path_length)

# Assuming ws_graph is your Watts-Strogatz graph
node_clustering, average_clustering = calculate_clustering_coefficients(ws_graph)
print("Average Clustering Coefficient:", average_clustering)
print("Node Clustering Coefficients:", node_clustering)

# Assuming ws_graph is your Watts-Strogatz graph
node_betweenness, average_betweenness = calculate_betweenness_centrality(ws_graph)
print("Average Betweenness Centrality:", average_betweenness)
print("Node Betweenness Centrality:", node_betweenness)

plt.show()

# Calculate Betweenness Centrality
#betweenness_centrality = nx.betweenness_centrality(ws_graph)

# Average Path Length
# Since the graph can be disconnected, we handle this by calculating the average path length only for the largest connected component
'''
largest_cc = max(nx.connected_components(ws_graph), key=len)
subgraph = ws_graph.subgraph(largest_cc)
average_path_length = nx.average_shortest_path_length(subgraph)
'''

'''
# Clustering Coefficient
clustering_coefficient = nx.clustering(ws_graph)
average_clustering_coefficient = sum(clustering_coefficient.values()) / len(clustering_coefficient)
'''

