"""
Builds a relations graph between GenAI vocabulary terms and the sections of report.md.
Explicit usage (the term itself) and implicit usage (paraphrases) are counted and drawn separately.
Outputs: relations-graph.png, usage-frequency.png, stats.json
"""
import json, re
import matplotlib.pyplot as plt
import networkx as nx

report = open("report.md", encoding="utf-8").read()
terms = json.load(open("terms.json", encoding="utf-8"))["terms"]
term_names = [t["term"] for t in terms]

# 1. Split the report into sections by "## " headings (the table of contents is skipped)
SKIP = {"Contents"}
sections, current = {}, "Intro"
for line in report.splitlines():
    if line.startswith("## "):
        current = line[3:].strip()
        continue
    sections[current] = sections.get(current, "") + line + "\n"
sections = {name: text for name, text in sections.items() if name not in SKIP}

def pattern(phrase):
    return re.compile(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", re.IGNORECASE)

def count_and_mask(text, kind):
    """Count phrases, longest first, and remove them from the text so nothing is counted twice."""
    pairs = sorted(((p, t["term"]) for t in terms for p in t[kind]),
                   key=lambda x: len(x[0]), reverse=True)
    counts = {name: 0 for name in term_names}
    for phrase, term in pairs:
        text, n = pattern(phrase).subn(" ", text)
        counts[term] += n
    return text, counts

# 2. Count explicit usage first, then implicit usage on the remaining text
stats = {name: {"explicit": {}, "implicit": {}} for name in term_names}
for sec, text in sections.items():
    masked, exp = count_and_mask(text, "explicit")
    _, imp = count_and_mask(masked, "implicit")
    for name in term_names:
        stats[name]["explicit"][sec] = exp[name]
        stats[name]["implicit"][sec] = imp[name]
for name in term_names:
    stats[name]["explicit_total"] = sum(stats[name]["explicit"].values())
    stats[name]["implicit_total"] = sum(stats[name]["implicit"].values())

with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

# 3. Draw two bipartite graphs: terms (left) <-> report sections (right)
def draw(ax, kind, color):
    G = nx.Graph()
    G.add_nodes_from(term_names)
    G.add_nodes_from(sections.keys())
    for name in term_names:
        for sec, n in stats[name][kind].items():
            if n > 0:
                G.add_edge(name, sec, weight=n)
    pos = nx.bipartite_layout(G, term_names)
    totals = {n: stats[n][f"{kind}_total"] for n in term_names}

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=color, alpha=0.45,
                           width=[0.6 + G[u][v]["weight"] for u, v in G.edges])
    nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=term_names, node_color=color,
                           node_size=[150 + 90 * totals[n] for n in term_names])
    nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=list(sections), node_color="lightgrey",
                           node_shape="s", node_size=500)
    for node, (x, y) in pos.items():
        is_term = node in totals
        label = f"{node} ({totals[node]})" if is_term else node
        ax.text(x - 0.06 if is_term else x + 0.06, y, label, fontsize=9,
                ha="right" if is_term else "left", va="center")
    ax.set_title(f"{kind.upper()} usage of vocabulary terms in report.md "
                 f"(total: {sum(totals.values())})", fontsize=14)
    ax.margins(x=0.55)
    ax.axis("off")

fig, axes = plt.subplots(1, 2, figsize=(26, 14))
draw(axes[0], "explicit", "#1f77b4")
draw(axes[1], "implicit", "#ff7f0e")
fig.suptitle("Relations graph: GenAI vocabulary ↔ report sections "
             "(edge width = number of uses)", fontsize=16)
plt.tight_layout()
plt.savefig("relations-graph.png", dpi=150, bbox_inches="tight")
plt.show()

# 4. Bar chart: explicit vs implicit totals for each term
order = sorted(term_names, key=lambda n: stats[n]["explicit_total"] + stats[n]["implicit_total"])
y = range(len(order))
fig, ax = plt.subplots(figsize=(12, 11))
ax.barh([i - 0.2 for i in y], [stats[n]["explicit_total"] for n in order],
        height=0.4, label="Explicit", color="#1f77b4")
ax.barh([i + 0.2 for i in y], [stats[n]["implicit_total"] for n in order],
        height=0.4, label="Implicit", color="#ff7f0e")
ax.set_yticks(list(y))
ax.set_yticklabels(order)
ax.set_xlabel("Number of uses in report.md")
ax.set_title("Explicit vs implicit usage frequency of GenAI terms")
ax.legend()
plt.tight_layout()
plt.savefig("usage-frequency.png", dpi=150)
plt.show()

# Download the results (works in Google Colab)
try:
    from google.colab import files
    for f in ["relations-graph.png", "usage-frequency.png", "stats.json"]:
        files.download(f)
except ImportError:
    print("Done! Files saved: relations-graph.png, usage-frequency.png, stats.json")
