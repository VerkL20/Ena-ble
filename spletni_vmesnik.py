import model
import bottle

datoteka_s_stanjem = 'datoteka_s_stanjem.json'
SECRET = 'nekaskrivnost'
enacble = model.Iskanje_enacbe()
#enacble.nalozi()
id_igre = enacble.nova_igra()


@bottle.get('/')
def osnovna_stran():
    return bottle.template('zacetna_stran.html')

@bottle.post('/novo/')
def nova_igra():
    #id_igre = enacble.nova_igra()
    #bottle.response.set_cookie('id_igre', str(id_igre), secret=SECRET, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def igra():
    #id_igre = enacble.nova_igra()
    #id_igre = int(bottle.request.get_cookie('idigre', secret=SECRET))
    (igra, stanje) = enacble.igre[id_igre]
    return bottle.template('igra.html', igra=igra, id_igre=id_igre, stanje=stanje)

@bottle.post('/igra/')
def ugibaj():
    #id_igre = enacble.nova_igra()
    #id_igre = int(bottle.request.get_cookie('idigre', secret=SECRET))
    ugibek = bottle.request.forms.getunicode('ugib')
    enacble.ugibaj(id_igre, ugibek)
    #igra, stanje = enacble.igre[id_igre]
    bottle.redirect('/igra/')

@bottle.get("/views/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="views")

bottle.run(reloader=True, debug=True)