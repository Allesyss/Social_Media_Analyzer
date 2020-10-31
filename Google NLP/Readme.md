## Description
The Google Natural Language API enables one to 
analyze the text, and shows the sentiment and entities of
it. This can also be done on the webpage: https://cloud.google.com/natural-language/

The analyze-sentiment function detects and prints the sentiment
of the text. The sentiment is quantified and represented by scores.
The higher the score is, the more happy the text is. The closer
the score is to 0, the more neutral it is.

A score from 0.25 to 1 represents positive, and one from -0.25 to -1 represents negative.
Scores from -0.25 to 0.25 represent neutral.

## Tests and Results
### Test1: Neutral Sentiment 
Input a neutral text from testfile1.txt, and let the NLP read and analyse it.

**Text:** "Test1 for google NLP. This text is designed to be neutral.
The google natural language API is a tool that can analyze the language, and, for example, detect the sentiment of the text. 
To use the google NLP locally on your computer, you need to download an authorization, which is a .json file. 
You need to link the key file to "GOOGLE_APPLICATION_CREDENTIALS" by the os.environ command."

**Result:** This text is considered neutral(overall score: -0.1), as it is meant to be.

An interesting fact is that, the first sentence is considered slightly positive(score +0.2). Perhaps one may not even 
realize it. Yet as we think deeply, a short sentence like this could indicate an easy atmosphere.
If we change the first sentence to "This is test1 for google NLP", the score turns to 0.

The second sentence is the only one that is considered negative(score -0.3) of all sentences.
This is probably because the word "designed" indicates dictatorship.

The last two sentences are considered neutral but slightly negative(-0.2 and -0.1 respectively). The word "need" is probably 
the major cause for this. 

### Test2: Positive Sentiment 
**Text:** "Another sunny day. A good weather is always cheering, especially when one needs to deviate a little bit from pressure. 
It reminds me of my last few days before graduating with a bachelorship, when life could not have been easier. 
I must admit studying in a master's program is very challenging and tiring, but it will be worth it. 
A promising future always gives me motivation."

**Results**: The first sentence is the only one considered neutral(0.1). Although "sunny" is positive, 
"another" might make it feel like one is bored with it, or one does not really want to see a sunny day.
If we change "another" into "a", the score becomes 0.2. A little higher, but still neutral.
Maybe "sunny" is not so positive after all.

The rest are all considered very positive, each scoring over 0.7. Apart from obviously positive words, the 
NLP is able to detect turns. The sentence "I must admit studying in a master's program is very challenging and tiring, but it will be worth it."
has scored highest (0.9) and is considered extremely positive, despite the "challenging" and "tiring" mentioned in the front. 
These two words are negative, but NLP has noticed the "but" behind, and knows that the seemingly negative mood before "but" is false.
This is really charming, because in many cases, one's mood is expressed in a complex way, and negative words can indeed be used to optimise the positive mood.
This is an example of understanding the complexity of grammar and mood expression, and google NLP has done great.

The overall score of this text is 0.7 out of 1, which means it is very positive.

### Test3: Negative Sentiment 
Instead of direct, obvious expressions, this test implements vague words indicating sadness.

**Text:**
- Happy families are all alike. Unhappy families are unhappy in their separate ways.
- The one I once loved is gone. 
- We once had every happiness ever imaginable, until time washed them all away.
- No word can describe how desperate he was.
- People will wait for him in the white tower, but he will never return.

These separate sentences all indicate negative moods, yet not all of them are detected.

Line1: A famous script from Anna Karenina. The two sentences were separated and analyzed respectively. The first line 
is considered very positive(0.8), and the second is very negative(-0.9). Yet if we combine them into one sentence, the 
new sentence scores -0.7, which is very negative. This is very correct. The NLP does not successfully detect sentiment 
among sentences, but it can detect sentiment in one sentence, especially in cases where the sentence contains a turn or
priority. It can tell false sentiment from real sentiment.

line2: Scores -0.7. The NLP has successfully detected the "loss" of something dear. There is no obviously negative word
in this sentence, but the word "gone" has created a huge difference, which the NLP has precisely detected.

Line3: Scores +0.3. This test is difficult, and the NLP failed. This sentence seems positive, but it destroys the positive 
atmosphere by "time washed them away". So, it is in fact very sad. Although the NLP has failed to dig out the hidden meaning, 
it did not rate this sentence very positive, but gave it a score of 0.3 instead. 

Line4: Scores -0.8. This sentence is very negative, and the NLP has successfully detected it.

Line5: Scores -0.6. A script from The Lord of the Rings. It contains negative indications, and the NLP has successfully detected it.

## Summary
Generally speaking, the NLP did well, despite very few failures. Not to mention obvious negative sentiment, it can detect hidden
 and vague negative sentiment with good accuracy.
