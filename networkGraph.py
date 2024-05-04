import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import itertools

# Function to calculate network metrics for a given graph
def calculate_network_metrics(G):
    largest_cc = max(nx.connected_components(G), key=len)
    subgraph = G.subgraph(largest_cc)
    avg_path_length = nx.average_shortest_path_length(subgraph)
    avg_clustering = nx.average_clustering(G)
    return avg_path_length, avg_clustering

# Function to apply the Girvan-Newman method for community detection
def girvan_newman_clusters(G):
    if G.number_of_edges() == 0:
        return [list(G.nodes())]  # No clusters if graph has no edges

    communities = nx.community.girvan_newman(G)
    limited_partitions = itertools.islice(communities, 1)  # Retrieve only the first partition
    return tuple(sorted(c) for c in next(limited_partitions))

# Function to map node labels to station names
def create_node_labels(df, max_num_nodes):
    unique_stations = pd.unique(df[['FROM STATION NAME', 'TO STATION NAME']].values.ravel('K'))
    selected_stations = unique_stations[:max_num_nodes]
    return {i: station for i, station in enumerate(selected_stations)}

# Function to generate graph labels dynamically based on the number of nodes
def generate_labels(node_labels, num_nodes):
    return {i: node_labels.get(i, f'Node {i}') for i in range(num_nodes)}

# Function to analyze clusters for insights
def analyze_clusters(G, clusters, node_labels):
    insights = {
        "Service and Maintenance": [],
        "Targeted Marketing": [],
        "Expansion Planning": []
    }

    for cluster in clusters:
        subgraph = G.subgraph(cluster)
        density = nx.density(subgraph)
        num_edges = subgraph.number_of_edges()
        print(f"Cluster Density: {density:.3f}, Number of Edges: {num_edges}, length of cluster:{len(cluster)}")
        # Service and Maintenance: High internal usage
        if density > 0.1:  # Example threshold
            insights["Service and Maintenance"].append(cluster)

        # Targeted Marketing: Low usage areas
        if density < 0.05 :  # Example thresholds
            insights["Targeted Marketing"].append(cluster)

        # Expansion Planning: Peripheral clusters
        if len(cluster) < 10:  # Small clusters as potential candidates for expansion
            insights["Expansion Planning"].append(cluster)

    return insights

# Function to run the simulation, analyze clusters, and provide insights
def small_world_simulation_and_insights(num_iterations, start_nodes, node_increment, nearest_neighbors, rewiring_prob, all_node_labels):
    for iteration in range(num_iterations):
        num_nodes = start_nodes + (node_increment * iteration)
        print(f"\nIteration {iteration + 1}: {num_nodes} Nodes")
        
        G = nx.watts_strogatz_graph(n=num_nodes, k=nearest_neighbors, p=rewiring_prob)
        
        clusters = girvan_newman_clusters(G)
        print(f"Number of Clusters: {len(clusters)}")
        
        avg_path_length, avg_clustering = calculate_network_metrics(G)
        print(f"Average Path Length: {avg_path_length}")
        print(f"Average Clustering Coefficient: {avg_clustering}")
        
        # Create a subset of labels that match the current graph's nodes
        current_labels = generate_labels(all_node_labels, num_nodes)
        
        # Analyze clusters to generate insights
        insights = analyze_clusters(G, clusters, current_labels)
        
        # Display insights
        print("\n--- Cluster Insights ---")
        for category, cluster_list in insights.items():
            print(f"{category}: {len(cluster_list)} Clusters")
            for idx, cluster in enumerate(cluster_list, 1):
                names = [current_labels.get(n, f'Node {n}') for n in cluster]
                #print(f"  {category} Cluster {idx}: {names}")
        
        # Plot the graph with station names as labels
        plt.figure(figsize=(10, 10))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color='lightblue', node_size=200, edge_color='gray', with_labels=True, labels=current_labels)
        for cluster in clusters:
            nx.draw_networkx_nodes(G, pos, nodelist=cluster, node_color=[(0.5, 0.5, 0.5)], node_size=200)
        plt.title(f"Small-World Network - Iteration {iteration + 1} ({num_nodes} Nodes)")
        plt.show()
        plt.close()  # Close the current plot

# Load station data from CSV file
file_path = 'Divvy_Trips_20240503_17k.csv'
divvy_data = pd.read_csv(file_path)

# Create node labels for up to 800 stations
all_node_labels = create_node_labels(divvy_data, 800)

# Parameters for the simulation
num_iterations = 4
start_nodes = 100
node_increment = 100
nearest_neighbors = 3
rewiring_prob = 0.5

# Run the simulation with insights analysis
small_world_simulation_and_insights(num_iterations, start_nodes, node_increment, nearest_neighbors, rewiring_prob, all_node_labels)
