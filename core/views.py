from django.shortcuts import render
import io, urllib, base64
import pandas as pd
import matplotlib as plt
import numpy as np

def get_dataframe():
    # Busca todos os dados do banco e retorna um DataFrame do Pandas
    tweets = Tweet.objects.all().values()
    df = pd.DataFrame(list(tweets ))
    return df

def _fig_to_base64(fig):
    # Converte uma figura Matplotlib para uma string base64 para ser usada no HTML
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_b64



def index(request):
    return render(request, 'index.html')
