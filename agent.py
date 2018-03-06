class Property:
    """Class of property"""

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """
        Initialize all arguments.
        :param square_feet: int
        :param beds: int
        :param baths: int
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Function show all info about property.
        :return:
        """
        print("\nPROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Function return dict with square_feet, beds, baths that input.
        :return: dict
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """Class of apartment that inherit class Property"""
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialize all arguments.
        :param balcony: str
        :param laundry: str
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Show all necessary info about apartment details.
        :return:
        """
        super().display()
        print("\nAPARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        Function determine info about laundry and balcony and add them
        to the dict from prompt_init in class Property
        :return: dict
        """
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in \
                Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? "
                "({})".format(
                    ", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Function get valid input to know info about laundry and balcony.
    :param input_string: str
    :param valid_options: list
    :return: str
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def prompt_init():
    """
    Function add values of landry and balcony into dict from prompt_init
    of class Property.
    :return: dict
    """
    parent_init = Property.prompt_init()
    laundry = get_valid_input(
        "What laundry facilities does "
        "the property have? ",
        Apartment.valid_laundries)
    balcony = get_valid_input(
        "Does the property have a balcony? ",
        Apartment.valid_balconies)
    parent_init.update({
        "laundry": laundry,
        "balcony": balcony
    })
    return parent_init


prompt_init = staticmethod(prompt_init)


class House(Property):
    """Class of house that inherit class Property"""
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        Initialize all arguments.
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Show all necessary info about house details.
        :return:
        """
        super().display()
        print("\nHOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Function add info about garage, fence, stories in dict from prompt_init
        of class Property
        :return: dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)

        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class of purchase.
    """

    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialize all arguments.
        :param price: str
        :param taxes: str
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Show all necessary info about purchase details.
        :return:
        """
        super().display()
        print("\nPURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Function make dict with price and taxes as key.
        :return: dict
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class of rental.
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        Initialize all arguments.
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Show all necessary info about rental details
        :return:
        """
        super().display()
        print("\nRENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Function make dict with rent, utilities and furnished as key.
        :return: dict
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Class of house rental that inherit two classes: Rental and House.
    """

    def prompt_init():
        """
        Update dict from class House by dict from class Rental.
        :return: dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class of apartment rental that inherit two classes: Rental and Apartment.
    """

    def prompt_init():
        """
        Update dict from class Apartment by dict from class Rental.
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class of apartment purchase that inherit two classes: Purchase and Apartment.
    """

    def prompt_init():
        """
        Update dict from class Apartment by dict from class Purchase.
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Class of house purchase that inherit two classes: Purchase and House.
    """

    def prompt_init():
        """
        Update dict from class House by dict from class Purchase.
        :return: dict
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class of agent.
    """

    def __init__(self):
        """
        Initialize property list.
        """
        self.property_list = []

    def start(self):
        """
        Function return yes or no and choose start the program or not.
        :return: str
        """
        print("Hello, I'am your online agent")
        choice = get_valid_input("Can we start?",
                                 ("yes", "no")).lower()
        if choice == "yes":
            print("\nOkey. Let`s start.")
        else:
            print("\nGoodbye. Hope to see you soon.")
            exit()

        return choice

    def display_properties(self):
        """
        Show property from property list
        :return:
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """

        :return:
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def main(self):
        """
        Function to start the program.
        :return:
        """
        step1 = self.start()
        step2 = self.add_property()
        step3 = self.display_properties()
        if step1 == "yes":
            print(step1, step2, step3)
        else:
            exit()


agent = Agent()
print(agent.main())
