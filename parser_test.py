from services.product_page_parser import ProductPageParser

parser = ProductPageParser()

image = parser.get_full_image(
    "https://engineden.co.za/product/toyota-2kd-engine-hilux-used/"
)

print(image)