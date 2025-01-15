try:
    assert sum(2, 3) == 5, f"Klaida vykdant funkciją 'sum()'. Atsakymas turi būti {5}"
    assert sub(17, 10) == 7, f"Klaida vykdant funkciją 'sub()'. Atsakymas turi būti {7}"
    assert mul(5, 5) == 25, f"Klaida vykdant funkciją 'mul()'. Atsakymas turi būti {25}"
    assert div(81, 9) == 9, f"Klaida vykdant funkciją 'div()'. Atsakymas turi būti {9}"
    assert pow(12, 2) == 144, f"Klaida vykdant funkciją 'pow()'. Atsakymas turi būti {144}"
    print(f'Visi testai yra sėkmingi')
except AssertionError as klaida:
    print(f"Testas: {klaida}")