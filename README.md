# Best Buy Sniper (Firefox Edition)

An optimized Firefox-based automated checkout assistant for Best Buy, specifically designed for fast stock checking and checkout process.

## Features

- Parallel stock checking (API + webpage)
- Firefox optimization for better anti-detection 
- Automated form filling with rate limiting
- Cookie persistence between sessions
- Configurable scroll delays
- Fast 2-second refresh rate
- Detailed console logging
- Anti-detection measures
- Parallel API and webpage stock checking
- Automatic cookie management
- Rate limiting to prevent blocks

## Requirements

- Python 3.8 or higher
- Firefox browser
- Stable internet connection
- Valid Best Buy shipping address
- Valid payment method

## Quick Start

1. Install Firefox if you haven't already
2. Clone the repository:
```bash
git clone https://github.com/teleman1991/Best-Buy-Firefox.git
cd Best-Buy-Firefox
```

3. Create and activate a conda environment:
```bash
conda env create -f environment.yml
conda activate bestbuy-sniper
```

4. Set up your configuration:
```bash
cp config.template.json config.json
```

5. Edit `config.json` with your information and SKU:
```json
{
    "sku": "6509243",  # Your target item SKU
    "email": "your.email@example.com",
    "phone": "1234567890",
    "first_name": "Your First Name",
    "last_name": "Your Last Name",
    "address": "123 Your Street",
    "city": "Your City",
    "state": "TX",
    "zip": "12345",
    "payment": {
        "card_number": "1234567890123456",
        "expiration": "0125",
        "cvv": "123"
    }
}
```

6. Run the bot:
```bash
python run.py
```

## Important Notes

### Firefox Optimizations
- Uses Firefox-specific optimizations for better performance
- Browser settings automatically configured for optimal speed
- Images and animations disabled for faster loading
- Memory management optimized for better performance

### Stock Checking
- Performs parallel API and webpage checks
- 2-second refresh interval for fast stock detection
- Automatically retries on network errors
- Rate limiting to prevent detection

### Checkout Process
- Uses guest checkout for speed
- Configurable scroll delays for reliable form submission
- Automatic retry on form submission failures
- Cookie persistence for faster subsequent runs

### Safety Features
- Stops at final purchase screen for manual verification
- No automatic order submission
- Detailed logging for monitoring
- Error handling throughout the process

## Troubleshooting

1. Firefox Issues:
   - Make sure Firefox is up to date
   - Try clearing Firefox cache and cookies
   - Check that you can access Best Buy manually

2. Form Filling Issues:
   - Verify all fields in config.json
   - Check address is valid for Best Buy shipping
   - Ensure payment information is correct

3. Stock Check Issues:
   - Verify SKU number is correct
   - Check Best Buy API access
   - Ensure stable internet connection

4. Checkout Issues:
   - Check if Best Buy is experiencing high traffic
   - Verify shipping address is valid
   - Ensure payment method is valid

## Support

For issues and feature requests:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include console logs for bug reports

## Project Structure

```
Best-Buy-Firefox/
├── bestbuy/
│   ├── __init__.py
│   ├── constants.py
│   ├── rate_limiter.py
│   ├── bot.py
│   └── main.py
├── run.py
├── config.template.json
├── requirements.txt
└── environment.yml
```

## Legal Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with Best Buy's terms of service. The developers are not responsible for any misuse of this tool.

## License

MIT License - See LICENSE file for details