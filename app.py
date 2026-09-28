# Calculadora de Consumo de Energia Elétrica

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dias = float(input("Digite o tempo médio de uso diario (horas): "))

consumo_mensal = (potencia * horas_dias * 30) / 1000

valor_kwh = 0.75

custo_mensal = consumo_mensal * valor_kwh

print("Calculadora de Consumo de Energia Elétrica")
print("Aparelho:", aparelho)
print("Consumo estimado:", consumo_mensal, "kWh/mês")
print("Custo estimado em reais: R$", custo_mensal)
