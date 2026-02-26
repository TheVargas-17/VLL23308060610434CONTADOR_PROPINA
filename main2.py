 #Ps en si es eso,todo programado con flet, es una App donde ingreses la cantidad de la cuenta qvas a pagar
# Y luego en la línea de abajo elijes un porcentaje (tienes que tener del 5% al 25% 8 porcentajes diferentes) que quieres darle de propina a el mesero
# Y al seleccionarlo T va a salir abajo de esa línea t va a salir el porcentaje de tu cuenta total
 #Por ejemplo
 #Mi cuenta es de 40 pesos y quiero darle el 10% a ps le daría 4 pesos
 #Eso saldría abajo de la línea de los porcentajes
 #Y ya al último t va a salir el total de todo,con el porcentaje incluido

import flet as ft
def main(page: ft.Page):
    page.title = "DESCUENTO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
   
    

        
        
    txt_total= ft.TextField(label="Total de la cuenta",
                            text_align=ft.TextAlign.CENTER,
                            width=200,
                            keyboard_type=ft.KeyboardType.NUMBER
                            )
    txt_resultado = ft.TextField(label="Total a pagar",
                            text_align=ft.TextAlign.CENTER, 
                            width=200,disabled=True
                            )


    slider_propina = ft.Slider(
        min=0,
        max=25,
        divisions=7,  
        value=5,
        label="{value}%",
        width=200
    )
    
    txt_mensaje=ft.Text("")

    def calcular(e):
        total = float(txt_total.value)
        porcentaje =(slider_propina.value)
        propina = total *  (porcentaje / 100)
        txt_resultado.value = f"{total + propina:.2f}"
        txt_mensaje.value = f"le daria de propina {propina:.2f} pesos"
        page.update()


    btn = ft.ElevatedButton("Calcular", on_click=calcular)

    page.add(
            ft.Column(
                [
                    txt_total,
                    ft.Text("Seleccione el porcentaje de propina"),
                    slider_propina,
                    txt_mensaje,
                    btn,
                    txt_resultado   
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )



ft.app(target=main)