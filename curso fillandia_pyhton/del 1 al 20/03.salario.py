"""Por favor, escriba un programa que solicite el
 salario por hora, las horas trabajadas y el día
   de la semana. El programa debería imprimir el
   salario diario, que equivale al salario por
     hora multiplicado por las horas trabajadas,
       excepto los domingos, que se duplica."""

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_the_week = input("Day of the week:").strip().lower()
#.strip()= elimina espacios al principio  al final
#.lower()= convierte todo a minusculas
if day_of_the_week == "sunday":
    hourly_wage *= 2

Daily_wages = hourly_wage * hours_worked


print(f"Daily wages: {Daily_wages:.1f} euros")
#:.1f → indica que se debe mostrar el número con una sola cifra decimal
"""salidas esperadas:

Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros

Hourly wage: 12.5
Hours worked: 10
Day of the week: Sunday
Daily wages: 250.0 euros
"""
