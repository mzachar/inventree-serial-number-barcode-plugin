from setuptools import setup, find_packages

setup(
    name = "inventree-serial-number-barcode-plugin",
    version = "2.0.0",
    author = "Matej Zachar",
    author_email = "mzachar@users.noreply.github.com",
    license = "MIT",
    description = "Scan barcodes which use StockItem Serial# as data, and control how the serial number counter is extracted",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    keywords = "inventree serial number barcode plugin",
    url = "https://github.com/mzachar/inventree-serial-number-barcode-plugin",

    packages = find_packages(),
    scripts = [],

    entry_points = {
        'inventree_plugins': [ 'SerialNumberBarcodePlugin = inventree_serial_number.plugin:SerialNumberBarcodePlugin' ]
    }
)
