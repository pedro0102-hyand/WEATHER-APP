import requests
import datetime
import json
import pytz
import pycountry_convert as pc

chave='018429e14ad71b92080590e40a10efa6'
cidade= 'Rio de Janeiro'
api_link='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)
r=requests.get(api_link)
dados=r.jason()
print(dados)
print('*' *45)

pais_codigo=dados['sys']['country']
print(pais_codigo)
zona_fuso=pytz.country_timezones[pais_codigo]
pais=pytz.country_names[pais_codigo]
zona=pytz.timezone(zona_fuso[0])
zona_horas=datetime.now(zona)
zona_horas=zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

tempo=dados['main']['temp']
pressao=dados['main']['pressure']
umidade=['main']['humidity']
velocidade=['wind']['speed']
descricao=['mweather'][0]['description']


def pais_para_continente(i):
    pais_alpha=pc.country_name_to_country_alpha2(i)
    pais_continent_codigo=pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome=pc.convert_continet_code_to_continent_name(pais_continent_codigo)
    return pais_continente_nome
continente=pais_para_continente(pais)

country_code=pc.country_name_to_country_alpha2("China",cn_name_forwat="default")
continente_name=pc.country_alpha2_to_continent_code(country_code)








