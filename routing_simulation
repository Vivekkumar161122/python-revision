import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# Parameters
NUM_GROUND = 30
NUM_UAV = 15
NUM_HAPS = 5
TOTAL_NODES = NUM_GROUND + NUM_UAV + NUM_HAPS
FAILURE_RATES = [0.1, 0.2, 0.3, 0.4, 0.5]
NUM_TRIALS = 20
JAMMING_PROB = 0.2

def create_topology():
    G = nx.Graph()
    for i in range(NUM_GROUND):
        G.add_node(i, type='ground')
    for i in range(NUM_GROUND, NUM_GROUND+NUM_UAV):
        G.add_node(i, type='uav')
    for i in range(NUM_GROUND+NUM_UAV, TOTAL_NODES):
        G.add_node(i, type='haps')
    pos = {i: (random.random(), random.random()) for i in G.nodes()}
    for i in G.nodes():
        for j in G.nodes():
            if i < j:
                dist = np.linalg.norm(np.array(pos[i])-np.array(pos[j]))
                if dist < 0.3:
                    G.add_edge(i, j, weight=dist)
    for uav in range(NUM_GROUND, NUM_GROUND+NUM_UAV):
        for _ in range(3):
            g = random.randint(0, NUM_GROUND-1)
            G.add_edge(uav, g, weight=0.5)
    for haps in range(NUM_GROUND+NUM_UAV, TOTAL_NODES):
        for _ in range(5):
            uav = random.randint(NUM_GROUND, NUM_GROUND+NUM_UAV-1)
            G.add_edge(haps, uav, weight=0.8)
    return G, pos

def simulate_routing(G, mode='centralized', failure_rate=0.2, jamming=False):
    H = G.copy()
    edges = list(H.edges())
    num_fail = int(len(edges) * failure_rate)
    failed_edges = random.sample(edges, num_fail)
    H.remove_edges_from(failed_edges)
    
    if jamming:
        for e in H.edges():
            if random.random() < JAMMING_PROB:
                H[e[0]][e[1]]['loss'] = 0.5
            else:
                H[e[0]][e[1]]['loss'] = 0.0
    else:
        for e in H.edges():
            H[e[0]][e[1]]['loss'] = 0.0

    sources = list(range(1, NUM_GROUND))
    target = 0
    delivered = 0
    total = len(sources) * 10
    latencies = []
    
    for src in sources:
        for _ in range(10):
            try:
                if mode == 'centralized':
                    if H.has_edge(src, target):
                        path = [src, target]
                    else:
                        continue
                elif mode == 'static':
                    path = nx.shortest_path(H, src, target, weight='weight')
                elif mode == 'rarn':
                    try:
                        path = nx.shortest_path(H, src, target, weight='weight')
                    except nx.NetworkXNoPath:
                        path = None
                        for uav in range(NUM_GROUND, NUM_GROUND+NUM_UAV):
                            if H.has_edge(src, uav) and H.has_edge(uav, target):
                                path = [src, uav, target]
                                break
                        if path is None:
                            continue
                success = True
                latency = 0
                for i in range(len(path)-1):
                    u, v = path[i], path[i+1]
                    if H.has_edge(u, v):
                        loss = H[u][v].get('loss', 0.0)
                        if random.random() < loss:
                            success = False
                            break
                        latency += H[u][v]['weight'] * 10
                    else:
                        success = False
                        break
                if success:
                    delivered += 1
                    latencies.append(latency)
            except nx.NetworkXNoPath:
                continue
    pdr = delivered / total if total > 0 else 0
    avg_lat = np.mean(latencies) if latencies else 0
    return pdr, avg_lat

def main():
    G, pos = create_topology()
    results = defaultdict(list)
    for mode in ['centralized', 'static', 'rarn']:
        for fr in FAILURE_RATES:
            pdrs = []
            lats = []
            for _ in range(NUM_TRIALS):
                pdr, lat = simulate_routing(G, mode, failure_rate=fr, jamming=True)
                pdrs.append(pdr)
                lats.append(lat)
            results[mode].append((fr, np.mean(pdrs), np.mean(lats)))
    
    plt.figure()
    for mode in ['centralized', 'static', 'rarn']:
        frs = [x[0] for x in results[mode]]
        pdrs = [x[1] for x in results[mode]]
        plt.plot(frs, pdrs, marker='o', label=mode)
    plt.xlabel('Link Failure Rate')
    plt.ylabel('Packet Delivery Ratio')
    plt.title('PDR vs Link Failure Rate')
    plt.legend()
    plt.grid(True)
    plt.savefig('pdr_vs_failure.png')
    plt.show()
    print("Simulation complete. Results saved as pdr_vs_failure.png")

if __name__ == '__main__':
    main()
