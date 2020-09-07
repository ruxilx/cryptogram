# cryptogram
This is a repository for a homemade cryptogram. The cipher logic is exceptionally simple.
It uses the wikiquote module or input to convert a quote into a cryptogram.
The cryptogram creates a cipher by:
  - Looping through all letters in the alphabet
  - For each letter in the alphabet, it randomly picks a cipher letter
    - If the cipher letter been used, it will loop until it picks a never assigned cipher letter

