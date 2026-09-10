from django.shortcuts import render
import io, urllib, base64
import pandas as pd
import matplotlib as plt
import numpy as np
from models import Tweet

def get_dataframe():
    # Busca todos os dados do banco e retorna um DataFrame do Pandas
    tweets = Tweet.objects.all().values()
    df = pd.DataFrame(list(tweets))
    return df

def plot_to_base64(fig):
    # Converte uma figura Matplotlib para uma string base64 para ser usada no HTML
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_b64

def line_chart_view(request):
    # Evolução do número de tweets por palavra-chave (top 15)
    df = get_dataframe()
    top = df['keyword'].value_counts().head(15).sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(top.index, top.values, marker='o', color='steelblue')
    ax.set_title('Top 15 Keywords — Número de Tweets (Linhas)')
    ax.set_xlabel('Keyword')
    ax.set_ylabel('Quantidade')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    grafico_linhas = plot_to_base64(plt.gcf())
    plt.close()
    context = {'grafico_linhas': grafico_linhas,}
    return render(request, 'core/index.html', context)

def index(request):
    return render(request, 'index.html')
