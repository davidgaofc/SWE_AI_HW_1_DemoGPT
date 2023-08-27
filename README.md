
# DemoGPT Research Paper Parser

## Description
This project is a demonstration of using DemoGPT to parse research papers and find areas of future research and related research directions that have not been explored extensively. Additionally, it suggests other papers for reference.

Given a research paper in the form of a PDF, the tool will:
- Parse through the text of the research paper.
- Identify and list down areas of future research mentioned in the paper.
- Highlight any related research directions that appear promising but haven't been extensively explored.
- Provide references to other papers if they can be helpful.

If there is an error in uploading the file, users can alternatively copy and paste the text of the research paper into the input.

**Note**: This project is a homework assignment for a class and is only intended as a demo.

## How to Use
1. Clone this repository: `git clone [repository link]`.
2. Navigate to the project directory: `cd [project directory name]`.
3. Install necessary dependencies: `pip install -r requirements.txt`.
4. Run the project: `python main.py` (This assumes you have Python installed).
5. Follow the on-screen prompts to upload your research paper in PDF format.
6. Wait for the tool to process and analyze the content.
7. Review the extracted areas of future research and related directions.
8. In case of any upload errors, copy and paste the text of the research paper into the provided input box.

## Behind the Scenes with DemoGPT
DemoGPT powers the core functionality of this tool. It's a model trained by OpenAI based on the GPT-4 architecture. For our project, it's responsible for:

- Reading and understanding the content of the research paper.
- Extracting relevant sections that hint at future research areas.
- Generating suggestions and linking to related research papers based on the content of the analyzed paper.

This integration allows for a more intuitive and context-aware extraction of future research directions, providing value to researchers and enthusiasts alike.

## Installation and Setup
- Ensure you have Python (version 3.x) installed on your machine.
- It's recommended to create a virtual environment for this project to manage dependencies.
- Follow the steps in the "How to Use" section for a smooth setup and execution.

## Feedback and Issues
For any feedback or if you encounter any issues, please raise them in the issue tracker of this repository.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Thanks to OpenAI and the GPT-4 model.
- Special gratitude to my class instructor and peers for their invaluable feedback.

---

**Disclaimer**: The accuracy and completeness of the extracted areas of research depend on the quality and clarity of the provided research paper. This tool is intended for educational purposes and should be used with discretion.
