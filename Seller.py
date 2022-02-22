from Deal import Deal


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.deals = dict()

    def add_deal(self, description: str, num_of_items: int, price: float, duration_in_mins: int):
        new_deal = Deal(description, num_of_items, price, duration_in_mins)
        self.deals[new_deal.get_deal_id()] = new_deal

    def end_deal(self, deal_id: str):
        if deal_id in self.deals and self.deals[deal_id].is_deal_live():
            deal = self.deals[deal_id]
            deal.end_deal()

    def update_deal(self, deal_id: str, update_vals):
        if deal_id in self.deals:
            deal = self.deals[deal_id]
            if not deal.is_deal_live():
                raise ValueError('Deal is expired already')

            if 'price' in update_vals:
                deal.update_price(update_vals['price'])

            if 'duration_in_mins' in update_vals:
                deal.update_end_duration(update_vals['duration_in_mins'])










