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

Here are the free sources, checked on the public sites. Google Sheets with GOOGLEFINANCE gives daily open, high, low, close and volume, needs a Google account, and exports a CSV. P S E Edge shows today's prices only, with no download. Yahoo Finance shows a history table for US stocks but no Philippine stocks and no download button when signed out. Investing dot com, TradingView and broker platforms could not be checked without an account, and the handout says so. The script works with any source whose CSV matches the contract.

## 20. Part 4a: Get the example prices yourself

*Picture: a title card*

Part 4a. Get the example prices yourself.

## 21. The GOOGLEFINANCE steps

*Picture: the handout page: 4a. Get the example prices*

Google Sheets is the one route this handout walks through. Open sheets dot new, type the GOOGLEFINANCE formula in cell A1 with the dates from the handout, wait for the rows to fill, then choose File, Download, comma separated values. Rename the file K O dot csv and put it in your data folder. Do the same for F. To update later, change the end date in the formula, download again, and replace the file. To use another stock, change only the ticker inside the first quotes.

## 22. Part 4: R in 14 small steps

*Picture: a title card*

Part 4. R in 14 small steps.

## 23. B1: A named value (a variable)

*Picture: the code of R step variable*

Step 1 of 14. A named value (a variable). A variable is a name that holds a value. The arrow arrow puts the value on the right into the name on the left. Text goes inside quotes. A line that starts with # is a comment: a note for people, which R skips. print() shows a value in the Console. The new lines are highlighted, and what R printed is below the code.

## 24. B2: Read a CSV file into a table

*Picture: the code of R step read*

Step 2 of 14. Read a CSV file into a table. read.csv() opens a CSV file and returns a table, which R calls a data frame. Each row is one trading day (one bar) and each column is one kind of price. head(bars, 3) shows only the first three rows. The new lines are highlighted, and what R printed is below the code.

## 25. B3: One column is a list of values (a vector)

*Picture: the code of R step column*

Step 3 of 14. One column is a list of values (a vector). bars$High is the whole High column. R calls a list of values like this a vector. Square brackets pick a position: highs[4] is the fourth value and highs[1:5] is the first five. The new lines are highlighted, and what R printed is below the code.

## 26. B4: Cut text down (the date)

*Picture: the code of R step trim*

Step 4 of 14. Cut text down (the date). The Date column is text and may carry a time, like 2026-07-02 16:00:00. substr(text, 1, 10) keeps only the first ten characters, the day. Assigning to bars$Date replaces the column. The new lines are highlighted, and what R printed is below the code.

## 27. B5: Compare two numbers

*Picture: the code of R step compare*

Step 5 of 14. Compare two numbers. A comparison such as > or <= gives TRUE or FALSE. We use the fourth bar, i arrow 4. The previous bar is i - 1. The first test asks the Oops question: did this bar open above the previous bar's high? The second asks whether price then came back to that high, that is, whether this bar's low is at or below it. The new lines are highlighted, and what R printed is below the code.

## 28. B6: Decide with if

*Picture: the code of R step if*

Step 6 of 14. Decide with if. if (condition) { ... } runs the lines inside the braces only when the condition is TRUE. && means both conditions must be true. cat() prints text and values on one line. This is the bearish Oops on slide 194. The new lines are highlighted, and what R printed is below the code.

## 29. B7: Give if a second case (else if)

*Picture: the code of R step elseif*

Step 7 of 14. Give if a second case (else if). else if is tried only when the first condition is FALSE. The bullish Oops on slide 199 is the mirror image: open below the previous low, then price comes back up to it. We change i to a bar that opened below the previous low. The new lines are highlighted, and what R printed is below the code.

## 30. B8: Repeat for every bar (a loop over rows)

*Picture: the code of R step loop*

Step 8 of 14. Repeat for every bar (a loop over rows). for (i in 2:nrow(bars)) runs the lines inside the braces once for every bar from the second to the last, with i taking each number in turn. We start at 2 because the first bar has no previous bar. The new lines are highlighted, and what R printed is below the code.

## 31. B9: Collect the results in a table

*Picture: the code of R step table*

Step 9 of 14. Collect the results in a table. Printing is not enough: we want a table we can save. First make an empty table with named columns. Then each time a signal is found, build a one-row table and add it to the bottom with rbind(). The new lines are highlighted, and what R printed is below the code.

## 32. B10: Write a CSV file

*Picture: the code of R step write*

Step 10 of 14. Write a CSV file. write.csv() saves a table as a CSV file. dir.create() makes the output folder first (it does nothing if the folder exists). Open the new file to see the signals. The new lines are highlighted, and what R printed is below the code.

## 33. B11: Draw a chart

*Picture: the code of R step plot*

Step 11 of 14. Draw a chart. png() opens a picture file, the plot commands draw into it and dev.off() closes it. plot() makes the empty frame, segments() draws each bar's high-to-low line and rect() draws its body from the open to the close: white when the bar closed up, black when it closed down. When the picture file is closed R prints null device 1. That is normal. The new lines are highlighted, and what R printed is below the code.

## 34. B12: Mark the signals on the chart

*Picture: the code of R step marks*

Step 12 of 14. Mark the signals on the chart. Chart commands draw on top of what is already there. points() puts a triangle at each signal's entry price: red pointing down for SELL, green pointing up for BUY. A short dash marks the stoploss and text() writes the signal's number just beyond that dash; it is its row in signals.csv. The new lines are highlighted, and what R printed is below the code.

## 35. B13: Give a block of code a name (a function)

*Picture: the code of R step function*

Step 13 of 14. Give a block of code a name (a function). A function packs lines under a name so they can be reused. name arrow function(inputs) { ... } defines it, and the last value it produces is what it gives back. We make three: read_bars, find_oops and draw_chart. The lines inside are the ones you already wrote; only the packaging is new. The new lines are highlighted, and what R printed is below the code.

## 36. B14: Repeat for every file (a loop over files)

*Picture: the code of R step files*

Step 14 of 14. Repeat for every file (a loop over files). list.files() returns the names of the files in a folder. A for loop over them runs the three functions once per file, so any CSV you drop into data is read. Adding and saving all the signals together is the last piece. This is the finished script, exactly the file you were given. The new lines are highlighted, and what R printed is below the code.

## 37. Part 5: Run the finished example

*Picture: a title card*

Part 5. Run the finished example.

## 38. Step 1: the folder

*Picture: screenshot `r01-folder`*

Step one. Copy the First Automation folder to your Documents folder. Next to the script, make a folder called data, and copy into it the two price files you downloaded: K O dot csv and F dot csv.

## 39. Step 2: open the script

*Picture: screenshot `r02-open-script`*

Step two. In RStudio, choose File, Open File, and pick the example script. It opens in the top left pane.

## 40. Step 3: set the folder

*Picture: screenshot `r03-working-dir`*

Step three, the one people forget. Choose Session, Set Working Directory, To Source File Location. Without this, R cannot find the data folder.

## 41. Step 4: run it

*Picture: screenshot `r04-source`*

Step four. Click Source. R reads both files, finds the signals, draws two charts and writes the table. The console says how many signals it found in each file.

## 42. Step 5: what it made

*Picture: screenshot `r05-output-folder`*

Step five. The Files pane now has an output folder. Inside are signals dot csv, and one chart for each stock.

## 43. Step 6: the signals

*Picture: screenshot `r06-signals-csv`*

Step six. Open signals dot csv. Each row is one Oops. Side says sell or buy. Entry is the price where the stop order waits. Stoploss is where the trade is closed. Reverse is the opposite side Lim starts at the stoploss.

## 44. Step 7: the chart

*Picture: screenshot `r07-chart`*

Step seven. Open the K O chart. White candles closed up and black candles closed down. A red triangle pointing down is a sell entry. A green triangle pointing up is a buy entry. The short dash is its stoploss, and the number is the signal's row in the table. Check one yourself: find signal one in the table and see that the triangle sits at that entry price.

## 45. Step 8: add new data

*Picture: screenshot `r08-new-data`*

Step eight. This is the automation. Download both files again from Google Sheets with the later end date, and copy them over the ones in your data folder. They are the same two stocks with a month of new rows at the bottom.

## 46. Step 9: run it again

*Picture: screenshot `r09-rerun`*

Step nine. Click Source again, and change nothing else. The counts go up, and the table and both charts are rewritten.

## 47. Step 10: the updated chart

*Picture: screenshot `r10-chart-updated`*

Step ten. Open the K O chart again. It is longer, and the new signals continue the numbering. That is what automation means: the rule is applied the same way every time you add data.

## 48. Part 6: The flowchart

*Picture: a title card*

Part 6. The flowchart.

## 49. The example flowchart

*Picture: a capture of a public web page*

A flowchart says, in shapes, what the script does and in what order. This is the example's flowchart in BPMN, opened in bpmn dot io from the dot bpmn file. A thin circle starts it. Tasks are rounded rectangles, named with a verb. A diamond with an X is a yes or no question, with every arrow labelled. There are two loops: one gateway asks whether a file is left, and one asks whether a bar is left.

## 50. Shapes tied to code

*Picture: the handout page: Which lines of the example script*

Each numbered shape stands for lines of the example script, and the handout's table gives them. Your flowchart must do the same: every shape should point at lines of your script, and every loop and decision in your code should be a shape.

## 51. Drawing: a blank diagram

*Picture: a capture of a public web page*

Now let's draw a few shapes in bpmn dot io. Open demo dot bpmn dot io and choose create a new diagram. It starts with one start event. Double click it and name it, for example Run the script.

## 52. Drawing: a task

*Picture: a capture of a public web page*

Pick the rounded rectangle from the palette on the left, or use the arrow on the start event, and place a task after it. Name it with a verb: Read the file into a table.

## 53. Drawing: a gateway

*Picture: a capture of a public web page*

Add a diamond gateway for a question, and name it with the question: Gap up and back to the previous high?

## 54. Drawing: label the arrow

*Picture: a capture of a public web page*

Add the task that happens when the answer is yes, and click the arrow to label it yes. Every arrow leaving a gateway needs a label.

## 55. Drawing: an end event

*Picture: a capture of a public web page*

Finish with a thick circle, an end event. Every path must reach one. When you are done, use the buttons at the bottom left to download your diagram as a dot bpmn file, and as an image or print it to a PDF. The PDF is the preferred submission.

## 56. Part 7: Your task

*Picture: a title card*

Part 7. Your task.

## 57. Your task

*Picture: the handout page: 7. Your task*

Your task is your own R script that applies one rule from Chapters one to seven and meets the contract, and a flowchart of how it works. Reuse Oops, or choose Hikkake, or another rule where the slides give exact buy and stop prices. Write the rule's name and slide numbers in a comment at the top. Where the slides leave something open, choose the simplest thing and say so. Do not bring in outside indicators.

## 58. What to submit

*Picture: the handout page: 7. Your task*

Submit two files, named exactly. Your script: FirstAutomation, underscore, your surname, underscore, your first name, dot R. Your flowchart: the same name with underscore Flowchart, as a PDF, which is preferred, or a dot bpmn file, or a Markdown file with a Mermaid flowchart. Do not send price files or output.

## 59. Check before you submit

*Picture: the handout page: 7. Your task*

Before you submit, check five things. Run your script in a clean folder with no changes and no installs. Check signals dot csv has the five columns and a chart exists for each file. Delete the output folder and run again. Run with an empty data folder, and it should not crash. And open your flowchart next to your script: every shape has lines behind it. The marker runs your script on files you have not seen, in both date layouts, and one file may have no signals.

## 60. Part 8: Using AI

*Picture: a title card*

Part 8. Using AI.

## 61. The AI rule

*Picture: the handout page: 8. Using AI*

You may use AI to help write your script. The condition is that you can properly visualise and explain it in your flowchart. The flowchart must match the script you actually submit. Each task must say, in your own words, what that part of the code does, and where the rule has a number, which slide it comes from. If you cannot explain a part of the script, do not submit it. A script that runs perfectly with a flowchart that does not match it loses the flowchart marks.

## 62. Part 9: How it is marked

*Picture: a title card*

Part 9. How it is marked.

## 63. The marks

*Picture: the handout page: 9. The marks*

One hundred points. Sixty are checked against the record by running your script on files you have never seen: ten for running, ten for writing the files the contract names, twenty for finding the right signals, ten for the right prices, and ten for the chart showing them. Forty are judged from your flowchart: ten for correct BPMN, fifteen for matching your script, and fifteen for explaining each step. How your code looks is not marked.

## 64. The rubric

*Picture: the handout page: How a written answer is marked*

The judged marks use the course's written answer rubric. An answer is marked on whether it is grounded, pointing at something specific you can check, and connected, so the conclusion follows. Naming what argues against you is never marked, but it is what the best answers do. The levels are full, partial, minimal and none, and the handout shows an example of every level.

## 65. Good luck

*Picture: a title card*

That is the whole activity. Install R and RStudio, get your prices from Google Sheets, run the example, then write your own script and draw its flowchart. Read the handout again whenever you are stuck, and good luck.
