def convert_usd_to_crypto(usd_amount, crypto_prices):
    print(f"\n{usd_amount} USD ile alınabilecek kripto miktarları:")
    for crypto, price in crypto_prices.items():
        if price > 0:
            amount = usd_amount / price
            print(f"- {amount:.8f} {crypto}")

if __name__ == "__main__":
    # Fiyatlar temsilidir.
    prices = {
        'BTC': 68000.0,
        'ETH': 3500.0,
        'SOL': 150.0
    }

    dolar_miktari = 1000.0
    convert_usd_to_crypto(dolar_miktari, prices)