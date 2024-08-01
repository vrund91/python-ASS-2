salary=float(input("Enter your salary:"))

HRA=0.10*salary
DA=0.20*salary
TA=0.10*salary
PF=0.10*salary

gross_salary = salary + HRA + DA + TA
net_sal = gross_salary - PF

print(f"Basic salary:{salary:.2f}")
print(f"HRA:{HRA:.2f}")
print(f"DA:{DA:.2f}")
print(f"TA:{TA:.2f}")
print(f"PF:{PF:.2f}")

print(f"Net salary is:{net_sal:.2f}")
