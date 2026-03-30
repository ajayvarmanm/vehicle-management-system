# main.py
from srcc.admin import Admin
from srcc.customer import Customer

def main():
    vehicles = {}
    customers = {}

    admin = Admin(vehicles)
    customer = Customer(customers, vehicles)

    while True:
        print("\n==== Vehicle Rental System ====")
        print("1. Admin Panel")
        print("2. Customer Panel")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            while True:
                print("\n--- Admin Panel ---")
                print("1. Add Vehicle")
                print("2. View Vehicles")
                print("3. Remove Vehicle")
                print("4. Back")
                admin_choice = input("Enter choice: ")

                if admin_choice == "1":
                    vid = input("Enter Vehicle ID: ")
                    regn_no = input("Enter Registration Number: ")
                    vtype = input("Enter Vehicle Type (Car/Bike/etc): ")
                    brand = input("Enter Brand: ")
                    rent = float(input("Enter Rent Price: "))
                    admin.add_vehicle(vid, regn_no, vtype, brand, rent)

                elif admin_choice == "2":
                    admin.view_vehicles()

                elif admin_choice == "3":
                    vid = input("Enter Vehicle ID to remove: ")
                    admin.remove_vehicle(vid)   
                elif admin_choice == "4":
                    break 

        elif choice == "2":
            while True:
                print("\n--- Customer Panel ---")
                
                print("1. Add Customer")
                print("2. View Available Vehicles")
                print("3. Rent Vehicle")
                print("4. Return Vehicle")
                print("5. View Customers")
                print("6. Remove Customer")
                print("7. Back")
                cust_choice = input("Enter choice: ")

                if cust_choice == "1":
                    cid = input("Enter Customer ID: ")
                    name = input("Enter Customer Name: ")
                    phone = input("Enter Customer Phone: ")
                    id_proof = input("Enter ID Proof: ")
                    customer.add_customer(cid, name, phone, id_proof)

                elif cust_choice == "2":
                    customer.view_available_vehicles()

                elif cust_choice == "3":
                    cid = input("Enter Customer ID: ")
                    vid = input("Enter Vehicle ID: ")
                    customer.rent_vehicle(cid, vid)

                elif cust_choice == "4":
                    cid = input("Enter Customer ID: ")
                    customer.return_vehicle(cid)

                elif cust_choice == "5":
                    customer.view_customers()
                elif cust_choice == "6":
                    cid = input("Enter Customer ID to remove: ")
                    customer.remove_customer(cid)   
                elif cust_choice == "7":
                    break

        elif choice == "3":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()