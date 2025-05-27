class Department:
    dept_count = 0

    def __init__(self, dept_id, dname, dloc, dhead):
        self.dept_id = dept_id
        self.dname = dname
        self.dloc = dloc
        self.dhead = dhead
        Department.dept_count += 1

    def display_dept_info(self):
        print(f"Department ID   : {self.dept_id}")
        print(f"Department Name : {self.dname}")
        print(f"Location        : {self.dloc}")
        print(f"Head            : {self.dhead}")
        print("-" * 30)

    @classmethod
    def get_total_depts(cls):
        return cls.dept_count


# Storing departments in a list
departments = []

# Get input from user
n = int(input("Enter number of departments: "))

for i in range(n):
    print(f"\nEnter details for department {i + 1}:")
    dept_id = input("Enter Department ID: ")
    dname = input("Enter Department Name: ")
    dloc = input("Enter Department Location: ")
    dhead = input("Enter Department Head: ")

    dept = Department(dept_id, dname, dloc, dhead)
    departments.append(dept)

# Display all departments
print("\nAll Department Details:")
for dept in departments:
    dept.display_dept_info()

# Display total count
print(f"\nTotal Departments in the Organization: {Department.get_total_depts()}")

# Search by Department ID
search_id = input("\nEnter Department ID to search: ")
found = False
for dept in departments:
    if dept.dept_id == search_id:
        print("\nDepartment Found:")
        dept.display_dept_info()
        found = True
        break
if not found:
    print("Department with that ID not found.")

# Search by Department Name (startswith or contains)
search_name = input("\nEnter part/full Department Name to search: ").lower()
print("\nMatching Departments:")
match_found = False
for dept in departments:
    if dept.dname.lower().startswith(search_name) or search_name in dept.dname.lower():
        dept.display_dept_info()
        match_found = True

if not match_found:
    print("No departments matched the given name.")
