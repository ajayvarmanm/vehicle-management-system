from database import conn, cursor

class Customer:
    def __init__(self, customers, vehicles):
        self.customers = customers
        self.vehicles = vehicles


    # ADD CUSTOMER
    def add_customer(self, customer_id, name, phone, id_proof):

        query = """
        INSERT INTO customers (customer_id, name, phone_number, id_proof)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (customer_id, name, phone, id_proof))
        conn.commit()

        print(f"✅ Customer {name} added successfully!")


    # VIEW AVAILABLE VEHICLES
    def view_available_vehicles(self):

        query = """
        SELECT vehicle_id, registration_no, vehicle_type, brand, rent_price
        FROM vehicles
        WHERE available = 1
        """

        cursor.execute(query)
        vehicles = cursor.fetchall()

        print("\n--- Available Vehicles ---")

        if not vehicles:
            print("❌ No vehicles available.")
            return

        for v in vehicles:
            print(f"ID: {v[0]}, RegNo: {v[1]}, Type: {v[2]}, Brand: {v[3]}, Rent: {v[4]}")


    # RENT VEHICLE
    def rent_vehicle(self, customer_id, vehicle_id):

        # check customer
        query = "SELECT * FROM customers WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()

        if not customer:
            print("❌ Customer does not exist!")
            return


        # check vehicle
        query = "SELECT available FROM vehicles WHERE vehicle_id = %s"
        cursor.execute(query, (vehicle_id,))
        vehicle = cursor.fetchone()

        if not vehicle:
            print("❌ Vehicle ID not found!")
            return

        if vehicle[0] == 0:
            print("❌ Vehicle already rented!")
            return


        # insert rental record
        query = """
        INSERT INTO rentals (customer_id, vehicle_id, rent_date)
        VALUES (%s, %s, CURDATE())
        """

        cursor.execute(query, (customer_id, vehicle_id))
        conn.commit()


        # update vehicle availability
        update_query = """
        UPDATE vehicles
        SET available = 0
        WHERE vehicle_id = %s
        """

        cursor.execute(update_query, (vehicle_id,))
        conn.commit()

        print("✅ Vehicle rented successfully!")


    # RETURN VEHICLE
    def return_vehicle(self, customer_id):

        # find rented vehicle
        query = """
        SELECT vehicle_id
        FROM rentals
        WHERE customer_id = %s AND return_date IS NULL
        """

        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()

        if not result:
            print("⚠️ No vehicle rented by this customer.")
            return

        vehicle_id = result[0]


        # update return date
        update_rental = """
        UPDATE rentals
        SET return_date = CURDATE()
        WHERE customer_id = %s AND vehicle_id = %s AND return_date IS NULL
        """

        cursor.execute(update_rental, (customer_id, vehicle_id))
        conn.commit()


        # make vehicle available again
        update_vehicle = """
        UPDATE vehicles
        SET available = 1
        WHERE vehicle_id = %s
        """

        cursor.execute(update_vehicle, (vehicle_id,))
        conn.commit()

        print("✅ Vehicle returned successfully!")

    def view_customers(self):

        query = """
        SELECT customer_id, name, phone_number, id_proof
        FROM customers
        """

        cursor.execute(query)
        data = cursor.fetchall()

        print("\n--- Customer List ---")

        if not data:
            print("❌ No customers found.")
            return

        for c in data:
            print(f"ID: {c[0]}, Name: {c[1]}, Phone: {c[2]}, ID Proof: {c[3]}")

    def remove_customer(self, customer_id):

        # check ANY rental history
        query = "SELECT * FROM rentals WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()

        if result:
            print("❌ Cannot delete. Customer has rental history!")
            return

        # delete customer
        query = "DELETE FROM customers WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        conn.commit()

        print("✅ Customer removed successfully!")

