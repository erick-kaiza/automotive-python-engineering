OBD-II Fault Code Lookup Tool

A command-line tool that looks up OBD-II diagnostic trouble codes (DTCs) and returns their description,using a Python dictionary as the lookup database.

Simulates a simplified fault code scanner interface.The User enters a DTC,and the tool returns its corresponding description.Invalid or unrecognized codes return a fallback message instead of crashing the program.

Features include :
    -15-entry fault code database,weighted towards diesel/turbo relevant codes
    -Case insensitive,whitespace-tolerant input handling
    -Safe dictionary lookups (no crash on invalid codes)
    -Continous lookup loop until user exits

Skills demonstrated:
    -Dictioneries as key-value lookups
    -Safe lookups with "dict.get()" and a fallback value
    -Input sanitization with ".upper()" and ".strip()"
    -Loop control with "while True" and "Break"
    -f-string formatting for output

AUTHOR 
Erick Kaiza Kirobi | Python for automotive engineering portfolio 