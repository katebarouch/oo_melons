import random
import datetime

"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas Melon":
            total = (1 + self.tax) * int(self.qty) *(1.5*base_price)
        if self.order_type == "international":
            if self.qty > 10:
                total = (4 + self.tax) * int(self.qty) * base_price
        else:
            total = (1 + self.tax) * int(self.qty) * base_price
        return total
    
    def get_base_price(self):

        base_price = random.randint(5,9) 

        now = datetime.datetime.now()
        time_of_order = now.hour
        day_of_order = now.weekday()

        if time_of_order == 8 or 9 or 10:
            if day_of_order == 0 or 1 or 2 or 3 or 4 :
                base_price += 4

        return base_price

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type = "domestic", tax = 0.8)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code, order_type = "international", tax = 0.17)

        self.country_code = country_code
      
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government Order"""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type = "domestic", tax = 0)

        self.passed_inspection = False
      
    def mark_inspection(self, passed):
        """Return the country code."""
        if passed == False:
            return self.passed_inspection == True