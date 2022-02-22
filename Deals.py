from Deal import Deal


class Deals:
    deals = dict()

    def __init__(self):
        pass

    @staticmethod
    def add_deal(deal: Deal):
        Deals.deals[deal.id] = deal

    def claim_deal(self, deal_id: str, customer_id: str, items_claimed: int):
        if deal_id not in Deals.deals:
            raise ValueError('Deal not existing')

        deal = Deals.deals[deal_id]
        deal.claim_deal(customer_id, items_claimed)

