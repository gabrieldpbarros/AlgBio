days = int(input("Dias: "))
hours = int(input("Horas: "))
minutes = int(input("Minutos: "))
seconds = int(input("Segundos: "))
total = seconds + (60 * minutes) + (3600 * hours) + (86400 * days)

print(f"{total} s")