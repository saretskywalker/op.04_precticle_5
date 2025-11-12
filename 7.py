# Калькулятор расхода и стоимости бензина за поездку
cost_of_gas = 49.5

def calculated_fue_consumption (distance, gasoline_consumption):
    """Расчет затраченного бензина на поездку
    args:
        distance, gasoline_consumption(float): расстояние и расход бензина на 100км
    returnes:
        float: затраченный бензин на поездку"""
    calculated_consmption_of_gas = distance * (gasoline_consumption / 100)
    return calculated_consmption_of_gas

def calculated_fue_cost (cost_of_gas, calculated_consmption_of_gas):
    """Расчет стоимости бензина на поездку
      args:
          calculated_fue_consumption(func): затраченный бензин на поездку
      returnes:
          float: стоимость бензина за поедку"""
    calculated_cost_of_gas = calculated_fue_consumption(distance, gasoline_consumption) * cost_of_gas
    return calculated_cost_of_gas

distance, gasoline_consumption = map(float, input("Введите расстояние и расход бензина на 100км ").split())
print(f"""Необходимо бензина {calculated_fue_consumption(distance, gasoline_consumption)}
Стоимость бензина {calculated_fue_cost(cost_of_gas, calculated_fue_consumption)}""")
