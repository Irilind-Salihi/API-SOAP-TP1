from spyne import application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Decimal
from wsgiref.simple_server import make_server
from spyne import Iterable


class TravelService(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
        def say_hello(ctx, name, times):
            for i in range(times):
                yield u'Hello, %s' % name
                
    @rpc(Integer, Integer, _returns=Iterable(Integer))
    def travelTime(ctx,  distance, speed):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = '*'
        total_time = distance/speed
        return total_time


application = Application([TravelService], 'spyne.examples.traject.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

app = wsgi_application
