# Print in color

print("Uh, oh, you've been given a","\033[31mwarning\033[0m")

# \033 representa el carácter de escape (ASCII 27) que inicia una secuencia de control en el terminal.
# [31m: Es la parte de la secuencia que especifica el color.

print("\033[32mSuccess:\033[0m The operation completed!")
print("\033[33mWarning:\033[0m Low disk space!")
print("\033[31mError:\033[0m File not found!")

# Another way of doing this

from colorama import Fore, Style, Back, init

print(f"{Fore.RED}Warning{Style.RESET_ALL}: Check your input!")

print(f"{Back.YELLOW}{Style.BRIGHT}{Fore.RED}Warning{Style.RESET_ALL}: Check your input!")


init(autoreset=True)

print(f"{Style.BRIGHT}{Fore.RED}Texto en rojo brillante{Style.RESET_ALL}")
print(f"{Fore.GREEN}{Back.YELLOW}Texto verde con fondo amarillo")
print(f"{Style.DIM}{Fore.BLUE}Texto azul atenuado{Style.RESET_ALL}")