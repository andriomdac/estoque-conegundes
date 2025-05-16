class DuplicateBarcodeException(Exception):
    """Raised when a product with the same barcode already exists."""
    def __init__(self, message='Product with this barcode already exists.'):
        super().__init__(message)


class DuplicateBrandException(Exception):
    """Raised when a brand with the same name already exists."""
    def __init__(self, message='Brand with this name already exists.'):
        super().__init__(message)

class DuplicateProductException(Exception):
    """Raised when a product with the same name and brand already exists."""
    def __init__(self, message='Product with this name and brand already exists.'):
        super().__init__(message)

