# Project Cleaner

## Description
Project Cleaner is a Python script designed to traverse through a directory containing multiple Flutter projects and run the `flutter clean` command for each project. This helps in cleaning up the build artifacts and ensuring that the projects are in a clean state.

## Features
- Automatically traverses through the specified directory.
- Identifies Flutter projects by looking for the `pubspec.yaml` file.
- Runs the `flutter clean` command for each identified Flutter project.
- Prints the output of the `flutter clean` command for each project.

## Prerequisites
- Python 3.x installed on your machine.
- Flutter SDK installed and added to your system's PATH.

## Installation
1. Clone the repository or download the script file.

```sh
git clone https://github.com/MaheshPhuyal02/Flutter-Clean.git
```

2. Ensure you have Python and Flutter installed on your machine.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `cleaner.py` script.

```sh
cd path/to/project-cleaner
```

3. Run the script using Python.

```sh
python3 cleaner.py
```

By default, the script will use the current directory of the terminal as the root directory and traverse through it to find and clean Flutter projects.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue or contact the repository owner.
