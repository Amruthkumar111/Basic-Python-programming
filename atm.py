#atm card
atm_card_inserted=True
correct_pin=True
account_locked=False

print(f"ATM card inserted: {atm_card_inserted}")
print(f"Correct PIN entered: {correct_pin}")
print(f"Account locked: {account_locked}")

if atm_card_inserted and correct_pin and not account_locked:
  print("Access Granted")
else:
  print("Access Denied")
