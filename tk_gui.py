from tkinter import *
from tkinter import Label

root=Tk()
root.title('Mapapp')
root.geometry('1025x760')

ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szegoly_obiektow.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
ramka_mapa.grid(row=2, column=0, columnspan=8)

#ramka_lista_obiektow
label_lista_obiektow=Label(root,text="Lista obiektów:")
listbox_lista_obiektow=Listbox(ramka_lista_obiektow)
button_pokaz_szczegoly=Button(ramka_lista_obiektow,text='Pokaż szczegóły')
button_usun_obiekt=Button(ramka_lista_obiektow,text='Usuń obiekt')
button_edytuj_obiekt=Button(ramka_lista_obiektow,text='Edytuj obiekt')

label_lista_obiektow.grid(row=0, column=0, cloumnspan=3)
listbox_lista_obiektow.grid(row=1, column=0, cloumnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)


#ramka_formularz
label_formularz=Label(ramka_formularz,text="Formularz:")
label_name=Label(ramka_formularz,text="Imię:")
label_surname=Label(ramka_formularz,text="Nazwisko:")
label_posts=Label(ramka_formularz,text="liczba postów:")
label_location=Label(ramka_formularz,text="Miejscowość:")

entry_name=Entry(ramka_formularz)
entry_surname=Entry(ramka_formularz)
entry_posts=Entry(ramka_formularz)
entry_location=Entry(ramka_formularz)

button_dodaj_obiekt=Button(ramka_formularz,text='Dodaj')

label_formularz.grid(row=0, column=0,columnspan=2)
label_name.grid(row=1, column=0, sticy=W)
label_surname.grid(row=2, column=0, sticky=W)
label_posts.grid(row=3, column=0, sticky=W)
label_location.grid(row=4, column=0, sticky=W)

entry_name.grid(row=1, column=1)
entry_surname.grid(row=2, column=1)
entry_posts.grid(row=3, column=1)
entry_location.grid(row=4, column=1)

button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)


#ramka_szczegoly_obiektu
label_szczegoly_obiektu=Label(ramka_szegoly_obiektow,text='Szczegóły obiektów',width=10)
label_name_szczegoly_obiektu=Label(ramka_szegoly_obiektow,text='imie',width=10)
label_name_szczegoly_obiektu_wartosc=Label(ramka_szegoly_obiektow,text='imie',width=10)
label_surname_szczegoly_obiektu=Label(ramka_szegoly_obiektow,text='Nazwisko', width=10)
label_surname_szczegoly_obiektu_wartosc=Label(ramka_szegoly_obiektow,text='Nazwisko',width=10)
label_posts_szczegoly_obiektu=Label(ramka_szegoly_obiektow,text='posty',width=10)
label_posts_szczegoly_obiektu_wartosc=Label(ramka_szegoly_obiektow,text='posty',width=10)
label_location_szczegoly_obiektu=Label(ramka_szegoly_obiektow,text='Miejscowość',width=10)
label_location_szczegoly_obiektu_wartosc=Label(ramka_szegoly_obiektow,text='Miejscowość',width=10)

label_szczegoly_obiektu.grid(row=0, column=0,sticky=W)
label_name_szczegoly_obiektu.grid(row=1, column=0)
label_name_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_surname_szczegoly_obiektu_wartosc.grid(row=1, column=2)
label_surname_szczegoly_obiektu.grid(row=1, column=2)
label_posts_szczegoly_obiektu.grid(row=1, column=4)
label_posts_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_location_szczegoly_obiektu.grid(row=1, column=6)
label_szczegoly_obiektu.grid(row=1, column=7)




#ramka_mapa
map_widget = tkintermapview.TkinterMapView(root_tk, width=1050, height=400, corner_radius=0)
map_widget.set_position(deg_x=.52.23 , deg_y=.21)  # Warszawa, Polska
map_widget.set_zoom(5)
map_widget.grid(row=0, column=0, columnspan=8)



root.mainloop()