import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import time

# 1. Page Configuration for a high-tech theme
st.set_page_config(page_title="AI-Driven Preemptive Suppression System", layout="wide", initial_sidebar_state="expanded")
st.title("🛡️ Project Autonomous Kill-Web: 3D Tactical Simulation")
st.markdown("Inspired by *Palantir AIP Architecture* & *Mission Sudarshan Chakra* paradigms.")

# 2. Sidebar Controls
st.sidebar.header("🕹️ Simulation Controllers")
threat_speed = st.sidebar.slider("Threat Launch Velocity (Mach)", 1, 8, 5)
simulation_speed = st.sidebar.slider("Refresh Delay (Seconds)", 0.1, 1.0, 0.2)
trigger_preemption = st.sidebar.button("Execute Left-of-Launch Suppression")

# 3. System Health Metrics Bar
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="System Status", value="ACTIVE / SECURE", delta="Quantum Encrypted")
col2.metric(label="Active Radar Nodes", value="6,742 / 7,000", delta="Online")
col3.metric(label="AI Compute Latency", value="0.24 ms", delta="-0.02 ms", delta_color="inverse")
col4.metric(label="Threat Condition", value="CRITICAL" if trigger_preemption else "MONITORING", delta="Level 4" if trigger_preemption else "Level 1")

# 4. Core Mathematical Engine: Simulating 3D Trajectories
def generate_trajectories(is_preempted):
    t = np.linspace(0, 1, 50)
    
    # Target 1: Enemy Ballistic Threat (Parabolic Arc)
    x_threat = 50 + 250 * t
    y_threat = 50 + 250 * t
    z_threat = 100 * np.sin(np.pi * t)  # Altitude arc peaking at 100km
    
    # Target 2: Preemptive Counter-Measure Vector
    if is_preempted:
        # Intercepts perfectly at mid-point (t = 0.5)
        x_intercept = 400 - 150 * t
        y_intercept = 400 - 150 * t
        z_intercept = 100 * t  # Rises sharply from the ground
        # Crop intercept vector at the collision point (t=0.5 corresponds to index 25)
        x_intercept = x_intercept[:26]
        y_intercept = y_intercept[:26]
        z_intercept = z_intercept[:26]
    else:
        x_intercept, y_intercept, z_intercept = [], [], []
        
    return x_threat, y_threat, z_threat, x_intercept, y_intercept, z_intercept

# 5. Execute Simulation Data Generation
x_t, y_t, z_t, x_i, y_i, z_i = generate_trajectories(trigger_preemption)

# 6. Building the 3D Plotly Space Engine
fig = go.Figure()

# Plot Layer 1: The Threat Path
fig.add_trace(go.Scatter3d(
    x=x_t, y=y_t, z=z_t,
    mode='lines+markers',
    name='Incoming Hostile Vector',
    line=dict(color='crimson', width=5),
    marker=dict(size=4, color='orange')
))

# Plot Layer 2: The Preemptive Intercept Vector (If Active)
if trigger_preemption:
    fig.add_trace(go.Scatter3d(
        x=x_i, y=y_i, z=z_i,
        mode='lines+markers',
        name='Preemptive Counterstrike Engine',
        line=dict(color='cyan', width=6, dash='dash'),
        marker=dict(size=4, color='teal')
    ))
    
    # Plot Layer 3: The AI Trigger Collision Point
    fig.add_trace(go.Scatter3d(
        x=[x_t[25]], y=[y_t[25]], z=[z_t[25]],
        mode='markers',
        name='Neutralization Coordinates',
        marker=dict(size=12, color='yellow', symbol='diamond', line=dict(color='red', width=2))
    ))

# 7. Chart Layout Customization (Dark Military Mode)
fig.update_layout(
    template="plotly_dark",
    margin=dict(l=0, r=0, b=0, t=40),
    scene=dict(
        xaxis_title="Ground X-Axis (km)",
        yaxis_title="Ground Y-Axis (km)",
        zaxis_title="Altitude (km)",
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.0)),
        aspectratio=dict(x=1, y=1, z=0.6)
    ),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

# 8. Render Engine in Web Layout
st.plotly_chart(fig, use_container_width=True)

# 9. Real-Time Status Log console
st.subheader("🖥️ AI Action Ontology Terminal")
with st.container(border=True):
    st.text(f"[{time.strftime('%H:%M:%S')}] [INFO] Radar Stream processing data packets from 6,742 sources...")
    if trigger_preemption:
        st.text(f"[{time.strftime('%H:%M:%S')}] [ALERT] AI Trapper engine caught a 'Left-of-Launch' structural anomaly at Coords (50, 50, 0).")
        st.text(f"[{time.strftime('%H:%M:%S')}] [ACTION] Auto-allocating response: Deploying Hypersonic Counter-Strike Vector.")
        st.success("Target Successfully Neutralized at 50km Altitude. Collateral Danger: 0%.")
    else:
        st.info("System idling. Scanning airspace footprint for anomalies.")
