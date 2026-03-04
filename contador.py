import flet as ft
def main(page: ft.Page):
    page.title = "DESCUENTO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    
    
    #TEXTO SIMPLE
    page.add(ft.Text(
        value="hola mundo",
        size=40,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
        
    ))
    #IMAGEN
    page.add(ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        fit="cover",
        border_radius=ft.BorderRadius.all(30),
        repeat=ft.ImageRepeat.NO_REPEAT
    ))
    
    #DIVISORES
    
    page.add(ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row([
        ft.VerticalDivider( width=10, thickness=2, color=ft.Colors.GREY_400)
            
    ]))
    
    
    

        
        
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
