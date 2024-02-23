

import os
os.system('cls')
cons_libretaInt = 5000
cons_borradorInt = 1000
cons_reglaInt = 1000
cons_lapizInt = 1500
cons_bolsoInt = 300000
cons_coloresInt = 60000
cons_uniformInt = 200000

var_nombreStr = input('nombre estudiante -> ')
var_contactoStr =  input('contacto estudiante -> ')
var_direccionStr = input('direccion estudiante -> ')
var_presupuestoFLt  = float(input('presupuesto -> '))
var_opcionesStr = input('>>>>>>>>>OPCIONES<<<<<<<<<<<< \n\ n1. libreta\ n2. borrador\ n3. regla\ n4. lapiz\ n5. bolso\ n6. colores/ n7. uniformes/ n8. salir -> ')
var_cntidadInt = int(input('cantidad -> '))
var_totalFlt = 0
if var_opcionesStr == '1':
    var_totalFlt += (var_cntidadInt * cons_libretaInt)
if var_opcionesStr == '2':
    var_totalFlt += (var_cntidadInt * cons_borradorInt)
if var_opcionesStr == '3':
    var_totalFlt += (var_cntidadInt * cons_reglaInt)
if var_opcionesStr == '4':
    var_totalFlt += (var_cntidadInt * cons_lapizInt)
if var_opcionesStr == '5':
    var_totalFlt += (var_cntidadInt * cons_bolsoInt)
if var_opcionesStr == '6':
    var_totalFlt += (var_cntidadInt * cons_coloresInt)
if var_opcionesStr == '7':
    var_totalFlt += (var_cntidadInt * cons_uniformInt)
    
print('valor  total a pagar:', var_totalFlt)
if var_presupuestoFLt >= var_totalFlt:
    print('gracias por su compra')
else:
    print('no tienes suficiente saldo')
