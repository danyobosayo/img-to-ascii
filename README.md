# img-to-ascii
Project that processes an image, and converts it into ascii characters based on lighting level.

## How to run?
1. Clone the repository into a new directory
    ```bash
    git clone https://github.com/danyobosayo/img-to-ascii.git
    ```
2. Navigate to the corresponding directory. 
3. Create the virtual environment: Assuming python is installed
    ```bash
    python -m venv myenv
    ```
4. Activate the virtual environment:<br>
    On Windows:
    ```bash
    myenv\Scripts\activate
    ```
    On Linux/MacOS:
    ```bash
    source myenv/bin/activate
    ```
5. Install required dependencies (only numpy and Pillow)
    ```bash
    pip install -r requirements.txt
    ```
6. Run the script with your desired image and parameters. 

## Examples:
```bash
    python main.py --file images/garfield.jpg --cols 100 --scale 0.5
    python main.py --file images/starrynight.jpg --cols 200 --scale 0.5 --morelevels
```

## Notes:
- Make sure to replace images/garfield.jpg and images/starrynight.jpg with the path to your desired image files.
- Adjust the cols and scale parameters to customize the output according to your preferences.
- Adding the --morelevels flag increases the number of brightness levels used for the ASCII conversion.

#### Thanks for reaching the end, have a good day!