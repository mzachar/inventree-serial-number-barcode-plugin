# inventree-serial-number-barcode-plugin

## Barcode matching

Scan a QR/barcode whose entire payload is a `StockItem` serial number to link to that
item.

Serial numbers must be unique across the parts being scanned. InvenTree only enforces
uniqueness within a part *variant tree* unless **Globally Unique Serials** is enabled, so
either enable that setting or use a naming convention which keeps serial numbers distinct.

A barcode which matches more than one stock item is treated as no match and fallbacks
to build-in implementation 

## Counter extraction

InvenTree stores an integer form of every serial number in `StockItem.serial_int`.
This allows to specify `trailing` or `custom regexp` extraction.
When the pattern does not match, the built-in extraction is used.

### Trailing
For serial numbers formatted as `<PREFIX><counter>` that uses digit `<PREFIX>`:

| Serial       | inventree `build-in` method | this plugin |
|--------------|-----------------------------|-------------|
| `Text000123` | 123                         | 123         |
| `100-000124` | 100                         | 124         |
| `100-000125` | 100                         | 125         |


### Custom
For serial numbers formated as `<PREFIX>-<counter>-<SUFFIX>` you can specify custom regex:

`-(\d+)-`

| Serial           | inventree `build-in` method | this plugin |
|------------------|-----------------------------|-------------|
| `Pre-000123-suf` | 0                           | 123         |
| `100-000124-745` | 100                         | 124         |
| `100-000125-745` | 100                         | 125         |

## Requirements

InvenTree **1.4.0** or newer

## Installation

Add the following line to the `pluings.txt`:
```
inventree-serial-number-barcode-plugin@git+https://github.com/mzachar/inventree-serial-number-barcode-plugin.git
```

## License

MIT
