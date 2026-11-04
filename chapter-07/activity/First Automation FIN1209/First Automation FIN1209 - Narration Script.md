# First Automation FIN1209: narration script

Read this over the video's pictures, one section per picture, in the handout's order. About twenty minutes. Say the words in your own voice and change anything that is not how you talk.

## 1. Welcome

*Picture: a capture of a public web page*

This is a short guide to your first automation. You will teach R one rule from Chapter 7, Larry Williams' Oops, so that it finds the buy and sell prices for you. You need R and RStudio, both free. The handout has the download links.

## 2. Sheets: a blank spreadsheet

*Picture: screenshot `g1-blank-sheet`*

First, the data. Open sheets dot new in your Google account, and click cell A1.

## 3. Sheets: the formula

*Picture: screenshot `g2-formula`*

Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. Change only the ticker to pick another US company. For Coca Cola it is N Y S E colon K O.

## 4. Sheets: the result

*Picture: screenshot `g3-result`*

Sixty four rows fill in, with Date, Open, High, Low, Close and Volume. The dates look like seven slash one slash twenty twenty six. The script reads them as they are.

## 5. Sheets: download

*Picture: screenshot `g4-download-menu`*

Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.

## 6. The flowchart

*Picture: a capture of a public web page*

Here is what the script will do, as a B P M N flowchart. The input is the price files in the data folder. The process: for every stock, go day by day. Did the day open above yesterday's high, then come back down to it? That is a sell, with the stoploss at today's high. Did it open below yesterday's low, then come back up to it? That is a buy, with the stoploss at today's low. The output is three things: an answer for each stock, a chart with every signal marked, and a table of all the signals.

## 7. Start a script

*Picture: a screen recording (00-new-script)*

Now we write it. In RStudio, choose File, New File, R Script. Save it in your First Automation folder, next to the data folder. Then choose Session, Set Working Directory, To Source File Location, so R looks for the data folder here.

## 8. Step 1: read a file

*Picture: a screen recording (01-read)*

Step one: read a file. A variable holds a value, so ticker holds the text KO. Read dot csv opens the file as a table, one row per day. Run it with Code, Source, and the first three rows appear.

## 9. Step 2: clean the date

*Picture: a screen recording (02-date)*

Step two: clean the date. Cut the time off the text, and turn it into a real date. Google Sheets writes month, day, year, and the script copes with that.

## 10. Step 3: test one day

*Picture: a screen recording (03-test)*

Step three: test one day. Yesterday is row i minus one. Did today open above yesterday's high? Did today's low come back down to it? Both true means the Oops on slide 194 happened that day.

## 11. Step 4: test every day

*Picture: a screen recording (04-loop)*

Step four: test every day. A for loop repeats the test for each day. If the Oops happened, print a sell, with the entry, the stoploss, and a plain why, built from that day's own prices. Else if the day mirrors it, slide 199, print a buy. Here are the signals, each one explained.

## 12. Step 5: keep the signals

*Picture: a screen recording (05-table)*

Step five: keep them. Each signal becomes a row in a table, and write dot csv saves the table in an output folder.

## 13. Step 6: draw the chart

*Picture: a screen recording (06-chart)*

Step six: draw the chart. The price line, a red triangle at each sell price, a green triangle at each buy price, and each signal's number.

## 14. Step 7: every file

*Picture: a screen recording (07-files)*

Step seven: do it for every file in the data folder, and print a plain answer for each stock. That is the whole script, about forty lines. Source it.

## 15. The answer

*Picture: the last frame of 07-files*

Here is the answer. Every signal comes with its why. For example: it opened above the previous day's high, then fell back to it, so the sell order at that price filled, and the stoploss is the day's high. Then, for each stock, how many signals, and the latest one.

## 16. The table

*Picture: a screen recording (08-outputs)*

And the table. Every signal, with the date, side, entry price and stoploss.

## 17. The chart

*Picture: an image R drew (start/KO)*

And the chart. The line is the closing price. Each red triangle is a sell, each green triangle is a buy, at the entry price, numbered like the table.

## 18. Add new data

*Picture: a screen recording (09-update)*

That is the automation. Download the files again with a later end date, replace them, and run the script again. The table and the charts update. Nothing else changes.

## 19. Why a sell

*Picture: an image R drew (why/why-sell)*

Why is that a sell? Take one real signal from the KO table, zoomed in. One: yesterday's high, eighty seven fifteen. Two: today opens above it, at eighty seven eighty six. Three: price comes back down to eighty seven fifteen. The sell order waits there, so that is the sell price. The gap failed, which is the idea of the Oops. Four: the stoploss, today's high. If price went there instead, the sale was wrong, and the trade is closed.

## 20. Why a buy

*Picture: an image R drew (why/why-buy)*

The buy is the mirror image. One: yesterday's low. Two: today opens below it. Three: price comes back up to it, and that is the buy price. Four: the stoploss, today's low. These are the prices a rule gives, not a forecast.

## 21. Your task

*Picture: a title card*

Your task: write your own script for Oops, Hikkake, or another Chapter 1 to 7 rule with exact prices, and draw its flowchart.

## 22. Submit

*Picture: a title card*

Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. And the flowchart, with the same name plus Flowchart, as a P D F, a dot bpmn file, or a Markdown file.

## 23. AI

*Picture: a title card*

You may use AI to help write the script. The condition: your flowchart must match the script you submit and explain each step in your own words.

## 24. Marks

*Picture: a title card*

One hundred points. Sixty are checked by running your script on files you have never seen. Forty are judged from your flowchart. The handout has the details. Good luck.
