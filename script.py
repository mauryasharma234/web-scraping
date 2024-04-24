from bs4 import BeautifulSoup

# Sample HTML content
HTMLFileToBeOpened = open("global2.html", "r") 

# Reading the file and storing in a variable 
html_content = HTMLFileToBeOpened.read() 

# Creating a BeautifulSoup object and 

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <h4> elements with class "name"
function_elements = soup.find_all('h4', class_='name')
# print("function elements", function_elements)

# for function in function_elements:
#     print(function.text)
# Create a list to store JSON objects for each function
functions = []
function_names = []
# # Iterate over each <h4> element
for function_element in function_elements:
    # Extract function name and signature
    function_signature = function_element.text.strip()
    function_name = function_signature.split('(')[0]
    print("Doing for ", function_name)
    function_names.append(function_name)
    # print(function_signature, function_name)

    # Extract function description
    description_element = function_element.find_next_sibling('div', class_='description')
    if description_element:
        description = description_element.text.strip().replace('\n', '').replace('  ', '')
    else:
        description = ""
    
    parameter_arr = []
    parameters = description_element.next_element.next_element.next_element
    parameters_text = parameters.text.strip()
    # print(parameters)
    
    if parameters_text == "Parameters:":
        table = parameters.find_next_sibling('table', class_='params')
        thead = table.find('thead')
        tbody = table.find('tbody')
        table_rows = tbody.find_all('tr')
        for row in table_rows:
            parameter_name = row.find('td', class_='name').text.strip().replace('\n', '').replace('  ', '')
            parameter_type = row.find('td', class_='type').text.strip().replace('\n', '').replace('  ', '')
            parameter_description = row.find('td', class_='description last').text.strip().replace('\n', '').replace('  ', '')
            # print(parameter_name, parameter_type, parameter_description)
            parameter_arr.append({"name": parameter_name, "type": parameter_type, "description": parameter_description})
        # print(len(table_rows))
        
    
#     # Extract returns
    returns_element = description_element.find_next_sibling('h5', string='Returns:')
    # print(returns_element)
#     # function_returns = returns_element.find_next_sibling().strip() if returns_element else ""

#     # Create JSON object
    function_data = {
        "name": function_name,
        "signature": function_signature,
        "description": description,
        "parameters": parameter_arr,
        # "returns": function_returns
    }

#     # Append the JSON object to the list
    functions.append(function_data)

# Print the list of functions
# print(functions)
# for function in functions:
#     print(function)

# print(functions[2])
answers = []
hovers = []
for function in functions:
    # print(function)
    # print("\n")
    insertText = ""

    insertText += function['name'] + " " + "("
    cnt = 1
    for parameter in function['parameters']:
        if cnt == len(function['parameters']):
            insertText += "${" + str(cnt) + ":" + parameter['name'] + "}"
        else:
            insertText += "${" + str(cnt) + ":" + parameter['name'] + "}, "
        cnt += 1
    insertText += ")"

    ans= {
        "label": function['name'],
        "kind": "monaco.languages.CompletionItemKind.Snippet",
        "insertText": insertText,
        "insertTextRules": "monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet",
        "documentation": function['name'] + " STATEMENT",
        "range": "range"
    }

    completion_item = f"{{\n"
    completion_item += f"    label: '{function['name']}',\n"
    completion_item += f"    kind: monaco.languages.CompletionItemKind.Snippet,\n"
    completion_item += f"    insertText: '{insertText}',\n"
    completion_item += f"    insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,\n"
    completion_item += f"    documentation: '{function['name']} STATEMENT',\n"
    completion_item += f"    range: range,\n"
    completion_item += f"}},"

    
    answers.append(completion_item)
    
    # hover = {
    #     "if (word && word.word === " + function['name'] + ")"+ " { return { contents: [{value: " + function['name'] + "}, {value: " + function['description'] + "}, {value: Syntax: " + function['signature'] + "}]}}",
    # }
    hover = f'if (word && word.word == "{function["name"]}")' + ' {\n'
    hover += '    return {\n'
    hover += '        contents: [\n'
    hover += f'            {{ value: "**{function["name"]} Statement**" }},\n'
    hover += f'            {{ value: "{function["description"]}" }},\n'
    hover += f'            {{ value: "Syntax: {function["signature"]}" }}\n'
    hover += '        ]\n'
    hover += '    }\n'
    hover += '}\n'

    hovers.append(hover)


# for ans in answers:
#     print(ans)  

# for hover in hovers:
#     print(hover)

print(function_names)

