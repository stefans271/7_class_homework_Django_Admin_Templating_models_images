from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ImageCompressor:
    def __init__(self, max_size=(1920,1080), quality=80,output_format='WBEP'):
        self.max_size = max_size
        self.quality = quality
        self.output_format = output_format

    def compress(self, image_field):
        img = Image.open(image_field)

        if img.mode in ["RGBA", "P"]:
            img = img.convert("RGB")

        if img.width > self.max_size[0] and img.height > self.max_size[1]:
            img.thumbnail(max_size, Image.LANCZOS)

        buffer = BytesIO()  # ucitaj sliku u memoriju

        img.save(buffer, format=self.output_format, quality=self.quality)
        #snimi sliku u memoriji
        buffer.seek(0)  # resetuj buffer

        return ContentFile(buffer.read())  #vrati nazad ceo fajl (sliku)

