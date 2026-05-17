from vehicles.models import Car, Motorcycle

print("=" * 55)
print("  VEHICLE MANAGEMENT SYSTEM — Django Shell Testing")
print("=" * 55)

# ── Create 1 Car object ──────────────────────────────────
print("\n[1] Creating Car object...")
car = Car.objects.create(brand="Tesla", price=3000000, doors=4)
print(f"    Saved: Car(id={car.id}, brand={car.brand}, price={car.price}, doors={car.doors})")

# ── Create 1 Motorcycle object ───────────────────────────
print("\n[2] Creating Motorcycle object...")
moto = Motorcycle.objects.create(brand="Kawasaki", price=160000, helmet_included=True)
print(f"    Saved: Motorcycle(id={moto.id}, brand={moto.brand}, price={moto.price}, helmet_included={moto.helmet_included})")

# ── Call vehicle_info() on both ──────────────────────────
print("\n[3] Calling vehicle_info() on both objects:")
print(f"Car - {car.vehicle_info()}")
print(f"Motorcycle - {moto.vehicle_info()}")

# ── Polymorphism demo ────────────────────────────────────
print("\n[4] Polymorphism — same method, different outputs:")
vehicles = [car, moto]
for v in vehicles:
    print(f"{v.__class__.__name__} → {v.vehicle_info()}")

print("\n" + "=" * 55)
print("  Inheritance:   Car and Motorcycle inherit brand & price from Vehicle")
print("  Overriding:    Each class overrides vehicle_info() differently")
print("  Polymorphism:  Same method call, different output per class")
print("=" * 55)