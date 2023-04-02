queries= {
     "get_customers":"SELECT * FROM Cliente",
     "add_customer":
     "INSERT INTO Cliente(nombre,cedula,correo,telefono,fechaRegistro) VALUES (@nombre,@cedula,@correo,@telefono,@fechaRegistro)",
     "get_products":"SELECT * FROM ProductoView  WHERE [stock] != 0",
     "get_product":"SELECT * FROM Producto  where  idProducto = ? and  [stock] != 0  ",
     "delete_product":"DELETE FROM Producto  where idProducto = ?"
}



   
