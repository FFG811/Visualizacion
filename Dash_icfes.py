import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('SB11_20211.txt', encoding='utf-8', sep='¬',engine='python')
df_head=df[0:6]

group_labels = ['distplot']

fig_box1 = px.box(df, x = df['ESTU_GENERO'], y = df['PUNT_GLOBAL'], title='Distribución del Puntaje por Género')
fig_bar1 = px.histogram(df, x=df['ESTU_GENERO'], title="Cantidad de Estudiantes por Género")
fig_dist1 = px.histogram(df, x=df['PUNT_GLOBAL'] , title="Distribución del Puntaje Global")
fig_scat = px.scatter_3d(df, x='PUNT_SOCIALES_CIUDADANAS', y='PUNT_MATEMATICAS', z= 'PUNT_C_NATURALES', color='COLE_JORNADA', title="Desempeño de Estudiantes por Jornada")
fig_dens = px.density_heatmap(df, x="COLE_JORNADA", y="PUNT_GLOBAL", title="Mapa de Densidad por Jornada")
fig_cont = go.Figure(go.Histogram2dContour( x = df['PUNT_MATEMATICAS'], y = df['PUNT_GLOBAL'],contours_showlabels = True))
fig_pie = px.pie(df, values='PUNT_INGLES', names='COLE_BILINGUE', title='Distribucion del Puntaje de Inlges en Colegios Bilingues')


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app = dash.Dash(__name__)

#Titulo
app.layout = html.Div([
    html.H1(children='Base de datos del icfes',style={'textAlign': 'center'}),
    html.H5(children='Realizado por: Fabian Fuertes',style={'textAlign': 'right'}),
    html.Hr(),
    
#Pestañas    
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Analsis Descriptivo', value='tab-1'),
        dcc.Tab(label='Modelo', value='tab-2')
#         ,dcc.Tab(label='tab 3', value='tab-3')
    ]),
    html.Div(id='tabs-content')
])

#callback - Pestañas
   
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    
#Pestaña1    
    if tab == 'tab-1':
        return html.Div([
#Objetivo
    html.H2(children='Objetivo',style={'textAlign': 'left'}),
    html.P("Determinar como el desempeño académico de los colegios en cada una de las áreas evaluadas en las pruebas saber 11 del primer semestre de 2021 se ven afectadas por las variables socio demograficas directamente relacionadas a la información de los colegios a nivel nacional."),
                        html.Br(),
                         
#Base de Datos
    html.H2(children='Base de Datos',style={'textAlign': 'left'}),
    html.P("La base de datos cuenta con 78 columnas y 15.528 filas, correspondientes a la información socio demográfica de cada estudiante que presento la prueba en el primer semestre del año 2021 y los puntajes obtenidos en cada uno de los ítems evaluados en la prueba. Cuenta con 61 variables cualitativas y 18 cuantitativas."),
            
                        html.Br(),
 
    
    dash_table.DataTable(
                            id='table-sorting-filtering',
                            columns=[
                                {'name': i, 'id': i, 'deletable': True} for i in df.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                'height': 'auto',
                                # all three widths are needed
                                'minWidth': '140px', 'width': '140px', 'maxWidth': '140px',
                                'whiteSpace': 'normal'
                            },
                            style_as_list_view=True,
                             style_header={
                                    'backgroundColor': '#CECED1',
                                    'fontWeight': '#FFFFFF'
                                    },
                            data=df.to_dict('records'),
                            page_current= 0,
                            page_size= 5,
                            page_action='native',
                            filter_action='native',
                            filter_query='',
                            sort_action='native',
                            sort_mode='multi',
                            sort_by=[]
                        ),
    
#Variables
    html.H2(children='Variables',style={'textAlign': 'left'}),
    html.Div([        
        html.H3(children='Variables Cualitativas',style={'textAlign': 'left'}),
        html.P("La base de datos cuenta con 61 variables cualitativas donde se observan datos socio demográficos de cada estudiante. Estos datos permiten comprender como afectan dichos datos en los resultados de cada estudiante donde se destacan las siguientes: "),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("ESTU_GENERO"),
                dbc.ListGroupItem("FAMI_ESTRATOVIVIENDA"),
                dbc.ListGroupItem("FAMI_EDUCACIONPADRE"),
                dbc.ListGroupItem("FAMI_TIENEINTERNET"),
                dbc.ListGroupItem("FAMI_TIENECOMPUTADOR"),
                dbc.ListGroupItem("FAMI_NUMLIBROS"),
            ],
            horizontal=True,
            className="mb-2",
        )
        ],
        style={'width':'50%','display': 'inline-block'}),
    html.Div([
        
        html.H2(children='Variables Cuantativas',style={'textAlign': 'left'}),
        html.P("Los resultados de las pruebas se encuentran en 18 variables cuantitativas donde se observan el puntaje obtenido en cada una de las áreas evaluadas, su desempeño. Para el análisis de este trabajo nos enfocaremos en las siguientes variables: "),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("PUNT_LECTURA_CRITICA"),
                dbc.ListGroupItem("PUNT_MATEMATICAS"),
                dbc.ListGroupItem("PUNT_C_NATURALES"),
                dbc.ListGroupItem("PUNT_SOCIALES_CIUDADANAS"),
                dbc.ListGroupItem("PUNT_INGLES"),
                dbc.ListGroupItem("PUNT_GLOBAL"),
            ],
            horizontal=True,
            className="mb-2",
        )
        ],
        style={'width':'50%','display': 'inline-block'}),      

    html.Hr(),
#Contenedor            
    html.Div([ 
        #Barras
        html.Div([dcc.Graph(id='bar-graph1',figure=fig_bar1, className='six columns')],style={'width':'50%','display': 'inline-block' }), 
        #3d
        html.Div([dcc.Graph(id='boxplot1',figure=fig_scat, className='six columns1')],style={'width':'50%','display': 'inline-block' })
         ]),  #Contenedor      
#Contenedor            
    html.Div([ 
        #Barras
        html.Div([dcc.Graph(id='boxplot1',figure=fig_box1, className='six columns')],style={'width':'33%','display': 'inline-block'}), 
        #3d
        html.Div([dcc.Graph(id='boxplot1',figure=fig_pie, className='six columns1')],style={'width':'33%','display': 'inline-block'}),
        #3d
        html.Div([dcc.Graph(id='boxplot1',figure=fig_bar1, className='six columns1')],style={'width':'33%','display': 'inline-block'}),
         ]),  #Contenedor  
#Contenedor            
    html.Div([ 
        #Barras
        html.Div([dcc.Graph(id='boxplot1',figure=fig_cont, className='six columns')],style={'width':'50%','display': 'inline-block'}), 
        #3d
        html.Div([dcc.Graph(id='boxplot1',figure=fig_dens, className='six columns1')],style={'width':'50%','display': 'inline-block'}),
         ]),  #Contenedor             
])        
#Pestaña2
    elif tab == 'tab-2':
        return html.Div([

])

    
if __name__ == '__main__':
    app.run_server(debug=True, port="2020")