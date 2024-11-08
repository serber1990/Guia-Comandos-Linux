from shellcolorize import Color

htop_commands = [
    {"command": f"{Color.GREEN}htop{Color.RESET}", "description": "Inicia la interfaz interactiva de htop con la configuración predeterminada"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -d <delay>", "description": "Establece el retardo de actualización en décimas de segundo (ej. -d 10 para 1 segundo)"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -C", "description": "Desactiva el uso de colores en la interfaz"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -h", "description": "Muestra la ayuda de línea de comandos y opciones de htop"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -u <user>", "description": "Muestra solo los procesos pertenecientes al usuario especificado"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -p <pid>[,<pid>...]", "description": "Muestra solo los procesos con los IDs de proceso especificados"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -s <column>", "description": "Ordena los procesos en la interfaz por la columna especificada (ej. 'cpu' o 'mem')"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -t", "description": "Activa el modo de árbol para visualizar procesos"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --no-color", "description": "Alias para -C; desactiva el uso de colores en la interfaz"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --tree", "description": "Alias para -t; muestra los procesos en modo de árbol"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --user <user>", "description": "Alias para -u; muestra solo los procesos del usuario especificado"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --sort-key <column>", "description": "Alias para -s; ordena los procesos por la columna especificada"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --pid <pid>[,<pid>...]", "description": "Alias para -p; muestra solo los procesos con los IDs especificados"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --delay <delay>", "description": "Alias para -d; establece el retardo de actualización"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --help", "description": "Muestra la ayuda de htop con todas las opciones disponibles"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --version", "description": "Muestra la versión de htop actualmente instalada"},
]

print(f"\nComandos de HTOP con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 130)
for cmd in htop_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")
