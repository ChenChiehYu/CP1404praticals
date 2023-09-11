from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
silver_taxi.drive(18)
print(silver_taxi)
print(f"${silver_taxi.get_fare():.2f}")