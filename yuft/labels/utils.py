import base64
import io
import qrcode


def generate_qr_code(data, size=10, border=0):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img


def generate_qr(url_text):
    generated_code = generate_qr_code(data=url_text, size=4, border=1)
    bio = io.BytesIO()
    img_save = generated_code.save(bio)
    png_qr = bio.getvalue()
    base64qr = base64.b64encode(png_qr)
    img_name = base64qr.decode("utf-8")
    context_dict = dict()
    context_dict['file_type'] = "png"
    context_dict['image_base64'] = img_name
    return context_dict


def get_qrcode(input_data: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')
    return
