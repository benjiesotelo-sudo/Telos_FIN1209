# First Automation FIN1209: narration script

Read this over the video's pictures, one section per picture, in the handout's order. About twenty minutes. Say the words in your own voice and change anything that is not how you talk.

## 1. Welcome

*Picture: a capture of a public web page*

This is a short guide to your first automation. You will teach R to read three window oscillators from Chapter 8: the R S I, the M A C D, and the stochastic. For each day it finds each oscillator's buy or sell signal, counts how many agree, and gives the price to act at. You need R and RStudio, both free, and one package, T T R. The handout has the links.

## 2. Sheets: a blank spreadsheet

*Picture: screenshot `g1-blank-sheet`*

First, the data. Open sheets dot new in your Google account, and click cell A1.

## 3. Sheets: the formula

*Picture: screenshot `g2-formula`*

Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. Our start is the third of November twenty twenty five. Change only the ticker to pick another US company. For Coca Cola it is N Y S E colon K O.

## 4. Sheets: the result

*Picture: screenshot `g3-result`*

About two hundred rows fill in, with Date, Open, High, Low, Close and Volume. The dates look like seven slash one slash twenty twenty six. The script reads them as they are.

## 5. Sheets: download

*Picture: screenshot `g4-download-menu`*

Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.

## 6. The flowchart

*Picture: a capture of a public web page*

Here is what the script does, as a B P M N flowchart in four stages. Data in: one price file per stock, with a date, four prices, and a volume. Measure: for each day, the R S I, the M A C D and the stochastic, each with its rule written beside it, and its slide. A signal is the day one line crosses another. Decide: count how many of the three crossed the same way. None means skip the day. Otherwise choose buy or sell by the net vote, and set the price: a buy at the day's high, which is Lim's trigger, and a sell at the close, which is our choice. Report: a chart, a summary for each stock, and one table of the signals.

## 7. Start a script

*Picture: a screen recording (00-new-script)*

Now we write it. In RStudio choose File, New File, R Script. Save it in your First Automation folder, next to the data folder. Then Session, Set Working Directory, To Source File Location.

## 8. Step 1: read a file

*Picture: a screen recording (01-read)*

Step one: read a price file. A variable holds a value. Read dot csv opens the file as a table, one row per day, and as dot Date turns the Google Sheets date into a real date. Run it with Code, Source.

## 9. Step 2: the RSI

*Picture: a screen recording (02-rsi)*

Step two: a package. T T R holds the indicators, and you install it once with install dot packages. Library loads it. R S I gives the relative strength index, fourteen days, plain averages as on slide 195.

## 10. Step 3: a crossing

*Picture: a screen recording (03-cross)*

Step three: a crossing is a signal. This small function gives plus one on the day one line crosses above another, and minus one when it crosses below. The R S I crossing fifty is the signal on slide 74. Here are the days it happened.

## 11. Step 4: three oscillators

*Picture: a screen recording (04-three)*

Step four: the other two. The M A C D is a twelve day average minus a twenty six day average, with a nine day signal line, slides 166 to 168. Its signal line crossing is on slide 83. The stochastic is on slide 187. Add the three signals to get a vote: positive is a buy, negative a sell.

## 12. Step 5: the table

*Picture: a screen recording (05-table)*

Step five: the table. One row per signal day: the date, buy or sell, the entry price, what each oscillator said, and how many agree. A buy uses the day's high, slide 201. The slides give no sell trigger, so a sell uses the close. That is our choice, not Lim's rule.

## 13. Step 6: the chart

*Picture: a screen recording (06-chart)*

Step six: the chart. Price on top, the three oscillators below, and a triangle on every signal day. Green up is a buy, red down is a sell, and the big numbered ones are where two or more agree.

## 14. Step 7: every file

*Picture: a screen recording (07-files)*

Step seven: do it for every file in the data folder, and print a line per stock. That is the whole script. Source it.

## 15. The answer

*Picture: the last frame of 07-files*

Here is the answer for each stock: how many signal days, and how many had two or more oscillators agreeing. The numbers are in the table.

## 16. The table

*Picture: a screen recording (08-outputs)*

Here is the table. Each row is a signal day, with the side, the entry price, each oscillator's signal, and the agree count.

## 17. The chart

*Picture: an image R drew (start/KO)*

And the chart. Price on top, then the R S I with its fifty line, the M A C D with its signal line, and the stochastic. The big numbered triangles are the days two oscillators agreed.

## 18. Add new data

*Picture: a screen recording (09-update)*

That is the automation. Download the files again with a later end date, replace them, and run the script again. The table and the charts update.

## 19. Why a buy

*Picture: an image R drew (why/why-buy)*

Now the justification. The script gives numbers. This is what they mean. Take a real buy from the KO table. On the day line, the R S I crosses up through fifty, and the stochastic crosses up through its signal line. Two of three agree, and that is the buy signal. The price to act at is that day's high, the entry, as slide 201 says. The M A C D did not cross that day, so it is empty in the table.

## 20. Why a sell

*Picture: an image R drew (why/why-sell)*

The sell is the mirror image. Here the M A C D crosses down through its signal line, and the stochastic crosses down too. The slides give no sell trigger, so the entry is that day's close. That is our choice, not Lim's rule.

## 21. False consensus

*Picture: a title card*

But agreeing is not proof. All three are built from the same closing prices. On this data the R S I and the stochastic correlate at 0.78, and the R S I and M A C D at 0.71. Lim calls this multicollinearity, a false consensus and a false sense of confidence. His cure is oscillators built from different data, such as volume.

## 22. Your task

*Picture: a title card*

Your task: your own stock, and your own pair of the three oscillators. Write your script, and draw its flowchart. The due date is in the manual.

## 23. Submit

*Picture: a title card*

Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. And the flowchart with the same name plus Flowchart, as a P D F, a dot bpmn file, or Markdown.

## 24. AI

*Picture: a title card*

You may use AI to help. Your flowchart must match the script you submit and explain each step in your own words.

## 25. Marks

*Picture: a title card*

One hundred points. Sixty come from running your script on files you have never seen. Forty come from your flowchart. Good luck.
