import plotly.graph_objects as go

# Putting nodes in lists makes positioning easier
inputs = ["Emails", "Alerts", "Spam Reports"]
work = ["Total Inputs"]
outputs = ["False Positives", "Incidents", "Requests", "Incident Communication Emails", "FTRs", "Simple Spam"]
secondary_outputs= ["General Risk FTR", "High Risk FTR", "Tuned"]
#define nodes
nodes = inputs + work + outputs + secondary_outputs
#
node_index = {name: i for i, name in enumerate(nodes)}
#flows in human-readable format
flows = [
    ("Alerts", "Total Inputs", 8000),
    ("Emails", "Total Inputs", 10000),
    ("Spam Reports", "Total Inputs", 12000),
    ("Total Inputs", "Incidents", 800),
    ("Total Inputs", "False Positives", 14000),
    ("Total Inputs", "Requests", 142),
    ("Total Inputs", "FTRs", 1200),
    ("Total Inputs", "Incident Communication Emails", 6400),
    ("False Positives", "Tuned", 1000),
    ("False Positives", "Simple Spam", 10000),
    ("FTRs", "General Risk FTR", 1100),
    ("FTRs", "High Risk FTR", 100),
]
#convert human-readable flows to machine-readable
sources = [node_index[s] for s, t, v in flows]
targets = [node_index[t] for s, t, v in flows]
values  = [v for s, t, v in flows]

node_colors = [
    # Inputs (3)
    "#00429d", "#73a2c6", "#e2e2e2",
    #total inputs
    "#00429d",
    # Outputs (6)
    "#f4777f", "#93003a", "#fdb863", "#b2abd2", "#5e3c99", "#d6604d",
    # Secondary outputs (3)
    "#f4a582", "#ca0020", "#92c5de"
]

#link colors if needed
"""link_colors = [
    "Hex1", "Hex2", etc
]"""

fig = go.Figure(data=[go.Sankey(
    arrangement="snap",  # required!
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes,
        color=node_colors,

        x=[0.1, 0.1, 0.1,
        #"Emails", "Alerts", "Spam Reports"
           .25,
        #total inputs
           0.5, 0.5, 0.5, 0.5, 0.5,
        #"False Positives", "Incidents", "Requests", "Incident Communication", "FTRs",
           0.75, .75, 0.75, 0.75],
        #Simple Spam, General Risk FTR, "High Risk FTR", "Tuned"

        y=[0.9, 0.15, 0.3,
           # "Emails", "Alerts", "Spam Reports"
           .5,
           #totalinputs
           0.25, 0.1, 0.6, 0.8, 0.9,
           # "False Positives", "Incidents", "Requests", "Incident Communication", "FTRs",
           0.3, 0.8, 0.9, 0.1],
           # "Simple Spam", "General Risk FTR", "High Risk FTR", "Tuned"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        #color=link_colors
    )
)])

fig.update_layout(
    title_text="Fully Custom-Colored Sankey Diagram",
    font_size=12,
    plot_bgcolor="white"
)

fig.show()
#freeze where you want it
#fig.write_html("sankey_layout.html", include_plotlyjs="cdn")
