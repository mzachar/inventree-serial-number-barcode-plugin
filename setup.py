from setuptools import setup, find_packages

setup(
    name = "inventree-serial-number-barcode-plugin",
    version = "1.0.0",
    author = "Matej Zachar",
    author_email = "mzachar@users.noreply.github.com",
    license = "MIT",
    description = "Scan barcodes which use StockItem Serial# as data. Requires globally unique serial numbers",
    keywords = "inventree serial number barcode plugin",
    url = "https://github.com/mzachar/inventree-serial-number-barcode-plugin",

    packages = find_packages(),
    scripts = [],

    entry_points = {
        'inventree_plugins': [ 'SerialNumberBarcodePlugin = inventree_plugin.serial_number_barcode:SerialNumberBarcodePlugin' ]
    }
)
