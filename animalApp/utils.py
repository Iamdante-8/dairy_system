import base64
from .models import *
from io import BytesIO
from matplotlib import pyplot as plt
from .models import milk_production

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
def get_chart(chart_type,df,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    chart = get_graph()
    return chart
            