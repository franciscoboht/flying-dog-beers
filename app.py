import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
#beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ingreso=[1000, 10000, 100000, 1000000]
whisky=[0, 0, 5, 100]
birra=[100, 80, 25, 3]
color1='lightblue'
color2='darkgreen'
mytitle='Guía gráfica de consumición de Whisky, para Juanma'
tabtitle='Whisky'
myheading='Guía gráfica de consumición de Whisky, para Juanma'
label1='Whisky'
label2='Cerveza'
#githublink='https://github.com/austinlasseter/flying-dog-beers'
#sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Scatter(
    x=ingreso,
    y=whisky,
    name=label1
)
alcohol = go.Scatter(
    x=ingreso,
    y=birra,
    name=label2
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    #barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )#,
    #html.A('Code on Github', href=githublink),
    #html.Br(),
    #html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
