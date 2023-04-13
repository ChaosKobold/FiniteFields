
from abc import ABC, abstractmethod
from utils.prime_mod_helper import get_inverse_entries, is_prime


def get_field(p: int):
    """
    Creates the most basic version of a finite field, the Field F_p where p is prime
    :param p: the p in F_p
    :return: The corresponmding field if p is prime, None otherwise
    """
    if not is_prime(p):
        return None
    inverses = get_inverse_entries(p)
    res_type = type(f"F_{p}",
                    (_BaseFiniteField,),
                    {
                        "_p": p,
                        "_inverses": inverses
                    })
    return res_type



class GeneralField(ABC):
    """
    A abstract field class to serve as an interface for general field operations.

    Supported are neutral elements for addition and multiplication,
    as well as an inversion method

    To implement a class, define a zero and a one element, as well as define +, -, * and - ,
    as well as the unary minus
    """

    @classmethod
    @abstractmethod
    def zero(cls):
        pass

    @classmethod
    @abstractmethod
    def one(cls):
        pass


class _BaseFiniteField(GeneralField):
    """
    Baseclass for all finite fields F_p where p is prime.
    For a concrete class inherit this one, and set the class variable p
    to the desired prime number
    """

    _p: int
    _inverses: list[int]

    @classmethod
    def zero(cls):
        return cls(0)

    @classmethod
    def one(cls):
        return cls(1)

    @classmethod
    def type_equals(cls, other: type):
        """
        Checks whether the other class is the same as this one, i.e.
        that both behave exactly the same
        :param other:
        :return:
        """

        if not issubclass(other, _BaseFiniteField):
            return False
        return cls._p == other._p


    def value(self) -> int:
        """
        Gets the value as an int for this instance
        :return:
        """
        return self._i

    def __inverse(self) -> int:
        i = self.value()
        if i == 0:
            return -1
        return self.__class__._inverses[i]

    def prime(self):
        return self.__class__._p

    def __init__(self, i: int):
        self._i = i % self.prime()

    def __str__(self):
        return str(self.value())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value()})"

    def __eq__(self, other):
        if not self.__same_class(other):
            return False
        other: _BaseFiniteField
        return self.value() == other.value()

    def __add__(self, other):
        if not self.__same_class(other):
            raise TypeError
        other: _BaseFiniteField
        return self.__class__(self.value() + other.value())

    def __neg__(self):
        return self.__class__(- self.value())

    def __sub__(self, other):
        if not self.__same_class(other):
            raise TypeError
        other: _BaseFiniteField
        return self.__class__(self.value() - other.value())

    def __mul__(self, other):
        if not self.__same_class(other):
            raise TypeError
        other: _BaseFiniteField
        return self.__class__(self.value() * other.value())

    def __truediv__(self, other):
        if not self.__same_class(other):
            raise TypeError
        other: _BaseFiniteField
        if other.value() == 0:
            raise ZeroDivisionError
        return self.__class__(self.value() * other.__inverse())





    def __same_class(self, other):
        """
        Checks whether another object is the same as this one.
        :param other:
        :return:
        """
        return self.__class__.type_equals(other.__class__)





















