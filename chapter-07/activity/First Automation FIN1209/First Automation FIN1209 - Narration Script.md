# First Automation FIN1209: narration script

Read this over the screenshots of Part 5 of the handout, one section per picture. About four minutes. Say the words in your own voice and change anything that is not how you talk.

## 1. Welcome

*Picture: a title card*

Welcome to First Automation, FIN1209. In this activity you teach a computer one of the rules from Chapter 7. You will write a small R script. You drop price files in a folder, run the script, and it tells you where the rule says to buy or sell, saves those signals in a table, and draws a chart with each signal marked. This video follows Part 5 of the handout, where we run a finished example. Nobody needs to know R already.

## 2. The rule

*Picture: a title card*

The example uses Larry Williams' Oops from Chapter 7, slides 194 to 199. If a bar opens above the previous bar's high, Lim places a sell-stop at the previous high and a stoploss at the new bar's high. If it opens below the previous low, it is the mirror image: a buy-stop at the previous low and a stoploss at the new low. These are the signals of a rule. They are not investment advice.

## 3. Before you start

*Picture: a title card*

Install R first, then RStudio Desktop, both free. The handout has the links and the Windows and Mac steps. If you cannot install, use Posit Cloud in your browser. The example needs no R packages at all.

## 4. Step 1: the folder

*Picture: `r01-folder.png`*

Step one. Copy the First Automation folder to your computer. Next to the script, make a folder called data, and copy into it the two price files from data, start here: K O dot csv and F dot csv.

## 5. Step 2: open the script

*Picture: `r02-open-script.png`*

Step two. In RStudio, choose File, Open File, and pick the example script. It opens in the top left pane.

## 6. Step 3: set the folder

*Picture: `r03-working-dir.png`*

Step three, the one people forget. Choose Session, Set Working Directory, To Source File Location. Without this, R cannot find the data folder.

## 7. Step 4: run it

*Picture: `r04-source.png`*

Step four. Click Source. R reads both files, finds the signals, draws two charts and writes the table. The console says how many signals it found in each file.

## 8. Step 5: what it made

*Picture: `r05-output-folder.png`*

Step five. The Files pane now has an output folder. Inside are signals dot csv, and one chart for each stock.

## 9. Step 6: the signals

*Picture: `r06-signals-csv.png`*

Step six. Open signals dot csv. Each row is one Oops. Side says sell or buy. Entry is the price where the stop order waits. Stoploss is where the trade is closed. Reverse is the opposite side Lim starts at the stoploss.

## 10. Step 7: the chart

*Picture: `r07-chart.png`*

Step seven. Open the K O chart. White candles closed up and black candles closed down. A red triangle pointing down is a sell entry. A green triangle pointing up is a buy entry. The short dash is its stoploss, and the number is the signal's row in the table. Check one yourself: find signal one in the table and see that the triangle sits at that entry price.

## 11. Step 8: add new data

*Picture: `r08-new-data.png`*

Step eight. This is the automation. Copy the two files from data, October update, over the ones in your data folder. They are the same two stocks with a month of new rows at the bottom.

## 12. Step 9: run it again

*Picture: `r09-rerun.png`*

Step nine. Click Source again, and change nothing else. The counts go up, and the table and both charts are rewritten.

## 13. Step 10: the updated chart

*Picture: `r10-chart-updated.png`*

Step ten. Open the K O chart again. It is longer, and the new signals continue the numbering. That is what automation means: the rule is applied the same way every time you add data.

## 14. Your turn

*Picture: a title card*

Now it is your turn. Write your own script for Oops, Hikkake, or another rule from Chapters 1 to 7 with exact prices, following the contract in Part 3. Then draw a flowchart of how your script works, in BPMN. AI may help you write the script, as long as your flowchart matches what you submit and explains each step. Read Parts 6 to 9 of the handout, and good luck.
