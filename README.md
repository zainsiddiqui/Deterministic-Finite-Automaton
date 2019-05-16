# Deterministic Finite Automaton
Program that reads a description of a deterministic finite automaton (DFA) and then classifies input strings as accepted or rejected by the DFA. Program input will consist of DFA specification followed by input strings.

DFAs are characterized by the following 5-tuple: (Q, Σ, δ, q0, F), where Q
denotes the set of states, Σ is the alphabet of possible input symbols, δ is
the set of transition rules, q0 is the start state, and F is the set of final
(accepting) states. 

* Project uses Python Programming language

Sample DFA Input Specification: 
states: q0 q1 q2 q3
symbols: a b c
begin_rules
q0 -> q1 on a
q1 -> q2 on b
q0 -> q2 on c
q1 -> q1 on a
q0 -> q3 on b
end_rules
start: q0
final: q2 q3
ab => outputs "accepted"
cba => outputs "rejected"
aaa => outputs "rejected"
aaab => outputs "accepted"

![image](https://user-images.githubusercontent.com/39894720/57886697-cb21d700-77fb-11e9-881b-569a6ddb7d94.png)
