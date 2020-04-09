def hex_dec(hex):
    return int(hex, 16)

if __name__=="__main__":
    hex = input("Hex: ")
    print(hex_dec(hex))