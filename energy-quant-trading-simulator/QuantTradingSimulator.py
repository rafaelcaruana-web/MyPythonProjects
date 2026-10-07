import csv
import random
import time

INITIAL_CAPITAL = 10000.0
GAS_PRICE = 80.0
PROFIT_TARGET = 1500.0

def run_trading_simulation():
    global GAS_PRICE
    cash = INITIAL_CAPITAL
    gas_Holdings = 0
    trade_count = 0
    target_achieved = False
    final_day_reached = 10
    
    print("\n -- Quant Simulation And Logger --")
    print(f"Starting Capital: £ {cash:.2f}")
    print(f"Target profit kill switch set at: £ {PROFIT_TARGET:.2f}")
    print("==========================================")
    time.sleep(1)
    
    with open("quant_trading_log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Day", "Gas price (£/Mwh)", "Action", "Balance (£)"])
        
        for day in range(1,11):
            final_day_reached = day
            price_change_percent = random.uniform(-0.35, 0.35)
            GAS_PRICE = GAS_PRICE* (1+price_change_percent)
            
            action = "HOLD"
            
            print(f"Day {day}: Gas price is £ {GAS_PRICE:.2f}/Mwh")
            
            if GAS_PRICE < 75.0 and cash >= GAS_PRICE:
                units_to_buy = int(cash // GAS_PRICE)
                cash -= units_to_buy * GAS_PRICE
                gas_Holdings += units_to_buy
                trade_count += 1
                action = "BUY"
                print(f"Bought {units_to_buy} units of gas at £ {GAS_PRICE:.2f}/Mwh. New balance: £ {cash:.2f}")
            elif GAS_PRICE > 76.0 and gas_Holdings > 0:
                print(f"Sold {gas_Holdings} units of gas at £ {GAS_PRICE:.2f}/Mwh.")
                cash += gas_Holdings * GAS_PRICE
                gas_Holdings = 0
                trade_count += 1
                action = "SELL"
            
            writer.writerow([day, round(GAS_PRICE, 2), action, round(cash, 2)])
            
            current_portfolio_value = cash + (gas_Holdings * GAS_PRICE)
            current_net_profit = current_portfolio_value - INITIAL_CAPITAL
            
            if current_net_profit >= PROFIT_TARGET:
                target_achieved = True
                print(f"Target profit of £ {PROFIT_TARGET:.2f} achieved on day {day}!")
                print("TRADING SIMULATION SHUTTING DOWN TO LOCK IN CAPITAL GAINS.")
                break
            time.sleep(1)
    
    final_portfolio_value = cash + (gas_Holdings * GAS_PRICE)
    net_profit = final_portfolio_value - INITIAL_CAPITAL
    
    print("===========================================")
    print("--- Final Simulation Summary ---")
    print(f"Total Simulation Window: {final_day_reached} days")
    print(f"Total Trades Executed: {trade_count}")
    print(f"Final Liquid Cash Balance: £ {cash:.2f}")
    print(f"REMAINING GAS HOLDINGS: {gas_Holdings} units")  
    print(f"Final Portfolio Value: £ {final_portfolio_value:.2f}")
    
    if net_profit >= 0:
        print(f"Net Trading Gain: £ {net_profit:.2f}")  
    else:
        print(f"Net Trading Loss: £ {net_profit:.2f}")
        
    if target_achieved:
        print("SYSTEM RUN STATUS  : SUCCESS (Target cleared via Kill Switch)")
    else:
        print("SYSTEM RUNS STATUS : COMPLETED (Standard Term Contract End)")
    
    print("LOG ENGINE PERK : Saved data rows to 'quant_trading_log.csv'")
    print("========================================")

run_trading_simulation()

                
            
        
    
