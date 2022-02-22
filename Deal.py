from datetime import datetime
import uuid


class Deal:
    def __init__(self, description: str, num_of_items: int, price: float, duration_in_mins: int, seller_id: str, max_items_allowed=1):
        self.description = description
        self.num_of_items = num_of_items
        self.price = price
        self.duration_in_mins = duration_in_mins
        self.start_time = datetime.now()
        self.max_items_allowed = max_items_allowed
        self.id = uuid.uuid4()
        self.claimed_customers = set()
        self.remaining_items = num_of_items

    def get_deal_id(self):
        return self.id

    def end_deal(self):
        if self.is_deal_live():
            self.duration_in_mins = 0

    def update_price(self, price):
        self.price = price

    def update_end_duration(self, duration_in_mins: int):
        if not self.is_deal_live():
            raise ValueError('Deal has closed already')

        self.duration_in_mins = duration_in_mins

    def claim_deal(self, customer_id: str, items_claimed: int):
        if not self.is_deal_live():
            raise ValueError('Deal is not live')

        if customer_id in self.claimed_customers:
            raise ValueError('Customer already claimed the deal')

        if self.remaining_items == 0:
            raise ValueError('Deal has run out of items')

        if items_claimed > self.max_items_allowed:
            raise ValueError('Required items more than allowed')

        self.remaining_items -= items_claimed
        self.claimed_customers.add(customer_id)
        return True

    def is_deal_live(self):
        time_diff = datetime.now() - self.start_time
        print(time_diff)
        time_diff_in_mins_abs = time_diff.total_seconds() / 60
        return not (time_diff_in_mins_abs > self.duration_in_mins)
