# Fluid-Key

A different kind of Swype Keyboard concept where the letters come to you!

## Concept

By default **begin** is a single column left aligned, **next** is right slightly of **current**.
**most_likely** is along the bottom with **less_likely** rising upward.

Assuming we have a reasonable predictive text engine (TBD) then to type a word.

- Display a list of predicted letters at the **begin** position
- Set **current** position = **begin** position
- User touches a letter to begin swipe motion
- Next predicted letters displayed in the **next** position
- User swipes toward the **next** position
- **next** position slides towards **current** position to allow for more space
- User arrives at **next** position selecting a letter
- repeat until (User lifts finger, ending word)

In essence the user swipes from (by default) left to right to type a word with slight up/down variation to select less likely words.

For readability max 4 letters can be shown vertically, extra letters will need to be available though some nice method.

May also consider displaying words or partial words instead of letters where appropriate

### Additions

For a complete keyboard the following would also need considered. But this is beyond the scope:

- Numbers
- Shift Key
- Symbols
- Emojis
