from database import conn, cursor

class Admin:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def add_vehicle(self, vehicle_id, regn_no, vehicle_type, brand, rent_price ):

        query = """
        INSERT INTO vehicles (vehicle_id, registration_no, vehicle_type, brand, rent_price, available)
        VALUES (%s, %s, %s, %s, %s, 1)
        """

        cursor.execute(query, (vehicle_id, regn_no, vehicle_type, brand, rent_price))
        conn.commit()

        print(f"✅ Vehicle {brand} ({vehicle_type}) added successfully!")

    def view_vehicles(self):

        query = """
        SELECT vehicle_id, registration_no, vehicle_type, brand, rent_price, available
        FROM vehicles
        """

        cursor.execute(query)
        vehicles = cursor.fetchall()

        print("\n--- Vehicle List (Admin View) ---")

        for v in vehicles:
            status = "Available" if v[5] == 1 else "Rented"
            print(f"ID: {v[0]}, RegNo: {v[1]}, Type: {v[2]}, Brand: {v[3]}, Rent: {v[4]}, Status: {status}")


    def remove_vehicle(self, vehicle_id):

    # check rental history
        query = "SELECT * FROM rentals WHERE vehicle_id = %s"
        cursor.execute(query, (vehicle_id,))
        result = cursor.fetchone()

        if result:
            print("❌ Cannot delete. Vehicle has rental history!")
            return

        # delete vehicle
        query = "DELETE FROM vehicles WHERE vehicle_id = %s"
        cursor.execute(query, (vehicle_id,))
        conn.commit()

        print("✅ Vehicle removed successfully!")