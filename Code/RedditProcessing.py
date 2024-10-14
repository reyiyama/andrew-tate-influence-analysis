"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2023

"""
import re

class RedditProcessing:
    """
    This class is used to pre-process Reddit posts.  This centralises the processing to one location.  Feel free to add or edit.
    """

    def __init__(self, tokeniser, stemmer,  lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """
        self.tokeniser = tokeniser
        self.lStopwords = lStopwords
        self.stemmer = stemmer

    def process(self, text):
        """
        Perform the processing.
        @param text: the text (tweet) to process

        @returns: list of (valid) tokens in text
        """
        if not isinstance(text, str):
            # Convert to string or skip depending on your preference
            text = str(text)

        text = text.lower()
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]
        lStemmedTokens = set([self.stemmer.stem(tok) for tok in tokensStripped])

        # pattern for digits
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        # regex pattern for http
        regexHttp = re.compile("^http")
        # regex pattern for emojis (matches a wide range of common emojis)
        regexEmoji = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001F004-\U0001F0CF\U0001F004-\U0001F0CF\U0001F170-\U0001F19F\U0001F200-\U0001F251]+")

        return [tok for tok in lStemmedTokens if tok not in self.lStopwords and regexDigit.match(tok) is None
                and regexHttp.match(tok) is None and not tok.isdigit() and regexEmoji.match(tok) is None]