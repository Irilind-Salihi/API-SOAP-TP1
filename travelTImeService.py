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
    def travelTime(ctx, autonomy, distance, speed, reload_time):
        time_to_travel = distance / speed
        reload_count = distance / autonomy
        time_to_reload = reload_count * reload_time
        total_time = time_to_travel + time_to_reload
        yield str(total_time)


application = Application([TravelService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

server = make_server('127.0.0.1', 8000, wsgi_application)
server.serve_forever()
