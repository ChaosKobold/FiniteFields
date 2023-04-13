
from utils.prime_mod_helper import get_inverse_entries
from finite_fields.finite_fields_module import get_field
from datetime import datetime

def main():
    print(get_inverse_entries(5))
    three = get_field(5)(3)
    print(repr(three))
    now = datetime.now()
    print(repr(now))
    F_7 = get_field(7)
    tree = F_7(3)
    print(tree)
    print(str(tree))
    print(repr(three))
    pass

if __name__ == '__main__':
    main()