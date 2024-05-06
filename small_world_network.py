import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random
import itertools

# Load station data from a CSV file
file_path = 'Divvy_Trips_20240503_17k.csv'
divvy_data = pd.read_csv(file_path)

# Function to map station IDs to nodes
def create_node_labels_from_ids(df, max_num_nodes):
    trips = df[['FROM STATION ID', 'TO STATION ID']].dropna().value_counts().reset_index()
    trips.columns = ['FROM', 'TO', 'COUNT']

    unique_station_ids = pd.unique(trips[['FROM', 'TO']].values.ravel('K'))
    selected_station_ids = unique_station_ids[:max_num_nodes]

    station_labels = {i: int(station_id) for i, station_id in enumerate(selected_station_ids)}
    return station_labels
def create_station_name_labels(df, max_num_nodes):
    # Get pairs of station IDs and station names
    trips = df[['FROM STATION ID', 'FROM STATION NAME']].drop_duplicates()
    trips.columns = ['STATION ID', 'STATION NAME']

    trips_to = df[['TO STATION ID', 'TO STATION NAME']].drop_duplicates()
    trips_to.columns = ['STATION ID', 'STATION NAME']

    # Combine 'from' and 'to' pairs
    all_stations = pd.concat([trips, trips_to]).drop_duplicates()

    # Map station IDs to station names
    station_id_to_name = dict(zip(all_stations['STATION ID'], all_stations['STATION NAME']))

    # Create node labels by limiting to max_num_nodes
    unique_station_ids = list(station_id_to_name.keys())[:max_num_nodes]
    node_labels = {i: station_id_to_name[station_id] for i, station_id in enumerate(unique_station_ids)}

    return node_labels

# Function to generate a list of edges with weights based on station trip pairs
def generate_station_trip_edges(df, station_labels):
    # Group by FROM STATION ID and TO STATION ID to count trips
    trip_counts = df.groupby(['FROM STATION ID', 'TO STATION ID']).size().reset_index(name='COUNT')
    
    edges = []
    id_to_index = {v: k for k, v in station_labels.items()}

    for _, row in trip_counts.iterrows():
        from_station = id_to_index.get(row['FROM STATION ID'])
        to_station = id_to_index.get(row['TO STATION ID'])
        weight = row['COUNT']

        if from_station is not None and to_station is not None:
            edges.append((from_station, to_station, weight))

    return edges

# Function to update or extend labels dynamically using station IDs
def update_node_labels_with_ids(existing_labels, num_new_nodes, remaining_ids):
    next_index = max(existing_labels.keys()) + 1 if existing_labels else 0
    updated_labels = {next_index + i: remaining_ids[i] for i in range(min(num_new_nodes, len(remaining_ids)))}
    existing_labels.update(updated_labels)
    return existing_labels

# Custom function to incrementally expand a small-world graph with weighted edges
def expand_small_world_graph(G, station_trip_edges, new_nodes, k, p):
    num_existing_nodes = len(G.nodes)
    total_nodes = num_existing_nodes + new_nodes

    G.add_nodes_from(range(num_existing_nodes, total_nodes))

    for node in range(num_existing_nodes, total_nodes):
        for i in range(1, (k // 2) + 1):
            neighbor = (node + i) % total_nodes
            reverse_neighbor = (node - i) % total_nodes

            # Add edges based on station trip edges
            for edge in station_trip_edges:
                if edge[0] == node and edge[1] == neighbor:
                    G.add_edge(node, neighbor, weight=edge[2])
                if edge[0] == node and edge[1] == reverse_neighbor:
                    G.add_edge(node, reverse_neighbor, weight=edge[2])

    # Rewiring process as per the small-world algorithm
    for node in range(total_nodes):
        for i in range(1, (k // 2) + 1):
            neighbor = (node + i) % total_nodes
            if G.has_edge(node, neighbor) and (p > 0):
                if random.random() < p:
                    new_neighbor = random.choice(list(set(range(total_nodes)) - {node} - set(G[node])))
                    if G.has_edge(node, new_neighbor) is False:
                        G.add_edge(node, new_neighbor, weight=1)

    return G

# Function to apply Girvan-Newman clustering
def girvan_newman_clusters(G):
    if G.number_of_edges() == 0:
        return [list(G.nodes())]
    communities = nx.community.girvan_newman(G)
    return tuple(sorted(c) for c in next(itertools.islice(communities, 1)))

# Function to analyze clusters and generate insights
def analyze_clusters(G, clusters):
    insights = {
        "Focused Service and Maintenance": [],
        "Targeted Marketing": [],
        "Expansion Planning": []
    }

    for cluster in clusters:
        subgraph = G.subgraph(cluster)
        density = nx.density(subgraph)
        num_edges = subgraph.number_of_edges()
        # Focused Service and Maintenance: High internal usage
        if density > 0.2:  # Example threshold
            insights["Focused Service and Maintenance"].append(cluster)

        # Targeted Marketing: Low usage areas
        elif density < 0.1 and len(cluster) > 1:  # Example threshold
            insights["Targeted Marketing"].append(cluster)
            #print closeness centrality for this cluster
            node_betweenness_centrality = nx.betweenness_centrality(subgraph)            
            
            max_node = max(node_betweenness_centrality, key=node_betweenness_centrality.get)
            print(f"\nTargeted Marketing : node_betweenness_centrality_max: {node_betweenness_centrality[max_node]}")
            print(f"max_node: {max_node}")
        # Expansion Planning: Small clusters with sparse connections
        elif len(cluster) < 10:  # Example size threshold
            insights["Expansion Planning"].append(cluster)

    return insights

# Function to visualize the graph with clusters
def visualize_graph_with_clusters(G, clusters, labels, title):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))

    # Create a color mapping for each cluster
    color_map = {}
    for idx, cluster in enumerate(clusters):
        for node in cluster:
            color_map[node] = idx

    # Generate colors based on clusters
    colors = [color_map.get(node, -1) for node in G.nodes]

    nx.draw(G, pos, node_color=colors, node_size=200, cmap=plt.cm.Set3, edge_color='gray', with_labels=True, labels=labels)
    plt.title(title)
    plt.show()


# Function to visualize the entire graph and separate subplots for each insight
def visualize_graph_with_insight_colors(G, insights, labels, title):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))

    # Define color mapping for each insight
    color_mapping = {
        "Focused Service and Maintenance": 'green',
        "Targeted Marketing": 'blue',
        "Expansion Planning": 'red'
    }

    # Initialize a default color for nodes not matching any insight
    default_color = 'blue'

    # Create a color map for all nodes
    color_map = {node: default_color for node in G.nodes}

    # Assign colors based on insights
    for insight, color in color_mapping.items():
        for cluster in insights[insight]:
            for node in cluster:
                color_map[node] = color

    # Extract node colors for all nodes
    node_colors = [color_map.get(node, default_color) for node in G.nodes]

    # Draw the graph with the node colors
    nx.draw(G, pos, node_color=node_colors, node_size=200, edge_color='gray', with_labels=False)
    
    # Draw the labels separately with customized font size and color
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=4, font_color='lightgray')
    
    plt.title(title)
    plt.show()


    
def calculate_network_metrics(G):
    largest_cc = max(nx.connected_components(G), key=len)
    subgraph = G.subgraph(largest_cc)
    avg_path_length = nx.average_shortest_path_length(subgraph)
    avg_clustering = nx.average_clustering(G)

    #degree_distribution = nx.degree_centrality(G)
    
    degrees = [G.degree(n) for n in G.nodes()]  # Get degrees for all nodes
    
    return degrees, avg_path_length, avg_clustering
    

def visualize_network_metrics(degrees, avg_path_length, clustering_coeffs, num_iterations):
    fig, ax = plt.subplots(figsize=(7, 7))  # Adjusted for a single histogram
    ax.hist(degrees, bins=range(max(degrees)+1), color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Degree Distribution')
    ax.set_xlabel('Degree')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, num_iterations + 1), clustering_coeffs, marker='o', linestyle='-', color='blue')
    plt.xlabel('Iteration')
    plt.ylabel('Average Clustering Coefficient')
    plt.title('Clustering Coefficient Over Iterations')
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, num_iterations + 1), average_path_lenth, marker='o', linestyle='-', color='blue')
    plt.xlabel('Iteration')
    plt.ylabel('Average Path Length')
    plt.title('Average path length Over Iterations')
    plt.grid(True)
    plt.show()
    
# Initial parameters
max_num_nodes = 20  # Max number of nodes overall
all_node_labels = create_node_labels_from_ids(divvy_data, max_num_nodes)
#station_name_labels = create_station_name_labels(divvy_data, max_num_nodes)

station_trip_edges = generate_station_trip_edges(divvy_data, all_node_labels)

# Watts-Strogatz graph parameters
k = 3
rewiring_prob = 0.5
initial_nodes = 3  # Number of starting nodes
increment_per_iteration = 1000  # Number of nodes to add per iteration
num_iterations = 5

# Remaining station IDs to be used
remaining_station_ids = list(set(divvy_data['FROM STATION ID']).union(set(divvy_data['TO STATION ID'])))
remaining_station_ids = [sid for sid in remaining_station_ids if sid not in all_node_labels.values()]

# Initialize the small-world graph
G_expanded = nx.Graph()
G_expanded.add_nodes_from(range(initial_nodes))

# Initialize node labels dynamically
dynamic_node_labels = {i: all_node_labels[i] for i in range(initial_nodes)}
#dynamic_node_labels = {i: station_name_labels[i] for i in range(initial_nodes)}

clustering_coeffs = []
average_path_lenth = []
# Iteratively expand the graph, cluster it, visualize it, and analyze clusters
for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}: Adding {increment_per_iteration} nodes")
    G_expanded = expand_small_world_graph(G_expanded, station_trip_edges, increment_per_iteration, k, rewiring_prob)

    # Update node labels for the newly added nodes
    dynamic_node_labels = update_node_labels_with_ids(dynamic_node_labels, increment_per_iteration, remaining_station_ids)
    degrees, avg_path_length, avg_clustering = calculate_network_metrics(G_expanded)
    clustering_coeffs.append(avg_clustering)
    average_path_lenth.append(avg_path_length)
    # Apply Girvan-Newman to identify clusters
    clusters = girvan_newman_clusters(G_expanded)

    # Visualize the graph with clusters
    #visualize_graph_with_clusters(G_expanded, clusters, dynamic_node_labels, f"Small-World Network Iteration {iteration + 1} ({len(G_expanded.nodes)} Nodes)")

    # Analyze clusters and provide insights
    cluster_insights = analyze_clusters(G_expanded, clusters)
    print("\n--- Insights from Clusters ---")
    for insight_type, clusters in cluster_insights.items():
        print(f"{insight_type}: {len(clusters)} clusters")
    print("\n" )
    #visualize_graph_with_subplots(G_expanded, cluster_insights, dynamic_node_labels, "Network Analysis")
    #visualize_graph_with_insight_colors(G_expanded, cluster_insights, dynamic_node_labels, "Clustered Graph")

    

visualize_network_metrics(degrees, avg_path_length, clustering_coeffs, num_iterations)
# Plot the clustering coefficient trend over iterations

