import tkinter 
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import datetime
import time
import requests
from datetime import datetime
import pytz
import pycountry_convert as pc
import json




co0="#444466"
co1="#feffff"
co2="#6f9fbd"


fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde="#bfb86d"
fundo=fundo_dia


janela=Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)



ttk.Separatot(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)
frame_top=Frame(janela,width=320,height=50,bg=co1,pady=0,padx=0)
frame_top.grid(row=1,column=0)
frame_corpo=Frame(janela,width=320,height=50,bg=co1,pady=0,padx=0)
frame_corpo.grid(row=2,column=0,sticky=NW)
style=ttk.Style(janela)
style.theme_use('clam')




def info():
chave='018429e14ad71b92080590e40a10efa6'
cidade= e_local.get()
api_link='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)
r=requests.get(api_link)
dados=r.jason()


pais_codigo=dados['sys']['country']
zona_fuso=pytz.country_timezones[pais_codigo]
pais=pytz.country_names[pais_codigo]
zona=pytz.timezone(zona_fuso[0])
zona_horas=datetime.now(zona)
zona_horas=zona_horas.strftime("%d %m %Y | %H:%M:%S %p")



tempo=dados['main']['temp']
pressao=dados['main']['pressure']
umidade=dados['main']['humidity']
velocidade=dados['wind']['speed']
descricao=dados['mweather'][0]['description']




def pais_para_continente(country_name):
    pais_alpha=pc.country_name_to_country_alpha2(country_name)
    pais_continent_codigo=pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome=pc.convert_continet_code_to_continent_name(pais_continent_codigo)
    return pais_continente_nome

continente=pais_para_continente(pais)

l_cidade['text']=cidade+"-"+pais +"/"+continente
l_data['text']=zona_horas
l_pressao['text']="Pressao": "+str(pressao)"
l_umidade['text']=umidade
l_umidade_simbol['text']="%"
l_umidade_nome['text']="Umidade"
l_velocidade['text']="velocidade do vento:"+str(velocidade)
l_descricao['text']=descricao


zona_periodo=datetime.now(zona)
zona_periodo=zona_periodo.strftime("%H")

global imagem
zona_periodo=int(zona_periodo)
if zona_periodo <=5:
    imagem=Image.open('images/lua.png')
    fundo=fundo_noite
elif zona_periodo <=11 :
    imagem=Image.open('imagens/sol_dia.png')
    fundo=fundo.dia
elif zona_periodo <=17:
    imagem=Image.open('images/sol_tarde.png')
    fundo=fundo_tarde
elif zona_periodo <=23:
    imagem=Image.open('images/lua.png')
    fundo=fundo_noite
else:
    pass

imagem=imagem.resize((130,130),Image.ANTIALIAS)
imagem=ImageTk.PhotoImage(imagem)
l_icon=Label(frame_corpo, image=imagem,bg=fundo)
l_icon.place(x=160, y=50)


janela.configure(bg=fundo)
frame_corpo.configure(bg=fundo)
frame_top.configure(bg=fundo)
l_cidade['bg']=fundo
l_data['bg']=fundo
l_pressao['bg']=fundo
l_umidade['bg']=fundo
l_umidade_nome['bg']=fundo
l_umidade_simbol['bg']=fundo
l_velocidade['bg']=fundo
l_descricao['bg']=fundo



e_local= Entry(frame_top,width=20, justify='left',font=("",14),highlightthickness=1,relief="solid")
e_local.place(x=15, y=10)

b_ver = Button(frame_top,command=info, text="Ver clima", height=1, bg=co1, fg=co2,font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_ver.place(x=250, y=10)

l_cidade = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co1)
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_data.place(x=10, y=54)

l_umidade = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 45 '), bg=fundo, fg=co1)
l_umidade.place(x=10, y=100)

l_umidade_simbol = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 bold '), bg=fundo, fg=co1)
l_umidade_simbol.place(x=85, y=110)

l_umidade_nome = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 8 '), bg=fundo, fg=co1)
l_umidade_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_corpo, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_descricao.place(x=170, y=190)



janela.mainloop()