global_gdp = 110.55e12  # Global GEP in USD
lambda_value = 0.5  # Average lambda value for pollination services

# Print a dot every tenth of a a second for 1 second
print("Calculating GEP. Please wait, this may take a couple seconds.")
import time
for i in range(60):
    print('.', end='', flush=True)
    time.sleep(0.033333333)
    
gep = global_gdp * lambda_value # Calculate Global Ecosystem Production (GEP)

print(f"\nYour GEP this year is {gep} (based on average lambda of {lambda_value}). Well done! Would you like me to optimize?")