import binascii

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.asymmetric import padding


def generate_keypair_files():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
    )
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('keys/privkey.pem', 'wb') as pem_out:
        pem_out.write(pem)
    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('keys/publickey.pem', 'wb') as pem_out:
        pem_out.write(pem)


with open("keys/privkey.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )


def sign_text(message: str) -> str:
    message_bytes = message.encode()
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    signature_string = binascii.hexlify(signature)
    return signature_string.decode()


def verify_signature(signature_string: str, message: str) -> bool:
    signature = binascii.unhexlify(signature_string)
    public_key = private_key.public_key()
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False
