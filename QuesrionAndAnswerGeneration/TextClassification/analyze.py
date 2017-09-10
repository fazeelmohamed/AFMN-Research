import nltk
import traceback
import sys

# Usage string
usage = """Usage: ./analyze.py text_filename.txt N
    where text_filename.txt is the text file containing the text content
    and N is an integer specifying the number of questions to output.
"""

#checks the correctness of comand line arguments.
def getInputs():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(usage);
    n = int(args[1])
    return (args[0], n)

if __name__ == "__main__":
    # Add the path to the nltk data
    nltk.data.path.append('/afs/andrew.cmu.edu/usr6/ericgan/nltk_data')

    # Get the arguments from the command line
    (textFileName, N) = getInputs()

    # Attempt to open the text file
    try:
        file = open(textFileName, 'r')
        textContent = file.read()
        sentences = nltk.sent_tokenize(textContent)
        print(sentences)


    except IOError:
        sys.stderr.write("Could not find text file: %s\n" % (textFileName));
