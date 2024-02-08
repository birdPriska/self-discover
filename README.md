# Self-Discover

Implementation of the [Self-Discover](https://arxiv.org/pdf/2402.03620.pdf) paper (2024/02):

<img width="1250" alt="self-discover-3" src="https://github.com/policecar/self-discover/assets/819210/575bc9d1-79c5-4d05-96d5-b018f10be12e">


## Setup

```
conda create -n self-discover python=3.11
conda activate self-discover

pip install -r requirements.txt
```

## Usage

```python self_discover.py```

The script will then prompt you for a task.

## Example tasks

#### From the paper:

**Problem:** This SVG path element \<path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L 45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/> draws a: (A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon (G) pentagon(H) rectangle (I) sector (J) triangle **Solution:** Heptagon


#### From "Problems in General Physics" by I.E. Irodov:

**Problem 1.7:** Two swimmers leave point A on one bank of the river to reach point B lying right across on the other bank. One of them crosses the river along the straight line AB while the other swims at right angles to the stream and then walks the distance that he has been carried away by the stream to get to point B. What was the velocity u of his walking if both swimmers reached the destination simultaneously? The stream velocity v_0 = 2.0 km/hour and the velocity v' of each swimmer with respect to water equals 2.5 km per hour. **Solution:** 3.0 km/h


#### Martin Gardner puzzles:

**Problem:** Ten red socks and ten blue socks are all mixed up in a dresser drawer. The 20 socks are exactly alike except for their colour. The room is in pitch darkness and you want two matching socks. What is the smallest number of socks you must take out of the drawer in order to be certain that you have a pair that match?

**Problem:** A logician vacationing in the South Seas finds himself on an island inhabited by two proverbial tribes of liars and truth-tellers. Members of one tribe always tell the truth, members of the other always lie. He comes to a fork in a road and has to ask a native bystander which branch he should take to reach a village. He has no way of telling whether the native is a truth-teller or a liar. The logician thinks a moment, then asks one question only. From the reply he knows which road to take. What question does he ask?


#### Psychometrics

**Problem:** Which of the following claims does not follow from the claim "If Guy is happy, then he laughs"? (1) Only if Guy laughs is he likely to be happy. (2) If Guy does not laugh, he is not happy. (3) If Guy does not laugh, he is happy. (4) Only if Guy is not happy, he does not laugh. 


## More details from the paper:

<img width="1008" alt="self-discover-1" src="https://github.com/policecar/self-discover/assets/819210/4572adf8-f12e-4764-b844-495f4297b2b4">


## Teuxdeux:

- add the missing details in IMPLEMENT
- add unrelated task examples for STAGE 1
- use a language model that can actually solve all the sample tasks ^^
- split the prompt into system and user bits
