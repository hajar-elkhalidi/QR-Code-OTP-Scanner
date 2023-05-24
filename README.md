# QR Code OTP Scanner

This project is a Python script that scans a QR code containing a One-Time Password (OTP) for enhanced security. It utilizes the `pyzbar` and `PIL` libraries to decode the QR code image and extract the OTP.

## Prerequisites

To run this script, ensure that you have the following dependencies installed:

- Python 3
- `pyzbar` library
- `PIL` library
- `pyotp` library

You can install the necessary libraries following this [guide](install_req.md)


## Usage

1. Place the QR code image file (in PNG format) in the same directory as the script file.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the following command:

    ```python3 get_otp.py <image_file_name_without_extension>```


    Replace `<image_file_name_without_extension>` with the actual name of your QR code image file (without the file extension).

4. The script will decode the QR code image and print the extracted OTP to the console.

## Example

Suppose you have a QR code image file named `otp_code.png`. To scan and retrieve the OTP, execute the following command:

```python3 get_otp.py otp_code```

The script will output the OTP to the console.

Please note that the QR code image file should be in PNG format and located in the same directory as the script file for successful execution.

## Create Alias
To make it easier to run the script without typing the full command, you can create an alias. Here's how:

1. Place the python script and the QR code image in the same directory (e.g, `otp/`)

1. Open your terminal's configuration file (e.g., `~/.bashrc` for Bash) in a text editor.

1. Add the following line at the end of the file:

    ```alias otp="cd /path/to/otp/folder && python3 get_otp.py"```

    Replace `/path/to/otp/folder` with the actual path to the `otp/` folder.

1. Save the file and exit the text editor.

1. Reload the terminal configuration by running the following command:

    ```source ~/.bashrc```

    Replace `~/.bashrc` with the path to your terminal's configuration file if it's different.

1. You can now use the `otp` alias followed by the image file name to run the script. For example:

    ```otp otp_code```

    This will execute the script and output the OTP to the console.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

## Acknowledgments

- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) library for QR code decoding.
- [PIL](https://pillow.readthedocs.io/en/stable/) library for image processing.
- [pyotp](https://github.com/pyotp/pyotp) library for OTP generation and validation.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk.