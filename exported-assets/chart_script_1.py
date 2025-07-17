import plotly.graph_objects as go
import plotly.io as pio

# Create flowchart diagram
fig = go.Figure()

# Define positions and text for each step
steps = [
    # Step 1: Top
    {"text": "CONVERGENCES<br>PHILOSOPHIQUES<br>UNIVERSELLES", "x": 0.5, "y": 0.9, "color": "#8B00FF", "width": 0.3},
    
    # Step 2: Collaborative writing
    {"text": "RÉDACTION<br>COLLABORATIVE<br>INTERCULTURELLE", "x": 0.5, "y": 0.75, "color": "#1E90FF", "width": 0.25},
    
    # Step 3: Global consultation
    {"text": "CONSULTATION<br>MONDIALE<br>INCLUSIVE", "x": 0.5, "y": 0.6, "color": "#32CD32", "width": 0.25},
    
    # Step 4: Universal adoption
    {"text": "ADOPTION PAR<br>CONSENSUS<br>UNIVERSEL", "x": 0.5, "y": 0.45, "color": "#FF8C00", "width": 0.25},
    
    # Step 5: Three parallel branches
    {"text": "INTÉGRATION<br>JURIDIQUE", "x": 0.2, "y": 0.3, "color": "#DC143C", "width": 0.2},
    {"text": "ÉDUCATION<br>TRANSFORMATIVE", "x": 0.5, "y": 0.3, "color": "#FFD700", "width": 0.2},
    {"text": "PRATIQUES<br>SOCIALES", "x": 0.8, "y": 0.3, "color": "#FF69B4", "width": 0.2},
    
    # Step 6: Conscious society
    {"text": "SOCIÉTÉ<br>CONSCIENTE DE<br>SON EXISTENCE", "x": 0.5, "y": 0.15, "color": "#FFD700", "width": 0.3},
    
    # Step 7: Evaluation
    {"text": "ÉVALUATION ET<br>RÉVISION<br>CONTINUE", "x": 0.5, "y": 0.02, "color": "#808080", "width": 0.25}
]

# Add rectangles for each step
for i, step in enumerate(steps):
    fig.add_shape(
        type="rect",
        x0=step["x"] - step["width"]/2,
        y0=step["y"] - 0.04,
        x1=step["x"] + step["width"]/2,
        y1=step["y"] + 0.04,
        fillcolor=step["color"],
        line=dict(color="black", width=2),
        opacity=0.8
    )
    
    # Add text
    fig.add_annotation(
        x=step["x"],
        y=step["y"],
        text=step["text"],
        showarrow=False,
        font=dict(color="white", size=10, family="Arial Black"),
        align="center"
    )

# Add arrows between steps
arrows = [
    # Vertical arrows
    {"x0": 0.5, "y0": 0.86, "x1": 0.5, "y1": 0.79},  # 1->2
    {"x0": 0.5, "y0": 0.71, "x1": 0.5, "y1": 0.64},  # 2->3
    {"x0": 0.5, "y0": 0.56, "x1": 0.5, "y1": 0.49},  # 3->4
    
    # From step 4 to three branches
    {"x0": 0.5, "y0": 0.41, "x1": 0.2, "y1": 0.34},  # 4->left
    {"x0": 0.5, "y0": 0.41, "x1": 0.5, "y1": 0.34},  # 4->center
    {"x0": 0.5, "y0": 0.41, "x1": 0.8, "y1": 0.34},  # 4->right
    
    # From three branches to conscious society
    {"x0": 0.2, "y0": 0.26, "x1": 0.5, "y1": 0.19},  # left->6
    {"x0": 0.5, "y0": 0.26, "x1": 0.5, "y1": 0.19},  # center->6
    {"x0": 0.8, "y0": 0.26, "x1": 0.5, "y1": 0.19},  # right->6
    
    # From conscious society to evaluation
    {"x0": 0.5, "y0": 0.11, "x1": 0.5, "y1": 0.06},  # 6->7
    
    # Feedback arrow from evaluation back to top (curved)
    {"x0": 0.375, "y0": 0.02, "x1": 0.125, "y1": 0.9, "curved": True}
]

# Add arrows
for arrow in arrows:
    if arrow.get("curved"):
        # Add curved feedback arrow
        fig.add_annotation(
            ax=arrow["x0"], ay=arrow["y0"],
            x=arrow["x1"], y=arrow["y1"],
            arrowhead=2, arrowsize=1, arrowwidth=2,
            arrowcolor="gray",
            axref="x", ayref="y"
        )
    else:
        fig.add_annotation(
            ax=arrow["x0"], ay=arrow["y0"],
            x=arrow["x1"], y=arrow["y1"],
            arrowhead=2, arrowsize=1, arrowwidth=2,
            arrowcolor="black",
            axref="x", ayref="y"
        )

# Update layout
fig.update_layout(
    title="Mise en Œuvre d'une Déclaration du Droit",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
    plot_bgcolor="white",
    paper_bgcolor="white"
)

# Save the chart
fig.write_image("declaration_droit_existence_flowchart.png", width=800, height=1000)