# task2_stock_tracker.py
# CodeAlpha Task 2 - Stock Portfolio Tracker (simple version)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "AMZN": 150,
    "MSFT": 300
}

def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("Please enter a valid whole number.")

def main():
    print("=== CodeAlpha Task 2: Stock Portfolio Tracker ===")
    print("Available symbols:", ", ".join(stock_prices.keys()))
    print("Enter stocks one by one. Type DONE when finished.\n")

    portfolio = {}
    while True:
        sym = input("Stock symbol (or DONE): ").strip().upper()
        if sym == "DONE":
            break
        if sym == "":
            continue
        if sym not in stock_prices:
            print("Symbol not in list. Please enter one of:", ", ".join(stock_prices.keys()))
            continue
        qty = get_int(f"Quantity for {sym}: ")
        portfolio[sym] = portfolio.get(sym, 0) + qty

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = 0
    lines = []
    lines.append("Your Portfolio Summary:\n")
    for sym, qty in portfolio.items():
        price = stock_prices[sym]
        value = price * qty
        total += value
        line = f"{sym} - Qty: {qty}, Price: {price}, Value: {value}"
        print(line)
        lines.append(line + "\n")
    summary = f"\nTotal Portfolio Value: {total}"
    print(summary)
    lines.append(summary + "\n")

    save = input("\nSave result to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        try:
            import csv
            with open("portfolio.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Symbol", "Quantity", "Price", "Value"])
                for sym, qty in portfolio.items():
                    w.writerow([sym, qty, stock_prices[sym], stock_prices[sym]*qty])
                w.writerow([])
                w.writerow(["Total", "", "", total])
            print("Saved to portfolio.csv")
        except Exception as e:
            print("Error saving CSV:", e)
            # fallback to txt
            with open("portfolio.txt", "w") as f:
                f.writelines(lines)
            print("Saved to portfolio.txt instead.")
    else:
        # also write a simple text file automatically (optional)
        with open("portfolio.txt", "w") as f:
            f.writelines(lines)
        print("Saved summary to portfolio.txt (auto).")

if __name__ == "__main__":
    main()