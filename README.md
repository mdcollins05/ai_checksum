# AI_Checksum

## Purpose

A simple tool to calculate the checksum for an Aqua Illumination light schedule (`.aip` file).

## Why

In the past, I've wanted to adjust the power level of a color channel in a schedule in finer amounts than the web interface could provide. After downloading a schedule and opening it in a text file, I found the checksum at the top and no documentation on the AI schedule file format. I reached out to support but never heard back more than "we'll pass the feedback on". A while later, someone had dug into the web UI's Javascript and made a [Powershell version](http://thereefuge.com/threads/reverse-engineering-a-hydra-26-hd.15524/) that would generate a new checksum and someone else had converted that into [Javascript for use in their project](https://github.com/chriswhong/ai-hydra-time-offset/blob/master/time-offset.js). I much prefer Python over either of those languages for the tools I write, so I set out to write a replacement. A couple nights later and here we are.

## That's nice but how do I use this thing?

Simply point it to your `.aip` file via the command line and it'll generate the new checksum for you. You'll need to modify the file to include the new checksum.

```
$ ./calculate_checksum.py -s "test_schedules/AI Setting.aip"
1808880171
```

## Disclaimer!

I do not take any responsibility if your schedule bricks your light, burns out an LED, fries your power supply, or anything else.
