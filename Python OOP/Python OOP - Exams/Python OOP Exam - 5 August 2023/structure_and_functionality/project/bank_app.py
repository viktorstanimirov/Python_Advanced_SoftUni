from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    granted_loans = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        curr_loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(curr_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        curr_loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
        curr_client = [c for c in self.clients if c.client_id == client_id][0]

        if (curr_loan.__class__.__name__ == "MortgageLoan" and curr_client.__class__.__name__ == "Student") or \
                (curr_loan.__class__.__name__ == "StudentLoan" and curr_client.__class__.__name__ == "Adult"):
            raise Exception(f"Inappropriate loan type!")

        self.loans.remove(curr_loan)
        curr_client.loans.append(curr_loan)
        self.granted_loans.append(curr_loan)
        return f"Successfully granted {loan_type} to {curr_client.name} with ID {client_id}."

    def remove_client(self, client_id):
        curr_client = [c for c in self.clients if c.client_id == client_id][0]

        if not curr_client:
            raise Exception("No such client!")

        if curr_client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(curr_client)
        return f"Successfully removed {curr_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        num_of_changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                num_of_changed_loans += 1

        return f"Successfully changed {num_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate):
        num_of_changed_clients = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                num_of_changed_clients += 1

        return f"Number of clients affected: {num_of_changed_clients}."

    def get_statistics(self):
        average_interest_rate = 0
        sum_of_granted_loans = sum([l.amount for l in self.granted_loans])

        if self.clients:
            average_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)

        return f"Active Clients: {len(self.clients)}\nTotal Income: {sum([c.income for c in self.clients]):.2f}\n" \
               f"Granted Loans: {len(self.granted_loans)}, Total Sum: {sum_of_granted_loans:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" \
               f"Average Client Interest Rate: {average_interest_rate:.2f}"
