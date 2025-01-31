class Data:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class View:
    @staticmethod
    def display_table(data_list):
        headers = ["Name", "Age"]
        print(f"| {headers[0]:<20} | {headers[1]:<5} |")
        print("="*32)
        for data in data_list:
            print(f"| {data.name:<20} | {data.age:<5} |")

class Process:
    @staticmethod
    def get_user_input():
        while True:
            try:
                name = input("Enter your name: ")
                if not name.strip():
                    raise ValueError("Name cannot be empty")
                age = int(input("Enter your age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive integer")
                return Data(name, age)
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

def main():
    data_list = []
    while True:
        data = Process.get_user_input()
        data_list.append(data)
        more_data = input("Do you want to add another entry? (yes/no): ")
        if more_data.lower() != 'yes':
            break
    View.display_table(data_list)

if __name__ == "__main__":
    main()
