class Player:
    def __init__(self, last_name, first_name, date_of_birth, sex, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        if rank < 0:
            raise ValueError(f"please enter positive number: {rank}")
            self.rank = rank

