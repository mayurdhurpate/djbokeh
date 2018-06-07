from django.shortcuts import render
from django.http import HttpResponse
from bokeh.embed import server_document
import bokeh
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required(login_url='/admin/login/')
def index(request):
    script = server_document("https://bokehdash.herokuapp.com")
    script = server_document("http://localhost:5006/linear_example")
    script = server_document("http://localhost:5006/bokeh_dashboard")
    script = server_document("https://bokehdash.herokuapp.com/linear_example")
    script = server_document("https://ntcdashboard.herokuapp.com/bokeh_dashboard")
    print(bokeh.__version__)
    return render(request,'index.html',{'script':script})
