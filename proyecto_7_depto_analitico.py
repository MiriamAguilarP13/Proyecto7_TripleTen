# %% [markdown]
# # Análisis de Y.Afisha
# 
# # Descripción del proyecto
# Haciendo prácticas en el departamento analítico de Y.Afisha. Tu primera tarea es ayudar a optimizar los gastos de marketing.  
# Se dispone de:  
# -- Registros del servidor con datos sobre las visitas a Y.Afisha desde  de 2017 hasta  2018.  
# -- Archivos con todos los pedidos del período.  
# -- Estadísticas de gastos de marketing.

# %% [markdown]
# # Contenido
# 
# * [Objetivos](#objetivos)
# * [Etapas](#etapas)
# * [Diccionario de Datos](#diccionario)
# * [1 Inicialización](#inicio)
# * [2 Cargar datos](#cargar_datos)
#     * [2.1 Descarga de una pequeña porción de datos](#porcion)
#     * [2.2 Descarga Completa de Datos Optimizados](#datos_op)
#     * [2.3 Estilo del encabezado](#header_style)
# * [3 Informe del Producto ](#informe_producto)
# * [4 Informe de Ventas](#informe_ventas)
# * [5 Informe de Marketing](#informe_marketing)
# * [6 Resumen y Conclusión General](#end)

# %% [markdown]
# # Objetivos <a id='objetivos'></a>  
# 
# * Obtener una comprensión general de los datos.  
# * Identificar tendencias y patrones importantes.  
# * Preparar los datos para un análisis más detallado.  
# * Cómo la gente usa el producto.  
# * Cuándo empiezan a comprar.  
# * Cuánto dinero trae cada cliente.
# 

# %% [markdown]
# # Etapas <a id='etapas'></a>  
# 
# Se tiene un dataset con la información necesaria sobre el departamento analítico de Y.Afisha, no hay información previa sobre la calidad de los datos, por lo tanto se revisará antes de comenzar a analizar los datos. 
# 
# Pasos a realizar:
# 1. Importar las librerías necesarias
# 2. Descripción de los datos, leer y guardar el Dataset con Pandas de manera optimizada.  
# 3. Procesamiento de los datos, preparar los datos para que sean analizados.
# 4. Análisis de datos y creación de gráficos.

# %% [markdown]
# # Diccionario de Datos <a id='diccionario'></a>   
# 
# * La tabla visits (registros del servidor con datos sobre las visitas al sitio web):  
#     * Uid: identificador único del usuario;  
#     * Device: dispositivo del usuario;  
#     * Start Ts: fecha y hora de inicio de la sesión;  
#     * End Ts: fecha y hora de término de la sesión;  
#     * Source Id: identificador de la fuente de anuncios de la que proviene el usuario.  
#     * Todas las fechas de esta tabla están en formato AAAA-MM-DD.  
# * La tabla orders (datos sobre pedidos):  
#     * Uid: identificador único del usuario que realiza un pedido;  
#     * Buy Ts: fecha y hora del pedido;  
#     * Revenue: ingresos de Y.Afisha de este pedido.  
# * La tabla costs (datos sobre gastos de marketing):  
#     * source_id: identificador de la fuente de anuncios  
#     * dt: fecha;  
#     * costs: gastos en esta fuente de anuncios en este día.

# %% [markdown]
# ## Inicialización <a id='inicio'></a>

# %%
# se cargan todas las librerías
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# %% [markdown]
# ## Cargar datos <a id='cargar_datos'></a>

# %% [markdown]
# ### Descarga de una pequeña porción de datos <a id='porcion'></a>

# %%
# se descargan las primeras 200 filas de cada archivo para revisar que cada columna contenga el tipo de datos correcto
# Y con base en lo anterior optimizar los datos para el análisis

visits_log_us = pd.read_csv('files/datasets/visits_log_us.csv', nrows=200)
orders_log_us = pd.read_csv('files/datasets/orders_log_us.csv', nrows=200)
costs_us = pd.read_csv('files/datasets/costs_us.csv', nrows=200)

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se imprimen las primeras 5 filas de cada DataFrame y despues la información con `info()` para revisar el tipo de dato para cada columna.
#     
# </span>
#     
# </div>
# 

# %%
# DataFrame sobre las visitas
visits_log_us.head()

# %%
# DataFrame sobre las visitas
visits_log_us.info()

# %%
# DataFrame sobre las ordenes
orders_log_us.head()

# %%
# DataFrame sobre las ordenes
orders_log_us.info()

# %%
# DataFrame sobre los costos
costs_us.head()

# %%
costs_us.info()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Cada DataFrame tiene columnas con tipo de datos object y son columnas que tienen fechas, sólo la columna `Device` del DataFrame `visits_log_us` no son fechas, por lo tanto, para esta columna se revisará cuantas categorías tiene y se convertirá al tipo de dato 'category'. Las columnas de fecha se convertirán al tipo de dato datetime con `to_datetime`.
#     
# </span>
#     
# </div>

# %%
# se busca la cantidad de valores únicos en la columna 'Device' del DataFrame 'visits_log_us' 
# se emplea el método value_counts()
visits_log_us['Device'].value_counts()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Sólo se tienen dos categorías, entonces cuando se descarguen todos los datos de cada DataFrame se hará con los tipos de datos correctos.  
# También, en los DataFrame `visits_log_us` y `orders_log_us` los nombres de las columnas no tienen el formato **snake_case**, lo anterior se corrgirá en pasos posteriores.
#     
# </span>
#     
# </div>

# %% [markdown]
# ### Descarga Completa de Datos Optimizados  <a id='datos_op'></a>

# %%
# se descargan los datos completos con los tipos de datos correctos
visits_log_us = pd.read_csv('/datasets/visits_log_us.csv', dtype= {'Device': 'category'}, parse_dates= ['Start Ts', 'End Ts'])
orders_log_us = pd.read_csv('/datasets/orders_log_us.csv', parse_dates= ['Buy Ts'])
costs_us = pd.read_csv('/datasets/costs_us.csv', parse_dates= ['dt'])

# %%
#se revisa la información de los datos de las visitas
visits_log_us.info()

# %%
#se revisa la información de los datos de las ordenes
orders_log_us.info()

# %%
#se revisa la información de los datos de los costos
costs_us.info()

# %% [markdown]
# ### Estilo del encabezado <a id='header_style'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se cambian los encabezados de los DataFrame `visits_log_us` y `orders_log_us` con el formato snake_case.  
#     
# </span>
#     
# </div>

# %%
#  se usa el atributo columns para obtener una lista con los nombres de las columnas de 'visits_log_us'
col_names_visits = visits_log_us.columns
col_names_visits

# %%
#  se usa el atributo columns para obtener una lista con los nombres de las columnas de 'orders_log_us'
col_names_orders = orders_log_us.columns
col_names_orders

# %%
# se crea una función para cambiar los nombres de las columnas a minúscula y sustituir los espacios por '_'
def underscore_lower_names(column_names):
    '''
    Función que pone los caracteres en minúscula y los espacios los reemplaza por guión bajo ('_').
    '''
    lower_col_names = [] # se define una nueva lista vacia para guardar los nuevos nombre de las columnas en minúscula
    for col in column_names:
        lower_names = col.lower()
        lower_col_names.append(lower_names)
    
    under_col_names = [] # se define una nueva lista vacia para guardar los nuevos nombre de las columnas con '_'

    for col in lower_col_names:
        underscore_col_names = col.replace(' ', '_')
        under_col_names.append(underscore_col_names)
        
    return under_col_names
    

# %%
# se corrigen los nombres de las columnas del DataFrame 'visits_log_us' 
new_visits_names = underscore_lower_names(col_names_visits)
# Se asignan los nuevos nombres de columna
visits_log_us.columns = new_visits_names
visits_log_us.columns

# %%
# se corrigen los nombres de las columnas del DataFrame 'orders_log_us' 
new_orders_names = underscore_lower_names(col_names_orders)
# Se asignan los nuevos nombres de columna
orders_log_us.columns = new_orders_names
orders_log_us.columns

# %% [markdown]
# ### Valores ausentes y duplicados <a id='missing_duplicated_values'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se verifica si hay valores ausentes y duplicados para cada DataFrame.
#     
# </span>
#     
# </div>
# 

# %%
# Valores ausentes en el DataFrame de visitas
visits_log_us.isna().sum()

# %%
# Valores duplicados en el DataFrame de visitas
visits_log_us.duplicated().sum()

# %%
# Valores ausentes en el DataFrame de ordenes
orders_log_us.isna().sum()

# %%
# Valores duplicados en el DataFrame de ordenes
orders_log_us.duplicated().sum()

# %%
# Valores ausentes en el DataFrame de costos
costs_us.isna().sum()

# %%
# Valores duplicados en el DataFrame de costos
costs_us.duplicated().sum()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# No hay valores ausentes ni duplicados en los DataFrame, por lo tanto los datos están listos para su análisis.
#     
# </span>
#     
# </div>

# %% [markdown]
# ## Informe del Producto <a id='informe_producto'></a>

# %%
# se imprimen las 5 filas del DataFrame visits_log_us
visits_log_us.head()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Para saber cuántas personas usan el sevidor cada día, semana y mes; primero se crea una columna para el año, mes, semana y día en el DataFrame `visits_log_us`. Con `dt` se extrae el dato de la fecha de interes.
#     
# </span>
#     
# </div>

# %%
# se crean las nuevas columnas
visits_log_us['session_year'] = visits_log_us['start_ts'].dt.year
visits_log_us['session_month'] = visits_log_us['start_ts'].dt.month
visits_log_us['session_week'] = visits_log_us['start_ts'].dt.isocalendar().week
visits_log_us['session_date'] = visits_log_us['start_ts'].dt.date

# %%
# se imprimen las 3 filas del DataFrame visits_log_us
visits_log_us.head(3)

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se calcula el número de usuarios que usan el servicio por día, mes y semana, que sería el DAU, MAU y WAU, respectivamente. 
# - **DAU**: el número de usuarios activos diarios (únicos);
# - **WAU**: el número de usuarios activos semanales;
# - **MAU**: el número de usuarios activos mensuales.
#     
# </span>
#     
# </div>

# %%
# Agruparemos los datos por fecha del día de la sesión y buscaremos la media
dau_total = visits_log_us.groupby(['session_date']).agg({'uid': 'nunique'}).mean().round()
dau_total

# %%
# Agruparemos los datos por semana de la sesión y buscaremos la media
wau_total = visits_log_us.groupby(['session_week']).agg({'uid': 'nunique'}).mean().round()
wau_total

# %%
# Agruparemos los datos por mes de la sesión y buscaremos la media
mau_total = visits_log_us.groupby(['session_month']).agg({'uid': 'nunique'}).mean().round()
mau_total

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Para saber con que frecuancia los usuarios y usuarias regresan, se calcula el Factor de Adherencia. Esta métrica nos dice qué tan leal es la audiencia, con qué frecuencia regresan a la aplicación o servicio. El factor de adherencia (sticky factor) se calcula: `DAU/WAU` o `DAU/MAU`.
#     
# </span>
#     
# </div>

# %%
# calcula el factor de adherencia semanal
sticky_wau = dau_total / wau_total
sticky_wau

# %%
# calcula el factor de adherencia semanal
sticky_mau = dau_total / mau_total
sticky_mau

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se calcula el número de sesiones por día y el número de usuarios por día. También la duración de cada sesión y el número de sesiones por usuario.
#     
# </span>
#     
# </div>

# %%
# se usa groupby() y la función agg() para contabilizar el total de las sesiones por día y 
# el número de usuarios únicos por día
sessions_per_user = visits_log_us.groupby(['session_year', 'session_date']).agg({'uid': ['count', 'nunique']})
# se renombran las columnas 
sessions_per_user.columns = ['n_sessions', 'n_users']
# se imprimen 5 filas del resultado
sessions_per_user.head()

# %%
# se calcula el número de sesiones por usuario, dividiendo el número de sesiones entre el número de usuarios
# se crea una nueva columna para almacenar el resultado
sessions_per_user['sess_per_user'] = sessions_per_user['n_sessions'] / sessions_per_user['n_users']
# se muestran 5 filas
sessions_per_user.head()

# %%
# se grafica un histograma para observar la distribución del número de sesiones por usuario para cada día

sessions_per_user['sess_per_user'].plot(kind= 'hist',
                                        bins= 100,
                                       title= 'Número de sesiones por usuario',
                                       figsize= (12, 8),
                                       color= 'darkcyan'
                                       )
plt.xlabel('Número de Sesiones por Día')
plt.ylabel('Frecuencia')
plt.show()

# %%
# se calcula la moda para el número de sesiones más frecuente por día
sessions_per_user['sess_per_user'].mode()

# %%
# se calculan la duración de las sesiones, se crea una nueva columna en el DataFrame 'visits_log_us'
visits_log_us['session_duration_min'] = (visits_log_us['end_ts'] - visits_log_us['start_ts']).dt.seconds
# se transforman los segundos a minutos
visits_log_us['session_duration_min'] = visits_log_us['session_duration_min'] / 60
# se imprimen las primeras 5 filas
visits_log_us.head()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se observa que hay sesiones con una larga duración, por tanto, se calcularan sus estadísticos descriptivos con `describe()` para esta columna y se graficará un histograma.
#     
# </span>
#     
# </div>

# %%
visits_log_us['session_duration_min'].describe()

# %%
# ahora se grafica un histograma para observar la distribución de la duración de las sesiones
visits_log_us['session_duration_min'].plot(kind= 'hist',
                                        bins= 100,
                                       title= 'Duración de las Sesiones',
                                       figsize= (10, 6),
                                       color= 'darkcyan'
                                       )
plt.xlabel('Duración de las Sesiones en Minutos')
plt.ylabel('Frecuencia')
plt.show()


# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Observaciones:**  
# A partir de los estadísticos descritivos se puede observar que probablemente hay valores atípicos, ya que el valor máximo de las duración de una sesión es de 1408 minutos. Lo anterior se confirma con el histograma, ya no tiene una distribución normal, por lo tanto, se busca la moda para saber la duración media de la sesión.
#     
# </span>
#     
# </div>

# %%
# se encuentra la moda con mode() para conocer la duración media de la sesión
visits_log_us['session_duration_min'].mode()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# La cantidad de usuarios activos diarios son de 908, a la semana 5,825 y al mes son 23,228. El factor de adherencia semanal es de 0.155, lo que nos dice que los usuarios interactuan con el servicio el 15.5 % de los días de las semana.  El factor de adherencia es bajo, por tanto, la frecuencia con la que los usuarios regresan a la semana se pueden mejorar. Por otro lado, el factor de adherencia mensual es es de 3.9 %, el cuál es muy bajo, también hay mucha área de oprtunidad para mejor dicho factor si el departamento de markenting desea aumentar la cantidad de los usuarios que regresan.  
# El número de sesiones diarias es de 1 aproximadamente, mientras que, la duración media de las sesiones es de 1 minuto. Hay valores para la duración de las sesión de 1408 minutos, aquí es importante revisar si son valores atípicos o sin los usuarios o usuarias dejaron abiertas sus sesiones.
# 
#     
# </span>
#     
# </div>

# %% [markdown]
# ## Informe de Ventas <a id='informe_ventas'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Para saber el tiempo que transcurre entre el registro y la conversión, es decir, cuando el/la usuario/a se convierte en cliente. Entonces se empleara el DataFrame `visits_log_us` para encontrar el primer registro (columna `start_ts`) y el DataFrame `orders_log_us` para encontrar la primera orden (columna `buy_ts`). Después se calcula la diferencia entre ambas fechas 
# 
# 
#     
# </span>
#     
# </div>

# %%
# agregar columna de mes de inicio de sesión en DataFrame 'visits_log_us'
# y en el DataFrame 'orders_log_us' la columna de mes de pedido
visits_log_us['session_month'] = visits_log_us['start_ts'].astype('datetime64[M]')
orders_log_us['order_month'] = orders_log_us['buy_ts'].astype('datetime64[M]')

# %%

# se busca la primer sesión para cada usuario
first_session_dates = visits_log_us.groupby('uid')['session_month'].min().reset_index()
# se cambia el nombre de la columna 
first_session_dates.columns = ['uid', 'first_session_month']
first_session_dates.head()

# %%
# se una al DataFrame 'visits_log_us' con merge
visits_log_us_ = visits_log_us.merge(first_session_dates, on= 'uid')
visits_log_us_.head(3)

# %%
# se busca la fecha para la primera orden para cada usuario
first_buy_dates = orders_log_us.groupby('uid')['order_month'].min().reset_index()
# se cambia el nombre de la columna 
first_buy_dates.columns = ['uid', 'first_buy_month']
first_buy_dates.head()

# %%
# se una al DataFrame 'orders_log_us' con merge
orders_log_us_ = orders_log_us.merge(first_buy_dates, on= 'uid')
orders_log_us_.head(3)

# %%
# se unen los DataFrame 'visits_log_us_' con 'orders_log_us_'
visits_orders = visits_log_us_.merge(orders_log_us_, on= 'uid')
visits_orders.head(3)

# %%
# se calcula los días trancurridos cuando el/la usuario/a se convierte en cliente
visits_orders['convertion_time_days'] = (visits_orders['first_buy_month'] - visits_orders['first_session_month']).dt.days
visits_orders.head(3)

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se categorizan los días, para esto se definen los intervalos  en los cuales categorizarán los valores de tiempo de conversión de la columna `convertion_time_days` y se guardan en `bins`. En la variable `labels` se alamcenan los nombres de las etiquetas para cada uno de los intervalos definidos en `bins`. Después se emplea la función `cut()` para asignar cada valor de `convertion_time_days` al intervalo adecuado según los límites definidos en bins, y luego se le asigna la etiqueta correspondiente de labels. 
#     
# </span>
#     
# </div>

# %%
# se categoriza el tiempo de conversión
bins = [-1, 0, 1, 7, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]  # Definir los intervalos 
labels = ['Conversion 0d', 'Conversion 1d', 'Conversion 1w', 'Conversion 1m', 'Conversion 2m', 'Conversion 3m', 'Conversion 4m', 'Conversion 5m', 'Conversion 6m', 'Conversion 7m', 'Conversion 8m', 'Conversion 9m', 'Conversion 10m', 'Conversion 11m', 'Conversion 12m']
visits_orders['conversion_category'] = pd.cut(visits_orders['convertion_time_days'], bins=bins, labels=labels)
# se imprime una muestra de filas
visits_orders.sample(5)

# %%
# ahora se crea una tabla dinámica para saber la cantidad de pedidos que hicieron los usuarios por cohorte (que son los que 
# se registracion por primera vez) y el tiempo que tardaron en hacer su primer pedido 'conversion_category'
first_session_cohort = visits_orders.pivot_table(index= 'first_session_month',
                                       columns= 'conversion_category',
                                       values= 'uid',
                                       aggfunc= 'nunique')

# %%
# se grafica un mapa de calor a partir de orders_pivot
plt.figure(figsize=(18, 9))

sns.heatmap(first_session_cohort, annot=True, fmt='g', cmap="crest", linewidth=.01)

plt.title('Cantidad de Usuarios por Primer Pedido', fontsize= 16)
plt.xlabel('Categoría de conversión', fontsize= 14)


plt.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# En en mapa de calor anterior muestra que los cohortes por primer inicio de sesión y la cantidad de usuarios que se hicieron su primer pedido por categoría de conversión, desde 0 días hasta 12 meses.  
# Se observa que para todas las cohortes los usuarios y usuarias hicieron su primer pedido el mismo día, (Conversion d). Las cohortes de octubre, noviembre y diciembre del 2017 tienen la mayoría de usuarios y usuarias que hicieron su primer pedido el mismo día, 3761, 3357 y 3491, respectivamente; probablemente es debido a la temporada, ya que se celebran diferentes festividades, por lo que los/las clientes pueden necesitar lo más pronto el producto.  
# También se observa que en algunas cohortes los y las clientes tardaron un mes en realizar su primer pedido y en otros hasta 4 meses; la cohorte de junio de 2017 es la única que tiene 54 usuarios que hicieron su primer pedido despues de 12 meses. Las usuarias y usurios del cohorte de mayo del 2018 la mayoría hizo su primer pedido el mismo día.   
# 
#     
# </span>
#     
# </div>

# %%
# Ahora las cohortes se definen por el periodo de tiempo de conversión
# se emplea una tabla dinámica para saber la cantidad de pedidos que hicieron de acuerdo a la fuente del anuncio
convertion_time_cohort = visits_orders.pivot_table(index= 'conversion_category',
                             columns= 'source_id',
                             values= 'uid',
                             aggfunc= 'nunique')

# %%
# se grafica un mapa de calor a partir de convertion_time_cohort
plt.figure(figsize=(18, 9))

sns.heatmap(convertion_time_cohort, annot=True, fmt='g', cmap="crest", linewidth=.01)

plt.title('', fontsize= 16)
plt.xlabel('Fuente de anuncios de la que proviene el usuario', fontsize= 14)


plt.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# En el mapa de calor anterior los usuarios se organizaron en cohortes de acuerdo a su periodo/tiempo de conversión, en el cohorte de 0 días la mayor cantidad de primeros pedidos fueron principalmente de tres fuentes: de la 4, 3 y 5.  
# Para las cohortes de 1 mes, 2, 3 y 4 meses, son las misma fuentes de anuncios las que tienen la mayoría de usuarios. La fuente 7 practicamente no genera primeras compras, sólo 1, por tanto no sería mala idea no usar más esa fuente de anuncios; por tanto, valdría más la pena centrar más esfuerzos en las fuentes 3, 4 y 5. También las fuentes de anuncios 1 y 2 genera una importante cantidad de primeras compras.  
# 
#     
# </span>
#     
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Ahora se calcula el total de pedidos para cada mes que se realizó la compra/pedido, también se calcula el promedio de pedidos que hizo cada usuario por mes. Se emplea el DataFrame `orders_log_us`.
# 
#     
# </span>
#     
# </div>

# %%
# se agrupan los datos por mes de compra
order_period = orders_log_us.groupby(['order_month'])['uid'].agg(['count', 'nunique']).reset_index()
# se cambia el nombre de las columnas
order_period.columns = ['order_month', 'n_orders', 'n_users']
# se crea una columna para las ordenes por usuario
order_period['orders_per_user'] = order_period['n_orders'] / order_period['n_users']
order_period.head()

# %%
# Se grafica los pedidos totales para cada mes donde se efectuo la compra
order_period.plot(x = 'order_month',
                  y= 'n_orders',
                  kind= 'line',
                  figsize= [12,8],
                  fontsize= 12,
                  rot= 90,
                  color= 'darkcyan'
                       )
plt.title('Pedidos de los Usuarios por Mes', fontsize=15)
plt.xlabel('Mes del Pedido', fontsize=15)
plt.ylabel('Cantidad Total de Pedidos', fontsize=15)


plt.show()

# %%
# Se calcula el promedio de los pedidos y el promedio de pedidos por usuario/a 
total_orders_mean = order_period['n_orders'].mean().round()
orders_per_user_mean = order_period['orders_per_user'].mean().round()
print(f'El promedio de pedidos que se hacen de {total_orders_mean}')
print(f'Los pedidos en promedio que se hacen por usuario/a son de {orders_per_user_mean}')

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# La cantidad de pedidos que hicieron los usuarios es mayor en los meses de octubre, noviembre y diciembre de 2017, siendo diciembre el mes con más pedidos con 6,000 pedidos aproximadamente; se puede deber a que son meses en los cuales se celebran varias festiviadades en la cuales las personas dan regalos. Después la cantidad de pedidos disminuye hay un ligero repunte en febrero y marzo del 2018, pero después vuelven a disminuir. En promedio cada usuario y usuaria hacen 1 pedido.
#     
# </span>
#     
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Para calcular el LTV (la cantidad total de dinero que un cliente aporta a la empresa en promedio al realizar compras), se agrupan los datos por clientes con la fecha de su primera compra a partir del DataFrame `orders_log_us`, por tanto los/las clientes se organizan por cohorte por fecha de primer pedido. Después se agrupan por fecha de la cohorte y se calcula la cantidad de usuarios y usuarias únicos/as. Luego el DataFrame que tiene las fechas de las cohortes se agregan al DataFrame `orders_log_us` con `merge`, enseguida se agrupan los datos por cohorte y por la fecha de compra (mes de compra) y se calcula el total de ganancias (revenue) para cada grupo. 
#     
# </span>
#     
# </div>

# %%
# se grupan los datos por id de usuario y se busca la fecha de su primer pedido con min()
first_orders = orders_log_us.groupby('uid').agg({'order_month': 'min'}).reset_index()
first_orders.columns = ['uid', 'first_order_month']
first_orders.head()

# %%
# se calcula el tamaño de la cohorte contando los usuarios y usuarias únicos/as para cada cohorte
cohort_sizes = first_orders.groupby('first_order_month').agg({'uid': 'nunique'}).reset_index()
# Cambia el nombre de las columnas
cohort_sizes.columns = ['first_order_month', 'n_buyers']
cohort_sizes.head()

# %%
# se agregan los meses de la primera compra de los clientes y clientas al DataFrame orders_log_us
orders_with_first_order = orders_log_us.merge( first_orders, on= 'uid')
orders_with_first_order.head()

# %%
# se agrupan los datos por fecha de la cohorte y el mes de la compra y se calculan las ganancias totles con sum()
cohorts = orders_with_first_order.groupby(['first_order_month', 'order_month']).agg({'revenue': 'sum'}).reset_index()
cohorts.head()

# %%
# se hace un merge de los DataFrame 'cohort_sizes' y 'cohorts'
report = pd.merge(cohort_sizes, cohorts, on='first_order_month')
report.head()

# %%
# se crea una columna para calcular la edad de cada cohorte
report['age'] = report['order_month'] - report['first_order_month']
# se cambia a meses
report['age'] = report['age'] / np.timedelta64(1, 'M')
# se redondean los meses
report['age'] = report['age'].round().astype('int')
report.head()

# %%
# se calcula el LTV, dividiendo las ganacias ('revenue') entre la cantidad de compradores ('n_buyers')
report['ltv'] = report['revenue'] / report['n_buyers']
report.head()

# %%
# Visualizaremos las cohortes como una tabla dinámica para visualizar el
# ltv dpromedio por cohorte y por edad de la cohorte
result = report.pivot_table(index= 'first_order_month',
                            columns= 'age',
                            values= 'ltv',
                            aggfunc= 'mean').round()


# %%
# se grafica un mapa de calor a partir de result
plt.figure(figsize=(16, 9))

sns.heatmap(result, annot=True, fmt='0.1f', cmap="crest", linewidth=.01)

plt.title('LTV promedio de los/las Clientes.', fontsize= 16)
plt.xlabel('Edad de la Cohorte', fontsize= 14)


plt.show()

# %%
# se calcula el ltv total por cohorte
result.sum(axis=1).round().sort_values(ascending= False)

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# En primer mes de vida de las cohortes es donde los/las clientes aportan más ganancias a la empresa, desués el ltv disminuye. En las cohortes de junio de 2017 aumenta a 1 en su mes 4 de vida y se mantiene hasta el mes 11 de vida, la cohorte de septimebre también aumenta su LTV a 4 en el mes 4 de vida. Las cohortes que aporta más ganancias es la de junio y septiembre de 2017.  
#  
# </span>
#     
# </div>

# %% [markdown]
# ## Informe de Marketing <a id='informe_marketing'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Se calculan los gastos totales en publicidad del Datarame `costs_us`, después se unirá el resultado al DataFrame `report`. Luego se calcula cuánto dinero se gastó a lo largo del tiempo, enseguida se hará el calculo del costo de adquisción de clientes de cada una de las fuentes. Luego se calcula el ROMI dividiendo el LTV (cantidad total de dinero que un cliente aporta a la empresa) entre el CAC (el costo de atraer a cada cliente).
# </span>
#     
# </div>

# %%
# se encuentra la suma total de los costos de marketing para cada mes y se guarda el resultado como monthly_costs
monthly_costs = costs_us.groupby(['dt', 'source_id'])['costs'].sum().reset_index()
monthly_costs.head()

# %%
# Agreguemos los datos sobre los costos al DataFrame 'report'
report_with_costs = pd.merge(report, monthly_costs, left_on= 'order_month', right_on= 'dt')
report_with_costs.head()


# %%
# Se agrupa el total de los costos de marketing a lo largo del tiempo
source_costs = report_with_costs.groupby('dt')['costs'].sum().sort_values(ascending= False)
source_costs

# %%
# se grafican los costos totales a los largo del tiempo
source_costs.plot(
                  kind= 'line',
                  figsize= [12,8],
                  fontsize= 12,
                  color= 'darkblue'
                       )
plt.title('Costos Totales a lo largo del tiempo', fontsize=15)
plt.xlabel('Fecha', fontsize=15)
plt.ylabel('Cantidad Total de Costos', fontsize=15)

plt.show()

# %%
# Agregamos una columna para calcular el CAC (costo de adquisición de clientes/as)
report_with_costs['cac'] = report_with_costs['costs'] / report_with_costs['n_buyers']
report_with_costs.head()

# %%
# se agrupan la suma del costo de adquisición por la fuente del anuncio
cac_by_source = report_with_costs.groupby('source_id')['cac'].sum().sort_values(ascending= False)
cac_by_source

# %%
# se grafican el cac por fuente del anuncio
cac_by_source.plot(
                  kind= 'bar',
                  figsize= [10,6],
                  fontsize= 12,
                  rot= 0,
                  color= 'darkblue'
                       )
plt.title('Costo de Adquisición por Fuente del Anuncio', fontsize=15)
plt.xlabel('Fuente del Anuncio', fontsize=15)
plt.ylabel('Costo de Adquisición', fontsize=15)

plt.show()

# %%
# se calcula el ROMI (retorno de la inversión en marketing, o return on marketing investment en inglés) 
# se divide el LTV por el CAC
report_with_costs['romi'] = report_with_costs['ltv'] / report_with_costs['cac']
report_with_costs.head()

# %%
result_romi = report_with_costs.pivot_table(index='first_order_month', 
                             columns='age', 
                             values='romi', 
                             aggfunc='mean')

# %%
# se grafica un mapa de calor a partir de result_romi
plt.figure(figsize=(16, 9))

sns.heatmap(result_romi, annot=True, fmt='0.0f', cmap="crest", linewidth=.01)

plt.title('LTV promedio de los/las Clientes.', fontsize= 16)
plt.xlabel('Edad de la Cohorte', fontsize= 14)


plt.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# El total de dinero gastado fue en el mes de marzo y febrero de 2018, con 14,372 y 12,408, respectivmente; los meses con menor gasto fueron julio y junio de 2017 con 756 y 735, respectivamente.  
# El costo de atraer a cada cliente por fuente de anuncio fueron la 3, 5 y 4 con 12.5, 4.5 y 3.8, respectivamente.  
# El ROMI, nos dice la rentabilidad de la inversión en marketing, en el primer mes de vida en todas las cohortes se recuperaron los gastos e incluso generaron un beneficio muy alto.  Las cohortes que generaron un mayor beneficio fueron las de julio, septiembre, octubre de 2017 y las de marzo y mayo del 2018. Después del primer ciclo de vida el ROMI es menor, sin embargo, los gastos en publicidad se recuperaron.
#  
# </span>
#     
# </div>

# %% [markdown]
# ## Resumen y Conclusión General <a id='end'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">
#     
# **Resumen General de los pasos seguidos:**  
# 1. Se descargaron los datos y se prepararon para el análisis.  
# 2. Se almacenaron los datos de visitas, pedidos y gastos.  
# 3. Se optimizaron los datos para el análisis, que cada columna contenga el tipo de datos correcto.  
# 4. Se buscaron valores ausentes y duplicados.    
# 5. Se hicieron los cálculos correspondientes para el informe del producto, el número de usuarios activos por día, semana y mes, la cantidad de sesiones por usuario, la duración de las sesiones en minutos.  
# 6. Para el informe de ventas se calculo el tiempo que transcurre entre el registro del usuario/usuaria y su primera compra (tiempo de conversión), luego se categorizaron de acuerdo al tiempo de conversión.   
# 7. Después se calcularon el total de pedidos por mes y el promedio de pedidos por usuario/usuaria., también se calculó el LTV.  8. Para el informe de marketing se calcularon los gastos totales y cuaánto se gastó a lo largo del tiempo. Después se calculó el costo de adquisición de los/las clientes y el ROMI .  
# 
#     
# </span>
# 
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# 
# <span style="color: darkblue;">
#     
# **Conclusión General:**  
# 1. La cantidad de usuarios activos diarios, semanales y mensuales muestra una participación constante (908, 5,825 y 23,228, respectivamente), sin embargo, el factor de adherencia semanal y mensual es bajo, de 0.155 y 0.039, respectivamente. Por tanto, hay área de oportunidad para incrementar dicho valor, si es lo que se desea.  
#     
# 2. La duración promedio de las sesiones es de 1 minuto, no obstante, hay algunos valores atípicos que requieren revisión para determinar si son errores o sesiones dejadas abiertas.  
#     
# 3. La mayoría de las conversiones (primeros pedidos de las/los clientes), sin embargo, hay usuarios y usuarias que hacen el primer pedido  hasta los 4 meses. Por lo que se puede sugerir hacer unainvestigación por que dichos clientes tardan 4 meses en hacer su primer pedido.  
#     
# 4. El análisis de cohortes revela algunos patrones de comportamiento de acuerdo a la fuente de anuncios, sugiriendo oportunidades para centrar esfuerzos en fuentes más efectivas, que son las 4, 3 y 5.  
#     
# 5. La cantidad de pedidos es más alta en los meses festivos como octubre, noviembre y diciembre, siendo diciembre el mes con más pedidos con 6,000 aproximadamente.  
#     
# 6. El LTV alcanza su punto máximo en el primer mes de vida de las cohortes y disminuye con el tiempo, destacando la importancia de las primeras interacciones con los clientes.  
#     
# 7. Los meses de marzo y febrero de 2018 registraron el mayor gasto en publicidad, mientras que en julio y junio de 2017 tuvieron los gastos más bajos.  
#     
# 8. El costo de adquisición por cliente varía entre el tipo de fuentes de anuncios, destacando las fuentes 3, 5 y 4 como más eficientes en términos de costos, las cuales coiciden o son las que tienen mayor cantidad de pedidos a lo largo del tiempo.  
#     
# 9. Con base en el valor de ROMI indica una rentabilidad positiva en el primer mes de vida de las cohortes, pero disminuye en los ciclos posteriores. Sin embargo, se logran recuperar los gastos en publicidad, por tanto, la campaña de publicidad es bastante excepcional y sugiere fue altamente rentable.  
#     
# Con base en los resultados, se aprecia que hay una oportunidad para mejorar la retención de los usuarios, enfatizar las estrategias de marketing en las fuentes más efectivas que son las 3,4 y 5, y optimizar los costos de adquisición para mantener una buena rentabilidad.
#     
#  
# 
#     
# </span>
# 
# </div>

# %%



