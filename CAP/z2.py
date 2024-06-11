def main(bit_fields):
    result = 0
    bit_positions = {
        'J1': 0,
        'J2': 9,
        'J3': 15,
        'J4': 16,
        'J5': 17,
        'J6': 19
    }
    for name, hex_value in bit_fields:
        value = int(hex_value, 16)
        position = bit_positions[name]
        result |= value << position
    return hex(result)


# Пример использования
print(main([('J1', '0x3'), ('J2', '0x18'), ('J3', '0x0'), ('J4', '0x1'), ('J5', '0x2'), ('J6', '0x3')]))  # '0x1d3003'
print(main([('J1', '0x1fc'), ('J2', '0x37'), ('J3', '0x0'), ('J4', '0x1'), ('J5', '0x2'), ('J6', '0x2')]))
print(main([('J1', '0x130'), ('J2', '0x7'), ('J3', '0x0'), ('J4', '0x0'), ('J5', '0x3'), ('J6', '0x1')]))
print(main([('J1', '0x7'), ('J2', '0x17'), ('J3', '0x0'), ('J4', '0x0'), ('J5', '0x2'), ('J6', '0x3')]))
