#!/usr/bin/python3
"""
This module extracts an OTP code from an image file containing a QR code.
"""

import re
import sys

import pyotp
from PIL import Image
from pyzbar.pyzbar import ZBarSymbol, decode


def get_otp_code(file_name):
    """
    Get the OTP code from a given image file.

    Args:
        file_name (str): The name of the image file.

    Returns:
        str: The OTP code extracted from the image.

    """
    image_path = f'./{file_name}.png'
    data = decode(Image.open(image_path), symbols=[ZBarSymbol.QRCODE])[0][0].decode("utf-8")
    data = data.split('&')[0]
    up_to_char = "?"
    rx_to_first = rf'^.*?{re.escape(up_to_char)}'
    data = re.sub(rx_to_first, '', data, flags=re.DOTALL).strip()
    secret = data.replace('secret=', '')
    totp = pyotp.TOTP(secret)
    return totp.now()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file name.")
    else:
        FILE_NAME = sys.argv[1]
        OTP_CODE = get_otp_code(FILE_NAME)
        print(OTP_CODE)