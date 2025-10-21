import numpy as np
import streamlit as st
import networkx as nx
import plotly.graph_objs as go
from processors import processors as pcr

# Page Configurations
st.set_page_config(layout="wide")

# Page Title
st.markdown("# Birthday Paradox")

# Number of individuals to be considered
size = st.slider("Number of individuals", min_value=2, max_value=366)

# Generate population and create the internal graph
population = pcr.generate_population(size)
G = pcr.create_graph(population)


# ========= NETWORKX GRAPH =========
pos = nx.spring_layout(G, k=0.5, iterations=50)

for node, p in pos.items():
    G.nodes[node]['pos'] = p

# Establish the edges
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=1,color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])

#Add nodes to plotly scatter plot
node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='Blues', 
        color=[],
        size=20,
        colorbar=dict(
            thickness=10,
            title='Connections',
            xanchor='left',
            dtick=1
        ),
        line=dict(width=0)))

# Add nodes from G into the node_traces
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)
    
    person = node
    birthday = G.nodes[node]['bday']
    node_trace['text'] += (f"Person {person} -- Birthday {birthday}",)

# Determine number of adjacencies (connections) -- for node colorway 
for node, adjacencies in enumerate(G.adjacency()):
    node_trace['marker']['color']+=tuple([len(adjacencies[1])]) 

# Plot the final figure
fig = go.Figure(data=[edge_trace, node_trace],
            layout=go.Layout(
                title='Networkx Visual',
                title_x=0.45,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

st.plotly_chart(fig, use_container_width=True) 


# ========= Logarithmic Graph =========
# Establish x-axis and y-axis values
x_vals = np.arange(2, 367)
y_vals = np.array([pcr.birthday_paradox_plot(n) for n in x_vals])

# Point to plot
y_selected = pcr.birthday_paradox_plot(size)

fig = go.Figure()

fig.add_traces([
    # Plot the static logarithmic function
    go.Scatter(x=x_vals, 
               y=y_vals,
               mode='lines',
               line=dict(color='#4292c6'), 
               showlegend=False),
    
    # Plot the selected y value (size)
    go.Scatter(x=[size], 
               y=[y_selected], 
               mode='markers',
               marker=dict(color='white', 
                           size=12), 
               showlegend=False)
])

# Axis labels
fig.update_layout(
    title="Logarithmic Visual",
    title_x=0.45,
    xaxis_title="Number of People", xaxis_range=[2, 366],
    yaxis_title="Probability", yaxis_range=[0, 1]
)

st.plotly_chart(fig, use_container_width=True)


# ========= STATISTICS =========
st.markdown(f" **Theoretical chance** that at least two individuals share a birthday: **{pcr.birthday_paradox_prob(size)}%**")
st.markdown(f" **Number of individuals** in the group: **{pcr.calculate_prob(population)[0]}**")
st.markdown(f" **Number of people** who share a birthday: **{pcr.calculate_prob(population)[1]}**")
st.markdown(f" **Percentage of people with at least one birthday match**: **{pcr.calculate_prob(population)[2]}**")