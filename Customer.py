from Deals import Deals


class Customer:
    def __init__(self, name: str, customer_id: str):
        self.name = name
        self.id = customer_id

    def claim_deal(self, deal_id: str, num_of_items: int):
        Deals.claim_deal(deal_id, num_of_items, self.id)