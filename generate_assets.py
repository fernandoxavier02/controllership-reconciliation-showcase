"""Generate professional mockup images for Controllership Reconciliation showcase."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

OUTPUT = "D:/controllership-reconciliation-showcase/assets"

def save(fig, name, sub="screenshots"):
    fig.savefig(f"{OUTPUT}/{sub}/{name}", dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"[ASSET] {name}")

# 1. Dashboard AR/AP
fig = plt.figure(figsize=(14, 9))
fig.patch.set_facecolor('#f8f9fa')
ax_title = fig.add_axes([0, 0.92, 1, 0.08])
ax_title.set_facecolor('#1565C0')
ax_title.text(0.5, 0.5, 'Controllership Reconciliation Engine — Dashboard', fontsize=16, fontweight='bold', color='white', ha='center', va='center')
ax_title.set_xticks([]); ax_title.set_yticks([]); ax_title.spines[:].set_visible(False)

kpis = [
    ('Total AR', 'R$ 17.3M', '#2E7D32'),
    ('Total AP', 'R$ 20.0M', '#C62828'),
    ('Sem Suporte', '18 (12%)', '#E65100'),
    ('Divergencias', '3 (2%)', '#6A1B9A'),
]
for i, (label, value, color) in enumerate(kpis):
    ax = fig.add_axes([0.03 + i*0.24, 0.74, 0.22, 0.15])
    ax.set_facecolor('white')
    rect = FancyBboxPatch((0,0),1,1, boxstyle="round,pad=0.02", facecolor='white', edgecolor=color, linewidth=3, transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.5, 0.55, value, fontsize=18, fontweight='bold', color=color, ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.2, label, fontsize=9, color='#555', ha='center', va='center', transform=ax.transAxes)
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([]); ax.set_yticks([]); ax.spines[:].set_visible(False)

# Tables
ax_left = fig.add_axes([0.05, 0.1, 0.42, 0.58])
ax_left.set_facecolor('white')
rect = FancyBboxPatch((0,0),1,1, boxstyle="round,pad=0.01", facecolor='white', edgecolor='#ddd', linewidth=1, transform=ax_left.transAxes)
ax_left.add_patch(rect)
ax_left.text(0.05, 0.95, 'Top 10 Contas por Valor', fontsize=11, fontweight='bold', color='#1a1a1a', transform=ax_left.transAxes)

table_data = [
    ('Conta', 'Tipo', 'Valor', 'Suporte'),
    ('Cliente C - Industria', 'AR', 'R$ 499,687', 'OK'),
    ('Fornecedor Y - Logistica', 'AP', 'R$ 498,052', 'OK'),
    ('Fornecedor W - Energia', 'AP', 'R$ 497,580', 'OK'),
    ('Cliente E - Exportacao', 'AR', 'R$ 495,026', 'OK'),
    ('Fornecedor Y - Logistica', 'AP', 'R$ 490,380', 'SEM SUPORTE'),
    ('Cliente A - Distribuidora', 'AR', 'R$ 488,920', 'OK'),
    ('Fornecedor Z - Tecnologia', 'AP', 'R$ 485,410', 'OK'),
    ('Cliente D - Servicos', 'AR', 'R$ 482,300', 'OK'),
    ('Fornecedor V - Manutencao', 'AP', 'R$ 478,150', 'OK'),
    ('Cliente B - Varejo', 'AR', 'R$ 475,890', 'SEM SUPORTE'),
]
y = 0.85
for row_idx, row in enumerate(table_data):
    for col_idx, cell in enumerate(row):
        x_pos = 0.05 + col_idx * 0.22
        weight = 'bold' if row_idx == 0 else 'normal'
        color = '#666' if row_idx == 0 else '#333'
        if col_idx == 3 and cell == 'SEM SUPORTE':
            color = '#C62828'
        ax_left.text(x_pos, y, cell, fontsize=8, fontweight=weight, color=color, transform=ax_left.transAxes)
    y -= 0.075
ax_left.set_xlim(0,1); ax_left.set_ylim(0,1); ax_left.set_xticks([]); ax_left.set_yticks([]); ax_left.spines[:].set_visible(False)

# Right: Risk matrix mini
ax_right = fig.add_axes([0.52, 0.1, 0.43, 0.58])
ax_right.set_facecolor('white')
rect = FancyBboxPatch((0,0),1,1, boxstyle="round,pad=0.01", facecolor='white', edgecolor='#ddd', linewidth=1, transform=ax_right.transAxes)
ax_right.add_patch(rect)
ax_right.text(0.05, 0.95, 'Matriz de Risco — Distribuicao', fontsize=11, fontweight='bold', color='#1a1a1a', transform=ax_right.transAxes)

labels = ['Alto', 'Medio', 'Baixo']
sizes = [3, 8, 139]
colors = ['#C62828', '#FF9800', '#2E7D32']
wedges, texts, autotexts = ax_right.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, pctdistance=0.6)
for text in texts:
    text.set_fontsize(9)
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_fontweight('bold')

ax_foot = fig.add_axes([0, 0, 1, 0.05])
ax_foot.set_facecolor('#1565C0')
ax_foot.text(0.5, 0.5, 'Controllership Reconciliation Engine v1.0.0 | 150 lancamentos processados | Usuario: controller@empresa.ficticia', fontsize=9, color='white', ha='center', va='center')
ax_foot.set_xticks([]); ax_foot.set_yticks([]); ax_foot.spines[:].set_visible(False)

save(fig, '01-ar-ap-dashboard.png')

# 2. Aging Chart
fig, ax = plt.subplots(figsize=(12, 6))
buckets = ['0-30 dias', '31-60 dias', '61-90 dias', '90+ dias']
counts = [35, 34, 42, 39]
values = [8918587, 7422723, 10199685, 10780597]
colors = ['#2E7D32', '#FF9800', '#E65100', '#C62828']

bars = ax.bar(buckets, values, color=colors, edgecolor='white', linewidth=2)
ax.set_ylabel('Valor (BRL)', fontsize=11)
ax.set_title('Aging de Contas — Distribuicao por Faixa de Atraso', fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,p: f'R${x/1e6:.1f}M'))

for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 100000, f'{count} lançamentos', ha='center', va='bottom', fontsize=9, color='#555')

ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
save(fig, '02-aging-chart.png')

# 3. ABC Chart
fig, ax = plt.subplots(figsize=(10, 6))
classes = ['Classe A\n(80% valor)', 'Classe B\n(15% valor)', 'Classe C\n(5% valor)']
counts = [81, 35, 34]
values = [29701152, 5675425, 1945015]
colors = ['#1565C0', '#42A5F5', '#90CAF9']

bars = ax.bar(classes, values, color=colors, edgecolor='white', linewidth=2)
ax.set_ylabel('Valor Acumulado (BRL)', fontsize=11)
ax.set_title('Curva ABC — Classificacao por Importancia (Pareto)', fontsize=13, fontweight='bold')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,p: f'R${x/1e6:.1f}M'))

for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 200000, f'{count} contas', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333')

ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
save(fig, '03-abc-chart.png')

# 4. Risk Matrix
fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 11); ax.set_ylim(0, 8); ax.axis('off')

ax.text(5.5, 7.5, 'Matriz de Risco — Valor vs Suporte Documental', fontsize=14, fontweight='bold', color='#1a1a1a', ha='center')
ax.text(5.5, 7.0, '150 lancamentos analisados | Classificacao automatica por algoritmo', fontsize=9, color='#666', ha='center')

# Grid
for i in range(3):
    for j in range(3):
        x, y = 1 + j*3, 1 + i*2
        color = '#E8F5E9' if i==0 and j==0 else '#FFF3E0' if i==1 or j==1 else '#FFEBEE'
        rect = FancyBboxPatch((x, y), 2.8, 1.8, boxstyle="round,pad=0.05", facecolor=color, edgecolor='#ccc', linewidth=1)
        ax.add_patch(rect)

# Labels
labels = [
    ('Baixo Valor\nCom Suporte', 2.4, 3.9, '#2E7D32'),
    ('Baixo Valor\nSem Suporte', 5.4, 3.9, '#FF9800'),
    ('Alto Valor\nCom Suporte', 2.4, 1.9, '#2E7D32'),
    ('Alto Valor\nSem Suporte', 5.4, 1.9, '#C62828'),
]
for text, x, y, color in labels:
    ax.text(x, y, text, fontsize=9, ha='center', va='center', color=color, fontweight='bold')

# Counts
ax.text(2.4, 3.4, '127 lancamentos', fontsize=8, ha='center', color='#555')
ax.text(5.4, 3.4, '12 lancamentos', fontsize=8, ha='center', color='#555')
ax.text(2.4, 1.4, '8 lancamentos', fontsize=8, ha='center', color='#555')
ax.text(5.4, 1.4, '3 lancamentos', fontsize=8, ha='center', color='#C62828', fontweight='bold')

# Legend
ax.text(9, 5.5, 'Legenda:', fontsize=10, fontweight='bold', color='#333')
ax.text(9, 5.0, 'ALTO: > R$ 100K\nsem suporte', fontsize=8, color='#C62828')
ax.text(9, 4.2, 'MEDIO: > R$ 50K\nsem suporte', fontsize=8, color='#FF9800')
ax.text(9, 3.4, 'BAIXO: Demais', fontsize=8, color='#2E7D32')

save(fig, '04-risk-matrix.png')

# 5. Architecture
fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13); ax.set_ylim(0, 9); ax.axis('off'); fig.patch.set_facecolor('white')

def box(x,y,w,h,c,t,s="",tc='white'):
    r = FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",facecolor=c,edgecolor='white',linewidth=2)
    ax.add_patch(r)
    ax.text(x+w/2,y+h/2+0.15,t,fontsize=9,fontweight='bold',color=tc,ha='center',va='center')
    if s: ax.text(x+w/2,y+h/2-0.25,s,fontsize=7,color=tc,ha='center',va='center',alpha=0.9)

def arrow(x1,y1,x2,y2,c='#888'):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color=c,lw=1.5))

ax.text(6.5,8.7,'Controllership Reconciliation — Architecture',fontsize=14,fontweight='bold',color='#1a1a1a',ha='center')

ax.text(0.5,8.0,'DATA SOURCES',fontsize=10,fontweight='bold',color='#555')
box(1,7.2,2.5,0.6,'#1565C0','ERP CSV','AR/AP')
box(3.8,7.2,2.5,0.6,'#1565C0','Bank CSV','Multi-banco')
box(6.6,7.2,2.5,0.6,'#1565C0','Support','PDF/CSV')
box(9.4,7.2,2.5,0.6,'#1565C0','GL CSV','Razao')

box(3.5,6.0,6,0.6,'#6A1B9A','ETL Pipeline (Python)','Parse · Normalize · Validate · Enrich')

ax.text(0.5,5.3,'ANALYTICAL ENGINE',fontsize=10,fontweight='bold',color='#555')
box(1,4.2,2.5,0.9,'#2E7D32','Aging\nBuckets','0-30 · 31-60 · 61-90 · 90+')
box(3.8,4.2,2.5,0.9,'#2E7D32','ABC\nPareto','A=80% · B=15% · C=5%')
box(6.6,4.2,2.5,0.9,'#2E7D32','Risk\nMatrix','Alto/Medio/Baixo')
box(9.4,4.2,2.5,0.9,'#2E7D32','Bank\nReconciliation','Fuzzy Matching')

ax.text(0.5,3.5,'OUTPUT LAYER',fontsize=10,fontweight='bold',color='#555')
box(3,2.4,3.5,0.9,'#E65100','JSON / CSV','Build-time static data')
box(7,2.4,3.5,0.9,'#E65100','Docker\nContainers','Per-bank parsers')

ax.text(0.5,1.7,'FRONTEND',fontsize=10,fontweight='bold',color='#555')
box(3,0.8,7,0.7,'#455A64','Angular 17 Dashboard','17 sections · TypeScript · RxJS · Tailwind')

save(fig, '05-architecture-diagram.png', sub='diagrams')

# 6. Bank Reconciliation Timeline
fig, ax = plt.subplots(figsize=(13, 6))
ax.set_facecolor('#fafafa')

banks = ['BMG', 'Citi', 'Bradesco', 'Itau', 'Santander']
total = [450, 320, 280, 510, 190]
matched = [445, 318, 275, 505, 188]
divergent = [5, 2, 5, 5, 2]

x = np.arange(len(banks))
width = 0.35

bars1 = ax.bar(x - width/2, total, width, label='Total Lancamentos', color='#1565C0', edgecolor='white')
bars2 = ax.bar(x + width/2, matched, width, label='Conciliados', color='#2E7D32', edgecolor='white')

# Divergent markers
for i, (t, d) in enumerate(zip(total, divergent)):
    ax.text(i, t + 10, f'{d} diverg.', fontsize=8, color='#C62828', ha='center', fontweight='bold')

ax.set_xlabel('Banco', fontsize=11)
ax.set_ylabel('Lancamentos', fontsize=11)
ax.set_title('Conciliacao Bancaria — Match Rate por Instituicao', fontsize=13, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(banks)
ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
save(fig, '06-bank-reconciliation.png')

print("\n[INFO] All Controllership Reconciliation assets generated successfully!")
