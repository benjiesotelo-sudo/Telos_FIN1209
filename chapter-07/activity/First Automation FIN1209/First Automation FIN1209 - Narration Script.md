# First Automation FIN1209: narration script

Read this over the video's pictures, one section per picture, in the handout's order. The video has a long and a short version of the coding, and the skip times below are the real ones. Say the words in your own voice and change anything that is not how you talk.

## 1. Teaser

*Picture: the finished chart, then the finished table filling in (real outputs of the final script)*

In the next half hour you will build a program that reads a stock's prices and, for every day, counts five votes for buy or sell. It draws this chart. It writes this table. And when new prices arrive, it updates both by itself. You do not need to know how to code, because we type every line together, and explain it. Let's build it.

## 2. Welcome

*Picture: a capture of a public web page*

This is a short guide to your first automation. You will teach R to read price, bars and volume, from Chapters 1 to 7, and three window oscillators from Chapter 8. For each day it takes five votes for buy or sell, counts how many agree, checks the volume, and gives a trigger price. You need R and RStudio, both free, and one package, T T R. The manual has the links.

## 3. Not foolproof

*Picture: a title card*

Before we start. This program is not foolproof. It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class exercise, not advice.

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

Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.

## 8. The flowchart

*Picture: a capture of a public web page*

Here is what the script does, as a B P M N flowchart in four stages. Data in: one price file per stock, with a date, four prices, and a volume. Measure: five votes for each day. The price trend, from Chapter 5. The price bar, a key reversal, from Chapter 7. And the R S I, the M A C D and the stochastic from Chapter 8, each with its rule beside it and its slide. Decide: add the votes. A signal day is a day the bar or an oscillator fires and the votes do not cancel. Choose buy or sell by the net vote, and set the trigger: a buy above the day's high, which is Lim's trigger on slide 201, and a sell below the day's low, which is the mirror of it and our choice. Volume is not a vote: above average volume marks the day confirmed. Report: a chart, a summary for each stock, and one table of the signals.

## 9. The long version

*Picture: a title card*
*On screen: Short version: skip to 28:12*


From here there are two versions of the coding. This is the long version: we type every line, at a speed you can follow, and explain each one. If you only want the short version, which explains each block of code and not each line, skip to 28 minutes 12 seconds.

## 10. Start a script

*Picture: a screen recording (00-new-script)*

Now we write it. In RStudio choose File, New File, R Script. Save it in your First Automation folder, next to the data folder. Then Session, Set Working Directory, To Source File Location.

## 11. Step 1: Read every price file

*Picture: the last frame of 00-new-script*

Step one: read every price file in the data folder.

## 12. Step 1: # Price, bars and volume (Chapters 1 to 

*Picture: a screen recording (01a-type)*

These six lines are comments. Anything after a hash is a note for people, and R skips it. Ours say what the script does, and which Chapter and slide each vote comes from. Always write down where a rule comes from.

## 13. Step 1: for (path in list.files("data", pattern 

*Picture: a screen recording (01b-type)*

This is a loop. List dot files looks in the folder called data and gives back the name of every file that ends in dot csv. For path in means: take the files one at a time, and run everything inside the curly brackets once for each file. The script will work for one stock or twenty.

## 14. Step 1: ticker <- sub("\\.csv$", "", basename(pa

*Picture: a screen recording (01c-type)*

Ticker is a variable, a name that holds a value. Basename strips the folder from the path, and sub removes the dot csv, so K O dot csv becomes K O. Read dot csv then opens the file as a table, one row per day, and calls it bars.

## 15. Step 1: bars$Date <- as.Date(sub(" .*", "", bars

*Picture: a screen recording (01d-type)*

Google Sheets writes dates like seven slash one slash twenty twenty six, followed by a time. Sub cuts off everything from the first space. As dot Date turns the text into a real date, and tryFormats lists the two layouts it may find. Now R can sort and plot by date.

## 16. Step 1: print(head(bars, 3))

*Picture: a screen recording (01e-type)*

To see what we have read, print the first three rows. Head gives the top of a table.

## 17. Step 1: run it

*Picture: a screen recording (01z-run)*

Now run it with Code, then Source. In the Console you should see the first three rows of each file, one after the other: a date, the open, high, low and close prices, and the volume. The dates are now real dates, written year, month, day.

## 18. Step 2: Vote 1: the price trend

*Picture: the last frame of 01z-run*

Step two, the first vote: is the price trending up or down?

## 19. Step 2: remove the check line

*Picture: a screen recording (02a-del)*

That print line was only there to let us look. We select it and delete it, so the finished script stays short.

## 20. Step 2: library(TTR)

*Picture: a screen recording (02b-type)*

R does a lot, but the indicators come in a package called T T R. Library loads it. You install it only once, with install dot packages, typed in the Console.

## 21. Step 2: pldot <- SMA(bars$Close, 3)

*Picture: a screen recording (02c-type)*

S M A is a simple moving average. Three means the average of the last three closes. Chapter 5, slides 109 and 110, call this line the PLdot. Price above it is bullish, and below it bearish.

## 22. Step 2: trend_vote <- ifelse(bars$Close > pldot,

*Picture: a screen recording (02d-type)*

If the close is above the average, the vote is plus one, up. Otherwise it is minus one, down. If else makes that choice for every day at once. A vote is just a number, plus one for buy, minus one for sell.

## 23. Step 2: trend_vote[is.na(trend_vote)] <- 0

*Picture: a screen recording (02e-type)*

The first two days have no three day average yet, so the vote is missing. Is dot na finds the missing ones, and we set them to zero, no vote.

## 24. Step 2: print(table(trend_vote))

*Picture: a screen recording (02f-type)*

To see the votes, print a table of them. Table counts how many days gave each value.

## 25. Step 2: run it

*Picture: a screen recording (02z-run)*

Run it. The Console shows a small table with a count for minus one, plus one and zero. Most days are one or the other, and zero appears only on the first two days, which have no three day average yet.

## 26. Step 3: Vote 2: the price bar

*Picture: the last frame of 02z-run*

Step three, the second vote: what is today's bar telling us?

## 27. Step 3: remove the check line

*Picture: a screen recording (03a-del)*

That print line was only there to let us look. We select it and delete it, so the finished script stays short.

## 28. Step 3: before <- function(x) c(NA, head(x, -1))

*Picture: a screen recording (03b-type)*

Before gives yesterday's value in today's row. It shifts a column down by one, and the first day gets N A, because it has no yesterday. We need it to compare today's bar with yesterday's.

## 29. Step 3: bar_vote <- ifelse(bars$Low < before(bar

*Picture: a screen recording (03c-type)*

The key reversal, Chapter 7, slides 123 and 126. A bullish one: today's low is lower than yesterday's, but the close is at or above yesterday's close. That is plus one. Bearish: a higher high, and a close at or below yesterday's close. That is minus one. Otherwise zero. The book says near; we say at or.

## 30. Step 3: bar_vote[is.na(bar_vote)] <- 0

*Picture: a screen recording (03d-type)*

The first day again has no yesterday, so the bar vote there is missing. Set it to zero.

## 31. Step 3: print(bars$Date[which(bar_vote != 0)])

*Picture: a screen recording (03e-type)*

To see which days had a key reversal bar, print the dates where the vote is not zero.

## 32. Step 3: run it

*Picture: a screen recording (03z-run)*

Run it. The Console lists the dates on which a key reversal bar happened, bullish or bearish. Not every day, only a handful.

## 33. Step 4: Votes 3 to 5: the oscillators

*Picture: the last frame of 03z-run*

Step four, three more votes: the oscillators.

## 34. Step 4: remove the check line

*Picture: a screen recording (04a-del)*

That print line was only there to let us look. We select it and delete it, so the finished script stays short.

## 35. Step 4: cross <- function(a, b) {        # +1 on

*Picture: a screen recording (04b-type)*

A function packs lines under a name so we can reuse them. Cross takes two lines of numbers, a and b. It rounds them, so a rounding error is not mistaken for a cross. Then it gives plus one on the day a goes from at or below b to above it, minus one on the day it goes from at or above to below, and zero otherwise. A crossing is the signal.

## 36. Step 4: word <- function(s) ifelse(s == 1, "BUY"

*Picture: a screen recording (04c-type)*

Word turns a vote into text: plus one becomes B U Y, minus one S E L L, zero nothing. We use it for the table.

## 37. Step 4: rsi <- RSI(bars$Close, n = 14, maType = 

*Picture: a screen recording (04d-type)*

The R S I, the relative strength index. The input is the close. N equals fourteen means it looks at the last fourteen days. M A type S M A means plain averages, as slide 195 says. It swings between zero and one hundred.

## 38. Step 4: macd <- MACD(bars$Close, nFast = 12, nSl

*Picture: a screen recording (04e-type)*

The M A C D is a twelve day average minus a twenty six day average, and its signal line is a nine day average of that, slides 166 to 168. N fast, n slow and n sig are those three numbers. Percent false keeps it as a plain difference.

## 39. Step 4: sto <- stoch(bars[, c("High", "Low", "Cl

*Picture: a screen recording (04f-type)*

The stochastic uses the high, low and close. Fast K, fourteen days, says where the close sits within the last fourteen days' range. Fast D, three, is a three day average of it, slide 187.

## 40. Step 4: rsi_sig <- cross(rsi, 50)

*Picture: a screen recording (04g-type)*

Now find the crossings. The R S I crossing its fifty line, slide 74. The M A C D crossing its signal line, slide 83. The stochastic K crossing D, slide 187. Each result is plus one, minus one, or zero.

## 41. Step 4: print(colSums(abs(cbind(rsi_sig, macd_si

*Picture: a screen recording (04h-type)*

To check the oscillators, add up how many crossings each one found. Col sums adds each column.

## 42. Step 4: run it

*Picture: a screen recording (04z-run)*

Run it. The Console shows, for each stock, how many times each oscillator crossed. The stochastic crosses most often, the M A C D least. These are just counts of crossings.

## 43. Step 5: Count the votes and keep the signal days

*Picture: the last frame of 04z-run*

Step five: add up the votes, and keep the signal days in a table.

## 44. Step 5: remove the check line

*Picture: a screen recording (05a-del)*

That print line was only there to let us look. We select it and delete it, so the finished script stays short.

## 45. Step 5: all_signals <- NULL

*Picture: a screen recording (05b-type)*

All signals will collect every stock's signals. Dir dot create makes the output folder if it is not there. Both go before the loop, because we only want them once.

## 46. Step 5: votes <- cbind(trend_vote, bar_vote, rsi

*Picture: a screen recording (05c-type)*

Cbind puts the five votes side by side, one column each, one row per day. Rows sums will add them up for each day.

## 47. Step 5: fired <- bar_vote != 0 | rsi_sig != 0 | 

*Picture: a screen recording (05d-type)*

A signal day is a day the bar or an oscillator fired, written with the vertical bar for or, and the votes do not cancel out. Which gives the row numbers of those days.

## 48. Step 5: side <- ifelse(rowSums(votes)[day] > 0, 

*Picture: a screen recording (05e-type)*

If the votes add up above zero the side is B U Y, otherwise S E L L.

## 49. Step 5: signals <- data.frame(ticker = ticker, d

*Picture: a screen recording (05f-type)*

Now the table. Data dot frame builds it, one row for each signal day. Ticker, date and side. The entry is a trigger level. A buy triggers above the signal day's high, as Lim says on slide 201. A sell triggers below the signal day's low. That is the mirror of Lim's buy trigger, our choice, because the slides give no sell trigger. The trade happens only if price later goes beyond the level.

## 50. Step 5: trend = word(trend_vote[day]), bar = wor

*Picture: a screen recording (05g-type)*

Then what each vote said, written as words, and agree: how many of the five votes are on the winning side. And the volume: if the day's volume is above the average volume of the file, it is CONFIRMED, as slide 128 marks the key reversal day. Volume is not a vote. It says how much weight the day carried.

## 51. Step 5: all_signals <- rbind(all_signals, signal

*Picture: a screen recording (05h-type)*

R bind adds this stock's table under all the others.

## 52. Step 5: print(tail(signals, 3))

*Picture: a screen recording (05i-type)*

To see the table, print its last three rows. Tail gives the end of a table.

## 53. Step 5: write.csv(all_signals, "output/signals.c

*Picture: a screen recording (05j-type)*

After the loop, write dot csv saves the whole table as signals dot csv in the output folder.

## 54. Step 5: run it

*Picture: a screen recording (05z-run)*

Run it. The Console shows the last three rows of the signals table. Each row is a signal day, with the side, the trigger level, each vote, how many agree, and whether the volume confirmed it. It is also saved as signals dot csv.

## 55. Step 6: Draw the chart

*Picture: the last frame of 05z-run*

Step six: draw the chart.

## 56. Step 6: remove the check line

*Picture: a screen recording (06a-del)*

That print line was only there to let us look. We select it and delete it, so the finished script stays short.

## 57. Step 6: png(file.path("output", paste0(ticker, "

*Picture: a screen recording (06b-type)*

Png opens a picture file in the output folder, named after the stock. Layout splits it into five panels, the first three times as tall as the others. Par sets the margins.

## 58. Step 6: plot(bars$Date, bars$Close, type = "l", 

*Picture: a screen recording (06c-type)*

Plot draws the closing price as a line, against the date. Lines adds the orange three day average on top of it.

## 59. Step 6: big <- signals$agree >= 3

*Picture: a screen recording (06d-type)*

Now mark the signals. Big means three or more votes agree. Points puts a triangle at each signal's trigger level, green up for a buy, red down for a sell, and bigger when three or more agree. Text numbers the big ones with their row in the table.

## 60. Step 6: plot(bars$Date, bars$Volume, type = "h",

*Picture: a screen recording (06e-type)*

The second panel is the volume as bars, gold on the days confirmed by volume, with a dashed line at the average.

## 61. Step 6: plot(bars$Date, rsi, type = "l", xlab = 

*Picture: a screen recording (06f-type)*

Then one panel for each oscillator: the R S I with its fifty line, the M A C D with its signal line, and the stochastic.

## 62. Step 6: dev.off()

*Picture: a screen recording (06g-type)*

Dev dot off closes the picture file. Until then nothing is saved.

## 63. Step 6: run it

*Picture: a screen recording (06z-run)*

Run it. Nothing prints, because the chart goes into a picture file. In the output folder there is now one picture for each stock. Here is the K O chart.

## 64. Step 7: A summary line for each stock

*Picture: the last frame of 06z-run*

Step seven: print one summary line for each stock.

## 65. Step 7: cat(ticker, ":", nrow(signals), "signal 

*Picture: a screen recording (07a-type)*

Cat prints a line in the Console. It says the stock, how many signal days, how many had three or more votes agreeing, and how many were on above-average volume. The numbers come straight from the table.

## 66. Step 7: run it

*Picture: a screen recording (07z-run)*

Run it for the last time. The Console now prints one line for each stock: how many signal days, how many had three or more votes agreeing, and how many were on above-average volume. That is the whole script.

## 67. Skip the short version

*Picture: the last frame of 07z-run*
*On screen: Already watched the long version? Skip to 30:20*


That was the long version. Already watched it? Skip to 30 minutes 20 seconds, where the outputs start, and leave out the short version.

## 68. The short version

*Picture: a title card*

This is the short version: the same seven steps, but we do not type. Each block of the finished script is shown, with what it does and what it produces.

## 69. Block 1: Read every price file

*Picture: the code of R step read*

Step one is the read block. It lists every csv file in the data folder and, for each one, works out the ticker from the file name, reads the file into a table called bars, and turns the Google Sheets dates into real dates. It produces a table of days with the open, high, low, close and volume.

## 70. Block 2: Vote 1: the price trend

*Picture: the code of R step trend*

Step two is the price trend block. It loads the T T R package, takes the three day moving average of the close, and votes plus one when the close is above it and minus one when it is below. It produces the first vote for every day, with zero on the first two days that have no average yet.

## 71. Block 3: Vote 2: the price bar

*Picture: the code of R step bar*

Step three is the price bar block. It looks at yesterday's bar and votes for a key reversal: a lower low that closes at or above yesterday's close is a buy, a higher high that closes at or below it is a sell. It produces the second vote, zero on every ordinary day.

## 72. Block 4: Votes 3 to 5: the oscillators

*Picture: the code of R step osc*

Step four is the oscillator block. A small function finds the day one line crosses another. The R S I is tested against fifty, the M A C D against its signal line, and the stochastic percent K against percent D. It produces three more votes, one for each oscillator.

## 73. Block 5: Count the votes and keep the signal days

*Picture: the code of R step table*

Step five is the table block. It puts the five votes side by side, keeps the days where the bar or an oscillator fired and the votes do not cancel, and decides buy or sell by the net vote. It sets the trigger level, a buy above the high and a sell below the low, counts how many votes agree, checks the volume, and saves everything as signals dot csv.

## 74. Block 6: Draw the chart

*Picture: the code of R step chart*

Step six is the chart block. For each stock it draws one picture with five panels: price and its average with a triangle on every signal, then volume, then the R S I, the M A C D and the stochastic. It produces one picture file for each stock in the output folder.

## 75. Block 7: A summary line for each stock

*Picture: the code of R step files*

Step seven is the summary line. For each stock it prints the number of signal days, how many had three or more votes agreeing, and how many were on above average volume. That completes the script.

## 76. The answer

*Picture: the last frame of 07z-run*

Here is the answer for each stock: how many signal days, how many had three or more votes agreeing, and how many were on above average volume. The details are in the table.

## 77. The table

*Picture: a screen recording (08-outputs)*

Here is the table. Each row is a signal day: the side, the trigger level, each vote, how many agree, and whether the volume confirmed it.

## 78. The chart

*Picture: an image R drew (start/KO)*

And the chart. Price on top, then volume, the R S I with its fifty line, the M A C D with its signal line, and the stochastic. Notice the M A C D panel is empty at the start: it needs about thirty four days of history first. So for your own stock, pull about a year.

## 79. Add new data

*Picture: a screen recording (09-update)*

That is the automation. Download the files again with a later end date, replace them, and run the script again. The table and the charts update.

## 80. Why: a price bar on volume

*Picture: an image R drew (why/why-bar)*

Now the justification. The script gives numbers. This is what they mean. Take a real bearish key reversal from the KO table. One: yesterday's high. Two: today makes a new high. Three: today closes below yesterday's close. Buyers pushed price up and could not hold it, so the bar votes sell. Four: the volume is above average, so the day is confirmed. Volume does not vote. It tells you how much weight the move carried.

## 81. Why an oscillator buy

*Picture: an image R drew (why/why-buy)*

An oscillator vote is a crossing. Here the R S I crosses up through fifty, and the stochastic crosses up through its signal line. Those two vote buy, and the trigger is above that day's high, as slide 201 says. The trade happens only if price later goes above it.

## 82. Why an oscillator sell

*Picture: an image R drew (why/why-sell)*

The sell is the mirror image. Here the R S I and the M A C D cross down, and the trigger is below that day's low. The slides give no sell trigger, so this is the mirror of Lim's buy trigger, our choice. The trade happens only if price later falls below it.

## 83. False consensus

*Picture: a title card*

But agreeing is not proof. The R S I, the M A C D and the stochastic are all built from the same closing prices. On this data the R S I and the stochastic correlate at 0.73, and the R S I and M A C D at 0.80. Lim calls this multicollinearity, a false consensus. His cure is data other than price, such as volume, which is why the volume check stands apart.

## 84. Not foolproof, again

*Picture: a title card*

One more reminder before your task. This program is not foolproof. It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class exercise, not advice.

## 85. Your task

*Picture: a title card*

Your task: your own stock, and your own pair of the three oscillators, with the price trend, price bar and volume check. Write your script, and draw its flowchart. The due date is in the manual.

## 86. Submit

*Picture: a title card*

Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. And the flowchart with the same name plus Flowchart, as a P D F, a dot bpmn file, or Markdown.

## 87. AI

*Picture: a title card*

You may use AI to help. Your flowchart must match the script you submit and explain each step in your own words.

## 88. Marks

*Picture: a title card*

One hundred points. Sixty come from running your script on files you have never seen. Forty come from your flowchart. Good luck.
