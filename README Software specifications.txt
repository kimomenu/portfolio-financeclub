1. Read excel file 'portfolio.xlsx' with: ticker, buy date, currency
2. Import portfolio.xlsx to a variable
3. Create variable of portfolio positions
3. Set current date
4.LOOP
	*Request of price history for stock from buy date to current date 
	*Write request result to variable
	*Compute and write column of price variation with base 100 at the purchase date
	*Request currency exchange in current date
	*Compute and write buy position in CHF according to purchase date exchange rate  
	*Compute and write actual position in CHF according to current exchange rate
	*Move to next ticker 

 END LOOP

5.Write a variation graph with all variables in a timeline
6.Write otuput excel file with portfolio postition and variation per ticker




######
to be considered for next revisions:
-dividends release
-stock splits
-portfolio global calculation ( with non equities)