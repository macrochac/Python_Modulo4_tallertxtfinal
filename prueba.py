import re

texto = "Llama al 555-1234 o al 555-5678 para más información."

# Buscar el primer número
resultado = re.search(r'\d{3}-\d{4}', texto)
if resultado:
    print("Encontrado:", resultado.group())

# Encontrar todos los números
todos = re.findall(r'\d{3}-\d{4}', texto)
print("Todos:", todos)

# Reemplazar los números
nuevo_texto = re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', texto)
print("Texto modificado:", nuevo_texto)