import sys

def build_loop_map(code):
    """
    Build the index mapping for Brainfuck loops:
    For each '[' find its corresponding ']', and vice versa.
    """
    loop_map = {}
    stack = []
    for pos, cmd in enumerate(code):
        if cmd == '[':
            stack.append(pos)
        elif cmd == ']':
            if not stack:
                raise SyntaxError("']' has no matching '['")
            start = stack.pop()
            loop_map[start] = pos
            loop_map[pos] = start
    if stack:
        raise SyntaxError("'[' has no matching ']'")
    return loop_map

def interpret_bf(bf_code):
    """
    Interpret and execute Brainfuck code, and return the output as a string.
    """
    # Filter out non-command characters
    code = [c for c in bf_code if c in ['+', '-', '>', '<', '.', ',', '[', ']']]
    loop_map = build_loop_map(code)
    
    tape = [0] * 30000  # Memory tape
    ptr = 0             # Pointer
    pc = 0              # Program counter
    output = []         # Store output

    while pc < len(code):
        cmd = code[pc]
        if cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '>':
            ptr += 1
            if ptr >= len(tape):
                # Automatically extend the memory tape if pointer exceeds current range
                tape.append(0)
        elif cmd == '<':
            if ptr > 0:
                ptr -= 1
            else:
                raise IndexError("Pointer has reached the beginning of the tape, cannot move left")
        elif cmd == '.':
            output.append(chr(tape[ptr]))
        elif cmd == ',':
            # Read one character from standard input and store it in the current memory cell
            inp = sys.stdin.read(1)
            tape[ptr] = ord(inp) if inp else 0
        elif cmd == '[':
            # If the current cell is 0, jump to the matching ']'
            if tape[ptr] == 0:
                pc = loop_map[pc]
        elif cmd == ']':
            # If the current cell is not 0, jump back to the matching '['
            if tape[ptr] != 0:
                pc = loop_map[pc]
        pc += 1
    return ''.join(output)

if __name__ == "__main__":
    # Hello World!
    bf_code = "+++++++++++[>++++++>+++++++++>++++++++>++++>+++>+<<<<<<-]>++++++.>++.+++++++..+++.>>.>-.<<-.<.+++.------.--------.>>>+.>-."
    try:
        result = interpret_bf(bf_code)
        print(result, end="")  # Output the final result without an extra newline
    except Exception as e:
        sys.stderr.write("Error: " + str(e) + "\n")
        sys.exit(1)