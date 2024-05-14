import flet as ft
from flet import *




class App(UserControl):
    first_name = ft.TextField(label="First name", text_align=ft.TextAlign.RIGHT, width=185, height=50)
    last_name = ft.TextField(label="Last name", text_align=ft.TextAlign.RIGHT, width=185, height=50)
    Age = ft.TextField(label="Age", text_align=ft.TextAlign.RIGHT, width=185, height=50)

    my_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First_name")),
            ft.DataColumn(ft.Text("Last_name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ],
        rows=[],

    )

    def add_btn(self, e):
        new_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(self.first_name.value)),
                ft.DataCell(ft.Text(self.last_name.value)),
                ft.DataCell(ft.Text(self.Age.value)),
            ],
        )

        self.my_table.rows.append(new_row)

        self.my_table.update()

    def recive_btn(self, e):

        data = self.my_table.rows[0].cells
        print(data)



    def build(self):
        return Column(
            controls=[
                Container(
                    width=Container.width.fget,
                    # width=1200,
                    height=300,

                   
                    # bgcolor=colors.AMBER_300,
                    bgcolor="#ffffe0",
                    border_radius=border_radius.all(5),

                    content=Column(
                        controls=[
                            Row(
                                # alignment="spaceAround",
                                spacing=2,
                                controls=[
                                    # self.txt_number
                                    Container(
                                        margin=margin.only(top=10, right=10),
                                        width=180,
                                        height=50,
                                        bgcolor="#ffffe0",
                                        content=Column(controls=[self.first_name])

                                    ),
                                    Container(
                                        margin=margin.only(top=10, right=5),
                                        width=185,
                                        height=50,
                                        bgcolor="#ffffe0",
                                        content=Column(controls=[self.last_name])

                                    ),
                                    Container(
                                        margin=margin.only(top=10, right=5),
                                        width=185,
                                        height=50,
                                        bgcolor="#ffffe0",
                                        content=Column(controls=[self.Age])

                                    ),


                                ],

                            ),                     
                      
                            ElevatedButton(
                                text="Elevated button1",
                                bgcolor="Green",
                                width=200,
                                height=40,
                                on_click=self.add_btn,
                            ),

                        ],
                    ),

                ),
                Container(
                    width=Container.width.fget,
                    # width=1200,
                    height=300,


                    bgcolor="#ffffe0",
                    border_radius=border_radius.all(5),

                    content=Column(

                        auto_scroll=True,
                        controls=[
                            self.my_table,

                            ElevatedButton(text="Elevated button2", bgcolor="Green", width=200, height=40,

                                           on_click=self.recive_btn, ###


                                           ),

                        ],
                    ),
                ),
            ]
        )


def main(page: Page):
    
    page.title = "flet tutorial"

    page.rtl = True
   
    page.window_width = 1200
    page.window_height = 700

    
    page.window_resizable = False

    page.bgcolor = "#e249fc"

    
    page.update()

    
    app = App()
    page.add(app)
