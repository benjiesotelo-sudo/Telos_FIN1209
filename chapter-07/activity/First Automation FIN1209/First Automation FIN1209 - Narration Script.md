# First Automation FIN1209: narration script

Read this over the video's pictures, one section per picture, in the order of the video. Say the words in your own voice and change anything that is not how you talk.

## 1. Opening: one real Coca Cola trade

*Picture: the animated opening: the question, the real Google Sheets recording, RStudio drawn from the real runs (buy mode, then sell mode), and the trade on a price chart*

Should you buy Coca-Cola today? And if you do, when should you sell? In this activity, your own program answers both, from real prices. First, the prices. One Google Sheets formula pulls Coca-Cola's daily prices. You download them as a file, and the program reads it. Our file ends on the twentieth of January, twenty twenty six. Four settings at the top: buy mode, for Coca-Cola. Then click Source. The answer is BUY. Enter if the price goes above seventy one dollars seventy eight. Stop at sixty nine dollars seventy nine. Here is that day on the chart. The buy signal, on the twentieth of January. The green line is the trigger, seventy one dollars seventy eight. The red line is the stop, sixty nine dollars seventy nine. The next day, Coca-Cola opened at seventy one dollars ninety eight, above the trigger. So you buy there, at seventy one dollars ninety eight. Now you run it again each day, in sell mode. Every day it says HOLD, with the stop at seventy dollars eighty three. On the second of March, you run it again. Sell mode, the price you paid, and the day you bought. Then click Source. SELL now, at about eighty dollars twenty two. The reason: a sell signal that day. Back on the chart: the sell, on the second of March. Bought at seventy one dollars ninety eight, sold at about eighty dollars twenty two. A gain of eleven point four percent, in about six weeks. That is what you are about to build. Your own buy and sell prices, in one click.

## 2. Not foolproof

*Picture: a title card*

Before we start. This program is not foolproof. It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class exercise, not advice.

## 3. Welcome

*Picture: a capture of a public web page*

This is a short guide to your first automation. You will teach R to read price, bars and volume, from Chapters 1 to 7, and three window oscillators from Chapter 8. Every day it takes five votes for buy or sell, and keeps the days when at least three of the five agree. Then your setting decides: buy mode says buy or wait, and sell mode says sell now or hold. You need R and RStudio, both free, and one package, T T R. The manual has the links.

## 4. Sheets: a blank spreadsheet

*Picture: a screen recording (sheets-1)*

First, the data. Open sheets dot new in your Google account, and click cell A1.

## 5. Sheets: the formula

*Picture: a screen recording (sheets-2)*

Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. Our start is the first of July twenty twenty six, and our end is the thirtieth of September. For Coca Cola the ticker is N Y S E colon K O. About sixty rows fill in, with Date, Open, High, Low, Close and Volume.

## 6. Sheets: another company

*Picture: a screen recording (sheets-3)*

To pick another US company, change only the ticker. Here it is N Y S E colon F, for Ford. The dates look like seven slash one slash twenty twenty six. The script reads them as they are.

## 7. Sheets: download

*Picture: a screen recording (sheets-4)*

Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. The last row is the latest trading day in your download, not the live price, and Google prices can be about twenty minutes late. Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.

## 8. The flowchart

*Picture: a capture of a public web page*

Here is what the script does, as a B P M N flowchart. Settings and data: you type four settings, and the script reads your stock's file. Measure: five votes for each day. The price trend, from Chapter 5. The price bar, a key reversal, from Chapter 7. And the R S I, the M A C D and the stochastic from Chapter 8, each with its rule beside it and its slide. Signal days: a day counts only when at least three of the five votes agree. Answer: if the mode is buy, today is either a buy signal, so enter above the signal day's high with a stop at its low, or you wait. If the mode is sell, you sell now if there was a sell signal since you bought or the price closed below your stop, and otherwise you hold. Report: a chart with today's answer marked, the table of signal days, and the answer file.

## 9. The script, block by block

*Picture: a title card*

Now the script. It has six labelled blocks: settings, read the data, the five votes, decide, draw the chart, and write the answer. For each block we look at the important lines. First the whole line is highlighted and explained, then the key part of it is boxed. The script uses no pipe operators: every line is plain R.

## 10. Block 1: Settings

*Picture: the labelled block b1 of the script*

Block 1 of 6: Settings. Lines 2 to 6. The only lines you edit. Change a value, run the script, read the answer.

## 11. Block 1, line 3

*Picture: line b1:r1:1 of the script, highlighted*

Line 3. Your question. "buy" asks: should I buy today? "sell" asks: I already own it, should I sell?

## 12. Block 1, line 3: the boxed part

*Picture: line b1:r1:2 of the script, highlighted*

The word in quotes is the setting. Type buy or sell exactly, in small letters.

## 13. Block 1, line 4

*Picture: line b1:r2:1 of the script, highlighted*

Line 4. Which price file to read. This one reads data/K O dot csv.

## 14. Block 1, line 4: the boxed part

*Picture: line b1:r2:2 of the script, highlighted*

Your stock's name. It must match the file name in the data folder.

## 15. Block 1, line 5

*Picture: line b1:r3:1 of the script, highlighted*

Line 5. Sell mode only: the price you paid for each share.

## 16. Block 1, line 5: the boxed part

*Picture: line b1:r3:2 of the script, highlighted*

A plain number, with no quotes.

## 17. Block 1, line 6

*Picture: line b1:r4:1 of the script, highlighted*

Line 6. Sell mode only: the day you bought it.

## 18. Block 1, line 6: the boxed part

*Picture: line b1:r4:2 of the script, highlighted*

Year, month, day, in quotes. It must be a trading day in your file.

## 19. Block 2: Read the data

*Picture: the labelled block b2 of the script*

Block 2 of 6: Read the data. Lines 7 to 11. Loads the indicator package and your stock's prices.

## 20. Block 2, line 8

*Picture: line b2:r1:1 of the script, highlighted*

Line 8. Loads the package that works out the moving average, the R S I, the M A C D and the stochastic.

## 21. Block 2, line 8: the boxed part

*Picture: line b2:r1:2 of the script, highlighted*

T T R is the only package we use. Install it once, in the Console, with install dot packages("T T R").

## 22. Block 2, line 9

*Picture: line b2:r2:1 of the script, highlighted*

Line 9. Reads your stock's file into a table called bars, one row for each trading day.

## 23. Block 2, line 9: the boxed part

*Picture: line b2:r2:2 of the script, highlighted*

paste0 glues pieces of text together: the stock K O and dot csv make K O dot csv.

## 24. Block 2, line 10

*Picture: line b2:r3:1 of the script, highlighted*

Line 10. Turns the Google Sheets dates into real dates, so R can sort and plot them.

## 25. Block 2, line 10: the boxed part

*Picture: line b2:r3:2 of the script, highlighted*

Sheets writes a time after the date. This cuts off everything from the first space.

## 26. Block 2, line 11

*Picture: line b2:r4:1 of the script, highlighted*

Line 11. n is the number of rows. Row n, the last row, is the latest trading day in the file: "today".

## 27. Block 2, line 11: the boxed part

*Picture: line b2:r4:2 of the script, highlighted*

Today is the last day in your download, not a live price. Sheets prices can be about 20 minutes late.

## 28. Block 3: The five votes

*Picture: the labelled block b3 of the script*

Block 3 of 6: The five votes. Lines 12 to 33. Each vote is plus one for BUY, minus one for SELL or 0 for nothing.

## 29. Block 3, line 13

*Picture: line b3:r1:1 of the script, highlighted*

Line 13. A small helper: yesterday's value, placed in today's row.

## 30. Block 3, line 13: the boxed part

*Picture: line b3:r1:2 of the script, highlighted*

Head with minus one is the list without its last value. The N A in front moves everything down one day.

## 31. Block 3, line 14

*Picture: line b3:r2:1 of the script, highlighted*

Line 14. A helper that spots a crossing: plus one the day line a crosses above line b, minus one the day it crosses below, 0 otherwise.

## 32. Block 3, line 14: the boxed part

*Picture: line b3:r2:2 of the script, highlighted*

A function packs lines under a name, so we write them once and use them three times.

## 33. Block 3, line 17

*Picture: line b3:r3:1 of the script, highlighted*

Line 17. Above b today but not above b yesterday: that is a crossing up.

## 34. Block 3, line 17: the boxed part

*Picture: line b3:r3:2 of the script, highlighted*

ifelse picks a value for every day at once: the first value when the test is true, the second when it is false. The ampersand means and.

## 35. Block 3, line 21

*Picture: line b3:r4:1 of the script, highlighted*

Line 21. The three day average of the closes: the P L dot line of Chapter 5 (slides 109, 110).

## 36. Block 3, line 21: the boxed part

*Picture: line b3:r4:2 of the script, highlighted*

S M A is a simple moving average: the average of the last 3 closes.

## 37. Block 3, line 22

*Picture: line b3:r5:1 of the script, highlighted*

Line 22. Vote 1, the price trend: plus one when the close is above its average, minus one when it is below.

## 38. Block 3, line 22: the boxed part

*Picture: line b3:r5:2 of the script, highlighted*

Greater than: it asks whether the close is bigger than its average.

## 39. Block 3, line 24

*Picture: line b3:r6:1 of the script, highlighted*

Line 24. Vote 2, the price bar, a key reversal (Chapter 7, slides 123, 126): a lower low that closes at or above yesterday's close votes BUY; a higher high that closes at or below it votes SELL.

## 40. Block 3, line 24: the boxed part

*Picture: line b3:r6:2 of the script, highlighted*

The ampersand joins two conditions: both must be true on the same day.

## 41. Block 3, line 27

*Picture: line b3:r7:1 of the script, highlighted*

Line 27. The R S I over 14 days (Chapter 8, slides 193 to 195).

## 42. Block 3, line 27: the boxed part

*Picture: line b3:r7:2 of the script, highlighted*

n = 14 is how many days it looks back.

## 43. Block 3, line 28

*Picture: line b3:r8:1 of the script, highlighted*

Line 28. The M A C D: two averages (12 and 26 days) and a 9 day signal line (slides 166 to 168).

## 44. Block 3, line 28: the boxed part

*Picture: line b3:r8:2 of the script, highlighted*

These numbers are the settings the slides use.

## 45. Block 3, line 29

*Picture: line b3:r9:1 of the script, highlighted*

Line 29. The stochastic: percent K over 14 days and percent D, its 3 day average (slides 185, 187).

## 46. Block 3, line 29: the boxed part

*Picture: line b3:r9:2 of the script, highlighted*

It needs the High, Low and Close columns, so we hand it those three.

## 47. Block 3, line 30

*Picture: line b3:r10:1 of the script, highlighted*

Line 30. Votes 3 to 5: plus one when the R S I crosses above 50 and minus one below (slide 74). The next two lines do the same for the M A C D and its signal line (slide 83) and for percent K and percent D (slide 187).

## 48. Block 3, line 30: the boxed part

*Picture: line b3:r10:2 of the script, highlighted*

The three lines use the same cross helper from above.

## 49. Block 3, line 33

*Picture: line b3:r11:1 of the script, highlighted*

Line 33. Puts the five votes side by side: one column each, one row for each day.

## 50. Block 3, line 33: the boxed part

*Picture: line b3:r11:2 of the script, highlighted*

cbind binds columns together.

## 51. Block 4: Decide: signal days, then buy or sell

*Picture: the labelled block b4 of the script*

Block 4 of 6: Decide: signal days, then buy or sell. Lines 34 to 70. Counts the votes, finds the signal days, then your setting decides what to answer.

## 52. Block 4, line 35

*Picture: line b4:r1:1 of the script, highlighted*

Line 35. For each day, counts how many of the five votes say BUY. The next line counts SELL.

## 53. Block 4, line 35: the boxed part

*Picture: line b4:r1:2 of the script, highlighted*

Where a vote says BUY the test is true. rowSums adds up the true values across the five votes.

## 54. Block 4, line 37

*Picture: line b4:r2:1 of the script, highlighted*

Line 37. A signal day is a day when at least 3 of the 5 votes agree. which() gives the row numbers of those days.

## 55. Block 4, line 37: the boxed part

*Picture: line b4:r2:2 of the script, highlighted*

The vertical bar means or: 3 or more BUY, or 3 or more SELL.

## 56. Block 4, line 40

*Picture: line b4:r3:1 of the script, highlighted*

Line 40. Builds the table of signal days, one row for each signal.

## 57. Block 4, line 40: the boxed part

*Picture: line b4:r3:2 of the script, highlighted*

data.frame makes a table from columns of equal length.

## 58. Block 4, line 41

*Picture: line b4:r4:1 of the script, highlighted*

Line 41. The trigger level. A buy triggers above the signal day's high (slide 201). A sell triggers below its low: the mirror, our choice. The trade happens only if price later goes beyond the level.

## 59. Block 4, line 41: the boxed part

*Picture: line b4:r4:2 of the script, highlighted*

Square brackets pick rows: this is the High column, on the signal days only.

## 60. Block 4, line 46

*Picture: line b4:r5:1 of the script, highlighted*

Line 46. Now your setting decides. Everything in the first brackets is buy mode.

## 61. Block 4, line 46: the boxed part

*Picture: line b4:r5:2 of the script, highlighted*

The double equals sign asks: is it equal to?

## 62. Block 4, line 48

*Picture: line b4:r6:1 of the script, highlighted*

Line 48. Is today, row n, one of the buy signal days?

## 63. Block 4, line 48: the boxed part

*Picture: line b4:r6:2 of the script, highlighted*

the in operator asks whether a value is in a list.

## 64. Block 4, line 49

*Picture: line b4:r7:1 of the script, highlighted*

Line 49. BUY: enter if price trades above today's high, with the stop at today's low.

## 65. Block 4, line 49: the boxed part

*Picture: line b4:r7:2 of the script, highlighted*

Square brackets pick row n, today.

## 66. Block 4, line 51

*Picture: line b4:r8:1 of the script, highlighted*

Line 51. WAIT: no buy signal today. It says how many votes say BUY today and that 3 are needed.

## 67. Block 4, line 51: the boxed part

*Picture: line b4:r8:2 of the script, highlighted*

Square brackets again: the count for today.

## 68. Block 4, line 57

*Picture: line b4:r9:1 of the script, highlighted*

Line 57. Sell mode starts here: finds the row of the day you bought.

## 69. Block 4, line 57: the boxed part

*Picture: line b4:r9:2 of the script, highlighted*

Max of which takes the last row that is on or before your date.

## 70. Block 4, line 58

*Picture: line b4:r10:1 of the script, highlighted*

Line 58. The stop: the low of the day you bought. Our choice. Chapter 5, slide 74 says a stop sits just below a significant trough but gives no rule.

## 71. Block 4, line 58: the boxed part

*Picture: line b4:r10:2 of the script, highlighted*

i is the row of your buy day.

## 72. Block 4, line 60

*Picture: line b4:r11:1 of the script, highlighted*

Line 60. The sell signal days after the day you bought.

## 73. Block 4, line 60: the boxed part

*Picture: line b4:r11:2 of the script, highlighted*

Only days after your buy day count.

## 74. Block 4, line 61

*Picture: line b4:r12:1 of the script, highlighted*

Line 61. The days after you bought that closed below your stop.

## 75. Block 4, line 61: the boxed part

*Picture: line b4:r12:2 of the script, highlighted*

Less than: it asks whether the close is smaller than your stop.

## 76. Block 4, line 62

*Picture: line b4:r13:1 of the script, highlighted*

Line 62. Your gain or loss so far, in percent, with a plus or minus sign.

## 77. Block 4, line 62: the boxed part

*Picture: line b4:r13:2 of the script, highlighted*

sprintf turns a number into text in the layout you choose.

## 78. Block 4, line 63

*Picture: line b4:r14:1 of the script, highlighted*

Line 63. SELL now if there was a sell signal or a close below the stop. Otherwise the answer is HOLD.

## 79. Block 4, line 63: the boxed part

*Picture: line b4:r14:2 of the script, highlighted*

The double bar means or.

## 80. Block 5: Draw the chart

*Picture: the labelled block b5 of the script*

Block 5 of 6: Draw the chart. Lines 71 to 87. One picture: price, volume and the three oscillators, with today's answer marked.

## 81. Block 5, line 73

*Picture: line b5:r1:1 of the script, highlighted*

Line 73. Opens a picture file in the output folder, named after your stock.

## 82. Block 5, line 73: the boxed part

*Picture: line b5:r1:2 of the script, highlighted*

The size of the picture in pixels.

## 83. Block 5, line 76

*Picture: line b5:r2:1 of the script, highlighted*

Line 76. Draws the closing price against the date. The title carries today's answer.

## 84. Block 5, line 76: the boxed part

*Picture: line b5:r2:2 of the script, highlighted*

type = "l" means a line.

## 85. Block 5, line 78

*Picture: line b5:r3:1 of the script, highlighted*

Line 78. A triangle on every signal day: green pointing up for a buy, red pointing down for a sell.

## 86. Block 5, line 78: the boxed part

*Picture: line b5:r3:2 of the script, highlighted*

pch is the shape of the mark: 24 points up, 25 points down.

## 87. Block 5, line 79

*Picture: line b5:r4:1 of the script, highlighted*

Line 79. Today's answer on the chart: a dashed line at the latest day, labelled BUY, WAIT, SELL or HOLD.

## 88. Block 5, line 79: the boxed part

*Picture: line b5:r4:2 of the script, highlighted*

abline draws a straight line. v is for vertical.

## 89. Block 5, line 81

*Picture: line b5:r5:1 of the script, highlighted*

Line 81. In sell mode only: a cross where you bought and a dotted red line at your stop.

## 90. Block 5, line 81: the boxed part

*Picture: line b5:r5:2 of the script, highlighted*

The cross is drawn at your buy date and the price you paid.

## 91. Block 5, line 82

*Picture: line b5:r6:1 of the script, highlighted*

Line 82. The panels below: volume (gold on confirmed days), then the R S I, the M A C D and the stochastic.

## 92. Block 5, line 82: the boxed part

*Picture: line b5:r6:2 of the script, highlighted*

type = "h" draws a thin bar for each day.

## 93. Block 5, line 87

*Picture: line b5:r7:1 of the script, highlighted*

Line 87. Closes the picture file. Until then nothing is saved.

## 94. Block 5, line 87: the boxed part

*Picture: line b5:r7:2 of the script, highlighted*

dev.off() turns the drawing off.

## 95. Block 6: Write the answer

*Picture: the labelled block b6 of the script*

Block 6 of 6: Write the answer. Lines 88 to 91. Saves the signal days and today's answer, and prints the answer.

## 96. Block 6, line 89

*Picture: line b6:r1:1 of the script, highlighted*

Line 89. Saves the table of signal days as output/signals dot csv.

## 97. Block 6, line 89: the boxed part

*Picture: line b6:r1:2 of the script, highlighted*

row.names = false leaves out the row numbers.

## 98. Block 6, line 90

*Picture: line b6:r2:1 of the script, highlighted*

Line 90. Saves today's answer as output/answer dot text, a fixed file anyone can open.

## 99. Block 6, line 90: the boxed part

*Picture: line b6:r2:2 of the script, highlighted*

writeLines writes each piece of text on its own line.

## 100. Block 6, line 91

*Picture: line b6:r3:1 of the script, highlighted*

Line 91. Prints the answer in the Console, one line each.

## 101. Block 6, line 91: the boxed part

*Picture: line b6:r3:2 of the script, highlighted*

cat prints text as it is.

## 102. Run it: buy mode, wait

*Picture: the settings and the real printed answer (buy_wait)*

Now we run it. In buy mode, for Coca Cola, with the file to the thirtieth of September. The answer is WAIT: no buy signal today, because none of the five votes say buy. It also shows the last buy signal in the file, with the level to enter above and the stop, and what has to happen next: three of the five votes on buy.

## 103. The chart

*Picture: an image R drew (modes/buy_wait)*

And the chart. Price on top with its three bar average, a triangle on every signal day, and a dashed line at today, labelled with the answer. Below are the volume, the R S I, the M A C D and the stochastic. Notice the M A C D panel is empty at the start: it needs about thirty four days of history first. So for your own stock, pull about a year.

## 104. Run it: buy mode, buy

*Picture: the settings and the real printed answer (buy_signal)*

The same file for Ford, downloaded a day earlier, ends on a day with a buy signal. The answer is BUY: enter if price trades above that day's high, with the stop at its low. This is a trigger level: the trade happens only if price later goes above it.

## 105. Run it: sell mode, sell now

*Picture: the settings and the real printed answer (sell_now)*

Now sell mode. You tell the script what you paid and the day you bought. Here you bought Coca Cola on the twelfth of August. A sell signal appeared after that, so the answer is SELL now, at about the last close, with your gain or loss in percent, and the reason.

## 106. Run it: sell mode, hold

*Picture: the settings and the real printed answer (sell_hold)*

And with the file to the thirtieth of October, and a purchase on the twelfth of October, there is no sell signal and no close below the stop, so the answer is HOLD, with your stop and your gain so far.

## 107. The chart in sell mode

*Picture: an image R drew (modes/sell_hold)*

In sell mode the chart also shows a cross where you bought, and a dotted red line at your stop.

## 108. The table

*Picture: the settings and the real printed answer (table)*

And the table. Each row of signals dot csv is a signal day: the side, the trigger level, the stop, what each vote said, how many agree, and whether the volume confirmed it.

## 109. Add new data

*Picture: the settings and the real printed answer (buy_update)*

That is the automation. Download the file again with a later end date, replace it, and run the script again. The answer, the table and the chart update.

## 110. Why: a price bar on volume

*Picture: an image R drew (why/why-bar)*

Now the justification. The script gives an answer. This is what the signals mean. Take a real bearish key reversal from the KO table. One: yesterday's high. Two: today makes a new high. Three: today closes below yesterday's close. Buyers pushed price up and could not hold it, so the bar votes sell. Four: the volume is above average, so the day is confirmed. Volume does not vote. It tells you how much weight the move carried.

## 111. Why an oscillator buy

*Picture: an image R drew (why/why-buy)*

An oscillator vote is a crossing. Here the R S I crosses up through fifty, and the stochastic crosses up through its signal line. Those two vote buy, and the trigger is above that day's high, as slide 201 says. The trade happens only if price later goes above it.

## 112. Why an oscillator sell

*Picture: an image R drew (why/why-sell)*

The sell is the mirror image. Here the R S I and the M A C D cross down, and the trigger is below that day's low. The slides give no sell trigger, so this is the mirror of Lim's buy trigger, our choice. The trade happens only if price later falls below it.

## 113. The stop

*Picture: a title card*

The stop is our choice too. Chapter 5, slide 74, says a stop is usually placed just below a significant trough for a long position, but it gives no rule. Ours is the low of the signal day in buy mode, and the low of the day you bought in sell mode.

## 114. False consensus

*Picture: a title card*

But agreeing is not proof. The R S I, the M A C D and the stochastic are all built from the same closing prices. On this data the R S I and the stochastic correlate at 0.73, and the R S I and M A C D at 0.80. Lim calls this multicollinearity, a false consensus. His cure is data other than price, such as volume, which is why the volume check stands apart.

## 115. Not foolproof, again

*Picture: a title card*

One more reminder before your task. This program is not foolproof. It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class exercise, not advice.

## 116. Your task

*Picture: a title card*

Your task: your own stock, and your own script. It has the same four settings at the top, takes the five votes, keeps the days when at least three agree, and answers in both modes. Test it: run it in buy mode, then change the mode to sell, type a price and a day you bought, and run it again. Then draw its flowchart. The due date is in the manual.

## 117. Submit

*Picture: a title card*

Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. And the flowchart with the same name plus Flowchart, as a P D F, a dot bpmn file, or Markdown.

## 118. AI

*Picture: a title card*

You may use AI to help. Your flowchart must match the script you submit and explain each step in your own words.

## 119. Marks

*Picture: a title card*

One hundred points. Sixty come from running your script, in both modes, on a file you have never seen. Forty come from your flowchart. Good luck.
