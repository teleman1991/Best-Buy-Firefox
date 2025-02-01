import logging
try:
    from colorama import Fore, Style
except Exception:
    logging.error(
        'Could not import all required modules. '
        'Please run the following command again:\n\n'
        '\tpip install -r requirements.txt\n')
    exit()

HEADER = f'''
{Fore.BLUE}
██████╗ ███████╗███████╗████████╗    ██████╗ ██╗   ██╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██║   ██║╚██╗ ██╔╝
██████╔╝█████╗  ███████╗   ██║       ██████╔╝██║   ██║ ╚████╔╝ 
██╔══██╗██╔══╝  ╚════██║   ██║       ██╔══██╗██║   ██║  ╚██╔╝  
██████╔╝███████╗███████║   ██║       ██████╔╝╚██████╔╝   ██║   
╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   
{Fore.YELLOW}
███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
███████║██║ ╚████║██║██║     ███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
'''

# Rate limiting constants
RATE_LIMIT_DELAY = 2  # Delay between requests in seconds
MAX_REQUESTS_PER_MINUTE = 20
REQUEST_WINDOW = 60  # Time window in seconds

# URLs
BASE_URL = 'https://www.bestbuy.com'
API_URL = 'https://api.bestbuy.com/v1'
CART_URL = f'{BASE_URL}/cart'
CHECKOUT_URL = f'{BASE_URL}/checkout/r/fast-track'

# Product page selectors
ADD_TO_CART_BTN = 'button.add-to-cart-button'
SOLD_OUT_BTN = '.btn-disabled'
INVENTORY_STATUS = '.fulfillment-add-to-cart-button'

# Cart and checkout selectors
CART_ICON = '.cart-icon'
CHECKOUT_BTN = '.checkout-buttons__checkout'
GUEST_BTN = '.guest-button'
CONTINUE_BTN = 'button[data-track="Continue to Payment Information"]'

# Form selectors
EMAIL_INPUT = '#user\\.emailAddress'
PHONE_INPUT = '#user\\.phone'
FIRST_NAME_INPUT = '#consolidatedAddresses\\.ui_address_2\\.firstName'
LAST_NAME_INPUT = '#consolidatedAddresses\\.ui_address_2\\.lastName'
ADDRESS_INPUT = '#consolidatedAddresses\\.ui_address_2\\.street'
CITY_INPUT = '#consolidatedAddresses\\.ui_address_2\\.city'
STATE_SELECT = '#consolidatedAddresses\\.ui_address_2\\.state'
ZIP_INPUT = '#consolidatedAddresses\\.ui_address_2\\.zipcode'

# Payment selectors
CARD_NUMBER_FRAME = '#credit-card-iframe'
CARD_NUMBER_INPUT = '#number'
EXPIRATION_INPUT = '#expiration'
CVV_INPUT = '#cvv'

# Error messages
RATE_LIMIT_ERROR = 'Rate limit exceeded. Waiting before next request...'
BLOCKED_ERROR = 'Access blocked by Best Buy. Rotating user agent...'
STOCK_CHECK_ERROR = 'Error checking stock status. Retrying...'
CART_ERROR = 'Error adding item to cart. Retrying...'
CHECKOUT_ERROR = 'Error during checkout process. Retrying...'