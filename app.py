from flask import Flask,render_template, session, redirect, url_for, session, abort, flash
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField, IntegerField, HiddenField)
from wtforms.fields.html5 import EmailField
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, HiddenField
from flask_wtf import Form
from Graph import WeightedGraph





class NEdges(FlaskForm):

    edges = IntegerField()
    
class graphForm(FlaskForm):
        source = TextField()
        dest = TextField()
        


app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def EdgesPage():
    form = NEdges()

    if form.validate_on_submit():
        session['edges'] = form.edges.data
        
        return redirect('createedges')
    
    return render_template('index.html', form=form)

@app.route('/createedges', methods=['GET', 'POST'])
def createEdges():
    
    class graphData(Form):
        edgesData = FieldList(FormField(graphForm), min_entries=session['edges'], max_entries=session['edges'])
        shortestFrom = TextField()
        shortestTo = TextField()
        
    form = graphData()

    if form.validate_on_submit():
        results = []
        for idx, data in enumerate(form.edgesData.data):
            results.append({
                'source':data["source"],
                'dest':data["dest"], 
            })
        vertexs=[]
        G=WeightedGraph()
        for v in results:
            src, dest = v['source'].split(',')
   
            w = v['dest']
            if src not in vertexs:
                G.addVertex(src)
                vertexs.append(src)
            if dest not in vertexs:
                G.addVertex(dest)
                vertexs.append(dest)
            G.addEdge(src,dest,int(w) )
            
        shrtPath = G.Dijkstra(form.shortestFrom.data,form.shortestTo.data)
        shrtPath = (" --> ".join(shrtPath)).upper()
        
        flash(shrtPath)

#         session['edgesData'] = results
#         return redirect('/')
    return render_template('createEdges.html', form=form, n=session['edges'])

app.run()