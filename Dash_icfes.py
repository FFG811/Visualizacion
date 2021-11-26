import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
from dash import Input, Output, State, html
# import dash_table
from dash import dash_table
from dash import dcc
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy  import dendrogram, linkage, fcluster



# df=pd.read_csv('SB11_20211.txt', encoding='utf-8', sep='¬',engine='python')
df=pd.read_csv('https://raw.githubusercontent.com/FFG811/Visualizacion/main/SB11_20211.txt', encoding='utf-8', sep='¬',engine='python')
df_clean=pd.read_csv('https://raw.githubusercontent.com/FFG811/Visualizacion/main/icfes_cluster.csv')

#######################################################################################################

# df_clean=df[df['PUNT_LECTURA_CRITICA'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_LECTURA_CRITICA'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_MATEMATICAS'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_C_NATURALES'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_SOCIALES_CIUDADANAS'].isnull()==False]
# df_clean=df_clean[df_clean['PERCENTIL_SOCIALES_CIUDADANAS'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_INGLES'].isnull()==False]
# df_clean=df_clean[df_clean['PUNT_GLOBAL'].isnull()==False]

# df2=df_clean.iloc[:,59:-3]
# df2=df2.drop(['DESEMP_INGLES'], axis=1).iloc[:,:]
# df2=df2.drop(['PERCENTIL_LECTURA_CRITICA'], axis=1).iloc[:,:]
# df2=df2.drop(['DESEMP_LECTURA_CRITICA'], axis=1).iloc[:,:]
# df2=df2.drop(['PERCENTIL_MATEMATICAS'], axis=1).iloc[:,:]
# df2=df2.drop(['DESEMP_MATEMATICAS'], axis=1).iloc[:,:]
# df2=df2.drop(['PERCENTIL_C_NATURALES'], axis=1).iloc[:,:]
# df2=df2.drop(['DESEMP_C_NATURALES'], axis=1).iloc[:,:]
# df2=df2.drop(['PERCENTIL_SOCIALES_CIUDADANAS'], axis=1).iloc[:,:]
# df2=df2.drop(['DESEMP_SOCIALES_CIUDADANAS'], axis=1).iloc[:,:]
# df2=df2.drop(['PERCENTIL_INGLES'], axis=1).iloc[:,:]
# df2=df2.drop(['PUNT_GLOBAL'], axis=1).iloc[:,:]
# # df2
# puntaje=df2.values

# cluster_jerarquico= linkage(puntaje,'ward')

# clusters= fcluster(cluster_jerarquico, t=1000, criterion='distance') 
# df_clean['Cluster Jerarquico'] = clusters

df_clean['Cluster Jerarquico'] = df_clean['Cluster Jerarquico'].apply(str)

card_dendro= dbc.Card(
    [
        dbc.CardBody(
            html.H4('Dendrograma', className="card-tittle")
        ),
        dbc.CardImg(src="https://raw.githubusercontent.com/FFG811/Visualizacion/main/Dendrogram.jpg", 
                    top=True, 
                    ) ,
    ]
)

df_clean['Cluster Jerarquico'] = df_clean['Cluster Jerarquico'].apply(str)

card_dendro= dbc.Card(
    [
        dbc.CardBody(
            html.H4('Dendrograma', className="card-tittle")
        ),
        dbc.CardImg(src="Dendrogram.jpg", 
                    top=True, 
                   ) ,
    ]
)

fig_hist2 = px.histogram(df_clean, x=df_clean['Cluster Jerarquico'], color=df_clean["COLE_JORNADA"],category_orders={'Cluster Jerarquico':['1','2','3']})

card_barras2=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Cantidad de Participantes por Jornada", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_hist2',figure=fig_hist2, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

fig_box2 = px.box(df_clean, x=df_clean['COLE_CALENDARIO'], y=df_clean['PUNT_GLOBAL'], color=df_clean['Cluster Jerarquico'],category_orders={'Cluster Jerarquico':['1','2','3'],'COLE_CALENDARIO':["A", "B", "OTRO"]})

card_box2=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Desempeño por Calendario en cada Cluster", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_box2',figure=fig_box2, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)


fig_scatter2 = px.scatter(df_clean, x=df_clean['PUNT_MATEMATICAS'], y=df_clean['PUNT_LECTURA_CRITICA'], color=df_clean['Cluster Jerarquico'],marginal_x="histogram", marginal_y="histogram",trendline="ols",category_orders={'Cluster Jerarquico':['1','2','3']})

card_scatter2=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Correlación entre los puntajes de Lectura crítica vs Matematicas", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_scatter2',figure=fig_scatter2, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)


fig_funnel2 = px.funnel_area(df_clean, names=df_clean['Cluster Jerarquico'], values=df_clean['PUNT_GLOBAL'])

card_funnel2=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Funnel de Puntaje Global por Cluster", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_funnel2',figure=fig_funnel2, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

# fig_funnel2 = px.funnel_area(df_clean, names=df_clean['Cluster Jerarquico'], values=df_clean['PUNT_GLOBAL'])

# card_funnel2=dbc.Card(
#     [
#         dbc.CardBody([
#             html.H4("TITULO", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
#         ]),
#         dcc.Graph(id='fig_funnel2',figure=fig_funnel2, className='six columns'),
#     ],
#     body=True,
#     color="dark",
#     outline=False ,
#     style={"border-radius": "2%"} 
# )

fig_tree2 = px.treemap(df_clean, path=[px.Constant("all"), df_clean['COLE_DEPTO_UBICACION'], df_clean['COLE_MCPIO_UBICACION']], 
                 values=df_clean['PUNT_GLOBAL'], color=df_clean['COLE_DEPTO_UBICACION'],color_continuous_scale='Blues')
#                  values=df_clean['PUNT_GLOBAL'], color=df_clean['COLE_DEPTO_UBICACION'],color_continuous_scale='Blues')

card_tree2=dbc.Card(
    [        
        dbc.CardBody([
            html.H4("Desempeño por Departamento y Municipio", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_tree2',figure=fig_tree2, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"}
)

#######################################################################################################

group_labels = ['distplot']

#fig_box1 = px.box(df, x = df['ESTU_GENERO'], y = df['PUNT_GLOBAL'])
fig_bar1 = px.histogram(df, x=df['ESTU_GENERO'])
# fig_dist1 = px.histogram(df, x=df['PUNT_GLOBAL'])
#fig_scat = px.scatter(df, x='PUNT_SOCIALES_CIUDADANAS', y='PUNT_MATEMATICAS', color='COLE_JORNADA', symbol='COLE_JORNADA')
fig_dens = px.density_heatmap(df, x="COLE_JORNADA", y="PUNT_GLOBAL")
# fig_cont = go.Figure(go.Histogram2dContour( x = df['COLE_JORNADA'], y = df['PUNT_GLOBAL'],contours_showlabels = True))
# fig_pie = px.pie(df, values=df['COLE_CARACTER'].value_counts().values, names=df['COLE_CARACTER'].value_counts().index)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# app = dash.Dash(__name__)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.config.suppress_callback_exceptions=True

#Tajetas
card_box=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Distribución del Puntaje por Género", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_box1'),#,figure=fig_box1, className='six columns'),
        html.Label('Seleccione el Área:',style={'width': '400px', 'textAlign': 'left', 'color': 'White'}),
        dcc.Dropdown(id='user_choice_gen', options=[{'label':'Puntaje Global','value':'PUNT_GLOBAL'},
                                                {'label':'Matematicas','value':'PUNT_MATEMATICAS'},
                                                {'label':'Ingles','value':'PUNT_INGLES'},
                                                {'label':'Sociales','value':'PUNT_SOCIALES_CIUDADANAS'},
                                                {'label':'Ciencias Naturales','value':'PUNT_C_NATURALES'},
                                                {'label':'Lectura','value':'PUNT_LECTURA_CRITICA'}],
                                                value='PUNT_GLOBAL',),
    ],
    body=True,
    color="primary",
    outline=False  ,
    style={"border-radius": "2%"}
)

card_barras=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Cantidad de Estudiantes por Género", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='bar-graph1',figure=fig_bar1, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False  ,
    style={"border-radius": "2%"}
)

card_dist1=dbc.Card(
    [
        dbc.CardBody([
            html.Br(),
            html.H4("Distribución por Puntaje.", className="card-tittle"),
            html.Br(),
            html.Br(),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        html.Br(),
        dcc.Graph(id='fig_dist1'),#figure=fig_dist1, className='six columns'),
        html.Label('Seleccione el Área:',style={'width': '400px', 'textAlign': 'left', 'color': 'White'}),
        dcc.Dropdown(id='user_choice', options=[{'label':'Puntaje Global','value':'PUNT_GLOBAL'},
                                                {'label':'Matematicas','value':'PUNT_MATEMATICAS'},
                                                {'label':'Ingles','value':'PUNT_INGLES'},
                                                {'label':'Sociales','value':'PUNT_SOCIALES_CIUDADANAS'},
                                                {'label':'Ciencias Naturales','value':'PUNT_C_NATURALES'},
                                                {'label':'Lectura','value':'PUNT_LECTURA_CRITICA'}],
                                                value='PUNT_GLOBAL',),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)


card_scat=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Correlación de los Puntajes", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_scat'),#,figure=fig_scat, className='six columns'),
        dbc.Row([
            html.Label('Eje X: ',style={'width': '70px', 'textAlign': 'center', 'color': 'White'}),
            dcc.Dropdown(id='user_choice_X', options=[{'label':'Puntaje Global','value':'PUNT_GLOBAL'},
                                                {'label':'Matematicas','value':'PUNT_MATEMATICAS'},
                                                {'label':'Ingles','value':'PUNT_INGLES'},
                                                {'label':'Sociales','value':'PUNT_SOCIALES_CIUDADANAS'},
                                                {'label':'Ciencias Naturales','value':'PUNT_C_NATURALES'},
                                                {'label':'Lectura','value':'PUNT_LECTURA_CRITICA'}],
                                                value='PUNT_GLOBAL',
                                                style={'width': '250px', 'display': 'inline-block'})
            ]),
        dbc.Row([
        html.Label('Eje Y: ',style={'width': '70px', 'textAlign': 'center', 'color': 'White'}),
        dcc.Dropdown(id='user_choice_Y', options=[{'label':'Puntaje Global','value':'PUNT_GLOBAL'},
                                                {'label':'Matematicas','value':'PUNT_MATEMATICAS'},
                                                {'label':'Ingles','value':'PUNT_INGLES'},
                                                {'label':'Sociales','value':'PUNT_SOCIALES_CIUDADANAS'},
                                                {'label':'Ciencias Naturales','value':'PUNT_C_NATURALES'},
                                                {'label':'Lectura','value':'PUNT_LECTURA_CRITICA'}],
                                                value='PUNT_MATEMATICAS',
                                                style={'width': '250px', 'display': 'inline-block'})
            ]),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

card_dens=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Mapa de Densidad por Jornada", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_dens',figure=fig_dens, className='six columns'),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

card_cont=dbc.Card(
    [
        dbc.CardBody([
            html.H4("Mapa de Contorno por Categoria", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        dcc.Graph(id='fig_cont'),#,figure=fig_cont, className='six columns'),
        html.Br(),
        dbc.Row([
            html.Label('Eje X: ',style={'width': '70px', 'textAlign': 'center', 'color': 'White'}),
            dcc.Dropdown(id='user_choice_cont_X', options=[{'label':'Genero del Estudiante','value':'ESTU_GENERO'},
                                                {'label':'Jornada del Colegio','value':'COLE_JORNADA'},
                                                {'label':'Colegio Bilingue','value':'COLE_BILINGUE'},
                                                {'label':'Naturaleza del Colegio','value':'COLE_NATURALEZA'},
                                                {'label':'Carácter del Establecimiento','value':'COLE_CARACTER'},
                                                {'label':'Género del Colegio','value':'COLE_GENERO'}],
                                                value='COLE_CARACTER',
                                                style={'width': '400px', 'display': 'inline-block'})
            ]),
        dbc.Row([
        html.Label('Eje Y: ',style={'width': '70px', 'textAlign': 'center', 'color': 'White'}),
        dcc.Dropdown(id='user_choice_cont_Y', options=[{'label':'Puntaje Global','value':'PUNT_GLOBAL'},
                                                {'label':'Matematicas','value':'PUNT_MATEMATICAS'},
                                                {'label':'Ingles','value':'PUNT_INGLES'},
                                                {'label':'Sociales','value':'PUNT_SOCIALES_CIUDADANAS'},
                                                {'label':'Ciencias Naturales','value':'PUNT_C_NATURALES'},
                                                {'label':'Lectura','value':'PUNT_LECTURA_CRITICA'}],
                                                value='PUNT_MATEMATICAS',
                                                style={'width': '400px', 'display': 'inline-block'})
            ]),
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

card_pie=dbc.Card(
    [
        dbc.CardBody([
            html.Br(),
            html.H4("Proporción por Categoría", className="card-tittle"),
#             html.P("Descripcion del grafico", className="card-text")
        ]),
        html.Br(),  
        dcc.Graph(id='fig_pie'),#,figure=fig_pie, className='six columns'),  
        html.Label('Seleccione la Categoria:',style={'width': '400px', 'textAlign': 'left', 'color': 'White'}),
        dcc.Dropdown(id='user_choice_cat', options=[{'label':'Genero del Estudiante','value':'ESTU_GENERO'},
                                                {'label':'Jornada del Colegio','value':'COLE_JORNADA'},
                                                {'label':'Colegio Bilingue','value':'COLE_BILINGUE'},
                                                {'label':'Naturaleza del Colegio','value':'COLE_NATURALEZA'},
                                                {'label':'Carácter del Establecimiento','value':'COLE_CARACTER'},
                                                {'label':'Género del Colegio','value':'COLE_GENERO'}],
                                                value='COLE_CARACTER',),     
        html.Br(),  
    ],
    body=True,
    color="primary",
    outline=False ,
    style={"border-radius": "2%"} 
)

#Titulo
app.layout = html.Div([
    
    html.H1(children='Base de datos del icfes',style={'textAlign': 'center'}),
    html.H3(children='Maestría en Analítica de Datos',style={'textAlign': 'center'}),
    html.Br(),  
    html.H3(children='Visualización',style={'textAlign': 'center'}),
    html.H3(children='Universidad Central',style={'textAlign': 'center'}),
    html.Br(),  
    html.H5(children='Realizado por: Fabian Fuertes',style={'textAlign': 'right'}),
    html.H5(children='Docente: Miguel Angel Rippe Espinosa',style={'textAlign': 'right'}),
    html.Hr(),

#Pestañas    
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Análisis Descriptivo', value='tab-1'),
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
    html.Br(),        
        dbc.Button(
            "Resumen",
            className="mb-3",
            color="primary",
            id="Resumen_ini",
        ),
    dbc.Collapse([    
            
#Objetivo
    html.H1(children='Objetivo',style={'textAlign': 'left'}),
    html.P("Determinar como el desempeño académico de los colegios en cada una de las áreas evaluadas en las pruebas saber 11 del primer semestre de 2021 se ven afectadas por las variables socio demograficas directamente relacionadas a la información de los colegios a nivel nacional."),
                        html.Br(),
                         
#Base de Datos
    html.H1(children='Base de Datos',style={'textAlign': 'left'}),
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
    html.H1(children='Variables',style={'textAlign': 'left'}),
    html.Div([        
        html.H4(children='Variables Cualitativas',style={'textAlign': 'left'}),
        html.P("La base de datos cuenta con 61 variables cualitativas donde se observan datos socio demográficos de cada estudiante. Estos datos permiten comprender como afectan dichos datos en los resultados de cada estudiante donde se destacan las siguientes: "),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("ESTU_GENERO"),
                dbc.ListGroupItem("COLE_JORNADA"),
                dbc.ListGroupItem("COLE_BILINGUE"),
                dbc.ListGroupItem("COLE_NATURALEZA"),
                dbc.ListGroupItem("COLE_CARACTER"),
                dbc.ListGroupItem("COLE_GENERO"),                
            ],
            horizontal=False,
            className="mb-2",
        )
        ],
        style={'width':'50%','display': 'inline-block'}),
    html.Div([
        
        html.H4(children='Variables Cuantativas',style={'textAlign': 'left'}),
        html.P("Los resultados de las pruebas se encuentran en 18 variables cuantitativas donde se observan el puntaje obtenido en cada una de las áreas evaluadas y su desempeño. Para el análisis de este trabajo nos enfocaremos en las siguientes variables: "),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("PUNT_LECTURA_CRITICA"),
                dbc.ListGroupItem("PUNT_MATEMATICAS"),
                dbc.ListGroupItem("PUNT_C_NATURALES"),
                dbc.ListGroupItem("PUNT_SOCIALES_CIUDADANAS"),
                dbc.ListGroupItem("PUNT_INGLES"),
                dbc.ListGroupItem("PUNT_GLOBAL"),
            ],
            horizontal=False,
            className="mb-2",
        )
        ],
        style={'width':'50%','display': 'inline-block'}),      

    html.Hr(),
        ],  id="Collapse_ini", is_open=False
    ),
    html.Br(),        
        dbc.Button(
            "DashBoard",
            className="mb-3",
            color="primary",
            id="DashBoard_ini",
        ),
    dbc.Collapse([
            
#Graficas
    html.Br(),    
    dbc.Row(card_dist1), 
            html.Br(),
    dbc.Row([dbc.Col(card_box,width=4),dbc.Col(card_pie,width=4),dbc.Col(card_scat,width=4)], justify="arround"),
            html.Br(),
    dbc.Row([dbc.Col(card_cont,width=6),dbc.Col(card_dens,width=6)]),
            
            ],  id="Collapse_ini2", is_open=True
    ),            
])        
#Pestaña2
    elif tab == 'tab-2':
        return html.Div([
            
    html.Br(),        
    dbc.Button(
        "Resumen",
        className="mb-3",
        color="primary",
        id="Resumen",
    ),

     dbc.Collapse([

                    html.Br(),
            html.P('Con el fin de evidenciar el comportamiento de cada una de las variables dentro de la base del icfes, se realizó un cluster jerárquico de acuerdo a los puntajes obtenidos en cada asignatura y el puntaje global.  Se realizo un corte en el cluster donde se obtuvo 3 ramas agrupando los estudiantes por su desempeño dejando los desempeños mas bajos en el cluster 1, desempeño medio en el cluster 2 y el desempeño mas alto en el cluster 3, como se observa en la gráfica del Dendrograma a continuación.'),
            html.Div([
            html.Img(src="https://raw.githubusercontent.com/FFG811/Visualizacion/main/Dendrogram.jpg"),
            ],    style={'textAlign': 'center'},
            ),
            html.Hr(),

            html.P('Con los grupos creados se analizo el comportamiento algunas variables cualitativas que hacen referencia a características de los colegios para identificar como influyeron el en desempeño de los estudiantes en las pruebas del icfes 2021-1 y se obtuvo los siguientes resultados:.'),

     ],    id="Collapse1", is_open=False
    ),
    html.Br(),        
#     dbc.CardHeader(
        dbc.Button(
            "DashBoard",
            className="mb-3",
            color="primary",
            id="DashBoard",
        ),
#     ),
    dbc.Collapse([         
    #Graficas
            html.Br(),
    dbc.Row([dbc.Col(card_barras2,width=4),dbc.Col(card_tree2,width=4),dbc.Col(card_box2,width=4)],),
            html.Br(),
    dbc.Row([dbc.Col(card_scatter2,width=7),dbc.Col(card_funnel2,width=5)]), ],
            id="Collapse2", is_open=True
    ),       
        
        ])
@app.callback(
    Output("Collapse1", "is_open"),
    [Input("Resumen", "n_clicks")],
    [State("Collapse1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("Collapse2", "is_open"),
    [Input("DashBoard", "n_clicks")],
    [State("Collapse2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("Collapse_ini", "is_open"),
    [Input("Resumen_ini", "n_clicks")],
    [State("Collapse_ini", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("Collapse_ini2", "is_open"),
    [Input("DashBoard_ini", "n_clicks")],
    [State("Collapse_ini2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
#################

@app.callback(
    Output('fig_scat', 'figure'),
    [Input('user_choice_X', 'value'),
     Input('user_choice_Y', 'value')])
def update_figure(area1, area2):
    fig_scat = px.scatter(df, x=area1, y=area2, color='COLE_JORNADA', symbol='COLE_JORNADA')
    return fig_scat
#fig_dist1 = px.histogram(df, x=df['PUNT_GLOBAL'])

@app.callback(
    Output('fig_dist1', 'figure'),
    [Input('user_choice', 'value')])
def update_figure(area):
    fig_distri = px.histogram(df, x=area)
    return fig_distri

@app.callback(
    Output('fig_box1', 'figure'),
    [Input('user_choice_gen', 'value')])
def update_figure(puntaje):
    fig_box1 = px.box(df, x = df['ESTU_GENERO'], y = puntaje)
    return fig_box1
#fig_box1 = px.box(df, x = df['ESTU_GENERO'], y = df['PUNT_GLOBAL'])


@app.callback(
    Output('fig_pie', 'figure'),
    [Input('user_choice_cat', 'value')])
def update_figure(categoria):
    fig_pie = px.pie(df, values=df[categoria].value_counts().values, names=df[categoria].value_counts().index)
    return fig_pie
# fig_pie = px.pie(df, values=df['COLE_CARACTER'].value_counts().values, names=df['COLE_CARACTER'].value_counts().index)


@app.callback(
    Output('fig_cont', 'figure'),
    [Input('user_choice_cont_X', 'value'),
     Input('user_choice_cont_Y', 'value')])
def update_figure(area1, area2):
    fig_cont = go.Figure(go.Histogram2dContour( x = df[area1], y = df[area2],contours_showlabels = True))
    return fig_cont
# fig_cont = go.Figure(go.Histogram2dContour( x = df['COLE_JORNADA'], y = df['PUNT_GLOBAL'],contours_showlabels = True))
#####################    

if __name__ == '__main__':
#     app.run_server(debug=True, port="2020")
    app.run_server(debug=False, host='0.0.0.0', port="2020")