class carro_Compra:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("CarroCompra")
        if not carro:
            carro=self.session['CarroCompra']
        else:
            self.carro=carro
    def agregar(self, producto):
        if (str(producto) not in self.carro.keys):
            self.carro[producto.id]={
                
                "producto.id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
                
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=["cantidad"]+1
                    break
        self.guardar_carro
        
    def guardar_carro(self):
        self.session["CarroCompra"]=self.carro
        self.session.modified=True
    def eliminacion_total(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    def restar_producto(self,producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminacion_total(producto)
                    break
        self.guardar_carro()
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True