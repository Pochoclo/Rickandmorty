# Tarea 5: 

## Backend/frontend
Para esto hice un modelo de backend frontend, donde los comunico por señales, 
Las señales enviadas por los objetos que se mueven desde el backend son de una sola direccion (como las pelotas), en cambio los humanos necesitan señales de dos direcciones ya que su movimiento depende del teclado, por lo tando cuando se presiona una tecla, se envia la señal al backend, se calcula cual es el movimiento que corresponde y luego se modifica y se manda la señal de que el personaje se movio o no.
La verdad no se si lo estoy haciendo bien, pero por lo menos es funcional hasta el momento y siento que me esta quedando un poco mas ordenado el codigo de esta forma
## Colisiones
Por el momento estoy probando hacer un thread que se encargue de ver las colisiones entre las burbujas, no esta funcionando por el momento
la opcion que estoy evaluando es que cada pelota detecte su propia colision y haga sus movimientos