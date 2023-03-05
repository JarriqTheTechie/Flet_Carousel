import random
from typing import List
import flet as ft


class Carousel(ft.UserControl):
    """
      Carousel Widget

      Allows user to swipe or click through a list of images.

      Parameters:
          images (List[str]): List of image URLs
          shuffle (bool): Shuffle the images
          active_color (str): Color of the active dot
          inactive_color (str): Color of the inactive dots

      Returns:
          Carousel: Carousel Widget

      Example:

      ```
          from carousel import Carousel
          import flet as flet

          carousel_images = list(
              [
                  "https://cookinglsl.com/wp-content/uploads/2019/02/chocolate-dipped-strawberries-wide-1.jpg",
                  "https://cdn.shopify.com/s/files/1/2305/2515/products/IMG_0746_3024x.jpg",
                  "https://www.coleinthekitchen.com/wp-content/uploads/2022/11/Small-Charcuterie-Board-6.jpg",
                  "https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_18/1712998/strawberry-shortcake-kb-main-210505.jpg"
              ]
          )

          def main(page: ft.Page):
              page.add(
                  Carousel(carousel_images, shuffle=True)
              )
              page.update()

      ```

      """

    def __init__(self,
                 images: List[str],
                 shuffle: bool = False,
                 active_color: str = ft.colors.BLACK,
                 inactive_color: str = ft.colors.WHITE):
        super().__init__()
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.images = images
        self.carousel_image_ref = ft.Ref()
        self.carousel_btn_container_ref = ft.Ref()
        self.carousel_button_ref = ft.Ref()
        self.shuffle = shuffle
        if self.shuffle:
            self.images = random.sample(self.images, len(self.images))

    def page_resize_handler(self, e):
        print(e)

    def swipe_handler(self, e: ft.DragEndEvent):
        # Get Current Image
        current_image = self.carousel_image_ref.current.src
        current_index = self.images.index(current_image)
        images_len = len(self.images)
        next_index = current_index + 1

        try:
            next_image = self.images[next_index]
        except IndexError:
            next_image = self.images[0]
        prev_index = current_index - 1
        try:
            prev_image = self.images[prev_index]
        except IndexError:
            prev_image = self.images[images_len]

        if e.primary_velocity > 0:
            self.carousel_image_ref.current.src = prev_image
            for carousel_btn in self.carousel_btn_container_ref.current.controls:
                if carousel_btn.data != prev_image:
                    carousel_btn.icon_color = self.inactive_color
                else:
                    carousel_btn.icon_color = self.active_color
            self.update()
        if e.primary_velocity < 0:
            self.carousel_image_ref.current.src = next_image
            for carousel_btn in self.carousel_btn_container_ref.current.controls:
                if carousel_btn.data != next_image:
                    carousel_btn.icon_color = self.inactive_color
                else:
                    carousel_btn.icon_color = self.active_color
            self.update()

    # Register callbacks
    def carousel_click(self, e):
        self.carousel_image_ref.current.src = e.control.data
        e.control.icon_color = self.active_color
        for carousel_btn in self.carousel_btn_container_ref.current.controls:
            if carousel_btn.data != e.control.data:
                carousel_btn.icon_color = self.inactive_color
        self.update()

    def build(self):
        return ft.GestureDetector(
            on_horizontal_drag_end=self.swipe_handler,
            content=ft.Container(
                padding=ft.padding.only(top=0),
                height=175,
                content=ft.Stack(
                    height=200,
                    controls=[
                        ft.Image(
                            src=[carousel_image for carousel_image in self.images][0],
                            fit=ft.ImageFit.FIT_WIDTH,
                            width=2000,
                            # opacity=.5,
                            color_blend_mode=ft.BlendMode.COLOR_BURN,
                            ref=self.carousel_image_ref,
                        ),
                        ft.Container(
                            # padding=ft.padding.only(top=-32),
                            alignment=ft.alignment.bottom_center,
                            content=ft.Row(ref=self.carousel_btn_container_ref,
                                           controls=[
                                               ft.IconButton(data=img,
                                                             icon=ft.icons.CIRCLE,
                                                             icon_size=15,
                                                             width=20,
                                                             icon_color=self.inactive_color,
                                                             on_click=self.carousel_click,
                                                             ref=self.carousel_button_ref)
                                               if img != self.images[0] else ft.IconButton(
                                                   data=img,
                                                   icon=ft.icons.CIRCLE,
                                                   icon_size=15,
                                                   width=20,
                                                   icon_color=self.active_color,
                                                   on_click=self.carousel_click,
                                                   ref=self.carousel_button_ref)
                                               for img in self.images
                                           ],
                                           scroll=ft.ScrollMode("auto"),
                                           alignment=ft.MainAxisAlignment.CENTER,
                                           spacing=0)),
                        ft.Column(
                            [
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "",
                                            color="white",
                                            size=25,
                                            weight="bold",
                                            opacity=1,
                                            text_align=ft.TextAlign.CENTER,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                )))
