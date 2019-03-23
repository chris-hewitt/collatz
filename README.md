# Collatz Conjecture Optimization

## Problem Definition

The Collatz Conjecture is a famous unsolved problem in mathematics. Its most distinguishing feature is arguably the simplicity of the problem space, which makes it all the more confounding. An explanation is available on [this Wolfram MathWorld page](http://mathworld.wolfram.com/CollatzProblem.html).

## Purpose

The purpose of this repo is to a) consolidate all the thoughts I've had about this problem over the past few months, b) experiment with algorithms to implement them, and c) familiarize myself with the syntax and control structures of Python.

## Output

This program (main.py) outputs the first n results of the Collatz sequence first using the original "naïve" algorithm, then using my shortcut "derived" algorithm which reduces calculation between even steps from N steps to 1 step.

It then benchmarks the two results for comparison.
