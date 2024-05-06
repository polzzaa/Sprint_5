import faker


def get_sign_up():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name, email, password