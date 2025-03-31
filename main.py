import sys
from TextAnalysisApp import TextAnalysisApp

if __name__ == "__main__":
    app = TextAnalysisApp(sys.argv)
    sys.exit(app.exec())
