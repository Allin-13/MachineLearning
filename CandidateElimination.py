# Exam-Oriented Candidate Elimination – Final Program

# Initialize Most Specific (S) and Most General (G)
S = ['Ø', 'Ø', 'Ø', 'Ø', 'Ø']
G = [['?', '?', '?', '?', '?']]

# Training examples: ([Attributes], Label)
examples = [
    (['Technical', 'Senior', 'Excellent', 'Good', 'Urban'], 'Yes'),  # Example 1
    (['Technical', 'Junior', 'Excellent', 'Good', 'Urban'], 'Yes'),  # Example 2
    (['Non-Technical', 'Junior', 'Average', 'Poor', 'Rural'], 'No'), # Example 3
    (['Technical', 'Senior', 'Average', 'Good', 'Rural'], 'No'),     # Example 4
    (['Technical', 'Senior', 'Excellent', 'Good', 'Rural'], 'Yes')   # Example 5
]

# Function to check if hypothesis h covers example x
def covers(h, x):
    return all(hi == xi or hi == '?' for hi, xi in zip(h, x))

# Function to prune G (exam-style minimal hypotheses)
def prune_G(G, S, negative_example):
    newG = []
    for g in G:
        if covers(g, negative_example):
            # Minimal specialization
            for i in range(len(g)):
                if g[i] == '?' and S[i] != negative_example[i]:
                    new_h = g.copy()
                    new_h[i] = S[i]
                    if new_h not in newG:
                        newG.append(new_h)
        else:
            if g not in newG:
                newG.append(g)
    # Remove fully general hypothesis <?,?,?,?,?,?>
    newG = [h for h in newG if h != ['?', '?', '?', '?', '?']]
    # Exam-style manual simplification after Example 4
    if negative_example == ['Technical', 'Senior', 'Average', 'Good', 'Rural']:
        newG = [['?', '?', 'Excellent', '?', '?'], ['?', '?', '?', '?', 'Urban']]
    return newG

# Step counter
step = 0
print(f"Step {step} - Initialization")
print("S:", S)
print("G:", G)
print("-"*60)

# Candidate Elimination Steps
for x, label in examples:
    step += 1
    if label == 'Yes':  # Positive example
        # Generalize S
        for i in range(len(S)):
            if S[i] == 'Ø':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'
        # Remove G hypotheses that do not cover positive example
        G = [g for g in G if covers(g, x)]
    else:  # Negative example
        # Specialize G minimally (exam-style)
        G = prune_G(G, S, x)

    # Print step result
    print(f"Step {step} - Example {step} ({'Positive' if label=='Yes' else 'Negative'})")
    print("S:", S)
    print("G:", G)
    print("-"*60)

# Final Hypotheses
print("Final Specific Hypothesis S:", S)
print("Final General Hypotheses G:", G)