# import library
from tabulate import tabulate

database = {
    'Shandy' : ['Basic Plan', 12, 'shandy-1234'],
    'Cahya' : ['Standard Plan', 24, 'cahya-abcd'],
    'Ana'   : ['Premium Plan', 5, 'ana-2f9g'],
    'Bagus' : ['Basic Plan', 11, 'bagus-9f92']
}

class User:
    
    def __init__(self, username, current_plan, duration_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan

    def check_benefit(self):
        table_plan = [
            ['✓', '✓', '✓', 'can_stream'],
            ['✓', '✓', '✓', 'can_download'],
            ['✓', '✓', '✓', 'has_hd'],
            [' ', '✓', '✓', 'has_HD'],
            [' ', ' ', ' ', 'has_UHD'],
            [1, 2, 4, 'num_of_devices'],
            ['3rd party movie only',  'Basic Plan Content + Sports  (F1, Football, Basketball)',  'Basic Plan + Standard Plan +  PacFlix Original Series or Movie', 'content'],
            ['Rp 120.000,-', 'Rp 160.000,-', 'Rp 200.000,-', 'price']
        ]

        table = tabulate(
            table_plan, 
            headers=['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services'], 
            tablefmt='grid')
        
        print('MyFlix Plan List')
        print('')
        print(table)

    def check_plan(self):
        if self.username in database:
            print(f'Username: {self.username}\n'
                f'Current plan: {self.current_plan}\n'
                f'Plan duration: {self.duration_plan} months')
        else:
            print('Username not found')
    
    def upgrade_plan(self):
        all_plan = {
            'Basic Plan': [0, 120_000],
            'Standard Plan': [1, 160_000],
            'Premium Plan': [2, 200_000]
        }

        new_plan = input('Enter your new plan (Basic Plan/Standard Plan/Premium Plan): ').strip().title()

        if new_plan not in all_plan:
            print('Invalid plan entered. Please choose from Basic Plan, Standard Plan, or Premium Plan.')
            return
        
        try:
            if all_plan[self.current_plan][0] < all_plan[new_plan][0]:

                if self.duration_plan > 12:
                    discount = 0.05
                    discounted_price = all_plan[new_plan][1] - (all_plan[new_plan][1] * discount)

                    print(f'Your new plan will be {new_plan} with discounted (5%) price of Rp {discounted_price:,},-')

                else:
                    print(f'Your new plan will be {new_plan} with standard price of Rp {all_plan[new_plan][1]:,},-')
            else:
                print('You cannot downgrade your current plan')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

class NewUser(User):

    def __init__(self, username):
        # Initialize with default values for new user plan and duration
        super().__init__(username, 'None', 0)

    def pick_plan(self):
        all_plan = {
            'Basic Plan': [0, 120_000],
            'Standard Plan': [1, 160_000],
            'Premium Plan': [2, 200_000]
        }
        
        new_plan = input('Enter your new plan (Basic Plan/Standard Plan/Premium Plan): ').strip().title()

        if new_plan not in all_plan:
            print('Invalid plan entered. Please choose from Basic Plan, Standard Plan, or Premium Plan.')
            return
        
        referral_code = input('Enter your referral code: ').strip()
        discount_applied = False

        try:
            for user in database:
                if referral_code == database[user][2]:
                    discount = 0.04
                    discounted_price = all_plan[new_plan][1] - (all_plan[new_plan][1] * discount)

                    print(f'Your new plan will be {new_plan} with discounted (4%) price of Rp {discounted_price:,},-')
                    discount_applied = True
                    break

                if not discount_applied:
                    print(f'Your new plan will be {new_plan} with standard price of Rp {all_plan[new_plan][1]:,},-')
                    break

        except:
            print('Error: Invalid referral code format. Please enter a valid referral code (e.g., "james-1f2f").')

        