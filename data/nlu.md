## intent:check_balance
- what is my balance <!-- no entity -->
- how much do I have on my [savings](source_account) <!-- entity "source_account" has value "savings" -->
- how much do I have on my [savings account](source_account:savings) <!-- synonyms, method 1-->
- Could I pay in [yen](currency)?  <!-- entity matched by lookup table -->

## intent:restaurant
- Isn't it delicious Italian in Shibuya?
- I would like to eat Japanese food, but is it recommended for Roppongi?
- I'm going to Azabu next time, but tell me a French shop

## intent:restaurant_ja
- [渋谷](location)で美味しい[イタリアン](restaurant_type)ない？
- [和食](restaurant_type)食べたいんだけど、[六本木](location)におすすめある？
- 今度[麻布](location)行くんだけど、[フレンチ](restaurant_type)のお店教えて 

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad