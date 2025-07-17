import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Define concise labels (under 15 chars each)
concepts = [
    "DROIT<br>EXISTENCE<br>UNIVERSELLE",
    "EXISTENCE<br>RELATION",  # Ubuntu
    "INTERDEPEND<br>UNIVERSELLE", # Buddhism  
    "RESPONSABIL<br>COSMIQUE", # Islam
    "DIGNITÉ<br>INTRINSÈQUE", # Natural law
    "TRANSPARENCE<br>ENTROPIQUE", # Constantinis
    "HARMONIE<br>DYNAMIQUE" # Confucianism
]

# Full tradition descriptions for hover
hover_texts = [
    "Centre: Droit à l'Existence Universelle",
    "Ubuntu: Je suis parce que nous sommes - Existence Relationnelle",
    "Bouddhisme: Tout est interconnecté - Interdépendance Universelle", 
    "Islam: Responsabilité divine et humaine - Responsabilité Cosmique",
    "Droit naturel: Valeur inaliénable - Dignité Intrinsèque",
    "Constantinis: Reflet informationnel - Transparence Entropique",
    "Confucianisme: Équilibre Ciel-Terre-Humanité - Harmonie Dynamique"
]

# More accurate colors for each tradition
colors = [
    '#1FB8CD',  # Central - Strong cyan
    '#FFC185',  # Ubuntu - Orange/Earth (light orange - perfect)
    '#6A4C93',  # Buddhism - Violet/Spiritual (using purple-like color)
    '#52B788',  # Islam - Green/Nature (using a green tone)
    '#5D878F',  # Natural law - Blue/Universal (cyan-blue)
    '#DB4545',  # Constantinis - Red/Science (soft red)
    '#D2BA4C'   # Confucianism - Yellow/Harmony (moderate yellow)
]

# Position nodes in circular arrangement
angles = np.linspace(0, 2*np.pi, 7)[1:]  # 6 points around circle
radius = 3.5

x_coords = [0] + [radius * np.cos(angle) for angle in angles]
y_coords = [0] + [radius * np.sin(angle) for angle in angles]

# Create the figure
fig = go.Figure()

# Add connecting lines between all nodes first (so they appear behind circles)
for i in range(len(x_coords)):
    for j in range(i+1, len(x_coords)):
        fig.add_trace(go.Scatter(
            x=[x_coords[i], x_coords[j]],
            y=[y_coords[i], y_coords[j]],
            mode='lines',
            line=dict(width=3, color='rgba(80,80,80,0.6)'),
            hoverinfo='skip',
            showlegend=False
        ))

# Add nodes (circles with text)
fig.add_trace(go.Scatter(
    x=x_coords,
    y=y_coords,
    mode='markers+text',
    marker=dict(
        size=[100, 80, 80, 80, 80, 80, 80],  # Larger sizes for better readability
        color=colors,
        line=dict(width=4, color='white'),
        opacity=0.95
    ),
    text=concepts,
    textposition="middle center",
    textfont=dict(size=11, color='white', family="Arial Black"),
    hovertemplate='<b>%{hovertext}</b><extra></extra>',
    hovertext=hover_texts,
    showlegend=False
))

# Add bidirectional arrows at connection points
arrow_positions = []
for i in range(len(x_coords)):
    for j in range(i+1, len(x_coords)):
        # Calculate direction vector
        dx = x_coords[j] - x_coords[i]
        dy = y_coords[j] - y_coords[i]
        length = np.sqrt(dx**2 + dy**2)
        
        # Normalize and scale for arrow positions
        dx_norm = dx / length
        dy_norm = dy / length
        
        # Position arrows closer to the circles (not at exact midpoint)
        offset1 = 0.7  # Distance from first circle
        offset2 = 0.7  # Distance from second circle
        
        arrow1_x = x_coords[i] + offset1 * dx_norm
        arrow1_y = y_coords[i] + offset1 * dy_norm
        arrow2_x = x_coords[j] - offset2 * dx_norm
        arrow2_y = y_coords[j] - offset2 * dy_norm
        
        # Add arrow symbols as scatter points
        fig.add_trace(go.Scatter(
            x=[arrow1_x, arrow2_x],
            y=[arrow1_y, arrow2_y],
            mode='markers',
            marker=dict(
                symbol='triangle-right',
                size=8,
                color='rgba(60,60,60,0.8)',
                line=dict(width=1, color='white')
            ),
            hoverinfo='skip',
            showlegend=False
        ))

# Update layout
fig.update_layout(
    title="Fondements Droit à l'Existence",
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False,
        range=[-5, 5]
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False,
        range=[-5, 5]
    ),
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(255,255,255,1)',  # White background for better contrast
    font=dict(size=12)
)

# Ensure equal aspect ratio for circular appearance
fig.update_yaxes(scaleanchor="x", scaleratio=1)

# Save the chart
fig.write_image("droit_existence_diagram.png", width=1200, height=1000)
fig.show()