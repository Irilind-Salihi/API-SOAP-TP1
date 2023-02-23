from zeep import Client
wsdl = "http://127.0.0.1:8000/?wsdl"
client = Client(wsdl=wsdl)
print(client.service.say_hello('Zeep', 3))

print(client.service.addition(2, 3))

