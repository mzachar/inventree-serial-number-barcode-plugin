"""Extraction of the numeric counter from a serial number."""

import re
from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from plugin.mixins import ValidationMixin

MODE_TRAILING = 'trailing'
MODE_REGEX = 'regex'
MODE_NATIVE = 'native'

TRAILING_PATTERN = r'(\d+)$'


def validate_pattern(value):
    """Check that the value is a regular expression with at least one capture group."""
    try:
        pattern = re.compile(value)
    except re.error as exc:
        raise ValidationError(
            _('Invalid regular expression: {error}').format(error=exc)
        )

    if pattern.groups < 1:
        raise ValidationError(_('Pattern must contain at least one capture group'))


COUNTER_SETTINGS = {
    'COUNTER_MODE': {
        'name': _('Counter Extraction'),
        'description': _('Pattern applied before the InvenTree default extraction'),
        'choices': [
            (MODE_TRAILING, _('Trailing digits - PREFIX-000123')),
            (MODE_REGEX, _('Custom regular expression')),
            (MODE_NATIVE, _('Disabled - InvenTree default only')),
        ],
        'default': MODE_NATIVE,
    },
    'COUNTER_REGEX': {
        'name': _('Counter Pattern'),
        'description': _(
            'Regular expression used when the extraction is set to custom. '
            'The first capture group must contain the digits.'
        ),
        'default': TRAILING_PATTERN,
        'validator': validate_pattern,
    },
}


class SerialCounterMixin(ValidationMixin):
    """Derive StockItem.serial_int from a serial number."""

    def convert_serial_to_int(self, serial: str) -> Optional[int]:
        if serial in (None, ''):
            return None

        mode = self.get_setting('COUNTER_MODE')

        if mode == MODE_NATIVE:
            return None

        pattern = (
            self.get_setting('COUNTER_REGEX')
            if mode == MODE_REGEX
            else TRAILING_PATTERN
        )

        match = re.search(pattern, str(serial).strip())

        if not match:
            return None

        try:
            return int(match.group(1))
        except (IndexError, ValueError):
            return None
