from django.shortcuts import render
from django.http import HttpResponse
from bokeh.embed import server_document
import bokeh

# Create your views here.




def index(request):
    script = server_document("https://bokehdash.herokuapp.com")
    script = server_document("http://localhost:5006/linear_example")
    script = server_document("http://localhost:5006/bokeh_dashboard")
    script = server_document("https://bokehdash.herokuapp.com/linear_example")
    
    print(bokeh.__version__)
    return render(request,'index.html',{'script':script})
