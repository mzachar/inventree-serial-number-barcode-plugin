"""InvenTree plugin treating the serial number as the identifier of a stock item."""

from django.utils.translation import gettext_lazy as _

from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin

from .barcode import BARCODE_SETTINGS, SerialBarcodeMixin
from .counter import COUNTER_SETTINGS, SerialCounterMixin


class SerialNumberBarcodePlugin(
    SerialBarcodeMixin, SerialCounterMixin, SettingsMixin, InvenTreePlugin
):
    """Scan barcodes containing a serial number, and control how its counter is read."""

    NAME = 'Serial# Barcodes'
    SLUG = 'serial-barcodes'
    TITLE = _('Serial Number Barcodes')
    DESCRIPTION = _(
        'Scan barcodes which use a StockItem serial number as data, and control how '
        'the numeric counter is extracted from it'
    )
    VERSION = '2.0.0'
    MIN_VERSION = '1.4.0'
    AUTHOR = 'Matej Zachar'
    LICENSE = 'MIT'
    WEBSITE = 'https://github.com/mzachar/inventree-serial-number-barcode-plugin'

    SETTINGS = {**BARCODE_SETTINGS, **COUNTER_SETTINGS}
