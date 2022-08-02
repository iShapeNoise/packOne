#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def try_me():
    funny_list = ['If you think you are too small to make a difference, try sleeping with a mosquito.',
		  'Remember, today is the tomorrow you worried about yesterday.',
		  'The road to success is always under construction.',
		  'Life isn\'t finding shelter in the storm. It\'s about learning to dance in the rain.',
		  'If life gives you lemons, make apple juice and make people wonder how the hell you did it.',
		  'Today you are you! That is truer than true! There is no one alive who is you-er than you!',
		  'To solve the human equation, we need to add love, subtract hate, multiply good, and divide between truth and error.',
		  'Even if you\'re on the right track, you\'ll get run over if you just sit there.',
		  'Always remember that you are absolutely unique. Just like everyone else.',
		  'I told my psychiatrist that everyone hates me. He said I was being ridiculous - everyone hasn\'t met me yet.',
		  'We don\'t stop playing because we grow old; we grow old because we stop playing.',
		  'Don\'t judge each day by the harvest you reap but by the seeds that you plant.',
		  'The difference between an optimist and a pessimist? An optimist laughs to forget, but a pessimist forgets to laugh.'
    ]
    number  = random.choice(range(len(funny_list)))
    quote = funny_list[number]
    return quote

if __name__ == "__main__":
    quote = try_me()
    print(quote)

