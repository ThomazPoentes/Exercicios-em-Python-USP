d = int(input("Segundos: "))

a = d // 86400
segundos_rest = d % 86400
b = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
c = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(a,"dias,",b,"horas,",c,"minutos e",segundos_rest,"segundos.")
