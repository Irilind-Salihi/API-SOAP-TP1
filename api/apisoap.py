from spyne import Application, rpc, ServiceBase, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class CalculService(ServiceBase):

    @rpc(Decimal, Decimal, _returns=Decimal)
    def calculTrajet(ctx, distance_km, vitesse_km_h):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = '*'


        return  distance_km/vitesse_km_h


application = Application([CalculService], 'info.802.calcul.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

app = wsgi_application