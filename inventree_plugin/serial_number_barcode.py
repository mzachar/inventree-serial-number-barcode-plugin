from plugin import InvenTreePlugin
from plugin.mixins import BarcodeMixin
from stock.models import StockItem

class SerialNumberBarcodePlugin(BarcodeMixin, InvenTreePlugin):

    NAME = "Serial# Barcodes"
    TITLE = "Serial Number Barcodes"
    DESCRIPTION = "Scan barcodes which use StockItem Serial# as data. Requires globally unique serial numbers"
    VERSION = "1.0.0"
    AUTHOR = "Matej Zachar"

    def scan(self, barcode_data):
        try:
            instance = StockItem.objects.get(serial=barcode_data)
            label = StockItem.barcode_model_type()

            return {label: instance.format_matched_response()}
        except StockItem.DoesNotExist:
            pass
