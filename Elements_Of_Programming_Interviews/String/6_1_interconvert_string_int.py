from typing import List
from loguru import logger 

def string_2_int(s: str) -> int:
    is_negative = s[0] == '-'
    start_idx = 1 if is_negative else 0 
    num = 0 
    
    for i in range(start_idx, len(s)):
        num = num * 10 + (ord(s[i]) - ord('0'))
        
    return -num if is_negative else num

def int_2_string(x: int) -> str:
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    
    s = []
    
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
        
    return ('-' if is_negative else '') + ''.join(reversed(s))

def main():
    logger.info("Starting the Application.")
    while True:
        ui = input("Please enter the number: \n")
        transformation = input("Please enter the transformation that you would like to apply. Your options are `s2i` and `i2s`:\n")      
        try:
            if transformation == 'i2s':
                converted = int_2_string(int(ui))
            elif transformation == 's2i':
                converted = string_2_int(ui)
            else:
                logger.error("Please enter the correct transformation choice.")
                continue
            print("The transformed output is: ", converted, "\n ans, of type: ", type(converted))
        except Exception as e:
            logger.error(f"Invalid input. Failed to convert. Error: {e}")
            
if __name__ == '__main__':
    main()
