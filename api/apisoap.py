from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class CalculService(ServiceBase):

    @rpc(Float, Float, _returns=Float)
    def calculTrajet(ctx, distance, vitesse):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = 'http:/localhost:4200'


        return  distance / vitesse


application = Application([CalculService], 'info.802.calcul.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

app = wsgi_application