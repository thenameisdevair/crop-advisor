import base64
from PIL import Image
import io
from config.settings import MAX_IMAGE_SIZE_KB, SUPPORTED_FORMATS

def validate_image(file_bytes, filename):
    ext = filename.split(".")[-1].lower()
    if ext not in SUPPORTED_FORMATS:
        return False, f"Unsupported format. Use: {', '.join(SUPPORTED_FORMATS)}"
    return True, "ok"

def compress_and_encode(file_bytes):
    img = Image.open(io.BytesIO(file_bytes))
    img = img.convert("RGB")
    output = io.BytesIO()
    quality = 85
    img.save(output, format="JPEG", quality=quality)
    while output.tell() > MAX_IMAGE_SIZE_KB * 1024 and quality > 40:
        output = io.BytesIO()
        quality -= 10
        img.save(output, format="JPEG", quality=quality)
    return base64.b64encode(output.getvalue()).decode("utf-8")
