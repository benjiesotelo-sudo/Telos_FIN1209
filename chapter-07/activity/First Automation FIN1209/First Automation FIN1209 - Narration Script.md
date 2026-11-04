# First Automation FIN1209: narration script

Read this over the video's pictures, one section per picture, in the handout's order. About twenty minutes. Say the words in your own voice and change anything that is not how you talk.

## 1. Welcome

*Picture: a title card*

Welcome to First Automation, FIN1209. This video goes through the whole activity, in the same order as the handout, with a title card at the start of each part. You will teach a computer one of the rules from Chapter 7. You write a small R script. You drop price files in a folder, run the script, and it tells you where the rule says to buy or sell, saves those signals in a table, and draws a chart with each signal marked. Nobody needs to know R already.

## 2. Part 0: What you are making

*Picture: a title card*

Part 0. What you are making.

## 3. What you are making

*Picture: the handout page: What you are making*

A trading rule says exactly when to buy or sell and at what price. You will automate one. Run the script, add new prices, run it again, and the signals and the chart update. That is automation: the rule is applied the same way every time. You hand in two files: your R script, and a flowchart of how it works. The whole activity is worth one hundred points.

## 4. Signals, not advice

*Picture: the handout page: What you are making*

One plain line before we start. The output is the signals of one rule, applied to past prices. It is not investment advice, and it does not say what price will do next. Chapter one's point still holds: a forecast cannot be checked when it is made. Later in the semester a bigger version of this comes, and you may be grouped for it.

## 5. Part 1: What to install

*Picture: a title card*

Part 1. What to install.

## 6. Install R

*Picture: a capture of a public web page*

Install R first. On Windows, go to the CRAN page for Windows and click Download R at the top. On a Mac, go to the CRAN page for macOS and pick the package for your chip, Apple silicon or Intel. Open the file and click through the installer, keeping every default.

## 7. Install R on a Mac

*Picture: a capture of a public web page*

This is the Mac page. The first package is for Apple silicon, the second is for older Intel Macs. The Apple menu, About This Mac, tells you which you have.

## 8. Install RStudio

*Picture: a capture of a public web page*

Then install RStudio Desktop. Go to the RStudio download page on docs dot posit dot co, and click the big download button for your system. On a Mac, drag RStudio into Applications. The example needs no R packages at all.

## 9. Posit Cloud

*Picture: a capture of a public web page*

If you cannot install anything, use Posit Cloud. It runs RStudio in your browser. Make a free account, start a new RStudio project, and use the Upload button in the Files pane to put the example folder in. Everything in the handout works the same way.

## 10. The flowchart tool

*Picture: a capture of a public web page*

For the flowchart, use bpmn dot io. It runs in the browser, is free, and needs no account. You can also use Camunda Modeler, or draw a Mermaid flowchart in Markdown at mermaid dot live.

## 11. Part 2: The rule the example uses

*Picture: a title card*

Part 2. The rule the example uses.

## 12. The rule

*Picture: the handout page: 2. The rule the example uses*

The example uses Larry Williams' Oops from Chapter 7. On slide 194: if a bar opens above the previous bar's high, Lim places a sell-stop at the previous high and a stoploss at the new bar's high. We sell only if price falls back to the previous high. On slide 199 the bullish Oops is the mirror image: open below the previous low, a buy-stop at the previous low, and a stoploss at the new low. Slide 197 adds that a stop and reverse order starts at the stoploss.

## 13. What the slides leave open

*Picture: the handout page: 2. The rule the example uses*

The slides leave four things open, and the handout says so. These are our choices, not Lim's rule. Only the gap bar can fill the order. The order of high and low inside a daily bar is not needed. There is no trend filter, because slide 195 gives no test a computer can run. And there is no profit exit. Where your rule leaves something open, choose the simplest thing and say so.

## 14. Part 3: The contract

*Picture: a title card*

Part 3. The contract.

## 15. Folders and files

*Picture: the handout page: 3. The contract*

Your script is marked by running it on files you have never seen, so everybody follows the same contract. The script runs from the folder that holds it, next to a folder called data. Every CSV in data is one stock, and the file name without dot csv is the ticker. The script writes output slash signals dot csv, and one chart per input file. Base R only, no packages, under sixty seconds.

## 16. Input and output columns

*Picture: the handout page: 3. The contract*

Input files have the columns Date, Open, High, Low, Close, and maybe Volume, with the oldest row first. Output signals dot csv has ticker, date, side, entry and stoploss, in that order, and may add your own columns after. If there are no signals, the file is still written with only the header.

## 17. Part 3b: Where to get price data, and what kind

*Picture: a title card*

Part 3b. Where to get price data, and what kind.

## 18. The data and what it is for

*Picture: the handout page: 3b. Where to get price data*

You need one bar per trading day, with date, open, high, low, close and volume. Open, high and low are what the Oops uses. The close colours the candle. The Oops does not use volume, but Chapter 7 mentions it in some patterns and Chapter 6 covers it in full. Open interest exists only for futures, so a stock has none.

## 19. The free sources

*Picture: the handout page: The free sources*

Here are the free sources, checked on the public sites. Google Sheets with GOOGLEFINANCE gives daily open, high, low, close and volume for US stocks only, needs a Google account, and exports a CSV. P S E colon J F C returned N slash A, so there is no daily history there. P S E Edge shows today's prices only, with no download. Yahoo Finance shows a history table for US stocks but no Philippine stocks and no download button when signed out. Investing dot com, TradingView and broker platforms could not be checked without an account, and the handout says so. The script works with any source whose CSV matches the contract.

## 20. Part 4a: Get the example prices yourself

*Picture: a title card*

Part 4a. Get the example prices yourself.

## 21. Sheets: a blank spreadsheet

*Picture: screenshot `g1-blank-sheet`*

Google Sheets is the one route this handout walks through, and it works for US listed stocks. Go to sheets dot new while signed in to your Google account. A blank spreadsheet opens. Click cell A1.

## 22. Sheets: the formula

*Picture: screenshot `g2-formula`*

In A1 type the GOOGLEFINANCE formula with the ticker N Y S E colon K O, the word all, the start date, the end date, and daily. Use the dates from the handout so your numbers match. For this first run the end date is September thirtieth. To pick another company, change only the ticker inside the first quotes.

## 23. Sheets: the result

*Picture: screenshot `g3-result`*

About sixty four rows fill in, with the six column names in row one. The dates read like seven slash one slash twenty twenty six. That is how Google Sheets writes them, and the script reads them exactly as they are, so you never edit a date.

## 24. Sheets: download

*Picture: screenshot `g4-download-menu`*

Choose File, Download, Comma Separated Values. The file holds the values, not the formula. Rename it K O dot csv and put it in your data folder, then do the same for F in a new spreadsheet.

## 25. Sheets: update and swap

*Picture: the handout page: 4a. Get the example prices*

To update later, change the end date in the formula to October thirtieth, download again, and replace the file. To use another US stock, change only the ticker inside the first quotes. Philippine stocks do not work here: we tried P S E colon J F C and Sheets answered N slash A. For a Philippine stock you need another source from the survey, for example Investing dot com, saved as a CSV with the contract's columns.

## 26. Part 4: R in 14 small steps

*Picture: a title card*

Part 4. R in 14 small steps.

## 27. Start a new script

*Picture: a screen recording (00-new-script)*

Now we write the script ourselves. In RStudio choose File, New File, R Script. A blank script opens in the top left pane. Choose File, Save As, name it, and save it in the First Automation folder, next to the data folder. Then choose Session, Set Working Directory, To Source File Location, so R works in this folder.

## 28. B1: A named value (a variable)

*Picture: a screen recording (01-variable)*

Step 1 of 14. A named value (a variable). A variable is a name that holds a value. The arrow arrow puts the value on the right into the name on the left. Text goes inside quotes. A line that starts with # is a comment: a note for people, which R skips. print() shows a value in the Console. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 29. B2: Read a CSV file into a table

*Picture: a screen recording (02-read)*

Step 2 of 14. Read a CSV file into a table. read.csv() opens a CSV file and returns a table, which R calls a data frame. Each row is one trading day (one bar) and each column is one kind of price. head(bars, 3) shows only the first three rows. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 30. B3: One column is a list of values (a vector)

*Picture: a screen recording (03-column)*

Step 3 of 14. One column is a list of values (a vector). bars$High is the whole High column. R calls a list of values like this a vector. Square brackets pick a position: highs[4] is the fourth value and highs[1:5] is the first five. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 31. B4: Clean up the date

*Picture: a screen recording (04-trim)*

Step 4 of 14. Clean up the date. The Date column is text, and it may look like 7/1/2026 16:00:00 (the Google Sheets layout) or 2026-07-02. sub(" .*", "", x) removes everything from the first space, which drops the time. as.Date() turns the text into a real date, trying each layout in tryFormats, and format() writes it back as YYYY-MM-DD. Assigning to bars$Date replaces the column. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 32. B5: Compare two numbers

*Picture: a screen recording (05-compare)*

Step 5 of 14. Compare two numbers. A comparison such as > or <= gives TRUE or FALSE. We use the fourth bar, i arrow 4. The previous bar is i - 1. The first test asks the Oops question: did this bar open above the previous bar's high? The second asks whether price then came back to that high, that is, whether this bar's low is at or below it. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 33. B6: Decide with if

*Picture: a screen recording (06-if)*

Step 6 of 14. Decide with if. if (condition) { ... } runs the lines inside the braces only when the condition is TRUE. && means both conditions must be true. cat() prints text and values on one line. This is the bearish Oops on slide 194. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 34. B7: Give if a second case (else if)

*Picture: a screen recording (07-elseif)*

Step 7 of 14. Give if a second case (else if). else if is tried only when the first condition is FALSE. The bullish Oops on slide 199 is the mirror image: open below the previous low, then price comes back up to it. We change i to a bar that opened below the previous low. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 35. B8: Repeat for every bar (a loop over rows)

*Picture: a screen recording (08-loop)*

Step 8 of 14. Repeat for every bar (a loop over rows). for (i in 2:nrow(bars)) runs the lines inside the braces once for every bar from the second to the last, with i taking each number in turn. We start at 2 because the first bar has no previous bar. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 36. B9: Collect the results in a table

*Picture: a screen recording (09-table)*

Step 9 of 14. Collect the results in a table. Printing is not enough: we want a table we can save. First make an empty table with named columns. Then each time a signal is found, build a one-row table and add it to the bottom with rbind(). Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 37. B10: Write a CSV file

*Picture: a screen recording (10-write)*

Step 10 of 14. Write a CSV file. write.csv() saves a table as a CSV file. dir.create() makes the output folder first (it does nothing if the folder exists). Open the new file to see the signals. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 38. B11: Draw a chart

*Picture: a screen recording (11-plot)*

Step 11 of 14. Draw a chart. png() opens a picture file, the plot commands draw into it and dev.off() closes it. plot() makes the empty frame, segments() draws each bar's high-to-low line and rect() draws its body from the open to the close: white when the bar closed up, black when it closed down. When the picture file is closed R prints null device 1. That is normal. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 39. B12: Mark the signals on the chart

*Picture: a screen recording (12-marks)*

Step 12 of 14. Mark the signals on the chart. Chart commands draw on top of what is already there. points() puts a triangle at each signal's entry price: red pointing down for SELL, green pointing up for BUY. A short dash marks the stoploss and text() writes the signal's number just beyond that dash; it is its row in signals.csv. Watch it being typed, then run with Code, Source, and read what R printed in the console.

## 40. Steps 13 and 14: the finished script

*Picture: a screen recording (13-finished-example)*

Steps 13 and 14 pack these lines into three functions and loop over every file in the data folder. Instead of retyping them, open the finished example script. It is exactly the file in your folder. We run it with Source: it reads both of the Google Sheets files, and the console says how many signals it found in each. Then the Files pane shows the output folder, and signals dot csv opens in the editor.

## 41. Adding new data

*Picture: a screen recording (14-update)*

Now the automation. Replace the two files in the data folder with the October downloads, the same stocks with a month of new rows. Run the script again and change nothing else. The counts go up, and the table and both charts are rewritten.

## 42. Part 5: Run the finished example

*Picture: a title card*

Part 5. Run the finished example.

## 43. Step 1: the folder

*Picture: screenshot `r01-folder`*

Step one. Copy the First Automation folder to your Documents folder. Next to the script, make a folder called data, and copy into it the two price files you downloaded: K O dot csv and F dot csv.

## 44. Step 2: open the script

*Picture: screenshot `r02-open-script`*

Step two. In RStudio, choose File, Open File, and pick the example script. It opens in the top left pane.

## 45. Step 3: set the folder

*Picture: screenshot `r03-working-dir`*

Step three, the one people forget. Choose Session, Set Working Directory, To Source File Location. Without this, R cannot find the data folder.

## 46. Step 4: run it

*Picture: screenshot `r04-source`*

Step four. Click Source. R reads both files, finds the signals, draws two charts and writes the table. The console says how many signals it found in each file.

## 47. Step 5: what it made

*Picture: screenshot `r05-output-folder`*

Step five. The Files pane now has an output folder. Inside are signals dot csv, and one chart for each stock.

## 48. Step 6: the signals

*Picture: screenshot `r06-signals-csv`*

Step six. Open signals dot csv. Each row is one Oops. Side says sell or buy. Entry is the price where the stop order waits. Stoploss is where the trade is closed. Reverse is the opposite side Lim starts at the stoploss.

## 49. Step 7: the chart

*Picture: screenshot `r07-chart`*

Step seven. Open the K O chart. White candles closed up and black candles closed down. A red triangle pointing down is a sell entry. A green triangle pointing up is a buy entry. The short dash is its stoploss, and the number is the signal's row in the table. Check one yourself: find signal one in the table and see that the triangle sits at that entry price.

## 50. Step 8: add new data

*Picture: screenshot `r08-new-data`*

Step eight. This is the automation. Download both files again from Google Sheets with the later end date, and copy them over the ones in your data folder. They are the same two stocks with a month of new rows at the bottom.

## 51. Step 9: run it again

*Picture: screenshot `r09-rerun`*

Step nine. Click Source again, and change nothing else. The counts go up, and the table and both charts are rewritten.

## 52. Step 10: the updated chart

*Picture: screenshot `r10-chart-updated`*

Step ten. Open the K O chart again. It is longer, and the new signals continue the numbering. That is what automation means: the rule is applied the same way every time you add data.

## 53. Part 6: The flowchart

*Picture: a title card*

Part 6. The flowchart.

## 54. The example flowchart

*Picture: a capture of a public web page*

A flowchart says, in shapes, what the script does and in what order. This is the example's flowchart in BPMN, opened in bpmn dot io from the dot bpmn file. A thin circle starts it. Tasks are rounded rectangles, named with a verb. A diamond with an X is a yes or no question, with every arrow labelled. There are two loops: one gateway asks whether a file is left, and one asks whether a bar is left.

## 55. Shapes tied to code

*Picture: the handout page: Which lines of the example script*

Each numbered shape stands for lines of the example script, and the handout's table gives them. Your flowchart must do the same: every shape should point at lines of your script, and every loop and decision in your code should be a shape.

## 56. Drawing it yourself

*Picture: a capture of a public web page*

Now we draw this same flowchart ourselves, one shape at a time, in bpmn dot io, and say which lines of the script each shape stands for. Open demo dot bpmn dot io and create a new diagram.

## 57. Draw: Run the script

*Picture: a capture of a public web page*

First the start event, a thin circle. Name it Run the script. It stands for the moment you click Source.

## 58. Draw: Name the data and output folders

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Name the data and output folders. It stands for lines 9 to 10 of the script.

## 59. Draw: List the CSV files in the data folder

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: List the CSV files in the data folder. It stands for line 94 of the script.

## 60. Draw: Another file left?

*Picture: a capture of a public web page*

A diamond gateway is a yes or no question: Another file left? It stands for line 96 of the script. Draw an arrow out of it for each answer, and label every one.

## 61. Draw: Read the file into a table

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Read the file into a table. It stands for lines 13 to 21 and line 98 of the script. The arrows are labelled yes.

## 62. Draw: Start an empty signals table

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Start an empty signals table. It stands for lines 33 to 36 of the script.

## 63. Draw: Another bar left?

*Picture: a capture of a public web page*

A diamond gateway is a yes or no question: Another bar left? It stands for line 40 of the script. Draw an arrow out of it for each answer, and label every one.

## 64. Draw: Gap up and price back to the previous high?

*Picture: a capture of a public web page*

A diamond gateway is a yes or no question: Gap up and price back to the previous high? It stands for line 43 of the script. Draw an arrow out of it for each answer, and label every one. The arrows are labelled yes.

## 65. Draw: Record a SELL signal entry = previous high stoploss = new high

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Record a SELL signal entry = previous high stoploss = new high. It stands for lines 45 to 48 of the script. The arrows are labelled yes.

## 66. Draw: Gap down and price back to the previous low?

*Picture: a capture of a public web page*

A diamond gateway is a yes or no question: Gap down and price back to the previous low? It stands for line 49 of the script. Draw an arrow out of it for each answer, and label every one. The arrows are labelled no and no.

## 67. Draw: Record a BUY signal entry = previous low stoploss = new low

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Record a BUY signal entry = previous low stoploss = new low. It stands for lines 51 to 54 of the script. The arrows are labelled yes.

## 68. Draw: Draw the chart and mark the signals

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Draw the chart and mark the signals. It stands for lines 64 to 89 and line 100 of the script. The arrows are labelled no.

## 69. Draw: Add this file's signals to the list

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Add this file's signals to the list. It stands for line 102 of the script.

## 70. Draw: Write output/signals.csv

*Picture: a capture of a public web page*

A task, a rounded rectangle, named with a verb: Write output/signals.csv. It stands for line 110 of the script. The arrows are labelled no.

## 71. Draw: Signals and charts updated

*Picture: a capture of a public web page*

Last, the end event, a thick circle, named Signals and charts updated. Every path must reach one. When you are happy, use the buttons at the bottom left of bpmn dot io to download the diagram as a dot bpmn file and as an image, or print it to a PDF. The PDF is the preferred submission.

## 72. Part 7: Your task

*Picture: a title card*

Part 7. Your task.

## 73. Your task

*Picture: the handout page: 7. Your task*

Your task is your own R script that applies one rule from Chapters one to seven and meets the contract, and a flowchart of how it works. Reuse Oops, or choose Hikkake, or another rule where the slides give exact buy and stop prices. Write the rule's name and slide numbers in a comment at the top. Where the slides leave something open, choose the simplest thing and say so. Do not bring in outside indicators.

## 74. What to submit

*Picture: the handout page: 7. Your task*

Submit two files, named exactly. Your script: FirstAutomation, underscore, your surname, underscore, your first name, dot R. Your flowchart: the same name with underscore Flowchart, as a PDF, which is preferred, or a dot bpmn file, or a Markdown file with a Mermaid flowchart. Do not send price files or output.

## 75. Check before you submit

*Picture: the handout page: 7. Your task*

Before you submit, check five things. Run your script in a clean folder with no changes and no installs. Check signals dot csv has the five columns and a chart exists for each file. Delete the output folder and run again. Run with an empty data folder, and it should not crash. And open your flowchart next to your script: every shape has lines behind it. The marker runs your script on files you have not seen, in both date layouts, and one file may have no signals.

## 76. Part 8: Using AI

*Picture: a title card*

Part 8. Using AI.

## 77. The AI rule

*Picture: the handout page: 8. Using AI*

You may use AI to help write your script. The condition is that you can properly visualise and explain it in your flowchart. The flowchart must match the script you actually submit. Each task must say, in your own words, what that part of the code does, and where the rule has a number, which slide it comes from. If you cannot explain a part of the script, do not submit it. A script that runs perfectly with a flowchart that does not match it loses the flowchart marks.

## 78. Part 9: How it is marked

*Picture: a title card*

Part 9. How it is marked.

## 79. The marks

*Picture: the handout page: 9. The marks*

One hundred points. Sixty are checked against the record by running your script on files you have never seen: ten for running, ten for writing the files the contract names, twenty for finding the right signals, ten for the right prices, and ten for the chart showing them. Forty are judged from your flowchart: ten for correct BPMN, fifteen for matching your script, and fifteen for explaining each step. How your code looks is not marked.

## 80. The rubric

*Picture: the handout page: How a written answer is marked*

The judged marks use the course's written answer rubric. An answer is marked on whether it is grounded, pointing at something specific you can check, and connected, so the conclusion follows. Naming what argues against you is never marked, but it is what the best answers do. The levels are full, partial, minimal and none, and the handout shows an example of every level.

## 81. Good luck

*Picture: a title card*

That is the whole activity. Install R and RStudio, get your prices from Google Sheets, run the example, then write your own script and draw its flowchart. Read the handout again whenever you are stuck, and good luck.
