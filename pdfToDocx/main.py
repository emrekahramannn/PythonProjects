# import package -> Class
from pdf2docx import Converter



def TakePaths():
    """
        This function takes paths/names for two files and corrects
        if extensions are not appopriate and returns a tuple.

        -> pdf_path, doc_path = TakePaths()
    """
    while True:
        pdf_path = input("Enter your input PDF file path/name: ")       # path (full/relative) for PDF file

        pdf_path = pdf_path.strip()

        extension = pdf_path[-4:]               # check for extension
        if extension == ".pdf":
            print("Valid input.")
            break
        elif not "." in pdf_path:
            pdf_path = pdf_path[:] + ".pdf"
            break
        elif "." in pdf_path:
            print("Please enter valid extension for your PDF file (.pdf).")


    while True:

        docx_path = input("Enter output DOCX file path/name: ")      # path/name for DOCX file

        docx_path = docx_path.strip()

        if docx_path == "":
            docx_path = pdf_path[:-4] + ".doc"
            print(f"Your output file name: {docx_path}")
            break

        extension_1 = docx_path[-4:]    # .doc
        extension_2 = docx_path[-5:]    # .docx
        if extension_1 == ".doc" or extension_2 == ".docx":
            print("Valid input.")
            break
        elif not "." in docx_path:
            docx_path = docx_path + ".doc"
            break
        elif "." in docx_path:
            print("Please enter valid extension for your DOCX file (.doc or .docx).")


    return pdf_path, docx_path



def ConvertPdfToDocx(pdf_path, docx_path):
    try:
        cv = Converter(pdf_file = pdf_path)                     # create an object
    except:
        # print an error message if any error occur and quit
        print("An error has occured. Please try again.")
        quit()
    else:
        cv.convert(docx_filename = docx_path)
        cv.close()

    print("Your Docx file is ready. Enjoy it.")



if __name__ == "__main__":
    pdf_path, docx_path = TakePaths() 
    ConvertPdfToDocx(pdf_path, docx_path)
