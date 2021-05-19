"""
This is a module for physical quantity handling, it is essentially a wrapper for pint with som extra functionality end improved ease of use.

"""
from pint import Quantity as _Quantity_
from pint import Measurement as _Measurement_

from pint import UnitRegistry, _DEFAULT_REGISTRY

reg = _DEFAULT_REGISTRY
reg.default_format = '~P'


class Qunatity(_Quantity_):

    def __init__(self) -> None:
        super().__init__()


class Q(Qunatity):

    def __init__(self,val,unit) -> None:
        super().__init__()


class Measurement(_Measurement_):

    def __init__(self) -> None:
        super().__init__()

class M(Measurement):

    def __init__(self,val,unit) -> None:
        super().__init__()




