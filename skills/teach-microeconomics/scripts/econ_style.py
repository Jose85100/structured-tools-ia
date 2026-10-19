"""Estilo económico docente; requiere numpy, matplotlib y seaborn."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

COLORS = {"base": "#0072B2", "alternative": "#D55E00", "benefit": "#009E73", "accent": "#CC79A7", "neutral": "#52606D"}

def theme():
    sns.set_theme(style="whitegrid", context="notebook", font="DejaVu Sans",
                  palette=list(COLORS.values()), rc={"axes.spines.top": False,
                  "axes.spines.right": False, "grid.alpha": .22, "lines.linewidth": 2.5,
                  "axes.titleweight": "bold", "figure.facecolor": "#FFFFFF"})

def save(fig, out, name, metadata):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fig.text(.06, .025, "Fuente: modelo educativo · Parámetros hipotéticos · Sin estimación empírica", fontsize=9, color=COLORS["neutral"])
    fig.subplots_adjust(bottom=.21, top=.85, wspace=.28)
    for ext in ("png", "svg"):
        fig.savefig(out / f"{name}.{ext}", dpi=200, bbox_inches="tight", facecolor="white")
    (out / f"{name}.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False))
    plt.close(fig)
