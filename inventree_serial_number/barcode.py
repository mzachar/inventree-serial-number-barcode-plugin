"""Barcode matching for barcodes whose payload is a bare serial number."""

from typing import Optional

from django.utils.translation import gettext_lazy as _

from plugin.mixins import BarcodeMixin
from stock.models import StockItem

BARCODE_SETTINGS = {
    'BARCODE_SCAN': {
        'name': _('Match Serial Number Barcodes'),
        'description': _(
            'Match scanned barcode data against StockItem serial numbers. '
            'Serial numbers must be unique across the parts being scanned.'
        ),
        'default': True,
        'validator': bool,
    }
}


class SerialBarcodeMixin(BarcodeMixin):
    """Match a barcode whose entire payload is a StockItem serial number."""

    def scan(self, barcode_data: str, user, **kwargs) -> Optional[dict]:
        if not self.get_setting('BARCODE_SCAN'):
            return None

        matches = StockItem.objects.filter(serial=barcode_data)[:2]

        if len(matches) != 1:
            return None

        return {
            StockItem.barcode_model_type(): matches[0].format_matched_response(
                user=user, **kwargs
            )
        }
