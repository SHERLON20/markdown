import flet as ft 
def main(page:ft.page):
    def update_view(e):
        view.value=editor.value
        view.update()
    editor=ft.TextField(
        expand=True,
        multiline=True,
        min_lines=13,
        max_lines=13,
        color=ft.colors.BLACK,
        content_padding=ft.padding.all(30),
        bgcolor=ft.colors.BLUE_GREY,
        border=ft.InputBorder.NONE,
        text_align=ft.CrossAxisAlignment.START,
        on_change=update_view,
        
    )
    how_to=ft.Container(
        expand=True,
        col={'xs':12,'lg':6},
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Text(value='para criar titulos em diferentes tamanhos',weight=ft.FontWeight.BOLD,color=ft.colors.BLACK),
                ft.Text(value='# h1',color=ft.colors.GREY_700),
                ft.Text(value='## h2',color=ft.colors.GREY_700),
                ft.Text(value='### h3',color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY,height=40),
                
                ft.Text(value='para formatar o estilo do texto',weight=ft.FontWeight.BOLD,color=ft.colors.BLACK),
                ft.Text(value='**texto em negrito**',color=ft.colors.GREY_700),
                ft.Text(value='*texto  em itálico*',color=ft.colors.GREY_700),
                ft.Text(value='~~texto tachado~~',color=ft.colors.GREY_700),
                ft.Divider(color=ft.colors.GREY,height=40),
            ]
        )
    )
    view=ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link=lambda e: page.launch_url(e.data),
    )
    layout=ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to,
                        ],
                    ),
                ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK26,
                padding=ft.padding.all(30),
                content=view,
                ),
        ]
    )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main)