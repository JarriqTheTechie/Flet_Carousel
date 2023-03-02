# Flet Carousel
## A functional carousel widget for flet framework.

Allows user to swipe or click through a list of images.

```
Parameters:
    images (List[str]): List of image URLs
    shuffle (bool): Shuffle the images
    active_color (str): Color of the active dot
    inactive_color (str): Color of the inactive dots

Returns:
    Carousel: Carousel Widget
```









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

``
