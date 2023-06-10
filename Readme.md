# Secure Password Generator

This program generates a secure password using a combination of lowercase letters, digits, and punctuation marks. The password generated is 16 characters long and is created by randomly sampling from these character sets.

## Prerequisites

To run this program, you need to have Python installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Getting Started

1. Download the `main.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `main.py` file is located.
4. Run the program by executing the following command:
   ```
   python main.py
   ```

## Usage

When you run the program, it will generate a random secure password and display it on the console.

Example output:
```
x2hqY+t1lwJ^CzbM
```

## Customization

You can modify the program to change the length of the generated password by adjusting the `16` value in the `secure_password` function. Additionally, you can customize the character sets used to generate the password by modifying the `string.ascii_lowercase`, `string.digits`, and `string.punctuation` variables in the `secure_password` function.

For example, if you want to generate an 8-character password using only lowercase letters and digits, you can modify the code as follows:
```python
import random, string

def secure_password():
    return  ''.join(random.sample(string.ascii_lowercase + string.digits, 8))

if __name__ == "__main__":
    print(secure_password())
```

## Security Considerations

This program generates passwords using randomization, which can provide a good level of security for most purposes. However, it's important to note that the security of a password also depends on other factors, such as the length, complexity, and how it is stored and used. Always consider the specific requirements and recommendations for password security in your particular context.

## License

This program is released under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.
