"""Aplicaciones Solow y deuda. Ejecutar: python plot_applications.py --out figures"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from econ_style import theme, save, COLORS as C

def solow(out):
    alpha, replacement = .33, .08
    savings = [.2, .4]
    k = np.linspace(.001, 45, 600)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.8))
    fig.suptitle("Más ahorro: más capital, pero no siempre más consumo", fontsize=16, weight="bold")
    values = []
    for s, color, ls in zip(savings, [C["base"], C["alternative"]], ["-", "--"]):
        ks = (s / replacement)**(1 / (1-alpha))
        cs = (1-s)*ks**alpha
        axes[0].plot(k, s*k**alpha, color=color, ls=ls, label=f"Inversión: s={s:.0%}")
        axes[0].scatter([ks], [replacement*ks], color=color, s=60, zorder=4)
        axes[0].annotate(f"k*={ks:.1f}", (ks, replacement*ks), xytext=(5,-22), textcoords="offset points", color=color)
        values.append({"s": s, "k_star": ks, "consumption_star": cs})
    axes[0].plot(k, replacement*k, color=C["neutral"], ls=":", label="Reposición: (n+g+δ)k")
    axes[0].set(xlabel="Capital por trabajador efectivo (unidades)", ylabel="Flujo por trabajador efectivo / año", title="Equilibrio de Solow · tiempo continuo")
    axes[0].legend(fontsize=9)
    ss = np.linspace(.001,.999,500)
    kk = (ss/replacement)**(1/(1-alpha))
    axes[1].plot(ss*100,(1-ss)*kk**alpha,color=C["benefit"])
    for v, color in zip(values, [C["base"], C["alternative"]]):
        axes[1].scatter(v["s"]*100,v["consumption_star"],color=color,s=70,zorder=4)
    axes[1].axvline(alpha*100,color=C["neutral"],ls="--",label=f"Regla de oro: s=α={alpha:.0%}")
    axes[1].set(xlabel="Tasa de ahorro (%)",ylabel="Consumo estacionario (unidades / año)",title="El consumo tiene un máximo")
    axes[1].legend(fontsize=9)
    save(fig,out,"solow",{"alpha":alpha,"n_g_delta":replacement,"steady_states":values,"assumptions":"Tecnología exógena, Cobb-Douglas, ahorro constante; no es una función de bienestar intertemporal."})
    return values

def debt(out):
    r,g,d0=.05,.03,.6
    stabilizer=(r-g)/(1+g)*d0
    fig,ax=plt.subplots(figsize=(10,5.8))
    results=[]
    for s,color,ls in zip([0,stabilizer,.025],[C["alternative"],C["base"],C["benefit"]],["--","-",":"]):
        debt=[d0]
        for _ in range(20): debt.append((1+r)/(1+g)*debt[-1]-s)
        ax.plot(range(21),np.array(debt)*100,color=color,ls=ls,label=f"Superávit primario: {s:.2%} del PIB")
        results.append({"primary_surplus":s,"debt_to_gdp":debt})
    ax.set(title="Deuda pública: el saldo primario cambia la trayectoria",xlabel="Años desde el escenario inicial",ylabel="Deuda / PIB (%)")
    ax.legend(fontsize=10)
    save(fig,out,"debt",{"r_real":r,"g_real":g,"initial_debt":d0,"stabilizing_surplus":stabilizer,"scenarios":results,"assumptions":"Tasas reales anuales constantes, saldo/PIB actual, sin ajustes stock-flujo."})
    return stabilizer

if __name__ == "__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("--out",default="figures"); args=parser.parse_args()
    theme(); solow(args.out); debt(args.out)
