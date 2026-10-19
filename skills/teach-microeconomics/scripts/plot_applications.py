"""Aplicaciones impuesto y consumidor. Ejecutar: python plot_applications.py --out figures"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from econ_style import theme, save, COLORS as C

def tax(out):
    q=np.linspace(0,100,400); t=20; q0=50; q1=40; pc=60; pp=40
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(q,100-q,color=C["base"],label="Demanda: P=100−Q")
    ax.plot(q,q,color=C["benefit"],label="Oferta: P=Q")
    ax.plot(q,q+t,color=C["alternative"],ls="--",label="Oferta + impuesto unitario 20")
    ax.fill_between([0,q1],[pp,pp],[pc,pc],color=C["accent"],alpha=.18,label="Recaudo: 800")
    ax.fill([q1,q0,q1],[pp,50,pc],color=C["alternative"],alpha=.23,label="Pérdida de eficiencia: 100")
    ax.scatter([q0,q1,q1],[50,pc,pp],color=C["neutral"],s=50,zorder=5)
    for text,xy,offset in [("Inicial: Q=50, P=50",(50,50),(28,-8)),("Comprador: P=60",(40,60),(-115,35)),("Vendedor: P=40",(40,40),(35,-32))]:
        ax.annotate(text,xy,xytext=offset,textcoords="offset points",fontsize=10,arrowprops={"arrowstyle":"-","color":C["neutral"]})
    ax.set(xlim=(0,100),ylim=(0,125),xlabel="Cantidad (unidades / periodo)",ylabel="Precio (unidades monetarias / unidad)",title="Incidencia tributaria: remitir el impuesto no determina quién lo soporta")
    ax.legend(loc="upper right",fontsize=9)
    save(fig,out,"tax",{"unit_tax":t,"q_before":q0,"q_after":q1,"consumer_price":pc,"producer_price":pp,"revenue":800,"deadweight_loss":100,"assumptions":"Competencia perfecta, curvas lineales, sin externalidades; recaudo como transferencia."})
    return q1,pc,pp

def consumer(out):
    income,py=100,1
    fig,axes=plt.subplots(1,2,figsize=(13,5.8),sharey=True)
    fig.suptitle("Elección del consumidor: un precio mayor cambia el presupuesto",fontsize=16,weight="bold")
    results=[]
    for ax,px,color in zip(axes,[2,4],[C["base"],C["alternative"]]):
        xstar=income/(2*px); ystar=income/(2*py); utility=np.sqrt(xstar*ystar)
        x=np.linspace(.2,income/px,500)
        ax.plot(x,(income-px*x)/py,color=color,label=f"Presupuesto: {px}x+y=100")
        ycurve=utility**2/x
        ax.plot(x,np.where(ycurve<=110,ycurve,np.nan),color=C["benefit"],ls="--",label="Indiferencia en el óptimo")
        ax.scatter([xstar],[ystar],color=color,s=70,zorder=4)
        ax.annotate(f"Óptimo: ({xstar:g}, {ystar:g})",(xstar,ystar),xytext=(10,20),textcoords="offset points",fontsize=10)
        ax.set(xlim=(0,52),ylim=(0,110),xlabel="Bien x (unidades)",ylabel="Bien y (unidades)",title=f"Precio de x = {px}")
        ax.legend(fontsize=9,loc="upper right")
        results.append({"income":income,"px":px,"py":py,"x":xstar,"y":ystar,"utility":utility})
    save(fig,out,"consumer",{"preferences":"u=sqrt(x*y)","scenarios":results,"assumptions":"Ingreso nominal fijo, precios positivos, bienes divisibles; no descompone Slutsky."})
    return results

if __name__ == "__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("--out",default="figures"); args=parser.parse_args()
    theme(); tax(args.out); consumer(args.out)
